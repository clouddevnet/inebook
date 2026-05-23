import ast
import json
import re
import subprocess
import tempfile
from pathlib import Path
from textwrap import dedent

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
PDF_PATH = Path(r"C:\Users\jag\Downloads\Python Crash Course - 3rd Edition - Eric Matthes.pdf")
GITHUB_REPO_URL = "https://github.com/ehmatthes/pcc_3e"
GITHUB_REF = "main"
GITHUB_CACHE = Path(tempfile.gettempdir()) / "pcc_3e_source"
SOURCE_EXTENSIONS = {
    ".py": "python",
    ".html": "html",
    ".css": "css",
    ".js": "javascript",
    ".json": "json",
    ".txt": "text",
    ".md": "markdown",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".toml": "toml",
}

PARTS = [
    {
        "name": "part1_ch1_11",
        "title": "Python Crash Course Part I: Chapters 1-11",
        "start": 1,
        "end": 11,
        "out": ROOT / "python_crash_course_part1_ch1_11_source_map_context_practice.ipynb",
        "coverage": ROOT / "python_crash_course_part1_ch1_11_coverage_index.md",
    },
    {
        "name": "part2_ch12_20",
        "title": "Python Crash Course Part II: Chapters 12-20",
        "start": 12,
        "end": 20,
        "out": ROOT / "python_crash_course_part2_ch12_20_source_map_context_practice.ipynb",
        "coverage": ROOT / "python_crash_course_part2_ch12_20_coverage_index.md",
    },
    {
        "name": "appendices",
        "title": "Python Crash Course Appendices A-C",
        "appendices": True,
        "out": ROOT / "python_crash_course_appendices_source_map_context_practice.ipynb",
        "coverage": ROOT / "python_crash_course_appendices_coverage_index.md",
    },
]


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


def flatten_outline(reader):
    rows = []

    def walk(items, depth=0):
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
            else:
                try:
                    page = reader.get_destination_page_number(item) + 1
                except Exception:
                    page = None
                rows.append({"title": getattr(item, "title", str(item)), "page": page, "depth": depth})

    walk(reader.outline)
    return rows


def build_units(reader):
    outline = flatten_outline(reader)
    units = []
    unit_pattern = re.compile(r"^(Chapter\s+\d+:|Appendix\s+[A-C]:)")
    main = [row for row in outline if row["page"] and unit_pattern.match(row["title"])]
    for idx, row in enumerate(main):
        next_page = main[idx + 1]["page"] if idx + 1 < len(main) else len(reader.pages) + 1
        if row["title"].startswith("Chapter"):
            number = int(re.search(r"Chapter\s+(\d+):", row["title"]).group(1))
            kind = "chapter"
        else:
            number = re.search(r"Appendix\s+([A-C]):", row["title"]).group(1)
            kind = "appendix"
        sections = [
            sec
            for sec in outline
            if sec["page"] and row["page"] <= sec["page"] < next_page and sec["title"] != row["title"]
        ]
        units.append(
            {
                "kind": kind,
                "number": number,
                "title": row["title"],
                "start_page": row["page"],
                "end_page": next_page - 1,
                "sections": sections,
            }
        )
    return units


def nearest_section(unit, page):
    candidates = [s for s in unit["sections"] if s["page"] <= page]
    if not candidates:
        return unit["title"]
    return candidates[-1]["title"]


def extract_code_blocks(reader, page_num):
    """Extract left-aligned monospace snippets from one 1-indexed PDF page."""
    chunks = []

    def visitor(text, cm, tm, font_dict, font_size):
        name = str((font_dict or {}).get("/BaseFont", "?")) if font_dict else "?"
        if "Mono" not in name or not text.strip():
            return
        x = float(tm[4])
        y = float(tm[5])
        if x <= 170:
            chunks.append((y, x, text.rstrip("\n")))

    reader.pages[page_num - 1].extract_text(visitor_text=visitor)
    chunks.sort()

    raw_blocks = []
    current = []
    last_y = None
    for y, x, text in chunks:
        if last_y is None or abs(y - last_y) <= 30:
            current.append((y, x, text))
        else:
            if current:
                raw_blocks.append(current)
            current = [(y, x, text)]
        last_y = y
    if current:
        raw_blocks.append(current)

    blocks = []
    for block in raw_blocks:
        lines = [text for _, _, text in block]
        text = "\n".join(lines).strip()
        if not text:
            continue
        looks_like_code = (
            len(lines) >= 2
            or any(symbol in text for symbol in "=()[]{}:.#$")
            or text.startswith((">>>", "...", "import", "from", "class", "def"))
        )
        if looks_like_code:
            blocks.append(text)
    return blocks


def code_preview(text, max_lines=14):
    lines = text.strip("\n").splitlines()
    preview = "\n".join(lines[:max_lines])
    if len(lines) > max_lines:
        preview += f"\n# ... {len(lines) - max_lines} more line(s) in this source example"
    return preview.replace("```", "'''")


def compact_summary(text, max_len=120):
    one_line = " ".join(text.split())
    if len(one_line) <= max_len:
        return one_line
    return one_line[: max_len - 3] + "..."


def safe_cell_source(source):
    cleaned = source.replace("❶", "").replace("❷", "").replace("❸", "").replace("❹", "").replace("❺", "")
    cleaned = "\n".join(line for line in cleaned.splitlines() if not line.lstrip().startswith("$"))
    return cleaned.strip()


def looks_runnable(source, unit):
    cleaned = safe_cell_source(source)
    if not cleaned:
        return False
    risky = [
        "input(",
        "pygame",
        "django",
        "requests.",
        "httpx",
        "matplotlib",
        "plotly",
        "open(",
        "Path(",
        "os.",
        "sys.exit",
        "subprocess",
        "API_KEY",
        "SECRET_KEY",
        "manage.py",
        "pytest",
        "unittest",
    ]
    if any(token in cleaned for token in risky):
        return False
    if cleaned.count("(") != cleaned.count(")"):
        return False
    try:
        ast.parse(cleaned)
    except SyntaxError:
        return False
    if unit["kind"] == "chapter" and unit["number"] >= 12:
        return False
    return True


def topic_for(unit):
    if unit["kind"] == "appendix":
        return {
            "A": "installation and troubleshooting",
            "B": "text editors and IDEs",
            "C": "getting help and asking good questions",
        }[unit["number"]]
    return {
        1: "getting Python installed and running code",
        2: "variables, strings, numbers, and comments",
        3: "introducing lists",
        4: "working through lists with loops, ranges, slices, and comprehensions",
        5: "if statements and conditional logic",
        6: "dictionaries and structured data",
        7: "user input and while loops",
        8: "functions",
        9: "classes and object-oriented thinking",
        10: "files, exceptions, and saved data",
        11: "testing your code",
        12: "starting the Alien Invasion game with Pygame",
        13: "adding aliens and gameplay movement",
        14: "scoring, levels, and play buttons",
        15: "generating data and visualizations",
        16: "downloading and visualizing real-world data",
        17: "working with APIs",
        18: "starting a Django web app",
        19: "adding user accounts and protected data",
        20: "styling and deploying a Django app",
    }[unit["number"]]


def prior_link(unit):
    if unit["kind"] == "appendix":
        return "This section supports the whole book: setup, editor habits, and help-seeking make every later coding task easier to finish."
    number = unit["number"]
    links = {
        1: "This is the launchpad: every later chapter assumes you can run small programs and read their output.",
        2: "This builds the vocabulary of programs: values, names, strings, numbers, and comments.",
        3: "This builds on variables by storing many related values under one name.",
        4: "This builds on lists by repeating actions, creating numeric sequences, and working with subsets.",
        5: "This builds on earlier values and lists by teaching programs to make decisions.",
        6: "This builds on lists by adding meaningful keys, which makes records easier to model.",
        7: "This connects strings, conditionals, and loops to interactive programs that keep running until a goal is met.",
        8: "This packages previous ideas into reusable named actions, making larger programs manageable.",
        9: "This extends functions and dictionaries into objects that keep related data and behavior together.",
        10: "This connects earlier data structures to files, errors, and persistence beyond one run.",
        11: "This builds confidence in functions and classes by checking behavior automatically.",
        12: "This begins the project phase by combining classes, functions, loops, conditionals, and external libraries.",
        13: "This grows the game by adding repeated objects, collision checks, and state changes.",
        14: "This adds user experience and game state, connecting classes, conditionals, and persistent scores.",
        15: "This reuses lists, loops, dictionaries, and files to turn data into visual insight.",
        16: "This builds on data visualization by pulling in real-world datasets from files and online sources.",
        17: "This builds on dictionaries, JSON, requests, and error handling to work with live web APIs.",
        18: "This starts the web project by applying functions, classes, files, and databases inside Django's structure.",
        19: "This builds on Django basics by adding authentication, ownership, forms, and user-specific records.",
        20: "This finishes the web app by connecting earlier Django work to styling, deployment, and production settings.",
    }
    return links[number]


def flow_diagram(unit):
    if unit["kind"] == "appendix":
        return {
            "A": "problem -> check install/path/version -> adjust setup -> rerun",
            "B": "choose editor -> configure Python tools -> run file -> iterate",
            "C": "stuck point -> isolate example -> search/ask clearly -> apply fix",
        }[unit["number"]]
    return {
        1: "editor/terminal -> Python interpreter -> program output",
        2: "value -> variable name -> operation/method -> printed result",
        3: "list -> index/slice/method -> selected or changed item",
        4: "collection/range -> loop/comprehension -> repeated transformation",
        5: "data -> condition -> if/elif/else branch -> action",
        6: "real object -> dictionary keys/values -> lookup/update/loop",
        7: "prompt/input -> convert/validate -> while loop -> result",
        8: "arguments -> function body -> return/side effect -> reuse",
        9: "class blueprint -> object instance -> attributes/methods -> behavior",
        10: "file/user data -> read/parse -> handle errors -> save result",
        11: "expected behavior -> test case -> run test -> fix code",
        12: "game class -> event loop -> draw/update screen -> repeat",
        13: "fleet/list of sprites -> update positions -> detect collisions -> respond",
        14: "game state -> button/score/level -> update display -> continue/reset",
        15: "generated data -> list/dict -> chart library -> visualization",
        16: "downloaded/file data -> parse -> clean -> plot/map",
        17: "API endpoint -> request -> JSON/dicts -> process/display",
        18: "Django project -> app/model/view/template -> web page",
        19: "user account -> form/authentication -> owned data -> protected view",
        20: "local app -> style/configure -> deploy -> production URL",
    }[unit["number"]]


def context_lines(unit, section, raw):
    text = raw.lower()
    purpose = f"This example belongs to {topic_for(unit)}, from the section `{section}`."
    concept = "Look for the input, the operation being demonstrated, and the visible result or side effect."
    link = prior_link(unit)
    importance = "The author's pattern is incremental: introduce one small idea, run it, then combine it into a larger program."
    caution = "Change one value at a time and predict the output before running; that habit turns examples into understanding."

    if "for " in text or "while " in text:
        purpose = "This example demonstrates repeated work, which is one of the main ways programs remove manual effort."
    elif "if " in text or "elif " in text or "else" in text:
        purpose = "This example demonstrates decision-making, where the program chooses a path based on data."
    elif "def " in text:
        purpose = "This example demonstrates a function: a named, reusable block of behavior."
    elif "class " in text or "self." in text:
        purpose = "This example demonstrates object-oriented structure: data and behavior grouped together."
    elif "with open" in text or "json" in text or "exception" in text or "except" in text:
        purpose = "This example demonstrates working with outside data and handling things that can go wrong."
    elif "assert" in text or "pytest" in text or "unittest" in text:
        purpose = "This example demonstrates testing: describing expected behavior so code can be checked automatically."
    elif "pygame" in text:
        purpose = "This example demonstrates game programming with a visible event loop and screen updates."
    elif "django" in text or "model" in text or "view" in text or "template" in text:
        purpose = "This example demonstrates web app structure: data models, views, templates, URLs, or deployment settings."
    elif "requests" in text or "api" in text:
        purpose = "This example demonstrates asking another web service for data and turning the response into Python objects."
    elif "plot" in text or "matplotlib" in text or "csv" in text:
        purpose = "This example demonstrates turning data into a readable report or visualization."

    return [purpose, concept, link, importance, caution]


def source_example_markdown(unit, block_index, block):
    lines = context_lines(unit, block["section"], block["raw"])
    label = f"{unit['number']}.{block_index}" if unit["kind"] == "chapter" else f"{unit['number']}.{block_index}"
    if block["origin"] == "GitHub":
        source_note = f"official GitHub source `{block['path']}`"
    else:
        source_note = f"PDF page {block['page']}, section **{block['section']}**"
    return "\n".join(
        [
            f"#### Source example {label}",
            "",
            f"Checklist note: captured from **{unit['title']}**, {source_note}.",
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
            flow_diagram(unit),
            "```",
            "",
            "**Code Preview**",
            "",
            f"```{block.get('language', 'python')}",
            code_preview(block["raw"]),
            "```",
        ]
    )


def extract_unit_blocks(reader, unit):
    blocks = []
    for page in range(unit["start_page"], unit["end_page"] + 1):
        for raw in extract_code_blocks(reader, page):
            blocks.append(
                {
                    "page": page,
                    "section": nearest_section(unit, page),
                    "raw": raw,
                    "origin": "PDF",
                    "language": "python",
                    "path": None,
                }
            )
    return blocks


def sync_github_repo():
    """Clone or update the official source repo used to replace PDF snippets."""
    if GITHUB_CACHE.exists():
        subprocess.run(["git", "-C", str(GITHUB_CACHE), "fetch", "--depth=1", "origin", GITHUB_REF], check=True)
        subprocess.run(["git", "-C", str(GITHUB_CACHE), "checkout", "-q", "FETCH_HEAD"], check=True)
    else:
        subprocess.run(["git", "clone", "--depth=1", "--branch", GITHUB_REF, GITHUB_REPO_URL + ".git", str(GITHUB_CACHE)], check=True)
    return subprocess.check_output(["git", "-C", str(GITHUB_CACHE), "rev-parse", "--short", "HEAD"], text=True).strip()


def sort_key_for_path(path):
    parts = path.parts
    priority = 0
    if "partial_programs" in parts:
        priority = 1
    elif "solution_files" in parts:
        priority = 3
    return (priority, [part.lower() for part in parts])


def section_for_source_path(relative_path):
    parent = relative_path.parent
    if str(parent) == ".":
        return "Official source files"
    readable = " / ".join(part.replace("_", " ").title() for part in parent.parts)
    return readable


def collect_github_blocks(unit):
    if unit["kind"] != "chapter":
        return []
    chapter_dir = GITHUB_CACHE / f"chapter_{unit['number']:02d}"
    if not chapter_dir.exists():
        return []

    files = [
        path
        for path in chapter_dir.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SOURCE_EXTENSIONS
        and "__pycache__" not in path.parts
    ]

    blocks = []
    for path in sorted(files, key=lambda item: sort_key_for_path(item.relative_to(chapter_dir))):
        try:
            raw = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raw = path.read_text(encoding="utf-8-sig")
        raw = raw.strip("\n")
        if not raw:
            continue
        relative_path = path.relative_to(chapter_dir)
        blocks.append(
            {
                "page": None,
                "section": section_for_source_path(relative_path),
                "raw": raw,
                "origin": "GitHub",
                "language": SOURCE_EXTENSIONS[path.suffix.lower()],
                "path": str(Path(f"chapter_{unit['number']:02d}") / relative_path).replace("\\", "/"),
            }
        )
    return blocks


def source_summary_for(unit):
    origins = {block["origin"] for block in unit["blocks"]}
    if origins == {"GitHub"}:
        return f"official GitHub files under chapter_{unit['number']:02d}"
    if origins == {"PDF"}:
        return f"PDF pages {unit['start_page']}-{unit['end_page']}"
    return f"GitHub files plus PDF pages {unit['start_page']}-{unit['end_page']}"


def extra_practice_for(unit):
    if unit["kind"] == "appendix":
        return [
            (
                "Practice: troubleshooting checklist",
                """
                checks = [
                    "Can Python run from the terminal?",
                    "Can the editor run the current file?",
                    "Can you reproduce the error with a tiny example?",
                    "Did you copy the exact traceback?",
                ]

                for number, check in enumerate(checks, start=1):
                    print(f"{number}. {check}")
                """,
            )
        ]
    number = unit["number"]
    if number <= 11:
        return [
            (
                "Practice: explain and mutate",
                """
                # Pick one example above.
                # 1. Write what each line does in plain English.
                # 2. Change one value.
                # 3. Predict the output.
                # 4. Run it and compare your prediction.
                """,
            )
        ]
    return [
        (
            "Practice: project-safe rewrite",
            """
            # Project chapters often depend on installed packages, files, servers, or assets.
            # Rewrite one source example with fake data first:
            # - replace file/API/game/web inputs with a small list or dictionary
            # - print the planned action
            # - only then connect it back to the real project
            planned_steps = ["identify input", "transform state", "show or save result"]
            for step in planned_steps:
                print(step)
            """,
        )
    ]


def build_notebook(part, units):
    cells = [
        md(
            f"""
            # {part['title']} Source Map, Context, and Practice

            Source PDF: `{PDF_PATH}`
            Official script source: `{GITHUB_REPO_URL}`

            This notebook follows the same study format as the Automate the Boring Stuff
            notebooks: source-map order, readable context, link to earlier ideas, ASCII
            concept flow, clean code preview, and safe practice/rewrite cells.

            Extraction note: chapter examples come from the official GitHub source files,
            with the PDF outline used for chapter titles and context. Appendix examples
            still come from PDF monospace snippets because the source repository does not
            provide matching appendix scripts. Use the coverage index to audit every block.
            """
        ),
        code(
            """
            import json
            import random
            import re
            import tempfile
            from pathlib import Path
            from pprint import pprint

            print("Setup complete.")
            """
        ),
    ]

    cells.append(md("## Coverage Summary"))
    cells.append(
        md(
            "\n".join(
                f"- {unit['title']}: {len(unit['blocks'])} captured source block(s) from {source_summary_for(unit)}"
                for unit in units
            )
        )
    )

    for unit in units:
        cells.append(md(f"## {unit['title']}\n\nPDF pages: {unit['start_page']}-{unit['end_page']}"))
        current_section = None
        for block_index, block in enumerate(unit["blocks"], start=1):
            if block["section"] != current_section:
                current_section = block["section"]
                cells.append(md(f"### {current_section}"))

            cells.append(md(source_example_markdown(unit, block_index, block)))
            if looks_runnable(block["raw"], unit):
                cells.append(code(f"# Adapted from source example {unit['number']}.{block_index}\n" + safe_cell_source(block["raw"])))
            else:
                cells.append(
                    md(
                        "Study transcript or context-dependent source block:\n\n"
                        + f"```{block.get('language', 'python')}\n"
                        + block["raw"].replace("```", "'''")
                        + "\n```"
                    )
                )
                cells.append(
                    code(
                        f"""
                        # Practice rewrite for source example {unit['number']}.{block_index}
                        # Recreate the idea safely with small sample data before using real project files.
                        """
                    )
                )

        cells.append(md(f"### {unit['title']} Practice Checkpoint"))
        for title, source in extra_practice_for(unit):
            cells.append(md(f"#### {title}"))
            cells.append(code(source))

    cells.append(
        md(
            """
            ## Final Study Routine

            For each chapter or appendix:

            1. Read the context.
            2. Trace the ASCII flow.
            3. Read the preview.
            4. Rewrite the example from memory.
            5. Change one thing and predict the result.
            """
        )
    )

    notebook = {
        "cells": cells,
        "metadata": {
            "colab": {"provenance": []},
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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
    return notebook


def write_coverage(part, units):
    lines = [
        f"# {part['title']} Coverage Index",
        "",
        f"Source PDF: `{PDF_PATH}`",
        f"Official script source: `{GITHUB_REPO_URL}`",
        "",
        "This index lists every captured source block.",
        "",
    ]
    for unit in units:
        lines.extend(
            [
                f"## {unit['title']}",
                "",
                f"Source: {source_summary_for(unit)}",
                f"PDF pages for outline/context: {unit['start_page']}-{unit['end_page']}",
                "",
                f"Captured blocks: {len(unit['blocks'])}",
                "",
            ]
        )
        for idx, block in enumerate(unit["blocks"], start=1):
            location = block["path"] if block["origin"] == "GitHub" else f"page {block['page']}"
            lines.append(
                f"- {unit['number']}.{idx} | {block['origin']} | {location} | {block['section']} | {compact_summary(block['raw'])}"
            )
        lines.append("")
    part["coverage"].write_text("\n".join(lines), encoding="utf-8")


def validate_notebook(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    failures = []
    code_cells = 0
    previews = 0
    flows = 0
    for index, cell in enumerate(notebook["cells"], start=1):
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            previews += source.count("**Code Preview**")
            flows += source.count("**Concept Flow**")
        if cell["cell_type"] == "code":
            code_cells += 1
            try:
                ast.parse(source)
            except SyntaxError as exc:
                failures.append((index, exc.msg))
    return {"cells": len(notebook["cells"]), "code_cells": code_cells, "previews": previews, "flows": flows, "failures": failures}


def main():
    source_rev = sync_github_repo()
    print(f"Using {GITHUB_REPO_URL} at {source_rev}")
    reader = PdfReader(str(PDF_PATH))
    units = build_units(reader)
    for unit in units:
        github_blocks = collect_github_blocks(unit)
        unit["blocks"] = github_blocks or extract_unit_blocks(reader, unit)

    for part in PARTS:
        if part.get("appendices"):
            selected = [unit for unit in units if unit["kind"] == "appendix"]
        else:
            selected = [
                unit
                for unit in units
                if unit["kind"] == "chapter" and part["start"] <= unit["number"] <= part["end"]
            ]
        notebook = build_notebook(part, selected)
        part["out"].write_text(json.dumps(notebook, indent=2), encoding="utf-8")
        write_coverage(part, selected)
        stats = validate_notebook(part["out"])
        print(part["out"])
        print(part["coverage"])
        print(stats)


if __name__ == "__main__":
    main()
