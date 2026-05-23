import json
import re
from pathlib import Path
from textwrap import dedent

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "automate_boring_stuff_ch1_10_source_map_and_extra_practice.ipynb"
COVERAGE_OUT = ROOT / "automate_boring_stuff_ch1_10_coverage_index.md"
BASE = "https://automatetheboringstuff.com/3e/chapter{}.html"


def md(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(text).strip().splitlines(True),
    }


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(text).strip("\n").splitlines(True),
    }


def nearest_heading(pre):
    current = pre
    while current:
        current = current.find_previous()
        if current and current.name in {"h1", "h2", "h3"}:
            return current.get_text(" ", strip=True)
    return "Chapter examples"


def clean_repl_block(text):
    """Return executable-ish input lines from a Python REPL transcript."""
    lines = text.splitlines()
    cleaned = []
    saw_prompt = False
    for line in lines:
        if line.startswith(">>> "):
            saw_prompt = True
            cleaned.append(line[4:])
        elif line.startswith("... "):
            cleaned.append(line[4:])
        elif line.strip() in {">>>", "..."}:
            saw_prompt = True
            cleaned.append("")
    if not saw_prompt:
        return None
    return "\n".join(cleaned).strip()


def looks_runnable(source):
    if not source.strip():
        return False
    risky = [
        "input(",
        "pyperclip.",
        "sys.exit(",
        "pdb.",
        "breakpoint(",
        "open(",
        "Path(",
        "shelve.open",
        "send2trash",
    ]
    if any(item in source for item in risky):
        return False
    if source.count("(") != source.count(")"):
        return False
    if "Traceback " in source or "SyntaxError" in source or "NameError" in source:
        return False
    return True


def compact_summary(text, max_len=220):
    one_line = " ".join(text.split())
    if len(one_line) <= max_len:
        return one_line
    return one_line[: max_len - 3] + "..."


def code_preview(text, max_lines=14):
    lines = text.strip("\n").splitlines()
    preview = "\n".join(lines[:max_lines])
    if len(lines) > max_lines:
        preview += f"\n# ... {len(lines) - max_lines} more line(s) in this source example"
    return preview.replace("```", "'''")


def topic_for(chapter_num):
    return {
        1: "Python values, expressions, variables, and basic input/output",
        2: "Boolean logic and choosing which code path runs",
        3: "repeating work with loops and stopping loops deliberately",
        4: "packaging repeated logic into functions",
        5: "finding, explaining, and handling bugs",
        6: "working with ordered collections using lists",
        7: "modeling structured records using dictionaries",
        8: "cleaning, formatting, and transforming text",
        9: "finding text patterns with regular expressions",
        10: "reading from and writing to files",
    }[chapter_num]


def prior_link(chapter_num):
    return {
        1: "This is the foundation: later chapters reuse values, variables, expressions, and function calls constantly.",
        2: "This builds directly on chapter 1 because comparisons use values and expressions to decide what happens next.",
        3: "This builds on chapters 1 and 2: loops repeat expressions and use Boolean conditions to know when to stop.",
        4: "This builds on chapters 1-3 by turning repeated expressions, decisions, and loops into named reusable tools.",
        5: "This builds on every earlier chapter because debugging is how you understand failures in variables, conditions, loops, and functions.",
        6: "This builds on loops and functions: lists give loops something useful to process, filter, and transform.",
        7: "This builds on lists by adding names to values, which makes your data easier to understand and update.",
        8: "This builds on lists, loops, and functions because text cleanup often means looping through many strings and transforming each one.",
        9: "This builds on string handling: regex is the next step when simple methods like split, strip, and replace are not enough.",
        10: "This connects all previous chapters to real automation because scripts become useful when they read input files and write results.",
    }[chapter_num]


def context_lines(chapter_num, section, raw):
    topic = topic_for(chapter_num)
    text = raw.lower()
    purpose = f"This example is part of {topic}, from the section `{section}`."
    concept = "It shows the small unit of thinking the author wants you to practice before combining ideas into bigger scripts."
    link = prior_link(chapter_num)
    real_world = "In real work, this pattern becomes one step in a repeatable automation: inspect data, decide what to do, transform it, then report or save the result."
    caution = "Read the code for inputs, outputs, and side effects; then change one value and predict what will happen."

    if "input(" in text:
        purpose = "This example shows how a program receives information from a person while it is running."
        real_world = "That matters for command-line helpers, setup scripts, calculators, and small tools that ask for filenames or options."
    elif "if " in text or "elif " in text or "else" in text:
        purpose = "This example shows how code chooses between different paths."
        real_world = "That matters anywhere a script must validate data, branch on a status, or handle special cases."
    elif "for " in text or "while " in text:
        purpose = "This example shows repeated work, which is the heart of automation."
        real_world = "That matters when processing many files, rows, messages, names, records, or matches."
    elif "def " in text:
        purpose = "This example shows how to name a reusable piece of behavior as a function."
        real_world = "That matters because reliable scripts are built from small pieces you can test and reuse."
    elif "try" in text or "except" in text or "assert" in text or "logging" in text:
        purpose = "This example shows how to make failures easier to understand."
        real_world = "That matters because automation often runs unattended, so clear errors and logs save time."
    elif "[" in text and "]" in text:
        purpose = "This example shows how to store and process multiple values together."
        real_world = "That matters when you need to clean a batch of filenames, tasks, contacts, or spreadsheet rows."
    elif "{" in text and "}" in text:
        purpose = "This example shows how to connect meaningful keys to values."
        real_world = "That matters when modeling contacts, inventory, settings, API responses, or JSON-like data."
    elif "re." in text or "regex" in text or "compile(" in text:
        purpose = "This example shows how to search text by pattern instead of by exact words."
        real_world = "That matters for extracting emails, phone numbers, dates, IDs, and other messy text patterns."
    elif "open(" in text or "read" in text or "write" in text or "path" in text:
        purpose = "This example shows how Python interacts with files and file paths."
        real_world = "That matters because most useful automation reads something from disk and writes a cleaner result."

    return [purpose, concept, link, real_world, caution]


def flow_diagram(chapter_num):
    diagrams = {
        1: "value/input -> expression/function call -> result/output",
        2: "data -> condition -> True path / False path -> next statement",
        3: "start -> check condition -> run body -> update state -> repeat/stop",
        4: "input arguments -> function body -> return value -> caller uses result",
        5: "run code -> observe error/log -> inspect state -> fix assumption -> rerun",
        6: "list of items -> loop/index/slice -> transform/filter -> new result",
        7: "real-world thing -> keys + values -> lookup/update -> structured result",
        8: "raw text -> strip/split/replace/format -> clean text -> display/save",
        9: "raw text -> regex pattern -> matches/groups -> extracted data",
        10: "file path -> read text/data -> process with earlier skills -> write output",
    }
    return diagrams[chapter_num]


def source_example_markdown(chapter_num, block_index, block, raw):
    lines = context_lines(chapter_num, block["section"], raw)
    return "\n".join(
        [
            f"#### Source example {chapter_num}.{block_index}",
            "",
            f"Checklist note: captured from section **{block['section']}**.",
            "",
            "**Context**",
            "",
            f"1. {lines[0]}",
            f"2. {lines[1]}",
            f"3. {lines[2]}",
            f"4. {lines[3]}",
            f"5. {lines[4]}",
            "",
            "**Concept Flow**",
            "",
            "```text",
            flow_diagram(chapter_num),
            "```",
            "",
            "**Code Preview**",
            "",
            "```python",
            code_preview(raw),
            "```",
        ]
    )


def fetch_chapter(chapter_num):
    url = BASE.format(chapter_num)
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find(["h1", "h2"])
    title = title_tag.get_text(" ", strip=True) if title_tag else f"Chapter {chapter_num}"
    blocks = []
    for pre in soup.find_all("pre"):
        text = pre.get_text("\n").strip("\n")
        if not text:
            continue
        blocks.append(
            {
                "section": nearest_heading(pre),
                "raw": text,
                "cleaned": clean_repl_block(text),
            }
        )
    return {"url": url, "title": title, "blocks": blocks}


practice_sections = {
    8: [
        (
            "String cleanup ladder",
            """
            messy_names = ["  ada lovelace", "GRACE HOPPER  ", "\\talan TURING\\n"]

            cleaned_names = []
            for name in messy_names:
                cleaned_names.append(name.strip().title())

            print(cleaned_names)

            # Practice:
            # 1. Add an empty string and skip it.
            # 2. Convert the list into one comma-separated sentence.
            # 3. Write a function clean_name(name) and reuse it.
            """,
        ),
        (
            "Text table formatter",
            """
            rows = [
                ("Item", "Qty", "Price"),
                ("Notebook", 3, 4.99),
                ("Pen", 12, 0.79),
                ("Backpack", 1, 39.5),
            ]

            for item, qty, price in rows:
                if isinstance(price, float):
                    price_text = f"${price:,.2f}"
                else:
                    price_text = str(price)
                print(f"{str(item):<12} {str(qty):>5} {price_text:>10}")

            # Practice:
            # Add a Total column and align it neatly.
            """,
        ),
        (
            "Clipboard-style text transformation without clipboard dependency",
            """
            pasted_text = '''
            milk
            eggs
            bread
            apples
            '''

            bullet_lines = []
            for line in pasted_text.strip().splitlines():
                bullet_lines.append("* " + line.strip())

            result = "\\n".join(bullet_lines)
            print(result)

            # Practice:
            # Change this to numbered lines: 1. milk, 2. eggs, and so on.
            """,
        ),
    ],
    9: [
        (
            "Regex date extractor",
            r'''
            text = "Deadlines: 2026-05-21, 2026-06-01, and bad date 2026-99-99."
            date_regex = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")

            for match in date_regex.finditer(text):
                year, month, day = match.groups()
                print(f"year={year}, month={month}, day={day}")

            # Practice:
            # Add simple validation so months must be 01 through 12.
            ''',
        ),
        (
            "Regex phone/email report",
            r'''
            contact_text = """
            Ada: ada@example.com, 555-111-2222
            Grace: grace@example.org, (555) 333-4444
            Bad: no email, 55555
            """

            email_regex = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
            phone_regex = re.compile(r"(?:\(\d{3}\)|\d{3})[- ]\d{3}-\d{4}")

            for line in contact_text.strip().splitlines():
                email = email_regex.search(line)
                phone = phone_regex.search(line)
                if email and phone:
                    print(email.group(), phone.group())

            # Practice:
            # Save valid contacts as dictionaries with name, email, and phone keys.
            ''',
        ),
        (
            "Regex substitution practice",
            r'''
            message = "Order ABC-123 ships to jane@example.com. Order XYZ-999 ships to admin@example.org."

            redacted = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "[EMAIL]", message)
            normalized = re.sub(r"\b[A-Z]{3}-(\d{3})\b", r"ORDER-\1", redacted)

            print(normalized)

            # Practice:
            # Redact order numbers completely instead of normalizing them.
            ''',
        ),
    ],
    10: [
        (
            "Safe text file workflow",
            """
            from pathlib import Path
            import tempfile

            folder = Path(tempfile.gettempdir()) / "atsbs_file_practice"
            folder.mkdir(exist_ok=True)

            notes = folder / "notes.txt"
            notes.write_text("alpha\\nbeta\\ngamma\\n", encoding="utf-8")

            lines = notes.read_text(encoding="utf-8").splitlines()
            print(lines)
            print("Line count:", len(lines))

            # Practice:
            # Write a second file named uppercase_notes.txt with each line uppercased.
            """,
        ),
        (
            "Folder scan and extension counts",
            """
            folder = Path(tempfile.gettempdir()) / "atsbs_file_practice_scan"
            folder.mkdir(exist_ok=True)

            for name in ["a.txt", "b.txt", "image.png", "data.csv", "notes.txt"]:
                (folder / name).write_text("sample", encoding="utf-8")

            counts = {}
            for path in folder.iterdir():
                if path.is_file():
                    counts[path.suffix] = counts.get(path.suffix, 0) + 1

            print(counts)

            # Practice:
            # Print the filenames grouped by extension.
            """,
        ),
        (
            "JSON settings file",
            """
            settings_path = Path(tempfile.gettempdir()) / "atsbs_settings.json"
            settings = {
                "theme": "light",
                "font_size": 14,
                "recent_projects": ["python-basics", "regex-practice"],
            }

            settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
            loaded_settings = json.loads(settings_path.read_text(encoding="utf-8"))

            print(loaded_settings["theme"])

            # Practice:
            # Add a new recent project, then write the JSON file again.
            """,
        ),
    ],
}


cells = [
    md(
        """
        # Automate the Boring Stuff: Chapters 1-10 Source Map + Extra Practice

        This notebook is a chapter-by-chapter companion for the first 10 chapters of
        Al Sweigart's *Automate the Boring Stuff with Python*, 3rd edition.

        Official book site: https://automatetheboringstuff.com/

        What this notebook gives you:

        - A source-map checklist for every code block extracted from chapters 1-10.
        - The examples in the same chapter and page-section order as the official pages.
        - Runnable practice cells after each chapter.
        - Extra practice after dictionaries, especially strings, regular expressions, and files.

        Note: Some source examples are interactive shell transcripts, intentional errors,
        clipboard examples, or examples that need local files. Those are included as study
        blocks and are not always meant to be run directly.
        """
    ),
    code(
        """
        import json
        import logging
        import random
        import re
        import tempfile
        from pathlib import Path
        from pprint import pprint

        print("Setup complete.")
        """
    ),
]


chapters = [fetch_chapter(ch) for ch in range(1, 11)]

cells.append(md("## Coverage Summary"))
summary_lines = []
for chapter in chapters:
    summary_lines.append(
        f"- {chapter['title']}: {len(chapter['blocks'])} code blocks mapped from {chapter['url']}"
    )
cells.append(md("\n".join(summary_lines)))


for chapter_index, chapter in enumerate(chapters, start=1):
    cells.append(md(f"## {chapter['title']}\n\nSource: {chapter['url']}"))
    current_section = None
    for block_index, block in enumerate(chapter["blocks"], start=1):
        if block["section"] != current_section:
            current_section = block["section"]
            cells.append(md(f"### {current_section}"))

        raw = block["raw"]
        cleaned = block["cleaned"]
        cells.append(md(source_example_markdown(chapter_index, block_index, block, raw)))

        if cleaned and looks_runnable(cleaned):
            cells.append(
                code(
                    f"# Adapted from source example {chapter_index}.{block_index}; run and modify it.\n"
                    + cleaned
                )
            )
        else:
            cells.append(
                md(
                    "Study transcript or context-dependent example:\n\n"
                    + "```python\n"
                    + raw.replace("```", "'''")
                    + "\n```"
                )
            )
            cells.append(code(f"# Practice rewrite for source example {chapter_index}.{block_index}\n"))

    cells.append(md(f"### Chapter {chapter_index} Practice Checkpoint"))
    cells.append(
        code(
            f"""
            # Chapter {chapter_index} checkpoint
            # Pick three source examples from this chapter.
            # 1. Run or rewrite them.
            # 2. Change one value.
            # 3. Predict the output before running.
            """
        )
    )
    if chapter_index in practice_sections:
        cells.append(md(f"### Extra Practice for Chapter {chapter_index}"))
        for title, source in practice_sections[chapter_index]:
            cells.append(md(f"#### {title}"))
            cells.append(code(source))


cells.extend(
    [
        md(
            """
            ## Beyond Dictionaries Practice Track

            Since you said you are comfortable until dictionaries, use this track as your
            main workout. These combine chapters 8, 9, and 10.
            """
        ),
        code(
            r'''
            # Project 1: Clean a messy contact list.
            raw_contacts = """
              ada lovelace | ADA@EXAMPLE.COM | 555-010-1111
            grace hopper| grace@example.org | (555) 010-2222
            bad row | missing email | 12345
            linus torvalds | linus@example.net | 555-010-3333
            """

            email_re = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
            phone_re = re.compile(r"(?:\(\d{3}\)|\d{3})[- ]\d{3}-\d{4}")

            contacts = []
            for row in raw_contacts.strip().splitlines():
                parts = [part.strip() for part in row.split("|")]
                if len(parts) != 3:
                    continue
                name, email_text, phone_text = parts
                email_match = email_re.search(email_text)
                phone_match = phone_re.search(phone_text)
                if email_match and phone_match:
                    contacts.append({
                        "name": name.title(),
                        "email": email_match.group().lower(),
                        "phone": phone_match.group(),
                    })

            pprint(contacts)
            '''
        ),
        code(
            """
            # Project 2: Save cleaned contacts to CSV and JSON.
            output_dir = Path(tempfile.gettempdir()) / "atsbs_contacts_project"
            output_dir.mkdir(exist_ok=True)

            csv_path = output_dir / "contacts.csv"
            json_path = output_dir / "contacts.json"

            csv_lines = ["name,email,phone"]
            for contact in contacts:
                csv_lines.append(f"{contact['name']},{contact['email']},{contact['phone']}")

            csv_path.write_text("\\n".join(csv_lines), encoding="utf-8")
            json_path.write_text(json.dumps(contacts, indent=2), encoding="utf-8")

            print(csv_path)
            print(json_path)
            """
        ),
        code(
            r'''
            # Project 3: Build a word-frequency report from text files.
            folder = Path(tempfile.gettempdir()) / "atsbs_word_report"
            folder.mkdir(exist_ok=True)

            sample_files = {
                "one.txt": "Spam spam eggs.",
                "two.txt": "Eggs toast spam.",
                "three.txt": "Toast, coffee, and eggs!",
            }

            for filename, text in sample_files.items():
                (folder / filename).write_text(text, encoding="utf-8")

            word_counts = {}
            word_re = re.compile(r"[A-Za-z]+")

            for path in folder.glob("*.txt"):
                text = path.read_text(encoding="utf-8")
                for match in word_re.finditer(text):
                    word = match.group().lower()
                    word_counts[word] = word_counts.get(word, 0) + 1

            report_path = folder / "word_counts.json"
            report_path.write_text(json.dumps(word_counts, indent=2, sort_keys=True), encoding="utf-8")

            pprint(word_counts)
            print(report_path)
            '''
        ),
    ]
)


notebook = {
    "cells": cells,
    "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "version": "3.13.5",
            "mimetype": "text/x-python",
            "codemirror_mode": {"name": "ipython", "version": 3},
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "file_extension": ".py",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}


OUT.write_text(json.dumps(notebook, indent=2), encoding="utf-8")

coverage_lines = [
    "# Automate the Boring Stuff Chapters 1-10 Coverage Index",
    "",
    "This index lists every source code block mapped into the comprehensive notebook.",
    "",
]
for chapter_index, chapter in enumerate(chapters, start=1):
    coverage_lines.extend(
        [
            f"## {chapter['title']}",
            "",
            f"Source: {chapter['url']}",
            "",
            f"Mapped code blocks: {len(chapter['blocks'])}",
            "",
        ]
    )
    for block_index, block in enumerate(chapter["blocks"], start=1):
        coverage_lines.append(
            f"- {chapter_index}.{block_index} | {block['section']} | {compact_summary(block['raw'], 120)}"
        )
    coverage_lines.append("")

COVERAGE_OUT.write_text("\n".join(coverage_lines), encoding="utf-8")
print(OUT)
print(COVERAGE_OUT)
print(f"cells={len(cells)}")
