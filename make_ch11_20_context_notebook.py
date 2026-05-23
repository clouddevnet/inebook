import json
import re
import ast
from pathlib import Path
from textwrap import dedent

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "automate_boring_stuff_ch11_20_source_map_context_practice.ipynb"
COVERAGE_OUT = ROOT / "automate_boring_stuff_ch11_20_coverage_index.md"
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
    if not source or not source.strip():
        return False
    risky = [
        "input(",
        "pyperclip",
        "sys.exit(",
        "smtplib",
        "imaplib",
        "ezgmail",
        "twilio",
        "pywhatkit",
        "requests.get(",
        "webbrowser.",
        "selenium",
        "openpyxl.load_workbook",
        "Credentials",
        "googleapiclient",
        "subprocess.",
        "Popen(",
        "Path.home()",
        "send2trash",
        "shutil.move",
        "shutil.copy",
        "os.unlink",
        "os.remove",
        "os.rmdir",
    ]
    if any(item in source for item in risky):
        return False
    if source.count("(") != source.count(")"):
        return False
    if any(error in source for error in ["Traceback ", "SyntaxError", "NameError"]):
        return False
    try:
        ast.parse(source)
    except SyntaxError:
        return False
    return True


def compact_summary(text, max_len=140):
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
        11: "organizing files and folders",
        12: "building command line programs",
        13: "web scraping and browser automation",
        14: "working with Excel spreadsheets",
        15: "automating Google Sheets",
        16: "storing structured data in SQLite databases",
        17: "reading and creating PDF and Word documents",
        18: "processing CSV, JSON, and XML data files",
        19: "time, scheduling, and launching programs",
        20: "sending email, texts, and push notifications",
    }[chapter_num]


def prior_link(chapter_num):
    return {
        11: "This chapter turns chapter 10 file reading/writing into practical folder automation, while still relying on loops, strings, and conditionals from the basics.",
        12: "This chapter wraps earlier functions and file logic into reusable command-line tools, so the same script can work with different inputs.",
        13: "This chapter builds on strings, regex, dictionaries, and file output: web pages become another source of text and structured data.",
        14: "This chapter applies lists, dictionaries, loops, and file concepts to spreadsheets, which are one of the most common real-world data sources.",
        15: "This chapter extends spreadsheet thinking to shared cloud data, adding authentication and remote updates to the same row-and-cell mindset.",
        16: "This chapter upgrades dictionaries and files into databases, giving you a reliable way to store, query, and update structured records.",
        17: "This chapter applies text processing and file I/O to office documents, where automation often means extracting or generating reports.",
        18: "This chapter connects directly to dictionaries, lists, strings, and files because CSV, JSON, and XML are structured-data formats.",
        19: "This chapter adds time as a trigger or measurement around earlier scripts, turning one-off code into scheduled automation.",
        20: "This chapter connects earlier automation to people: once a script finishes or fails, it can send a message with the result.",
    }[chapter_num]


def flow_diagram(chapter_num):
    return {
        11: "files/folders -> inspect paths -> choose action -> copy/move/archive -> verify result",
        12: "terminal args -> parse options -> call functions -> produce output/errors",
        13: "URL/HTML -> fetch/open page -> parse/select elements -> extract/save data",
        14: "workbook file -> sheet/rows/cells -> transform values -> save workbook",
        15: "credentials -> cloud sheet -> rows/cells -> read/update -> shared result",
        16: "records -> table schema -> insert/query/update -> report/export",
        17: "document file -> extract/compose text -> format content -> save document",
        18: "CSV/JSON/XML file -> parser -> Python lists/dicts -> transform -> write/export",
        19: "current time/event -> wait/schedule/measure -> run task -> log/notify",
        20: "script result -> format message -> authenticate service -> send notification",
    }[chapter_num]


def context_lines(chapter_num, section, raw):
    text = raw.lower()
    topic = topic_for(chapter_num)
    purpose = f"This example belongs to the chapter on {topic}, and shows one small building block from the section `{section}`."
    concept = "Pay attention to the library calls, the data type being passed in, and what the code returns or changes."
    link = prior_link(chapter_num)
    importance = "In real automation work, this kind of pattern lets you replace repeated manual steps with a script you can rerun."
    caution = "Run it carefully: later chapters often touch real files, websites, accounts, or installed applications."

    if "shutil" in text or "send2trash" in text or "zipfile" in text:
        purpose = "This example demonstrates file-management automation: copying, moving, deleting safely, or compressing files."
        concept = "The key idea is that paths are data, so your program can inspect many files and apply the same rule consistently."
        importance = "This matters when cleaning Downloads folders, archiving reports, collecting logs, or preparing project backups."
        caution = "Use sample folders first, because a small path mistake can affect many files quickly."
    elif "argparse" in text or "sys.argv" in text:
        purpose = "This example shows how a Python script receives options and filenames from the command line."
        concept = "Command line arguments make a script reusable because the behavior changes without editing the source code."
        importance = "That is important for tools you want to run from terminals, scheduled jobs, shortcuts, or other programs."
        caution = "Practice with harmless inputs first, then add validation and helpful error messages."
    elif "requests" in text or "bs4" in text or "beautifulsoup" in text or "selenium" in text:
        purpose = "This example shows how Python can fetch web pages or inspect browser-visible HTML."
        concept = "The core skill is separating page structure from page appearance so you can extract the data you need."
        importance = "This is useful for monitoring prices, collecting public data, checking pages, or filling repetitive forms."
        caution = "Respect site terms, rate limits, robots policies, and login/security boundaries."
    elif "openpyxl" in text or "workbook" in text or "worksheet" in text:
        purpose = "This example demonstrates spreadsheet automation with workbooks, sheets, cells, rows, or formulas."
        concept = "Python treats a spreadsheet as structured data, so you can read, transform, and write it systematically."
        importance = "This saves time when cleaning reports, generating invoices, updating trackers, or merging spreadsheet exports."
        caution = "Always keep a backup copy before writing changes to an important spreadsheet."
    elif "google" in text or "ezsheets" in text:
        purpose = "This example introduces cloud spreadsheet automation through Google Sheets APIs or helper libraries."
        concept = "The main idea is authenticated access: your script needs permission before it can read or update online sheets."
        importance = "This is valuable when teams already collaborate in shared sheets and you want automation without manual downloads."
        caution = "Keep credentials private and test with a throwaway sheet before touching team data."
    elif "sqlite" in text or "select" in text or "insert" in text or "create table" in text:
        purpose = "This example demonstrates database work: creating tables, inserting rows, querying, or updating records."
        concept = "A database lets you ask precise questions of structured data without manually scanning files."
        importance = "SQLite is practical for personal tools, local caches, app prototypes, logs, and repeatable reports."
        caution = "Use parameterized queries for user input and commit changes deliberately."
    elif "pypdf" in text or "docx" in text or "pdf" in text:
        purpose = "This example shows document automation for PDF or Word files."
        concept = "The useful skill is extracting text or assembling documents from predictable pieces."
        importance = "This helps with invoices, forms, reports, contracts, meeting notes, and document-heavy office workflows."
        caution = "Document layouts can be tricky, so inspect the output visually when formatting matters."
    elif "csv" in text or "json" in text or "xml" in text:
        purpose = "This example focuses on data-interchange files such as CSV, JSON, or XML."
        concept = "These formats let programs exchange structured data using plain files."
        importance = "They appear in exports, APIs, configuration files, logs, and integrations between tools."
        caution = "Use parsers instead of manual string splitting when the format has quoting, nesting, or special characters."
    elif "datetime" in text or "time." in text or "schedule" in text:
        purpose = "This example demonstrates time-based programming: dates, durations, delays, or scheduled actions."
        concept = "Programs need explicit time handling because humans use many time formats and computers need exact values."
        importance = "This is important for reminders, backups, status checks, reports, and anything that runs regularly."
        caution = "Be careful with time zones, long sleeps, and scripts that might keep running longer than expected."
    elif "email" in text or "smtp" in text or "imap" in text or "twilio" in text or "push" in text:
        purpose = "This example demonstrates outbound or inbound notification automation."
        concept = "Your script connects to a service, authenticates, formats a message, and sends or receives information."
        importance = "Notifications turn scripts into useful assistants that can report results, failures, reminders, or alerts."
        caution = "Use app passwords or tokens securely and avoid sending real messages while practicing."

    return [purpose, concept, link, importance, caution]


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
    response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
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


extra_practice = {
    11: [
        (
            "Practice: organize files by extension",
            """
            from pathlib import Path
            import tempfile
            import shutil

            sandbox = Path(tempfile.gettempdir()) / "atsbs_ch11_organize"
            sandbox.mkdir(exist_ok=True)

            for name in ["report.txt", "photo.png", "notes.txt", "sales.csv"]:
                (sandbox / name).write_text("sample", encoding="utf-8")

            for path in sandbox.iterdir():
                if path.is_file():
                    target_dir = sandbox / path.suffix.removeprefix(".")
                    target_dir.mkdir(exist_ok=True)
                    shutil.copy(path, target_dir / path.name)

            print("Organized copy created at:", sandbox)
            """,
        )
    ],
    12: [
        (
            "Practice: command-line style function",
            """
            def rename_preview(prefix, filenames):
                planned = []
                for number, filename in enumerate(filenames, start=1):
                    planned.append((filename, f"{prefix}_{number:03d}_{filename}"))
                return planned

            for old, new in rename_preview("invoice", ["jan.pdf", "feb.pdf", "mar.pdf"]):
                print(f"{old} -> {new}")
            """,
        )
    ],
    13: [
        (
            "Practice: parse a saved HTML snippet",
            """
            from bs4 import BeautifulSoup

            html = '''
            <main>
              <article class="product"><h2>Keyboard</h2><span class="price">$79</span></article>
              <article class="product"><h2>Mouse</h2><span class="price">$35</span></article>
            </main>
            '''

            soup = BeautifulSoup(html, "html.parser")
            for product in soup.select(".product"):
                print(product.select_one("h2").get_text(strip=True), product.select_one(".price").get_text(strip=True))
            """,
        )
    ],
    14: [
        (
            "Practice: spreadsheet-like rows without needing Excel files",
            """
            rows = [
                ["Name", "Hours", "Rate"],
                ["Ada", 6, 50],
                ["Grace", 8, 55],
                ["Linus", 5, 60],
            ]

            totals = []
            for name, hours, rate in rows[1:]:
                totals.append({"name": name, "pay": hours * rate})

            print(totals)
            """,
        )
    ],
    15: [
        (
            "Practice: simulate a shared sheet update",
            """
            sheet_rows = [
                {"task": "backup", "status": "todo"},
                {"task": "report", "status": "done"},
            ]

            for row in sheet_rows:
                if row["task"] == "backup":
                    row["status"] = "done"

            print(sheet_rows)
            """,
        )
    ],
    16: [
        (
            "Practice: tiny SQLite project",
            """
            import sqlite3

            connection = sqlite3.connect(":memory:")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE tasks (name TEXT, done INTEGER)")
            cursor.executemany("INSERT INTO tasks VALUES (?, ?)", [("backup", 0), ("report", 1), ("email", 0)])

            cursor.execute("SELECT name FROM tasks WHERE done = ?", (0,))
            print(cursor.fetchall())
            connection.close()
            """,
        )
    ],
    17: [
        (
            "Practice: document paragraph assembly",
            """
            title = "Weekly Report"
            bullets = ["Backups completed", "Invoices checked", "Three follow-ups pending"]

            document_text = [title, "=" * len(title), ""]
            for bullet in bullets:
                document_text.append(f"- {bullet}")

            print("\\n".join(document_text))
            """,
        )
    ],
    18: [
        (
            "Practice: CSV to JSON transformation",
            """
            import csv
            import io
            import json

            csv_text = "name,score\\nAda,98\\nGrace,95\\nLinus,91\\n"
            rows = list(csv.DictReader(io.StringIO(csv_text)))

            for row in rows:
                row["score"] = int(row["score"])

            print(json.dumps(rows, indent=2))
            """,
        )
    ],
    19: [
        (
            "Practice: elapsed time measurement",
            """
            import time

            start = time.time()
            total = sum(range(1_000_000))
            elapsed = time.time() - start

            print("Total:", total)
            print(f"Elapsed seconds: {elapsed:.4f}")
            """,
        )
    ],
    20: [
        (
            "Practice: notification message builder",
            """
            def build_status_message(job_name, success, details):
                status = "SUCCESS" if success else "NEEDS ATTENTION"
                return f"[{status}] {job_name}: {details}"

            print(build_status_message("Nightly backup", True, "12 files archived."))
            print(build_status_message("Invoice scan", False, "Missing March invoice."))
            """,
        )
    ],
}


cells = [
    md(
        """
        # Automate the Boring Stuff: Chapters 11-20 Source Map, Context, and Practice

        This notebook continues the chapter-by-chapter companion format for chapters 11-20
        of Al Sweigart's *Automate the Boring Stuff with Python*, 3rd edition.

        Official book site: https://automatetheboringstuff.com/

        Each source-mapped example includes:

        - The chapter and section where it appears.
        - A preview of the source block.
        - A 4-line explanation of purpose, concept, real-world importance, and caution.
        - Either a runnable adapted cell or a practice rewrite cell for examples that need
          external files, websites, credentials, installed apps, or user input.

        Later chapters automate real systems. Use sample files, fake accounts, and test
        sandboxes before running anything against your real data.
        """
    ),
    code(
        """
        import csv
        import io
        import json
        import logging
        import random
        import re
        import sqlite3
        import tempfile
        import time
        from pathlib import Path
        from pprint import pprint

        print("Setup complete.")
        """
    ),
]


chapters = [fetch_chapter(ch) for ch in range(11, 21)]

cells.append(md("## Coverage Summary"))
cells.append(
    md(
        "\n".join(
            f"- {chapter['title']}: {len(chapter['blocks'])} code blocks mapped from {chapter['url']}"
            for chapter in chapters
        )
    )
)


for chapter_num, chapter in zip(range(11, 21), chapters):
    cells.append(md(f"## {chapter['title']}\n\nSource: {chapter['url']}"))
    current_section = None
    for block_index, block in enumerate(chapter["blocks"], start=1):
        if block["section"] != current_section:
            current_section = block["section"]
            cells.append(md(f"### {current_section}"))

        raw = block["raw"]
        cleaned = block["cleaned"]
        cells.append(md(source_example_markdown(chapter_num, block_index, block, raw)))

        if cleaned and looks_runnable(cleaned):
            cells.append(code(f"# Adapted from source example {chapter_num}.{block_index}\n" + cleaned))
        else:
            cells.append(
                md(
                    "Study transcript or context-dependent example:\n\n"
                    + "```python\n"
                    + raw.replace("```", "'''")
                    + "\n```"
                )
            )
            cells.append(
                code(
                    f"""
                    # Practice rewrite for source example {chapter_num}.{block_index}
                    # Goal: recreate the idea using safe sample data before using real files/accounts.
                    """
                )
            )

    cells.append(md(f"### Chapter {chapter_num} Practice Checkpoint"))
    cells.append(
        code(
            f"""
            # Chapter {chapter_num} checkpoint
            # Choose three source examples from this chapter.
            # For each one:
            # 1. Explain what input it expects.
            # 2. Explain what output or side effect it creates.
            # 3. Rewrite it with safe sample data.
            """
        )
    )
    if chapter_num in extra_practice:
        cells.append(md(f"### Extra Practice for Chapter {chapter_num}"))
        for title, source in extra_practice[chapter_num]:
            cells.append(md(f"#### {title}"))
            cells.append(code(source))


cells.extend(
    [
        md(
            """
            ## Capstone: Office Automation Pipeline

            This project combines the next-ten-chapter skills without requiring real email,
            Google credentials, Excel files, or web access. It simulates a practical workflow:
            collect records, store them in SQLite, export JSON/CSV, and build a notification
            message.
            """
        ),
        code(
            """
            raw_csv = '''name,department,hours,rate
            Ada,Engineering,6,75
            Grace,Operations,8,65
            Linus,Infrastructure,5,80
            '''

            records = list(csv.DictReader(io.StringIO(raw_csv)))
            for record in records:
                record["hours"] = int(record["hours"])
                record["rate"] = int(record["rate"])
                record["pay"] = record["hours"] * record["rate"]

            pprint(records)
            """
        ),
        code(
            """
            database = sqlite3.connect(":memory:")
            cursor = database.cursor()
            cursor.execute(
                "CREATE TABLE payroll (name TEXT, department TEXT, hours INTEGER, rate INTEGER, pay INTEGER)"
            )
            cursor.executemany(
                "INSERT INTO payroll VALUES (:name, :department, :hours, :rate, :pay)",
                records,
            )

            cursor.execute("SELECT department, SUM(pay) FROM payroll GROUP BY department")
            pprint(cursor.fetchall())
            """
        ),
        code(
            """
            output_dir = Path(tempfile.gettempdir()) / "atsbs_ch11_20_capstone"
            output_dir.mkdir(exist_ok=True)

            json_path = output_dir / "payroll.json"
            csv_path = output_dir / "payroll.csv"

            json_path.write_text(json.dumps(records, indent=2), encoding="utf-8")

            with csv_path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "department", "hours", "rate", "pay"])
                writer.writeheader()
                writer.writerows(records)

            print(json_path)
            print(csv_path)
            """
        ),
        code(
            """
            total_pay = sum(record["pay"] for record in records)
            message = f"[SUCCESS] Payroll export complete: {len(records)} records, total ${total_pay:,.2f}."
            print(message)

            # Real-world next step:
            # Send this message through email, SMS, Slack, or a push notification service.
            """
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
    "# Automate the Boring Stuff Chapters 11-20 Coverage Index",
    "",
    "This index lists every source code block mapped into the context notebook.",
    "",
]
for chapter_num, chapter in zip(range(11, 21), chapters):
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
            f"- {chapter_num}.{block_index} | {block['section']} | {compact_summary(block['raw'], 120)}"
        )
    coverage_lines.append("")

COVERAGE_OUT.write_text("\n".join(coverage_lines), encoding="utf-8")

print(OUT)
print(COVERAGE_OUT)
print(f"cells={len(cells)}")
