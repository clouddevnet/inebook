import ast
import json
from pathlib import Path
from textwrap import dedent

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "automate_boring_stuff_ch21_24_source_map_context_practice.ipynb"
COVERAGE_OUT = ROOT / "automate_boring_stuff_ch21_24_coverage_index.md"
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
        "pyautogui",
        "pytesseract",
        "pyperclip",
        "webbrowser.",
        "subprocess.",
        "speech_recognition",
        "pyttsx3",
        "gTTS",
        "playsound",
        "Image.open(",
        "cv2.",
        "plt.show(",
        "time.sleep(",
        "Path.home()",
        "open(",
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
        21: "making graphs and manipulating images",
        22: "recognizing text in images with OCR",
        23: "controlling the keyboard and mouse",
        24: "text-to-speech and speech recognition",
    }[chapter_num]


def prior_link(chapter_num):
    return {
        21: "This chapter builds on lists, dictionaries, files, and external packages: data becomes a chart or an image output instead of plain text.",
        22: "This chapter extends image handling from chapter 21 and text processing from chapters 8-10: pixels become text you can clean, search, and save.",
        23: "This chapter combines loops, timing, coordinates, and safety checks to automate actions in other programs when no clean API exists.",
        24: "This chapter connects strings, files, external services, and notifications: programs can speak text or turn spoken input into text.",
    }[chapter_num]


def flow_diagram(chapter_num):
    return {
        21: "data/image file -> load/inspect -> transform/draw/chart -> save/display result",
        22: "image/screenshot -> OCR engine -> raw text -> clean/search/save",
        23: "screen state -> mouse/keyboard action -> wait/check -> repeat safely",
        24: "text/audio -> speech engine/API -> spoken audio/transcript -> respond/save",
    }[chapter_num]


def context_lines(chapter_num, section, raw):
    text = raw.lower()
    topic = topic_for(chapter_num)
    purpose = f"This example belongs to the chapter on {topic}, from the section `{section}`."
    concept = "Focus on what object is being controlled: a data series, an image, the screen, the mouse, the keyboard, text, or audio."
    link = prior_link(chapter_num)
    importance = "In real automation work, this is where scripts start interacting with visual outputs and human-facing tools."
    caution = "Use safe sample data and test slowly, especially when automation can move the mouse, type, open files, or call services."

    if "matplotlib" in text or "plt." in text or "plot" in text or "chart" in text:
        purpose = "This example shows how to turn numbers into a visual chart."
        concept = "The key idea is mapping structured values into axes, labels, marks, and a saved or displayed figure."
        importance = "Charts help automation produce reports that people can understand quickly."
    elif "pillow" in text or "image" in text or "rgba" in text or "crop" in text or "resize" in text:
        purpose = "This example demonstrates image automation: opening, resizing, cropping, drawing, or saving image files."
        concept = "An image becomes data your program can inspect and change pixel by pixel or region by region."
        importance = "This is useful for thumbnails, badges, screenshots, watermarks, OCR prep, and batch media cleanup."
    elif "pytesseract" in text or "ocr" in text:
        purpose = "This example shows OCR: extracting text from an image."
        concept = "OCR turns visual pixels into strings, which lets you reuse string, regex, and file skills from earlier chapters."
        importance = "That matters for receipts, screenshots, scanned forms, labels, and other image-only text."
    elif "pyautogui" in text or "click" in text or "hotkey" in text or "screenshot" in text:
        purpose = "This example demonstrates GUI automation through mouse, keyboard, or screenshots."
        concept = "The script treats the screen as the interface and performs the same actions a person would."
        importance = "This helps when a task is trapped inside an app or website that has no API."
        caution = "Keep failsafe behavior enabled and test in harmless windows before automating real work."
    elif "speech" in text or "pyttsx3" in text or "gtts" in text or "microphone" in text:
        purpose = "This example demonstrates speech automation: converting text to audio or audio to text."
        concept = "The program turns strings into spoken output, or spoken input back into strings for later processing."
        importance = "This can support accessibility tools, voice notes, reminders, alerts, and hands-free workflows."
        caution = "Speech examples often require microphones, speakers, internet services, or local system voices."

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
    21: [
        (
            "Practice: create chart data without external plotting",
            """
            monthly_sales = {"Jan": 120, "Feb": 150, "Mar": 90, "Apr": 180}

            for month, value in monthly_sales.items():
                bar = "#" * (value // 10)
                print(f"{month}: {bar} {value}")

            # Next step:
            # Replace this ASCII chart with matplotlib when you are ready.
            """,
        ),
        (
            "Practice: image batch plan",
            """
            image_files = ["logo.png", "header.jpg", "avatar.png"]
            planned_actions = []

            for filename in image_files:
                if filename.endswith(".png"):
                    planned_actions.append((filename, "resize to 512x512 and keep transparency"))
                else:
                    planned_actions.append((filename, "resize to 1200px wide and convert to jpg"))

            for filename, action in planned_actions:
                print(f"{filename}: {action}")
            """,
        ),
    ],
    22: [
        (
            "Practice: clean OCR-like text",
            """
            raw_ocr = '''
            INVOICE # 1007
            Tota1: $48.50
            Due Date: 2026-O5-21
            '''

            cleaned = raw_ocr.replace("Tota1", "Total").replace("O5", "05")
            lines = [line.strip() for line in cleaned.splitlines() if line.strip()]

            for line in lines:
                print(line)
            """,
        )
    ],
    23: [
        (
            "Practice: plan GUI automation before clicking",
            """
            steps = [
                {"action": "open app", "wait": 2},
                {"action": "click search box", "wait": 1},
                {"action": "type customer name", "wait": 1},
                {"action": "press enter", "wait": 3},
                {"action": "copy result", "wait": 1},
            ]

            for number, step in enumerate(steps, start=1):
                print(f"{number}. {step['action']} (wait {step['wait']}s)")

            # Real GUI automation should first print or log planned steps.
            """,
        )
    ],
    24: [
        (
            "Practice: voice command parser",
            """
            commands = [
                "open report",
                "send reminder to Alex",
                "stop",
            ]

            for command in commands:
                words = command.split()
                if words[0] == "open":
                    print("Opening:", " ".join(words[1:]))
                elif words[0] == "send":
                    print("Preparing message:", command)
                elif words[0] == "stop":
                    print("Stopping listener")
            """,
        )
    ],
}


cells = [
    md(
        """
        # Automate the Boring Stuff: Chapters 21-24 Source Map, Context, and Practice

        This notebook covers the remaining numbered chapters of Al Sweigart's
        *Automate the Boring Stuff with Python*, 3rd edition.

        Official book site: https://automatetheboringstuff.com/

        Each mapped source example includes:

        - Easy-to-read context.
        - A link back to earlier chapter concepts.
        - An ASCII concept flow.
        - A clean fenced code preview.
        - A runnable adapted cell or a safe rewrite cell.

        These chapters touch visual output, screenshots, OCR, GUI control, and speech.
        Practice with fake data and harmless windows before using real files or real apps.
        """
    ),
    code(
        """
        import csv
        import io
        import json
        import random
        import re
        import tempfile
        import time
        from pathlib import Path
        from pprint import pprint

        print("Setup complete.")
        """
    ),
]


chapters = [fetch_chapter(ch) for ch in range(21, 25)]

cells.append(md("## Coverage Summary"))
cells.append(
    md(
        "\n".join(
            f"- {chapter['title']}: {len(chapter['blocks'])} code blocks mapped from {chapter['url']}"
            for chapter in chapters
        )
    )
)


for chapter_num, chapter in zip(range(21, 25), chapters):
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
                    # Goal: recreate the idea safely with fake data, sample files, or a harmless test window.
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
            # 1. Identify the input: data, image, screen, audio, or file.
            # 2. Identify the output or side effect.
            # 3. Rewrite a safe version using fake data or a sandbox.
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
            ## Final Capstone: Human-Facing Automation Plan

            The last chapters teach Python to communicate through visual reports,
            images, screenshots, mouse/keyboard actions, and speech. This capstone
            uses safe simulated data to design that kind of workflow before touching
            real applications.
            """
        ),
        code(
            """
            workflow = [
                {"stage": "collect", "input": "CSV export", "output": "clean records"},
                {"stage": "visualize", "input": "clean records", "output": "chart image"},
                {"stage": "extract", "input": "screenshot", "output": "OCR text"},
                {"stage": "act", "input": "validated text", "output": "GUI steps"},
                {"stage": "notify", "input": "result summary", "output": "spoken or sent message"},
            ]

            for step in workflow:
                print(f"{step['stage']:<10} {step['input']} -> {step['output']}")
            """
        ),
        code(
            """
            results = {
                "records_processed": 42,
                "chart_created": True,
                "ocr_lines_found": 7,
                "manual_review_needed": 2,
            }

            message = (
                f"Automation complete. Processed {results['records_processed']} records, "
                f"found {results['ocr_lines_found']} OCR lines, "
                f"and flagged {results['manual_review_needed']} items for review."
            )

            print(message)
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
    "# Automate the Boring Stuff Chapters 21-24 Coverage Index",
    "",
    "This index lists every source code block mapped into the context notebook.",
    "",
]
for chapter_num, chapter in zip(range(21, 25), chapters):
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
