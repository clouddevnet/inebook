import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "automate_boring_stuff_first_10_chapters_practice.ipynb"


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
        "source": dedent(text).strip().splitlines(True),
    }


cells = [
    md(
        """
        # Automate the Boring Stuff: First 10 Chapters Practice Notebook

        This notebook is an original, practice-heavy companion for the first 10 chapters of
        Al Sweigart's *Automate the Boring Stuff with Python*, 3rd edition.

        It does not copy the chapters. Instead, it gives you the basics in a readable form,
        with runnable examples, exercises, and small automation-style projects.

        Official reference: https://automatetheboringstuff.com/

        Chapters covered:

        1. Python Basics
        2. if-else and Flow Control
        3. Loops
        4. Functions
        5. Debugging
        6. Lists
        7. Dictionaries and Structuring Data
        8. Strings and Text Editing
        9. Text Pattern Matching with Regular Expressions
        10. Reading and Writing Files
        """
    ),
    md(
        """
        ## How to use this notebook

        Run cells from top to bottom. Type your own answers in the practice cells before
        looking at the nearby sample solutions. In Google Colab, upload this `.ipynb` file
        and run it as-is.

        The best way to learn this material is to change the examples. Break them, read the
        errors, fix them, and then write a slightly different version.
        """
    ),
    code(
        """
        # Notebook setup
        from pathlib import Path
        import json
        import logging
        import random
        import re
        import tempfile
        import traceback
        from pprint import pprint

        print("Ready. Python is awake.")
        """
    ),
]


chapters = [
    (
        "1. Python Basics",
        "https://automatetheboringstuff.com/3e/chapter1.html",
        [
            "Expressions combine values and operators to produce one result.",
            "Common beginner types are `int`, `float`, `str`, and `bool`.",
            "`print()` displays values. `input()` reads text from the user.",
            "Convert user input with `int()`, `float()`, or `str()` before doing math.",
        ],
        [
            (
                "Expressions, operators, and types",
                """
                subtotal = 18.75
                tax_rate = 0.0825
                tip_rate = 0.18

                tax = subtotal * tax_rate
                tip = subtotal * tip_rate
                total = subtotal + tax + tip

                print("Subtotal:", subtotal)
                print("Tax:", round(tax, 2))
                print("Tip:", round(tip, 2))
                print("Total:", round(total, 2))
                print(type(total))
                """,
            ),
            (
                "Practice: convert minutes into hours and minutes",
                """
                total_minutes = 157

                hours = total_minutes // 60
                minutes = total_minutes % 60

                print(f"{total_minutes} minutes is {hours} hours and {minutes} minutes.")
                """,
            ),
        ],
        """
        Change `total_minutes` to several values, including `59`, `60`, `61`, and `1440`.
        Then write a small calculator that converts Fahrenheit to Celsius.
        Formula: `(fahrenheit - 32) * 5 / 9`.
        """,
    ),
    (
        "2. if-else and Flow Control",
        "https://automatetheboringstuff.com/3e/chapter2.html",
        [
            "Boolean expressions evaluate to `True` or `False`.",
            "`if`, `elif`, and `else` choose which block of code runs.",
            "`and`, `or`, and `not` combine conditions.",
            "Indentation is part of Python syntax.",
        ],
        [
            (
                "Decision making with conditions",
                """
                password = "swordfish"
                attempt = "Swordfish"

                if attempt == password:
                    print("Access granted")
                elif attempt.lower() == password:
                    print("Close: capitalization matters.")
                else:
                    print("Access denied")
                """,
            ),
            (
                "Practice: shipping cost rules",
                """
                order_total = 42
                is_member = True

                if order_total >= 50 or is_member:
                    shipping = 0
                elif order_total >= 25:
                    shipping = 5
                else:
                    shipping = 9

                print("Shipping:", shipping)
                """,
            ),
        ],
        """
        Add a new rule: if the order is above 100, print a message saying the customer
        earned a coupon. Try values around each boundary: 24, 25, 49, 50, 100, 101.
        """,
    ),
    (
        "3. Loops",
        "https://automatetheboringstuff.com/3e/chapter3.html",
        [
            "`while` repeats while a condition is true.",
            "`for` loops walk through a sequence like `range()` or a list.",
            "`break` exits a loop early. `continue` skips to the next iteration.",
            "Loops are perfect for repeated checks, counting, searching, and cleanup tasks.",
        ],
        [
            (
                "for loops and range",
                """
                total = 0
                for number in range(1, 101):
                    total += number

                print("Sum of 1 through 100:", total)
                """,
            ),
            (
                "while loop with a stopping condition",
                """
                target = 37
                guesses = [10, 25, 40, 37, 99]

                index = 0
                while index < len(guesses):
                    guess = guesses[index]
                    print("Trying", guess)
                    if guess == target:
                        print("Found it!")
                        break
                    index += 1
                """,
            ),
        ],
        """
        Write a loop that prints only the even numbers from 2 through 20.
        Then write another loop that keeps a running total of those even numbers.
        """,
    ),
    (
        "4. Functions",
        "https://automatetheboringstuff.com/3e/chapter4.html",
        [
            "Functions package code behind a name so you can reuse it.",
            "Parameters receive input. `return` sends a result back.",
            "Local variables live inside a function; global variables live outside it.",
            "Small functions are easier to test and debug.",
        ],
        [
            (
                "Create and call functions",
                """
                def format_receipt_item(name, price, quantity=1):
                    line_total = price * quantity
                    return f"{quantity} x {name:<12} ${line_total:>6.2f}"

                print(format_receipt_item("notebook", 3.5, 2))
                print(format_receipt_item("pen", 1.25, 4))
                print(format_receipt_item("sticker", 0.99))
                """,
            ),
            (
                "Practice: pure function for grading",
                """
                def letter_grade(score):
                    if score >= 90:
                        return "A"
                    if score >= 80:
                        return "B"
                    if score >= 70:
                        return "C"
                    if score >= 60:
                        return "D"
                    return "F"

                for score in [100, 89, 72, 60, 59]:
                    print(score, letter_grade(score))
                """,
            ),
        ],
        """
        Write a function named `is_strong_password(password)` that returns `True` only
        if the password has at least 8 characters, at least one lowercase letter, at least
        one uppercase letter, and at least one digit.
        """,
    ),
    (
        "5. Debugging",
        "https://automatetheboringstuff.com/3e/chapter5.html",
        [
            "Errors are clues. Read the last line of a traceback first.",
            "`try`/`except` lets your program handle expected failures.",
            "`assert` documents assumptions during development.",
            "`logging` gives you controlled diagnostic messages without scattering prints.",
        ],
        [
            (
                "Handle exceptions",
                """
                raw_values = ["42", "3.14", "oops", "100"]
                numbers = []

                for raw in raw_values:
                    try:
                        numbers.append(float(raw))
                    except ValueError:
                        print(f"Skipping non-number: {raw!r}")

                print(numbers)
                """,
            ),
            (
                "Use logging while developing",
                """
                logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

                def average(values):
                    assert values, "average() needs at least one value"
                    logging.info("Averaging %s values", len(values))
                    return sum(values) / len(values)

                print(average([10, 20, 30]))
                """,
            ),
        ],
        """
        Uncomment `print(average([]))` in the next cell after you create it. Read the
        assertion message, then change the function to raise `ValueError` instead.
        """,
    ),
    (
        "6. Lists",
        "https://automatetheboringstuff.com/3e/chapter6.html",
        [
            "Lists store ordered collections and can be changed.",
            "Use indexes, slices, `append`, `insert`, `remove`, `sort`, and `len` often.",
            "`for item in items` is usually cleaner than indexing by hand.",
            "Variables can refer to the same list; copy when you need independence.",
        ],
        [
            (
                "List operations",
                """
                tasks = ["email invoices", "rename files", "backup notes"]
                tasks.append("clean downloads")
                tasks.insert(1, "check calendar")

                print("First task:", tasks[0])
                print("Last two:", tasks[-2:])

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task.title()}")
                """,
            ),
            (
                "Practice: filter and transform",
                """
                file_names = ["report.docx", "photo.png", "budget.xlsx", "notes.txt", "logo.png"]
                image_files = []

                for name in file_names:
                    if name.endswith(".png"):
                        image_files.append(name)

                print(image_files)
                """,
            ),
        ],
        """
        Create a list of messy names like `[" ada ", "GRACE", "linus "]`.
        Build a new list with cleaned title-cased names: `["Ada", "Grace", "Linus"]`.
        """,
    ),
    (
        "7. Dictionaries and Structuring Data",
        "https://automatetheboringstuff.com/3e/chapter7.html",
        [
            "Dictionaries map keys to values.",
            "Use `.get()` for defaults and `.items()` for key/value loops.",
            "Nested dictionaries and lists can model real-world records.",
            "Good data shape makes the rest of the program simpler.",
        ],
        [
            (
                "Count things with a dictionary",
                """
                words = "spam eggs spam toast eggs spam".split()
                counts = {}

                for word in words:
                    counts[word] = counts.get(word, 0) + 1

                pprint(counts)
                """,
            ),
            (
                "Nested data",
                """
                contacts = {
                    "Ada": {"email": "ada@example.com", "tags": ["python", "math"]},
                    "Grace": {"email": "grace@example.com", "tags": ["systems", "debugging"]},
                }

                for name, info in contacts.items():
                    tags = ", ".join(info["tags"])
                    print(f"{name}: {info['email']} ({tags})")
                """,
            ),
        ],
        """
        Make an inventory dictionary such as `{"apples": 4, "bananas": 2}`.
        Write `add_to_inventory(inventory, item, amount)` and use it several times.
        """,
    ),
    (
        "8. Strings and Text Editing",
        "https://automatetheboringstuff.com/3e/chapter8.html",
        [
            "Strings are sequences of characters.",
            "Useful methods include `.strip()`, `.lower()`, `.upper()`, `.split()`, `.join()`, `.replace()`, `.startswith()`, and `.endswith()`.",
            "f-strings are the easiest way to format values into text.",
            "Many automation scripts are text cleanup scripts in disguise.",
        ],
        [
            (
                "Clean and format text",
                """
                raw_lines = [
                    "  alice@example.com  ",
                    "\\nBOB@EXAMPLE.COM",
                    " carol@example.com\\t",
                ]

                cleaned = []
                for line in raw_lines:
                    cleaned.append(line.strip().lower())

                print("; ".join(cleaned))
                """,
            ),
            (
                "Practice: simple report generator",
                """
                sales = [12.5, 9.99, 25, 3.5]
                total = sum(sales)
                report = f\"\"\"
                Sales Report
                ------------
                Transactions: {len(sales)}
                Total:        ${total:.2f}
                Average:      ${total / len(sales):.2f}
                \"\"\"

                print(report.strip())
                """,
            ),
        ],
        """
        Given `"last, first"` names, create `"First Last"` names.
        Example: `"lovelace, ada"` should become `"Ada Lovelace"`.
        """,
    ),
    (
        "9. Text Pattern Matching with Regular Expressions",
        "https://automatetheboringstuff.com/3e/chapter9.html",
        [
            "Regular expressions find text patterns that plain string methods cannot easily express.",
            "`re.search()` finds the first match; `re.findall()` finds all matches.",
            "Parentheses create groups. Character classes like `\\d` and `\\w` match categories.",
            "Use raw strings, such as `r'\\d+'`, for regex patterns.",
        ],
        [
            (
                "Find phone numbers and emails",
                r'''
                text = """
                Call Ada at 555-123-4567 or Grace at (555) 987-6543.
                Email help@example.com or admin.team@example.org.
                """

                phone_pattern = re.compile(r"(?:\(\d{3}\)|\d{3})[- ]\d{3}-\d{4}")
                email_pattern = re.compile(r"[\w.-]+@[\w.-]+\.\w+")

                print("Phones:", phone_pattern.findall(text))
                print("Emails:", email_pattern.findall(text))
                ''',
            ),
            (
                "Substitute sensitive text",
                r'''
                message = "My card is 4111-1111-1111-1111 and my backup is 5555-4444-3333-2222."
                redacted = re.sub(r"\b\d{4}-\d{4}-\d{4}-\d{4}\b", "[CARD REDACTED]", message)
                print(redacted)
                ''',
            ),
        ],
        """
        Write a regex that finds dates like `2026-05-21`.
        Then use groups to print year, month, and day separately.
        """,
    ),
    (
        "10. Reading and Writing Files",
        "https://automatetheboringstuff.com/3e/chapter10.html",
        [
            "`pathlib.Path` is a modern way to work with file paths.",
            "Use `with open(...)` or `Path.read_text()` / `Path.write_text()` for text files.",
            "Use JSON when you want simple structured data saved as text.",
            "Automation scripts often read input files, transform them, and write results.",
        ],
        [
            (
                "Create, read, and update a text file",
                """
                work_dir = Path(tempfile.gettempdir()) / "automate_practice"
                work_dir.mkdir(exist_ok=True)

                notes_path = work_dir / "notes.txt"
                notes_path.write_text("eggs\\nspam\\nspam\\n", encoding="utf-8")

                text = notes_path.read_text(encoding="utf-8")
                print(text)
                print("Saved at:", notes_path)
                """,
            ),
            (
                "Save structured data as JSON",
                """
                settings = {
                    "theme": "light",
                    "autosave": True,
                    "recent_files": ["notes.txt", "report.txt"],
                }

                settings_path = work_dir / "settings.json"
                settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")

                loaded = json.loads(settings_path.read_text(encoding="utf-8"))
                pprint(loaded)
                """,
            ),
        ],
        """
        Mini project: create a folder in the temp directory, write three `.txt` files,
        read them back, count all words, and save the counts to `word_counts.json`.
        """,
    ),
]


for title, url, bullets, examples, practice in chapters:
    cells.append(md(f"## Chapter {title}\n\nReference: {url}"))
    cells.append(md("\n".join(f"- {item}" for item in bullets)))
    for example_title, source in examples:
        cells.append(md(f"### {example_title}"))
        cells.append(code(source))
    cells.append(md(f"### Practice\n\n{practice.strip()}"))
    cells.append(code("# Your turn: write your solution here\n"))


cells.extend(
    [
        md(
            """
            ## Capstone Project: Personal Automation Toolkit

            This final section combines the first 10 chapters. You will clean messy text,
            extract useful patterns, organize the results in dictionaries and lists, and
            write files.
            """
        ),
        code(
            r'''
            messy_text = """
            Ada Lovelace <ada@example.com> called from 555-010-1000.
            Grace Hopper <grace@example.org> called from (555) 010-2000.
            Unknown contact used bad-email and 12345.
            Linus Torvalds <linus@example.net> called from 555-010-3000.
            """

            email_pattern = re.compile(r"[\w.-]+@[\w.-]+\.\w+")
            phone_pattern = re.compile(r"(?:\(\d{3}\)|\d{3})[- ]\d{3}-\d{4}")

            contacts = []
            for line in messy_text.strip().splitlines():
                emails = email_pattern.findall(line)
                phones = phone_pattern.findall(line)
                if emails and phones:
                    name = line.split("<")[0].strip()
                    contacts.append({"name": name, "email": emails[0], "phone": phones[0]})

            pprint(contacts)
            '''
        ),
        code(
            """
            output_dir = Path(tempfile.gettempdir()) / "automation_toolkit_output"
            output_dir.mkdir(exist_ok=True)

            csv_lines = ["name,email,phone"]
            for contact in contacts:
                csv_lines.append(f"{contact['name']},{contact['email']},{contact['phone']}")

            csv_path = output_dir / "contacts.csv"
            json_path = output_dir / "contacts.json"

            csv_path.write_text("\\n".join(csv_lines), encoding="utf-8")
            json_path.write_text(json.dumps(contacts, indent=2), encoding="utf-8")

            print("Wrote:")
            print(csv_path)
            print(json_path)
            """,
        ),
        md(
            """
            ## More practice ideas

            - Write a tip calculator that accepts a list of meal totals.
            - Build a number guessing game with input validation.
            - Rename a list of fake filenames into a consistent format.
            - Parse a block of text and extract emails, phone numbers, or dates.
            - Read a text file, count word frequency, and write the top 10 words to JSON.
            - Turn repeated code from any exercise into functions.
            - Add logging to one of your mini projects.
            - Add `try`/`except` around file reading and JSON parsing.
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
print(OUT)
