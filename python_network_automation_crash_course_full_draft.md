# Python Network Automation Crash Course



## Full Draft, Chapters 1-9



This Markdown draft was prepared from the provided chapter HTML files and normalized for book editing.


---


# Why Network Engineers Need Python (And Not the Other Way Around)

> "Any sufficiently advanced technology is indistinguishable from magic. But behind the magic is always a craftsperson." — Inspirational

> **Note:** 📝
Note
*"Any sufficiently advanced technology is indistinguishable from magic. But behind the magic is always a craftsperson."*

## Chapter Goal

Establish the business case for Python in network engineering — not as an academic exercise, but as a practical multiplier of everything you already know. By the end of this chapter, you will understand what Python can do that no amount of CLI proficiency can match, and what you actually need to learn (which is considerably less than you might fear).

**Key Points:**

- The hidden cost of manual network operations and why 70% of outages are human error
- Why Python specifically — the ecosystem, readability, and vendor alignment
- The automation mindset shift: from imperative to declarative thinking
- What level of Python you actually need (not a developer, but not CLI-only either)

## The Problem with Manual Operations

Let's be honest about what manual network operations actually look like at scale.

A change request arrives: add a new VLAN across forty access switches, update the description on all WAN-facing interfaces, or push a new NTP server configuration fleet-wide. A skilled network engineer opens their terminal emulator, pulls up their device list, and starts SSHing through the inventory one by one.

Device 1: connect, enter enable, enter config mode, type the commands, save, disconnect. Device 2: repeat. Device 3: repeat. By device 15, the mind wanders. By device 30, fatigue sets in. On device 37, a digit gets transposed.

That transposed digit is a misconfiguration. That misconfiguration causes a service impact. That service impact becomes an incident ticket. That incident ticket becomes an outage postmortem. And somewhere in that postmortem, someone writes "human error during change implementation" — which is true, but incomplete. The real cause was the system that required a human to repeat the same set of operations forty times in a row.

> **Note:** 📝
Note
💡
Industry data:
Gartner, Forrester, and most major network vendors consistently report that 60–80% of network downtime is caused by human configuration errors during manual change windows. This is not a skill problem. It is a systems problem. Automation is the solution.

## What Python Actually Changes

Here is the same scenario — forty switches, same VLAN change — done in Python:

```python
# vlan_deploy.py
import csv
from netmiko import ConnectHandler
from getpass import getpass

password = getpass("SSH Password: ")

with open('switches.csv') as f:
    devices = [dict(row) for row in csv.DictReader(f)]

vlan_commands = ['vlan 100', 'name PRODUCTION_SERVERS']

for device in devices:
    device['password'] = password
    print(f"Configuring {device['hostname']}...", end=" ")
    try:
        with ConnectHandler(**device) as conn:
            conn.send_config_set(vlan_commands)
            conn.save_config()
            print("✅ Done")
    except Exception as e:
        print(f"❌ Failed: {e}")

print("\nAll devices processed.")
```

**What changed:**

| Manual Process | Automated Process |
| --- | --- |
| 40 × SSH sessions | 1 script run |
| ~4 hours elapsed | ~45 seconds elapsed |
| Risk of human error on every device | Zero human error in configuration |
| No audit trail | Git commit records every change |
| Difficult to verify consistently | Same commands, every device, guaranteed |
| Hard to repeat exactly | Run again anytime with same result |

The script above is seventeen lines. You could write it after finishing Chapter 6 of this book.

## Should Every Network Engineer Code

This question always comes up, so let's address it directly.

**No, not every network engineer needs to become a software developer.** Software development is a separate discipline with its own depth — system design, performance optimization, security engineering, and much more. You do not need that depth to be an effective network automation engineer.

**Yes, every network engineer should be able to:**

- Read a Python script and understand what it does
- Modify an existing script safely for their environment
- Write basic scripts (file reading, loops, conditionals, function calls)
- Use libraries like Netmiko to interact with devices

Think of it like the relationship between a network engineer and spreadsheets. You do not need to be an Excel expert to use formulas, maintain a device inventory, or produce a report. But if you cannot use a spreadsheet at all, you are at a significant disadvantage. Python — for network automation purposes — is similar.

Here is the practical spectrum:

```python
CLI-Only Engineer          Automation-Aware        NetDevOps Engineer
       |                          |                        |
  Manual config             Runs & modifies          Writes automation
  No scripts                existing scripts         from scratch
                                                     Git + CI/CD
                                                     AI-augmented tools
  ← This book starts here →         ← This book ends here →
```

## Why Python Specifically

Network engineers sometimes ask whether they should learn Go, Ruby, or JavaScript instead. For network automation specifically, Python wins for three concrete reasons.

### 1. The Ecosystem

Every major network automation library is Python:

| Library | Purpose |
| --- | --- |
| Netmiko | SSH to network devices across vendors |
| NAPALM | Vendor-agnostic network APIs |
| Nornir | Parallel network automation framework |
| pyATS / Genie | Cisco test automation + structured parsing |
| Ansible | Agentless configuration management |
| Scapy | Packet crafting and analysis |

Cisco, Arista, Juniper, and most other vendors ship Python libraries and even Python interpreters on their operating systems. When you write Python for network automation, you are writing in the native language of the tools.

### 2. Readability

Python syntax reads like English. This line:

```python
if device in approved_list and status == 'up':
```

...is comprehensible even to someone who has never written a line of Python. This matters enormously when you are not a developer by training — you can often understand what code is doing before you fully understand how to write it yourself. That comprehension accelerates learning.

### 3. Dynamism

Python is dynamically typed. You do not declare variable types before using them:

```python
# Java (statically typed) — must declare type
String hostname = "ROUTER_1";

# Python (dynamically typed) — just use it
hostname = "ROUTER_1"
```

Coming from a CLI background where you type commands and see immediate results, the dynamic nature of Python feels natural. You create something, use it, see what happens — just like working in an IOS shell.

> **Note:** 📝
Note
📝
Note:
All code in this book uses Python 3 (3.8+). Python 2 reached End of Life in January 2020. If you see
python
in a command and are unsure of the version, use
python3
explicitly.

## The Python Interactive Interpreter: Your Always-On Lab

Before writing a single script, you need to know about the Python interactive interpreter — also called the Python shell. This tool lets you write Python code line-by-line and see immediate results.

```python
$ python3
Python 3.8.12 (default, Feb 26 2022, 00:05:23)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` prompt means Python is ready. You type code, hit Enter, and it responds instantly:

```python
>>> hostname = 'ROUTER_1'
>>> print(hostname)
ROUTER_1
>>> hostname.upper()
'ROUTER_1'
>>> 2 ** (32 - 24) - 2
254
>>>
```

This is the same as having an IOS device in front of you to test a command before putting it in a config. The Python shell is your learning environment — use it for everything in the next four chapters before moving to standalone scripts.

> **Note:** 📝
Note
💡
Cisco devices run Python too.
Cisco IOS-XE has a built-in Python interpreter accessible via
guestshell
. The same
python3
shell you use on your laptop is available directly on Catalyst 9000 series switches.

## The Automation Mindset: From Imperative to Declarative

The hardest part of learning network automation is not the Python syntax. It is the shift in how you think about network changes.

**Imperative thinking** (manual operations): "SSH to the device, enter enable, enter configure terminal, type this command, type this command, exit, write memory."

**Declarative thinking** (automation): "Every access port should have PortFast enabled, be in its assigned VLAN, and have a description that matches the connected endpoint."

The imperative thinker describes the *steps*. The declarative thinker describes the *desired state*. Automation enforces the desired state — and checks whether the current state matches it.

This is a profound shift. It means your job as an automated network engineer is not to execute procedures, but to:

1. **Define the desired state** — what should the network look like
2. **Build automation to enforce it** — code that detects and corrects drift
3. **Monitor and analyze** — AI tools that surface deviations and anomalies

Your protocol knowledge, troubleshooting instincts, and understanding of network behavior become more valuable in this model, not less. They inform the desired state definition and the interpretation of what the AI surfaces.

## What You Will Learn in This Book

Here is the complete progression:

```python
Section 1: Python Fundamentals
    ↓
    Variables, strings, lists, dictionaries
    Control flow: if/elif, for loops, while
    Functions, classes, modules
    Files, exceptions, environment variables

    Result: You can read and write Python scripts

Section 2: Network Automation
    ↓
    Netmiko — SSH to devices, send commands
    Multi-device loops, file-driven inventory
    Exception handling, config backup, Genie parsing
    Nornir parallel automation
    Git and CI/CD pipelines

    Result: You can automate your network

Section 3: AI-Powered Automation
    ↓
    LLM APIs, prompt engineering
    AI troubleshooter (Netmiko + Claude)
    AI syslog analyzer, config auditor
    Digital CX Coworker

    Result: Your automation can reason about your network
```

## Chapter Summary

The network engineering role is transforming from manual, device-by-device CLI operations toward programmatic automation and now toward AI-augmented intelligence. Python is the right first language for network automation because of its ecosystem, readability, and alignment with vendor tools.

You do not need to become a software developer. You need to become a network engineer who can write automation — and those are very different things.

In the next chapter, we open the Python interpreter for the first time and start building the data structures that will eventually drive your entire automation platform.

## Practice Exercises

Practice Exercises
1
Open the Python interpreter (
python3
) and type
2 ** (32 - 24) - 2
. What does this calculate
2
Create a variable
hostname = 'sw-core-01'
and try calling
.upper()
on it. What do you get
3
Look up the Netmiko project on GitHub. How many device types does it support (This will take 30 seconds and immediately show you why the ecosystem matters.)


---


# Python Data Types: The Building Blocks of Network Automation

> "Data is a precious thing and will last longer than the systems themselves." — Inspirational

> **Note:** 📝
Note
*"Data is a precious thing and will last longer than the systems themselves."* — Tim Berners-Lee

## Chapter Goal

Master Python's core data types through a networking lens. Every data type introduced here maps directly to something you already work with every day — hostnames are strings, VLAN IDs are integers, interface states are booleans, device inventories are lists, and connection parameters are dictionaries.

**Key Points:**

- Strings and their methods — the language your devices speak
- Numbers, booleans, and the arithmetic you already know
- Lists — your device inventory in code
- Dictionaries — the most important data structure in network automation
- Nested structures — lists of dictionaries, the real-world inventory pattern

## The Python Interactive Interpreter: Your Lab Bench

Every example in this chapter should be run in the Python interactive interpreter. Think of it as your lab environment — the same way you would verify a routing protocol before assuming it works, verify Python behavior before trusting it in a script.

```python
$ python3
Python 3.8.12 ...
>>>
```

The `>>>` prompt means Python is waiting. The convention throughout this book:

- Lines starting with `>>>` are Python interpreter input
- Lines without `>>>` are the output Python returns
- Lines starting with `$` are terminal (bash) commands

## Strings: The Language of Network Devices

Every piece of text your devices produce — show command output, log messages, configuration text, hostname, IP addresses — is a string. A string is any sequence of characters enclosed in quotes (single or double, both work):

```python
>>> hostname = 'ROUTER_1'
>>> ipaddr = "192.168.1.1"
>>> banner = '\n  WELCOME TO ROUTER_1  \n'
```

### Verifying Types

Python's `type()` function tells you what you are working with — invaluable when debugging:

```python
>>> type(hostname)

>>> type(42)

>>> type(3.14)
```

> **Note:** 📝
Note
💡
The
dir()
and
help()
trio:
Three built-in functions accelerate your learning: -
type(obj)
— what type is this object -
dir(obj)
— what methods does it have -
help(obj.method)
— how do I use this method  ``
python >>> dir(str)  # Shows all string methods >>> help(str.strip)  # Explains strip() in detail
``

### String Concatenation and F-Strings

The old way to combine strings was concatenation with `+`. The modern way is f-strings — use them:

```python
>>> hostname = 'sw-core-01'
>>> ip = '10.10.1.1'
>>> version = '17.9.4a'

# Old (avoid)
>>> 'Device ' + hostname + ' at ' + ip
'Device sw-core-01 at 10.10.1.1'

# Modern: f-strings (preferred)
>>> f'Device {hostname} at {ip} running IOS-XE {version}'
'Device sw-core-01 at 10.10.1.1 running IOS-XE 17.9.4a'

# F-strings can do math and formatting inline
>>> ports_used = 31
>>> ports_total = 48
>>> f'Port utilization: {ports_used/ports_total*100:.1f}%'
'Port utilization: 64.6%'
```

The `:.1f` inside the braces is a format specifier — it says "format this float to 1 decimal place." You will use this constantly for percentages and measurements.

### Essential String Methods

String methods are functions attached to string objects. Call them with dot notation: `string.method()`.

**Case conversion — essential for comparisons:**

```python
>>> interface = 'GigabitEthernet0/1'
>>> interface.lower()
'gigabitethernet0/1'
>>> interface.upper()
'GIGABITETHERNET0/1'

# Safe case-insensitive comparison
>>> user_input = 'GigabitEthernet0/1'
>>> user_input.lower() == 'gigabitethernet0/1'
True
```

**Strip — remove whitespace:**

```python
# Show command output often has leading/trailing whitespace
>>> raw_line = '  10.1.1.1      YES manual up      up  '
>>> raw_line.strip()
'10.1.1.1      YES manual up      up'
>>> raw_line.lstrip()   # Left side only
'10.1.1.1      YES manual up      up  '
>>> raw_line.rstrip()   # Right side only
'  10.1.1.1      YES manual up      up'
```

**Split — turn a string into a list:**

```python
>>> raw_line = '10.1.1.1      YES manual up      up'
>>> raw_line.split()  # Split on any whitespace
['10.1.1.1', 'YES', 'manual', 'up', 'up']

# Split on a specific character
>>> ipaddr = '10.1.20.30'
>>> ipaddr.split('.')
['10', '1', '20', '30']

# Split a show output line and extract fields
>>> parts = raw_line.split()
>>> interface_ip = parts[0]
>>> status = parts[3]
>>> protocol = parts[4]
```

**Join — combine a list into a string:**

```python
>>> commands = ['config t', 'interface Ethernet1/1', 'shutdown']
>>> '\n'.join(commands)      # Newline between commands
'config t\ninterface Ethernet1/1\nshutdown'
>>> ' ; '.join(commands)     # Semicolon (for NX-API)
'config t ; interface Ethernet1/1 ; shutdown'
```

**Membership testing:**

```python
>>> line = 'Interface GigabitEthernet0/1, changed state to down'
>>> 'changed state to down' in line
True
>>> line.startswith('Interface')
True
>>> line.endswith('down')
True
```

> **Note:** 📝
Note
📝
Note:
String methods return
new strings
— they do not modify the original. If you want to keep the result, assign it:
lower_intf = interface.lower()

### Real-World: Parsing show ip interface brief

This combination of strip + split + in is the foundation of every show-command parser you will ever write:

```python
# Simulated line from 'show ip interface brief'
>>> raw = '  GigabitEthernet0/0          10.10.1.1   YES manual up       up  '
>>> parts = raw.strip().split()
>>> parts
['GigabitEthernet0/0', '10.10.1.1', 'YES', 'manual', 'up', 'up']

>>> interface = parts[0]
>>> ip        = parts[1]
>>> status    = parts[4]
>>> protocol  = parts[5]

>>> if status == 'up' and protocol == 'up':
...     print(f'✅ {interface}: {ip} — HEALTHY')
... else:
...     print(f'❌ {interface}: {ip} — PROBLEM')
✅ GigabitEthernet0/0: 10.10.1.1 — HEALTHY
```

## Numbers: Counting What Matters

Network automation uses numbers for port counts, VLAN IDs, prefix lengths, utilization percentages, and timing. Python handles two main number types:

- **int** — whole numbers: `48`, `100`, `9300`
- **float** — decimals: `52.3`, `99.9`

```python
>>> port_count = 48
>>> cpu_util = 52.3
>>> type(port_count)

>>> type(cpu_util)
```

### Arithmetic Operators

```python
>>> 5 + 3      # Addition
8
>>> 10 - 4     # Subtraction
6
>>> 3 * 4      # Multiplication
12
>>> 10 / 3     # Division (always returns float)
3.3333333333333335
>>> 10 // 3    # Integer (floor) division
3
>>> 10 % 3     # Modulo (remainder)
1
>>> 2 ** 8     # Exponentiation
256
```

### Networking Applications

```python
# Subnet host calculation
>>> prefix = 24
>>> 2 ** (32 - prefix) - 2
254

# Usable hosts for common prefixes
>>> for prefix in [24, 25, 26, 27, 28, 29, 30]:
...     hosts = 2 ** (32 - prefix) - 2
...     print(f'/{prefix}: {hosts} usable hosts')
/24: 254 usable hosts
/25: 126 usable hosts
/26: 62 usable hosts
/27: 30 usable hosts
/28: 14 usable hosts
/29: 6 usable hosts
/30: 2 usable hosts

# String repetition (useful for formatting)
>>> '=' * 50
'=================================================='
>>> print('=' * 50)
==================================================

# Increment pattern
>>> counter = 0
>>> counter += 1    # Same as counter = counter + 1
>>> counter
1
```

### Type Conversion

```python
>>> str(10)        # int → string
'10'
>>> int('10')      # string → int
10
>>> float('52.3')  # string → float
52.3

# Critical: input() always returns a string!
>>> age = input('How old are you ')  # User types 25
>>> type(age)

>>> age = int(age)  # Must convert before arithmetic
>>> type(age)
```

## Booleans: The Yes/No of Your Network

Boolean values are `True` or `False`. They are the engine of every decision in your scripts:

```python
>>> is_layer3 = True
>>> has_ospf = False
>>> in_maintenance = False

# Boolean operations
>>> is_layer3 and has_ospf
False
>>> is_layer3 or has_ospf
True
>>> not is_layer3
False

# Comparison operators return booleans
>>> status = 'down'
>>> status == 'up'
False
>>> status != 'up'
True
>>> cpu = 87.4
>>> cpu > 80
True
```

### Empty Object Evaluation

One of Python's most elegant features: empty objects evaluate to `False`:

```python
>>> down_interfaces = []
>>> if not down_interfaces:
...     print('All interfaces are up!')
All interfaces are up!

>>> error_devices = ['10.1.1.5']
>>> if error_devices:
...     print(f'Warning: {len(error_devices)} devices had errors')
Warning: 1 devices had errors
```

This lets you write conditions that read like English: "if there are no down interfaces..." rather than "if the length of down_interfaces equals zero..."

## Lists: Your Device Inventory in Code

A list is an ordered collection of items enclosed in square brackets. If you have a mental model for a spreadsheet column, you understand lists:

```python
>>> hostnames = ['r1', 'r2', 'r3', 'r4', 'r5']
>>> interfaces = ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4']
>>> vlans = [10, 20, 30, 100, 200]
```

### Accessing Items

```python
# Index starts at 0
>>> hostnames[0]
'r1'
>>> hostnames[1]
'r2'
>>> hostnames[-1]    # Last item
'r5'
>>> hostnames[-2]    # Second to last
'r4'

# Slicing: list[start:end] (end is NOT included)
>>> hostnames[1:4]   # Index 1, 2, 3
['r2', 'r3', 'r4']
>>> hostnames[:3]    # First three
['r1', 'r2', 'r3']
>>> hostnames[-3:]   # Last three
['r3', 'r4', 'r5']
```

> **Note:** 📝
Note
⚠️
Warning:
Python indexing starts at 0. The first item is
[0]
, not
[1]
. Print the index and value side by side when debugging:
for i, item in enumerate(mylist): print(i, item)

### Modifying Lists

```python
>>> switches = ['sw-core-01', 'sw-dist-01']

# Add to end
>>> switches.append('sw-access-01')
>>> switches
['sw-core-01', 'sw-dist-01', 'sw-access-01']

# Insert at position
>>> switches.insert(0, 'sw-access-00')
>>> switches
['sw-access-00', 'sw-core-01', 'sw-dist-01', 'sw-access-01']

# Remove by value
>>> switches.remove('sw-access-00')

# Sort
>>> switches.sort()

# Count items
>>> len(switches)
3

# Check membership
>>> 'sw-core-01' in switches
True
>>> 'sw-access-99' in switches
False
```

### Looping Through a List

The `for` loop processes every item in sequence:

```python
>>> devices = ['10.1.1.1', '10.1.1.2', '10.1.1.3']
>>> for ip in devices:
...     print(f'Connecting to {ip}...')
Connecting to 10.1.1.1...
Connecting to 10.1.1.2...
Connecting to 10.1.1.3...
```

This single pattern — a list of devices and a for loop — is the foundation of every multi-device automation script you will write.

### Copying a List

```python
# ❌ WRONG — both variables point to the SAME list
>>> original = ['sw-01', 'sw-02']
>>> copy = original
>>> copy.append('sw-03')
>>> original    # Original was also modified!
['sw-01', 'sw-02', 'sw-03']

# ✅ CORRECT — independent copy using [:]
>>> original = ['sw-01', 'sw-02']
>>> copy = original[:]
>>> copy.append('sw-03')
>>> original    # Unchanged
['sw-01', 'sw-02']
```

## Dictionaries: The Heart of Network Automation

If lists are spreadsheet columns, dictionaries are spreadsheet rows — they store related attributes together, accessible by name:

```python
>>> device = {
...     'hostname': 'router1',
...     'vendor':   'cisco',
...     'os':       'ios-xe',
...     'version':  '17.9.4a',
...     'ip':       '10.10.1.1',
... }
```

### Accessing Values

```python
>>> device['hostname']
'router1'
>>> device['version']
'17.9.4a'

# CRITICAL: Use get() for safe access
>>> device['model']       # KeyError if missing — crashes!
KeyError: 'model'

>>> device.get('model')           # Returns None if missing — safe
>>> device.get('model', 'UNKNOWN') # Returns default if missing
'UNKNOWN'
```

> **Note:** 📝
Note
💡
Always use
.get()
for dictionary access when the key might not exist.
Networks are inconsistent — parsed device data often has missing fields. Crashing because one device in fifty is missing a
model
key is unacceptable in production automation.

### Modifying Dictionaries

```python
>>> device = {'hostname': 'router1', 'vendor': 'cisco'}

# Add a new key
>>> device['version'] = '17.9.4a'

# Update existing key
>>> device['vendor'] = 'cisco-ios-xe'

# Remove a key
>>> del device['vendor']

# Merge two dictionaries
>>> oper_data = {'cpu': '5%', 'memory': '10%'}
>>> device.update(oper_data)
>>> device
{'hostname': 'router1', 'version': '17.9.4a', 'cpu': '5%', 'memory': '10%'}
```

### Iterating Over Dictionaries

Three methods, three use cases:

```python
>>> facts = {'hostname': 'r1', 'vendor': 'cisco', 'os': 'ios-xe'}

# Keys only
>>> for key in facts.keys():
...     print(key)
hostname
vendor
os

# Values only
>>> for val in facts.values():
...     print(val)
r1
cisco
ios-xe

# Key-value pairs simultaneously — most common!
>>> for key, val in facts.items():
...     print(f'{key}: {val}')
hostname: r1
vendor: cisco
os: ios-xe
```

The `.items()` pattern appears in nearly every automation script — when building config commands from a template dictionary, when printing device summaries, when comparing current state to desired state.

## The Most Important Data Structure: List of Dictionaries

Real-world device inventories are not flat lists of strings. They are **lists of dictionaries** — one dictionary per device, each containing that device's attributes:

```python
>>> inventory = [
...     {'hostname': 'sw-core-01', 'ip': '10.10.1.1', 'role': 'core'},
...     {'hostname': 'sw-dist-01', 'ip': '10.10.1.2', 'role': 'distribution'},
...     {'hostname': 'sw-access-01', 'ip': '10.10.1.3', 'role': 'access'},
... ]

# Access nested data
>>> inventory[0]['hostname']
'sw-core-01'
>>> inventory[0]['ip']
'10.10.1.1'

# Loop and print summary
>>> for device in inventory:
...     print(f"{device['hostname']:15} {device['ip']:15} {device['role']}")
sw-core-01      10.10.1.1       core
sw-dist-01      10.10.1.2       distribution
sw-access-01    10.10.1.3       access

# Filter: get only core devices
>>> core_devices = [d for d in inventory if d['role'] == 'core']
>>> len(core_devices)
1
```

> **Note:** 📝
Note
🔑
Key Insight:
The list-of-dictionaries pattern is the single most important data structure in network automation. Your device inventory, your parsed Genie output, your configuration records — all use this exact pattern. Master it here, recognize it everywhere.

## Data Types Reference

| Type | Notation | Example | Network Use |
| --- | --- | --- | --- |
| str | 'text' | 'sw-core-01' | Hostnames, IPs, commands, show output |
| int | 42 | 48 | Port counts, VLANs, prefix lengths |
| float | 3.14 | 52.3 | CPU %, bandwidth utilization |
| bool | True/False | True | Interface state, reachability |
| list | [a, b, c] | ['sw-01', 'sw-02'] | Device inventories, command lists |
| dict | {k: v} | {'ip': '10.0.0.1'} | Device facts, connection params |
| tuple | (a, b) | (1, 1002, 1003) | Immutable: reserved VLANs, fixed values |
| set | set([...]) | set(vendors) | Unique values, deduplication |

## Practice Exercises

Practice Exercises
1
Create a dictionary for one network device with at least 5 keys. Access each value using
.get()
with a default of
'UNKNOWN'
.

1. Build a list of 5 switch hostnames. Print the first two, the last two, and the length. Sort them alphabetically.

1. Take this raw show output line and extract the interface name, IP address, status, and protocol using `.strip().split()`:

1. Create a list of 3 device dictionaries (different IPs and roles). Loop through and print only the devices with role `'access'`.

1. Open the Python interpreter and run: `2 ** (32 - n) - 2` for n = 24, 26, 28, 30. What are the usable host counts


---


# Control Flow, Loops, and Functions: Making Python Do the Work

> "Code is like humor. When you have to explain it, it's bad." — Inspirational

> **Note:** 📝
Note
*"Code is like humor. When you have to explain it, it's bad."* — Cory House

## Chapter Goal

Transform your Python vocabulary into automation logic. Data types hold information — control flow decides what to do with it. By the end of this chapter, you will write scripts that make decisions, process every device in a list, and reuse logic through functions. Every concept maps directly to a real network automation scenario.

**Key Points:**

- `if/elif/else` — your script makes decisions about interface states, VLAN validity, and device health
- `for` and `while` loops — the engine that processes every device in your fleet
- `break` and `continue` — controlling loop flow for skip-and-continue error handling
- Functions — write once, call hundreds of times
- List comprehensions — transform data in a single readable line

## Conditionals: Teaching Your Script to Think

An `if` statement evaluates an expression and runs code only when it is `True`. This is how your script decides whether an interface is down, whether a VLAN is in the approved list, or whether CPU utilization has crossed a threshold.

### Basic Structure

```python
cpu_util = 87.4

if cpu_util > 90:
    print('CRITICAL: CPU above 90%')
elif cpu_util > 75:
    print('WARNING: High CPU utilization')
elif cpu_util > 50:
    print('NOTICE: CPU is elevated')
else:
    print('OK: CPU within normal range')

# Output: WARNING: High CPU utilization
```

Python uses **indentation** (4 spaces) to delimit code blocks — no curly braces. Every line at the same indent level belongs to the same block. This forces readable structure.

### Comparison Operators

```python
# These all return True or False
status = 'down'

status == 'up'        # False — equal to
status != 'up'        # True  — not equal to
cpu = 87.4
cpu > 80              # True  — greater than
cpu >= 90             # False — greater than or equal
cpu < 90              # True  — less than
cpu <= 87.4           # True  — less than or equal
```

### Logical Operators: and, or, not

```python
interface_up   = True
has_ip         = True
in_maintenance = False

# AND — both conditions must be True
if interface_up and has_ip:
    print('Interface is reachable')

# OR — at least one must be True
if interface_up or has_ip:
    print('Some connectivity exists')

# NOT — reverses True/False
if not in_maintenance:
    print('Device is in production')

# Combined — real-world config push check
if interface_up and has_ip and not in_maintenance:
    print('Safe to push configuration')
```

### Membership Testing: in and not in

One of Python's most network-friendly operators — reads exactly like English:

```python
approved_vlans = [10, 20, 30, 100, 200]
requested_vlan = 50

if requested_vlan in approved_vlans:
    print('VLAN approved — configuring')
else:
    print('VLAN not in approved list — blocked')

# Works on strings too (substring search)
syslog = 'Interface GigabitEthernet0/1, changed state to down'
if 'changed state to down' in syslog:
    print('ALERT: Interface down event detected!')

# not in
banned_devices = ['legacy-sw-01', 'eol-router-01']
device = 'sw-core-01'
if device not in banned_devices:
    print(f'Processing {device}...')
```

### Checking Empty Collections

```python
# Empty lists, dicts, and strings evaluate to False
down_interfaces = []
error_devices   = ['10.1.1.5']

if not down_interfaces:
    print('All interfaces are up!')

if error_devices:
    print(f'WARNING: {len(error_devices)} devices had errors')
```

## For Loops: Processing Every Device Without Writing It Twice

A `for` loop executes the same code block for every item in a collection. This is the most important control structure in network automation — write the logic once, Python applies it to every device:

```python
devices = [
    {'hostname': 'sw-core-01',   'ip': '10.10.1.1', 'status': 'up'},
    {'hostname': 'sw-dist-01',   'ip': '10.10.1.2', 'status': 'down'},
    {'hostname': 'sw-access-01', 'ip': '10.10.1.3', 'status': 'up'},
]

for device in devices:
    icon = '✅' if device['status'] == 'up' else '❌'
    print(f"{icon} {device['hostname']:15} {device['ip']:15} {device['status']}")
```

Output:

```python
✅ sw-core-01      10.10.1.1       up
❌ sw-dist-01      10.10.1.2       down
✅ sw-access-01    10.10.1.3       up
```

The loop variable (`device`) holds one item from the list on each iteration. Code indented under `for` runs once per item. Code at the same level as `for` runs after all iterations.

### Nested Loops: Every Command on Every Device

```python
devices  = ['198.18.1.11', '198.18.1.12']
commands = ['show version', 'show ip int brief', 'show logging']

for ip in devices:              # outer loop: each device
    print(f'\n=== {ip} ===')
    for cmd in commands:        # inner loop: each command
        print(f'  Running: {cmd}')
        # In real code: output = conn.send_command(cmd)
```

### The range() Function

`range()` generates sequences of numbers without storing them in memory:

```python
# range(stop)          → 0 to stop-1
for i in range(5):
    print(i)            # 0 1 2 3 4

# range(start, stop)   → start to stop-1
for i in range(1, 6):
    print(i)            # 1 2 3 4 5

# range(start, stop, step)
for vlan in range(10, 51, 10):
    print(f'Creating VLAN {vlan}')   # 10 20 30 40 50

# Create a list from range
all_vlans = list(range(1, 4095))
print(len(all_vlans))   # 4094
```

### enumerate(): Loop with Index

```python
switches = ['sw-core-01', 'sw-dist-01', 'sw-access-01']

for i, switch in enumerate(switches, start=1):
    print(f'{i}. {switch}')

# Output:
# 1. sw-core-01
# 2. sw-dist-01
# 3. sw-access-01
```

### zip(): Loop Over Two Lists Together

```python
hostnames = ['sw-core-01', 'sw-dist-01', 'sw-access-01']
ip_addrs  = ['10.10.1.1',  '10.10.1.2',  '10.10.1.3']

for hostname, ip in zip(hostnames, ip_addrs):
    print(f'{hostname}: {ip}')
```

## break and continue: Controlling Loop Behavior

Two keywords let you control what happens inside loops.

### break — Exit the Loop Entirely

```python
# Find the first device with a problem and stop
for device in devices:
    if device['status'] == 'critical':
        print(f'CRITICAL device found: {device["hostname"]}')
        break       # Stop checking — escalate immediately
```

### continue — Skip This Item, Keep Going

`continue` is the most important loop control keyword in production network automation. When a device fails to connect, skip it and keep processing the rest:

```python
# Pattern from 5-netmiko-final.py (production lab script)
results  = []
failures = []

for device_ip in device_list:
    print(f'Connecting to {device_ip}...')

    try:
        connection = connect_to_device(device_ip)
    except TimeoutError:
        print(f'  Timeout: {device_ip} — skipping')
        failures.append({'ip': device_ip, 'error': 'timeout'})
        continue    # ← Skip to next device. Do NOT crash.
    except AuthError:
        print(f'  Auth failed: {device_ip} — skipping')
        failures.append({'ip': device_ip, 'error': 'auth_failed'})
        continue    # ← Skip to next device.

    # Only reaches here if connection succeeded
    output = connection.send_command('show version')
    results.append({'ip': device_ip, 'output': output})
    print(f'  ✅ Done')

print(f'\nSuccess: {len(results)}  Failed: {len(failures)}')
```

> **Note:** 📝
Note
⚠️
Critical pattern:
Without
continue
, the first device timeout crashes the entire script — you lose all results from all the devices that would have succeeded. With
continue
, failures are logged and the script processes every remaining device.

## While Loops: Running Until a Condition Changes

A `while` loop runs as long as its condition is `True`. Use it when you do not know in advance how many iterations you need:

```python
# Retry connection up to 3 times
max_attempts = 3
attempt = 0

while attempt < max_attempts:
    attempt += 1
    print(f'Attempt {attempt}/{max_attempts}...')

    if attempt_connection():        # Simulated
        print('Connected!')
        break

    print(f'Failed. Waiting...')

else:   # runs only if loop completed without break
    print('Max attempts reached — giving up')
```

### while True with break

```python
# Interactive command loop — keep running until user says 'quit'
while True:
    command = input('Enter command (or quit): ').strip()

    if not command:
        continue        # Empty input — ask again

    if command.lower() == 'quit':
        print('Exiting.')
        break

    print(f'Running: {command}')
    # output = connection.send_command(command)
```

## Functions: Write Once, Use Everywhere

A function is a named block of code that you can call as many times as you need, from anywhere in your script. Functions eliminate duplicated logic, make code readable, and enable testing.

### Defining and Calling

```python
def greet_device(hostname):
    """Print a connection banner for a device."""
    print('=' * 50)
    print(f'  Connecting to: {hostname}')
    print('=' * 50)

# Call the function
greet_device('sw-core-01')
greet_device('sw-dist-01')
```

The `def` keyword declares a function. The docstring (triple-quoted string on the first line) describes what it does — always write one. The parameter `hostname` accepts input.

### Return Values

```python
def get_vlan_commands(vlan_id, vlan_name):
    """Return IOS commands to create a VLAN."""
    return [
        f'vlan {vlan_id}',
        f'name {vlan_name}',
    ]

# Use the returned value
cmds = get_vlan_commands(100, 'PRODUCTION')
print(cmds)
# ['vlan 100', 'name PRODUCTION']

# Use in automation
vlans = [
    {'id': 10,  'name': 'MGMT'},
    {'id': 20,  'name': 'USERS'},
    {'id': 100, 'name': 'SERVERS'},
]

for vlan in vlans:
    commands = get_vlan_commands(vlan['id'], vlan['name'])
    print(f"Commands for VLAN {vlan['id']}: {commands}")
```

### Default Parameters

Parameters can have default values, making them optional:

```python
def build_connection_dict(ip, username='cisco', password='cisco',
                          device_type='cisco_ios', port=22):
    """Build a Netmiko connection dictionary."""
    return {
        'device_type': device_type,
        'ip':          ip,
        'username':    username,
        'password':    password,
        'port':        port,
    }

# Use defaults
params = build_connection_dict('10.10.1.1')

# Override specific parameters
params = build_connection_dict('10.10.1.1', port=8022)
params = build_connection_dict('10.10.1.1', username='admin', password='secret')
```

### Keyword Arguments

```python
# Call with keyword arguments — order doesn't matter
params = build_connection_dict(
    password='secret99',
    ip='10.10.1.2',
    username='netadmin'
)
```

### Functions That Return Multiple Values

```python
def analyze_interface(status, protocol):
    """Analyze interface state and return health info."""
    if status == 'up' and protocol == 'up':
        return 'HEALTHY', 'green', True
    elif status == 'up' and protocol == 'down':
        return 'DEGRADED', 'yellow', False
    else:
        return 'DOWN', 'red', False

health, color, is_up = analyze_interface('up', 'down')
print(f'State: {health}, Color: {color}, Reachable: {is_up}')
# State: DEGRADED, Color: yellow, Reachable: False
```

### *args and **kwargs

For functions that accept a variable number of arguments:

```python
def push_commands(hostname, *commands):
    """Push any number of commands to a device."""
    print(f'Pushing {len(commands)} commands to {hostname}')
    for cmd in commands:
        print(f'  → {cmd}')

push_commands('sw-core-01', 'vlan 10', 'name MGMT')
push_commands('sw-dist-01', 'vlan 10', 'name MGMT', 'vlan 20', 'name USERS')
```

```python
def build_device(**kwargs):
    """Build device dict from any keyword arguments."""
    return kwargs

device = build_device(hostname='sw-01', ip='10.0.0.1', role='core')
# {'hostname': 'sw-01', 'ip': '10.0.0.1', 'role': 'core'}
```

## List Comprehensions: Elegant Data Transformation

A list comprehension builds a new list from an existing one in a single readable line. The pattern: `[expression for item in collection if condition]`

```python
# Old way — loop
up_interfaces = []
for intf in all_interfaces:
    if intf['status'] == 'up':
        up_interfaces.append(intf)

# New way — comprehension
up_interfaces = [i for i in all_interfaces if i['status'] == 'up']

# Build IP list for a /24 subnet
host_ips = [f'10.10.1.{n}' for n in range(1, 255)]
print(host_ips[:3])   # ['10.10.1.1', '10.10.1.2', '10.10.1.3']

# Uppercase all hostnames
hostnames = ['sw-core-01', 'sw-dist-01', 'sw-access-01']
upper = [h.upper() for h in hostnames]
# ['SW-CORE-01', 'SW-DIST-01', 'SW-ACCESS-01']

# Filter: only Gigabit interfaces
interfaces = ['Gi0/0', 'Fa0/1', 'Gi0/1', 'Lo0']
gig_only = [i for i in interfaces if i.startswith('Gi')]
# ['Gi0/0', 'Gi0/1']
```

## Dictionary Comprehensions

Same idea, for dictionaries:

```python
# Map hostnames to IPs
hostnames = ['sw-core-01', 'sw-dist-01', 'sw-access-01']
ips       = ['10.10.1.1',  '10.10.1.2',  '10.10.1.3']

device_map = {h: ip for h, ip in zip(hostnames, ips)}
# {'sw-core-01': '10.10.1.1', ...}

# Squares
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Putting It Together: A Complete Show Command Parser

Here is everything from this chapter combined into a realistic function:

```python
def parse_interface_brief(show_output):
    """
    Parse 'show ip interface brief' output.
    Returns: (up_interfaces, down_interfaces)
    """
    up   = []
    down = []

    for line in show_output.splitlines():
        # Skip header lines and empty lines
        if not line.strip() or 'Interface' in line:
            continue

        parts = line.split()
        if len(parts) < 6:
            continue

        interface = parts[0]
        ip_addr   = parts[1]
        status    = parts[4]
        protocol  = parts[5]

        record = {
            'interface': interface,
            'ip':        ip_addr,
            'status':    status,
            'protocol':  protocol,
        }

        if status == 'up' and protocol == 'up':
            up.append(record)
        else:
            down.append(record)

    return up, down

# Example usage
sample_output = """
Interface              IP-Address      OK Method Status    Protocol
GigabitEthernet0/0     10.10.1.1       YES manual up        up
GigabitEthernet0/1     unassigned      YES unset  down      down
Loopback0              10.255.255.1    YES manual up        up
Vlan10                 10.10.10.1      YES manual up        up
Vlan20                 unassigned      YES unset  down      down
"""

up_ints, down_ints = parse_interface_brief(sample_output)

print(f'UP interfaces ({len(up_ints)}):')
for intf in up_ints:
    print(f"  ✅ {intf['interface']:25} {intf['ip']}")

print(f'\nDOWN interfaces ({len(down_ints)}):')
for intf in down_ints:
    print(f"  ❌ {intf['interface']}")
```

Output:

```python
UP interfaces (3):
  ✅ GigabitEthernet0/0       10.10.1.1
  ✅ Loopback0                 10.255.255.1
  ✅ Vlan10                    10.10.10.1

DOWN interfaces (2):
  ❌ GigabitEthernet0/1
  ❌ Vlan20
```

## Practice Exercises

Practice Exercises
1
Write a function
check_vlan(vlan_id)
that returns
'reserved'
if the VLAN is in
(1, 1002, 1003, 1004, 1005)
,
'invalid'
if outside 1–4094, and
'valid'
otherwise. Test it with VLANs 0, 1, 10, 1002, 4094, 4095.

1. Write a loop that iterates through a list of CPU percentages `[23, 55, 72, 88, 95, 12]` and prints a severity label (`NORMAL`, `WARNING`, `HIGH`, `CRITICAL`) for each. Use a function to determine the severity.

1. Use a list comprehension to build a list of all VLAN IDs that are multiples of 10 between 10 and 100.

1. Write a `while` loop that simulates retrying a device connection up to 5 times, with a different error message for each failure. Use `break` when simulated success occurs.


---


# Files, Error Handling, and Writing Your First Automation Scripts

> "It's not enough to be good. You have to be good for something." — Inspirational

> **Note:** 📝
Note
*"It's not enough to be good. You have to be good for something."* — Henry David Thoreau

## Chapter Goal

Wire Chapters 2 and 3 together into real automation scripts — scripts that read device inventories from files, collect credentials securely at runtime, handle failures gracefully, and write structured output. By the end of this chapter, you will have working patterns used in production network automation every day.

**Key Points:**

- Reading device inventories from text files and CSV files
- Writing results, reports, and configs to files
- `try/except/else/finally` — production exception handling
- `getpass` and environment variables — keeping secrets out of code
- JSON for storing structured automation data

## Working with Files

Production automation does not hardcode device IPs or credentials. It reads them from files — CSV inventories, YAML configs, plain text lists. Separating your data from your logic is the first step toward professional automation.

### The with Statement

The `with` statement manages file opening and closing automatically — even if an error occurs. Always use it:

```python
# ✅ Best practice: with statement
with open('device_list.txt') as f:
    contents = f.read()
# File automatically closed here, even if an exception occurred

# ❌ Old way: manual close required
f = open('device_list.txt')
contents = f.read()
f.close()   # If an exception occurs before here, file is never closed
```

### Reading a Plain Text Device List

The simplest inventory format — one IP per line:

```python
# device_list.txt
198.18.1.11
198.18.1.12
198.18.1.13
```

```python
# Read all IPs into a list
with open('device_list.txt') as f:
    device_ips = f.read().splitlines()

# device_ips = ['198.18.1.11', '198.18.1.12', '198.18.1.13']

for ip in device_ips:
    print(f'Will process: {ip}')
```

The `.splitlines()` method splits on newline characters and strips them — you get clean IP strings, no trailing `\n`.

### Reading a CSV Inventory

For richer inventories with multiple fields:

```python
# inventory.csv
hostname,ip,device_type,username,password
sw-core-01,10.10.1.1,cisco_ios,admin,cisco123
sw-dist-01,10.10.1.2,cisco_ios,admin,cisco123
sw-access-01,10.10.1.3,cisco_ios,admin,cisco123
```

```python
import csv

with open('inventory.csv') as f:
    reader = csv.DictReader(f)
    devices = [dict(row) for row in reader]

# devices[0] = {
#     'hostname': 'sw-core-01',
#     'ip': '10.10.1.1',
#     'device_type': 'cisco_ios',
#     'username': 'admin',
#     'password': 'cisco123'
# }

print(f'Loaded {len(devices)} devices from inventory')
for device in devices:
    print(f"  {device['hostname']:15} {device['ip']}")
```

`csv.DictReader` automatically uses the first row as column headers and returns each subsequent row as a dictionary — exactly the list-of-dictionaries pattern from Chapter 2.

### Checking if a File Exists

```python
from pathlib import Path

path = Path('inventory.csv')

if path.exists():
    with open(path) as f:
        devices = [dict(row) for row in csv.DictReader(f)]
else:
    print(f'ERROR: {path} not found. Create your inventory file first.')
    devices = []
```

## Writing Output to Files

Automation scripts that only print to screen are development tools. Production scripts save their output — reports to CSV, configurations to text files, results to JSON.

### Writing Text Files

```python
from pathlib import Path
from datetime import datetime

# Simple write (overwrites existing file)
path = Path('report.txt')
path.write_text('Automation Report\n')

# Write with a timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
report = f'Automation Report — {timestamp}\n'
report += f'Devices processed: 12\n'
report += f'Errors: 0\n'
path.write_text(report)

# Append to existing file
existing = path.read_text()
existing += '\nDevice sw-core-01: SUCCESS'
path.write_text(existing)
```

### Writing CSV Reports

```python
import csv
from datetime import datetime

results = [
    {'device': 'sw-core-01',   'status': 'success', 'version': '17.9.4a'},
    {'device': 'sw-dist-01',   'status': 'timeout',  'version': None},
    {'device': 'sw-access-01', 'status': 'success', 'version': '17.9.4a'},
]

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'results_{timestamp}.csv'

with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['device', 'status', 'version'])
    writer.writeheader()
    writer.writerows(results)

print(f'Results saved to {filename}')
```

### Writing JSON

JSON is the best format for structured automation data — human-readable, machine-parseable, and compatible with every other tool:

```python
import json
from pathlib import Path

# Save structured data as JSON
inventory_data = {
    'timestamp': datetime.now().isoformat(),
    'devices': [
        {'hostname': 'sw-core-01', 'ip': '10.10.1.1', 'version': '17.9.4a'},
        {'hostname': 'sw-dist-01', 'ip': '10.10.1.2', 'version': '17.9.4a'},
    ]
}

path = Path('inventory.json')
path.write_text(json.dumps(inventory_data, indent=2))

# Load it back
loaded = json.loads(path.read_text())
print(f"Loaded {len(loaded['devices'])} devices")
print(f"Timestamp: {loaded['timestamp']}")
```

### Creating Directories

```python
import os
from pathlib import Path

# Create backup directory if it doesn't exist
backup_dir = Path('backup/')
backup_dir.mkdir(exist_ok=True)   # exist_ok=True means no error if it exists

# Save a config file into it
hostname = 'sw-core-01'
config_text = '! Running config from sw-core-01\nhostname sw-core-01\n'
config_path = backup_dir / f'{hostname}.cfg'
config_path.write_text(config_text)

print(f'Saved: {config_path}')
```

## Exception Handling: Scripts That Survive Reality

The real world is messy. Devices are unreachable. Passwords are wrong. SSH sessions drop mid-transfer. A script without exception handling crashes at the first problem — losing all results from all devices that would have succeeded.

### The try/except Pattern

```python
try:
    # Code that might fail
    result = risky_operation()
except SpecificError:
    # Handle this specific type of failure
    print('Specific thing went wrong')
except AnotherError:
    # Handle another type of failure
    print('Another thing went wrong')
except Exception as e:
    # Catch-all for anything unexpected
    print(f'Unexpected error: {e}')
else:
    # Runs ONLY if no exception occurred
    print('Success!')
finally:
    # Always runs — for cleanup
    print('Cleanup code here')
```

### The Production Netmiko Exception Pattern

This is the complete exception handling structure from `5-netmiko-final.py` — memorize this pattern:

```python
from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)
from paramiko.ssh_exception import SSHException

results  = []
failures = []

for device_ip in device_list:
    print(f'Connecting to {device_ip}...')
    ios_device = {
        'device_type': 'cisco_ios',
        'ip':          device_ip,
        'username':    username,
        'password':    password,
    }

    try:
        net_connect = ConnectHandler(**ios_device)

    except NetmikoAuthenticationException:
        msg = f'Authentication failure: {device_ip}'
        print(f'  ❌ {msg}')
        failures.append({'ip': device_ip, 'error': 'auth_failed'})
        continue   # Skip to next device

    except NetmikoTimeoutException:
        msg = f'Timeout (unreachable): {device_ip}'
        print(f'  ❌ {msg}')
        failures.append({'ip': device_ip, 'error': 'timeout'})
        continue

    except EOFError:
        msg = f'EOF error (connection dropped): {device_ip}'
        print(f'  ❌ {msg}')
        failures.append({'ip': device_ip, 'error': 'eof'})
        continue

    except SSHException:
        msg = f'SSH error (is SSH enabled): {device_ip}'
        print(f'  ❌ {msg}')
        failures.append({'ip': device_ip, 'error': 'ssh_error'})
        continue

    except Exception as e:
        msg = f'Unexpected error: {str(e)}'
        print(f'  ❌ {msg}')
        failures.append({'ip': device_ip, 'error': str(e)})
        continue

    # Only reaches here if connection succeeded
    output = net_connect.send_config_from_file('config_commands')
    net_connect.save_config()
    net_connect.disconnect()
    print(f'  ✅ Done: {device_ip}')
    results.append({'ip': device_ip, 'status': 'success'})

# Summary
print(f'\n{"="*40}')
print(f'Completed: {len(results)} success, {len(failures)} failed')
if failures:
    print('Failed devices:')
    for f in failures:
        print(f"  {f['ip']}: {f['error']}")
```

> **Note:** 📝
Note
🔑
Key Insight:
The four specific exception types (Auth, Timeout, EOF, SSH) each represent a different failure mode with different causes and different remediation steps. Catching them separately lets you give meaningful error messages instead of generic failures. The catch-all
Exception
at the end catches anything unexpected without crashing.

### Common Exception Types

| Exception | Meaning | Common Cause |
| --- | --- | --- |
| NetmikoTimeoutException | Connection timed out | Device unreachable, firewall, wrong IP |
| NetmikoAuthenticationException | Login failed | Wrong credentials, AAA issue |
| SSHException | SSH protocol error | SSH not enabled, version mismatch |
| EOFError | Connection dropped | VTY limit reached, session timeout |
| FileNotFoundError | File not found | Wrong path, file not created |
| KeyError | Dict key missing | Parsing error, unexpected output |
| ValueError | Wrong value type | int('not a number') |

## Secure Credentials: Secrets Out of Code

Never hardcode credentials in scripts. Ever. Even if the script lives only on your laptop.

### getpass — Interactive Password Input

```python
from getpass import getpass

# input() shows what the user types — fine for username
username = input('Enter SSH username: ')

# getpass() hides what the user types — required for passwords
password = getpass('Enter SSH password: ')
enable_secret = getpass('Enter enable secret (Enter to skip): ')

print(f'Will connect as: {username}')
# Password never printed
```

### os.getenv — Environment Variables

For automated runs (cron jobs, CI/CD pipelines) where there is no interactive terminal:

```python
import os
from getpass import getpass

# Use environment variable if set; otherwise prompt
username = os.getenv('NETMIKO_USERNAME') or input('Enter username: ')
password = os.getenv('NETMIKO_PASSWORD') or getpass('Enter password: ')

# Set in terminal before running:
# export NETMIKO_USERNAME="admin"
# export NETMIKO_PASSWORD="cisco123"

# Check if variable is set
if not os.getenv('ANTHROPIC_API_KEY'):
    print('WARNING: ANTHROPIC_API_KEY not set')
```

### .env Files with python-dotenv

For development, a `.env` file is the cleanest approach:

```python
# .env file in project root (add to .gitignore!)
NETMIKO_USERNAME=cisco
NETMIKO_PASSWORD=cisco
ANTHROPIC_API_KEY=sk-ant-...
```

```python
from dotenv import load_dotenv
import os

load_dotenv()   # Reads .env file and sets environment variables

username = os.getenv('NETMIKO_USERNAME')
password = os.getenv('NETMIKO_PASSWORD')
```

> **Note:** 📝
Note
⚠️
Critical:
Add
.env
to your
.gitignore
file immediately. Credentials committed to Git — even a private repository — are a security incident waiting to happen. The
.env
file is for your local machine only.

## Your First Complete Automation Script

Combining everything from this chapter into a realistic, production-ready script:

```python
#!/usr/bin/env python3
"""
show_command_collector.py

Connects to all devices in device_list.txt and runs all commands
in show_commands.txt. Saves results to JSON.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from paramiko.ssh_exception import SSHException

# ─── Configuration ────────────────────────────────────────────
DEVICE_LIST_FILE  = 'device_list.txt'
COMMANDS_FILE     = 'show_commands.txt'
OUTPUT_DIR        = Path('output')

# ─── Load Files ───────────────────────────────────────────────
def load_device_list(filepath):
    """Load device IPs from a text file (one IP per line)."""
    path = Path(filepath)
    if not path.exists():
        print(f'ERROR: {filepath} not found')
        return []
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]

def load_commands(filepath):
    """Load show commands from a text file (one command per line)."""
    path = Path(filepath)
    if not path.exists():
        print(f'ERROR: {filepath} not found')
        return []
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]

# ─── Run Commands on One Device ───────────────────────────────
def run_commands_on_device(device_ip, username, password, commands):
    """Connect to one device and run all commands. Returns result dict."""
    ios_device = {
        'device_type': 'cisco_ios',
        'ip':          device_ip,
        'username':    username,
        'password':    password,
    }

    try:
        with ConnectHandler(**ios_device) as conn:
            hostname = conn.find_prompt().rstrip('#>')
            command_results = {}
            for cmd in commands:
                command_results[cmd] = conn.send_command(cmd)
            return {
                'ip':       device_ip,
                'hostname': hostname,
                'status':   'success',
                'results':  command_results,
            }

    except NetmikoAuthenticationException:
        return {'ip': device_ip, 'status': 'auth_failed', 'results': {}}
    except NetmikoTimeoutException:
        return {'ip': device_ip, 'status': 'timeout', 'results': {}}
    except SSHException:
        return {'ip': device_ip, 'status': 'ssh_error', 'results': {}}
    except Exception as e:
        return {'ip': device_ip, 'status': f'error: {e}', 'results': {}}

# ─── Main ──────────────────────────────────────────────────────
def main():
    print('=' * 55)
    print('  Network Show Command Collector')
    print('=' * 55)

    # Credentials
    username = os.getenv('NETMIKO_USERNAME') or input('Username: ')
    password = os.getenv('NETMIKO_PASSWORD') or getpass('Password: ')

    # Load data
    device_ips = load_device_list(DEVICE_LIST_FILE)
    commands   = load_commands(COMMANDS_FILE)

    if not device_ips or not commands:
        print('Nothing to do. Check your input files.')
        return

    print(f'Devices: {len(device_ips)} | Commands: {len(commands)}')
    print()

    # Run automation
    all_results = []
    for ip in device_ips:
        print(f'Processing {ip}...', end=' ')
        result = run_commands_on_device(ip, username, password, commands)
        all_results.append(result)
        status = '✅' if result['status'] == 'success' else '❌'
        hostname = result.get('hostname', ip)
        print(f'{status} {hostname} ({result["status"]})')

    # Save results
    OUTPUT_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = OUTPUT_DIR / f'results_{ts}.json'
    output_file.write_text(json.dumps(all_results, indent=2))

    # Summary
    success = sum(1 for r in all_results if r['status'] == 'success')
    print(f'\nDone: {success}/{len(device_ips)} succeeded')
    print(f'Results saved: {output_file}')

if __name__ == '__main__':
    main()
```

## Practice Exercises

Practice Exercises
1
Create a
device_list.txt
file with 3 IP addresses (real or fake). Write a script that reads it and prints
"Processing: {ip}"
for each.

1. Write a script that collects a username via `input()` and a password via `getpass()`, then prints `"Would connect as: {username}"` without ever printing the password.

1. Add a `try/except` block to the script from Exercise 1 that catches `FileNotFoundError` and prints a helpful error message instead of crashing.

1. Extend the script from Exercise 1 to save results to a JSON file with this structure:


---


# Classes, Modules, and Building Reusable Automation Code

> "Good code is its own best documentation." — Inspirational

> **Note:** 📝
Note
*"Good code is its own best documentation."* — Steve McConnell

## Chapter Goal

Organize your Python knowledge into professional, reusable code using classes and modules. By the end of this chapter, you will understand how Netmiko's `ConnectHandler` works from the inside, how to build your own `NetworkDevice` class, and how to structure a growing automation platform into maintainable modules.

**Key Points:**

- What classes are and why they make automation code cleaner
- Building a `NetworkDevice` class with attributes and methods
- Inheritance — `CiscoSwitch` built on `NetworkDevice`
- Modules — splitting code across files for a professional project structure
- Understanding `ConnectHandler` from the inside out

## What is a Class

A class is a blueprint for creating objects. An object created from a class is called an **instance**. Classes bundle together related data (**attributes**) and behavior (**methods**) for a concept you want to model.

For network automation, the most natural class is a `NetworkDevice` — an object that knows its own connection parameters and can perform its own operations.

You have already been using classes without realizing it. When you run:

```python
net_connect = ConnectHandler(**ios1)
```

You are creating an **instance** of Netmiko's `ConnectHandler` class. When you call:

```python
net_connect.send_command('show version')
```

You are calling a **method** on that instance. Understanding classes from the inside makes you far better at using libraries from the outside.

## Creating Your First Class

```python
class NetworkDevice:
    """Represents a network device with connection capabilities."""

    def __init__(self, hostname, ip, device_type='cisco_ios'):
        """Initialize device attributes.

        __init__ runs automatically when you create an instance.
        self refers to the specific instance being created.
        """
        self.hostname    = hostname     # Instance attribute
        self.ip          = ip
        self.device_type = device_type
        self.connected   = False        # Default: not connected
        self.facts       = {}           # Empty dict for collected data

    def get_connection_params(self, username, password):
        """Return a Netmiko-compatible connection dictionary."""
        return {
            'device_type': self.device_type,
            'ip':          self.ip,
            'username':    username,
            'password':    password,
        }

    def mark_connected(self):
        """Mark this device as connected."""
        self.connected = True
        print(f'✅ Connected to {self.hostname} ({self.ip})')

    def show_summary(self):
        """Print a one-line device summary."""
        status = 'ONLINE' if self.connected else 'OFFLINE'
        print(f'{self.hostname:15} | {self.ip:15} | {status}')

    def __repr__(self):
        """String representation for debugging."""
        return f'NetworkDevice({self.hostname}, {self.ip})'
```

### Creating Instances

```python
# Create instances from the class
core_sw = NetworkDevice('sw-core-01', '10.10.1.1')
dist_sw = NetworkDevice('sw-dist-01', '10.10.1.2')

# Access attributes
print(core_sw.hostname)    # sw-core-01
print(core_sw.ip)          # 10.10.1.1
print(core_sw.connected)   # False

# Call methods
core_sw.mark_connected()   # ✅ Connected to sw-core-01 (10.10.1.1)
core_sw.show_summary()     # sw-core-01      | 10.10.1.1       | ONLINE
dist_sw.show_summary()     # sw-dist-01      | 10.10.1.2       | OFFLINE

# Each instance is independent
print(core_sw.connected)   # True
print(dist_sw.connected)   # False

# Use in automation
params = core_sw.get_connection_params('admin', 'cisco123')
# {'device_type': 'cisco_ios', 'ip': '10.10.1.1', ...}
```

### Understanding self

`self` is the instance the method was called on. When you call `core_sw.show_summary()`, Python automatically passes `core_sw` as `self`. That is why you can access `self.hostname` inside the method — it is the same as `core_sw.hostname` from outside.

```python
# These are equivalent:
core_sw.show_summary()
NetworkDevice.show_summary(core_sw)
```

## Class Attributes vs Instance Attributes

```python
class NetworkDevice:
    # Class attribute — shared by ALL instances
    vendor_default = 'cisco'
    connection_count = 0

    def __init__(self, hostname, ip):
        # Instance attributes — unique to EACH instance
        self.hostname = hostname
        self.ip = ip

sw1 = NetworkDevice('sw-01', '10.0.0.1')
sw2 = NetworkDevice('sw-02', '10.0.0.2')

# Class attribute is the same for both
print(sw1.vendor_default)   # cisco
print(sw2.vendor_default)   # cisco

# Instance attributes differ
print(sw1.hostname)   # sw-01
print(sw2.hostname)   # sw-02
```

## Inheritance: Extending What Exists

Inheritance lets you create a specialized version of an existing class. A `CiscoSwitch` is a `NetworkDevice` with extra Layer-2 capabilities. You get everything the parent has, plus whatever you add:

```python
class CiscoSwitch(NetworkDevice):
    """A Cisco switch with Layer-2 specific capabilities."""

    def __init__(self, hostname, ip, num_ports=48):
        """Initialize CiscoSwitch — call parent __init__ first."""
        super().__init__(hostname, ip)   # Initialize NetworkDevice part
        self.num_ports = num_ports       # New attribute
        self.vlans = []                  # New attribute

    def add_vlan(self, vlan_id, vlan_name=''):
        """Add a VLAN to this switch's tracking list."""
        vlan = {
            'id':   vlan_id,
            'name': vlan_name or f'VLAN{vlan_id}',
        }
        self.vlans.append(vlan)
        print(f'Added VLAN {vlan_id} ({vlan["name"]}) to {self.hostname}')

    def get_vlan_commands(self):
        """Return IOS commands to provision all tracked VLANs."""
        commands = []
        for vlan in self.vlans:
            commands.append(f"vlan {vlan['id']}")
            commands.append(f"name {vlan['name']}")
        return commands

    def show_vlans(self):
        """Display all tracked VLANs."""
        print(f'\nVLANs on {self.hostname}:')
        for vlan in self.vlans:
            print(f"  VLAN {vlan['id']:4}: {vlan['name']}")

# Use the subclass
sw = CiscoSwitch('sw-core-01', '10.10.1.1', num_ports=48)

# Inherited methods work
sw.mark_connected()         # From NetworkDevice
sw.show_summary()           # From NetworkDevice

# New methods from CiscoSwitch
sw.add_vlan(10, 'MGMT')
sw.add_vlan(20, 'USERS')
sw.add_vlan(100, 'SERVERS')
sw.show_vlans()

cmds = sw.get_vlan_commands()
print('\nCommands to push:')
for cmd in cmds:
    print(f'  {cmd}')
```

Output:

```python
✅ Connected to sw-core-01 (10.10.1.1)
sw-core-01      | 10.10.1.1       | ONLINE
Added VLAN 10 (MGMT) to sw-core-01
Added VLAN 20 (USERS) to sw-core-01
Added VLAN 100 (SERVERS) to sw-core-01

VLANs on sw-core-01:
  VLAN   10: MGMT
  VLAN   20: USERS
  VLAN  100: SERVERS

Commands to push:
  vlan 10
  name MGMT
  vlan 20
  ...
```

### super().__init__()

`super().__init__(hostname, ip)` calls the parent class's `__init__` method. This initializes all the parent's attributes (`self.hostname`, `self.ip`, `self.connected`, `self.facts`) before adding the subclass-specific ones. Always call `super().__init__()` at the top of a subclass `__init__`.

## Understanding ConnectHandler from the Inside

Now you understand classes, you can understand exactly what Netmiko does:

```python
# Simplified version of how ConnectHandler works internally
class ConnectHandler:
    """Manages SSH connections to network devices."""

    def __init__(self, device_type, ip, username, password, **kwargs):
        """Establish SSH connection on instantiation."""
        self.device_type = device_type
        self.ip = ip
        self.username = username
        # ... (SSH handshake happens here)
        self._connection = self._establish_ssh()

    def __enter__(self):
        """Support 'with' statement — return self."""
        return self

    def __exit__(self, *args):
        """Disconnect when 'with' block exits."""
        self.disconnect()

    def send_command(self, command, **kwargs):
        """Send a show command and return output."""
        # Send over SSH, wait for prompt, return output
        return self._connection.send(command)

    def send_config_set(self, commands):
        """Enter config mode, send commands, exit."""
        self._connection.send('configure terminal')
        for cmd in commands:
            self._connection.send(cmd)
        self._connection.send('end')

    def find_prompt(self):
        """Return the device's current prompt string."""
        return self._connection.get_prompt()

    def save_config(self):
        """Save running config to startup config."""
        return self.send_command('write memory')

    def disconnect(self):
        """Close the SSH connection."""
        self._connection.close()
```

When you write `with ConnectHandler(**ios1) as conn:`, Python:

1. Calls `ConnectHandler.__init__()` — establishes SSH
2. Calls `ConnectHandler.__enter__()` — returns the object as `conn`
3. Runs your code block
4. Calls `ConnectHandler.__exit__()` — disconnects automatically

This is why the `with` statement is so important — it guarantees cleanup even if an exception occurs.

## Modules: Organizing Your Automation Platform

As your automation code grows, a single file becomes unmanageable. Modules let you split code into logical, importable Python files.

### Recommended Project Structure

```python
network_automation/
├── inventory.py        # Device loading and management
├── connection.py       # Connection helpers, exception handling
├── commands.py         # Show command runners and parsers
├── config_gen.py       # Configuration template generation
├── reporting.py        # Output formatting and file writing
├── models.py           # NetworkDevice and subclasses
└── main.py             # Orchestration (imports everything else)
```

### Creating and Importing Modules

```python
# File: models.py
class NetworkDevice:
    """Base class for all network devices."""
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

class CiscoSwitch(NetworkDevice):
    """Cisco switch with L2 capabilities."""
    pass
```

```python
# File: inventory.py
import csv
from pathlib import Path

def load_devices(filepath='inventory.csv'):
    """Load device inventory from CSV file."""
    path = Path(filepath)
    if not path.exists():
        return []
    with open(path) as f:
        return [dict(row) for row in csv.DictReader(f)]

def load_device_ips(filepath='device_list.txt'):
    """Load plain list of device IPs."""
    path = Path(filepath)
    if not path.exists():
        return []
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]
```

```python
# File: connection.py
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from paramiko.ssh_exception import SSHException

def safe_connect(device_params):
    """Connect to a device with full exception handling. Returns conn or None."""
    try:
        conn = ConnectHandler(**device_params)
        return conn
    except NetmikoAuthenticationException:
        print(f"  Auth failed: {device_params['ip']}")
        return None
    except NetmikoTimeoutException:
        print(f"  Timeout: {device_params['ip']}")
        return None
    except Exception as e:
        print(f"  Error: {e}")
        return None
```

```python
# File: main.py
from inventory import load_devices
from connection import safe_connect

def main():
    devices = load_devices('inventory.csv')

    for device in devices:
        conn = safe_connect(device)
        if not conn:
            continue

        output = conn.send_command('show version')
        conn.disconnect()
        print(f"  ✅ {device['hostname']}: collected {len(output)} chars")

if __name__ == '__main__':
    main()
```

### The if __name__ == '__main__' Pattern

This is one of Python's most important idioms:

```python
# When you RUN the file directly:
#   __name__ == '__main__'  → main() is called
#
# When you IMPORT the file as a module:
#   __name__ == 'main'      → main() is NOT called automatically

if __name__ == '__main__':
    main()
```

Without this pattern, importing your file would immediately run the automation — undesirable when you just want to use its functions in another script.

## Building a NetworkDevice Inventory Class

A more complete, production-ready model:

```python
# models.py

import json
import csv
from pathlib import Path
from datetime import datetime

class NetworkDevice:
    """Represents a managed network device."""

    def __init__(self, hostname, ip, device_type='cisco_ios',
                 username='', password='', role='unknown'):
        self.hostname    = hostname
        self.ip          = ip
        self.device_type = device_type
        self.username    = username
        self.password    = password
        self.role        = role
        self.connected   = False
        self.last_seen   = None
        self.facts       = {}

    @classmethod
    def from_dict(cls, data):
        """Create instance from a dictionary (e.g., CSV row)."""
        return cls(
            hostname    = data.get('hostname', data.get('ip', 'unknown')),
            ip          = data['ip'],
            device_type = data.get('device_type', 'cisco_ios'),
            username    = data.get('username', ''),
            password    = data.get('password', ''),
            role        = data.get('role', 'unknown'),
        )

    def to_dict(self):
        """Convert to dictionary for serialization."""
        return {
            'hostname':    self.hostname,
            'ip':          self.ip,
            'device_type': self.device_type,
            'role':        self.role,
            'connected':   self.connected,
            'last_seen':   self.last_seen,
            'facts':       self.facts,
        }

    def get_netmiko_params(self):
        """Return Netmiko connection dictionary."""
        return {
            'device_type': self.device_type,
            'ip':          self.ip,
            'username':    self.username,
            'password':    self.password,
        }

    def __repr__(self):
        return f'NetworkDevice({self.hostname!r}, {self.ip!r})'

    def __str__(self):
        status = 'ONLINE' if self.connected else 'OFFLINE'
        return f'{self.hostname} ({self.ip}) [{status}]'

class DeviceInventory:
    """Manages a collection of NetworkDevice instances."""

    def __init__(self):
        self.devices = []

    def load_from_csv(self, filepath):
        """Load devices from a CSV inventory file."""
        with open(filepath) as f:
            for row in csv.DictReader(f):
                self.devices.append(NetworkDevice.from_dict(row))
        return self

    def get_by_role(self, role):
        """Return all devices with a specific role."""
        return [d for d in self.devices if d.role == role]

    def get_by_ip(self, ip):
        """Find a device by IP address."""
        return next((d for d in self.devices if d.ip == ip), None)

    def summary(self):
        """Print a formatted inventory summary."""
        print(f'{"Hostname":15} {"IP":15} {"Role":15} {"Status"}')
        print('-' * 60)
        for d in self.devices:
            status = '✅ ONLINE' if d.connected else '❌ OFFLINE'
            print(f'{d.hostname:15} {d.ip:15} {d.role:15} {status}')

    def __len__(self):
        return len(self.devices)

    def __iter__(self):
        return iter(self.devices)

# Usage
if __name__ == '__main__':
    inv = DeviceInventory()
    inv.load_from_csv('inventory.csv')

    print(f'Loaded {len(inv)} devices\n')
    inv.summary()

    core_devices = inv.get_by_role('core')
    print(f'\nCore devices: {len(core_devices)}')
```

## Section 1 Complete — What You Can Now Do

You have covered every Python concept needed for professional network automation:

| Concept | Chapter | Network Application |
| --- | --- | --- |
| Variables, strings, f-strings | Ch 2 | Device names, IPs, log messages |
| Lists and dictionaries | Ch 2 | Inventories, connection params |
| Control flow (if/elif/else) | Ch 3 | Interface checks, VLAN validation |
| Loops (for, while) | Ch 3 | Multi-device automation |
| break and continue | Ch 3 | Skip failed devices |
| Functions | Ch 3 | Reusable automation logic |
| List comprehensions | Ch 3 | Filter, transform device data |
| File I/O | Ch 4 | Read inventories, save reports |
| Exception handling | Ch 4 | Production-grade error recovery |
| Secure credentials | Ch 4 | getpass, environment variables |
| Classes and objects | Ch 5 | NetworkDevice model |
| Inheritance | Ch 5 | CiscoSwitch, AreoRouter |
| Modules | Ch 5 | Organized project structure |

In Section 2, we apply all of this to real Cisco devices with Netmiko, Genie, and Nornir.

## Practice Exercises

Practice Exercises
1
Build a
NetworkDevice
class with at least 5 attributes. Add a
get_netmiko_params()
method that returns a connection dictionary.

1. Create a `CiscoRouter` subclass that adds routing-specific attributes (`routing_protocols`, `bgp_asn`) and a `get_bgp_summary()` method.

1. Build a simple `DeviceInventory` class with `add_device()`, `get_by_role()`, and `summary()` methods. Test it with 3 devices of different roles.

1. Create a `connection.py` module with a `safe_connect(device_params)` function that includes full exception handling. Import and use it from `main.py`.


---


# Netmiko: SSHing to Your Network at Python Speed

> "Don't repeat yourself. And when you must, let the computer do the repeating." — Inspirational

> **Note:** 📝
Note
*"Don't repeat yourself. And when you must, let the computer do the repeating."* — Andy Hunt

## Chapter Goal

Apply every concept from Section 1 to real network devices. Netmiko bridges your Python knowledge to your network — this chapter walks through the first two lab scripts in full detail, explaining every line and how it connects to what you already know.

**Key Points:**

- What Netmiko is and how to install it
- The device dictionary — the most important Netmiko pattern
- `send_command()` vs `send_config_set()` — two different purposes
- The `with` statement for automatic disconnection
- Your first single-device show command and config script

## What is Netmiko

Netmiko is an open-source Python library that makes SSH connections to network devices simple. Without it, raw SSH handling in Python requires hundreds of lines of Paramiko code — dealing with channel setup, prompt detection, banner handling, and timing. Netmiko wraps all of that complexity in a clean interface.

One line connects you. One line sends a command. One line gets the output.

```python
pip install netmiko
```

Verify the installation:

```python
import netmiko
print(netmiko.__version__)   # e.g., 4.3.0
```

## Lab Environment

The examples in this chapter and the next four use the **jagadnag/labato_1010** lab environment (Cisco dCloud or compatible CML lab):

```python
Device IPs:   198.18.1.11,  198.18.1.12
Username:     cisco
Password:     cisco
Device type:  Cisco IOS / IOS-XE (CSR1000V)
```

You can substitute any Cisco IOS or IOS-XE device. Update the IPs in `device_list` to match your environment.

## Supported Device Types Reference

| Platform | device_type | Notes |
| --- | --- | --- |
| Cisco IOS / IOS-XE | cisco_ios | Catalyst 9K, CSR, ISR, ASR |
| Cisco NX-OS | cisco_nxos | Nexus 5K/7K/9K |
| Cisco IOS-XR | cisco_iosxr | ASR 9000, NCS |
| Cisco ASA | cisco_asa | Firewall |
| Arista EOS | arista_eos | All Arista |
| Juniper JunOS | juniper_junos | MX, QFX, SRX |
| Palo Alto | paloalto_panos | PA-Series |
| Fortinet | fortinet | FortiGate |

> **Note:** 📝
Note
📝
Note:
Cisco IOS-XE uses
'cisco_ios'
— not
'cisco_iosxe'
. The Catalyst 9000 series uses
'cisco_ios'
.

## Lab Script 1 — 1-netmiko-show.py

The simplest possible Netmiko script. Connect to one device, run one show command, print the output.

### The Full Script

```python
#!/usr/bin/env python
from netmiko import ConnectHandler

# SSH Connection Details
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}

# Establish SSH to device and run show command
net_connect = ConnectHandler(**ios1)
output = net_connect.send_command('show version')
net_connect.disconnect()
print(output)
```

### Line-by-Line Walkthrough

**Line 1: `#!/usr/bin/env python`**

The shebang line. On Linux/Mac, it tells the OS which interpreter to use when you run the script directly (`./1-netmiko-show.py`). Harmless on Windows. Good practice to include.

**Line 2: `from netmiko import ConnectHandler`**

Import the `ConnectHandler` class from the netmiko package. Remember Chapter 5 — `ConnectHandler` is a class, and we are about to create an **instance** of it.

**Lines 4–8: The device dictionary**

```python
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}
```

This is a plain Python **dictionary** (Chapter 2). Five key-value pairs define everything Netmiko needs to make the SSH connection. The variable name `ios1` is arbitrary — you could name it `device` or `router1` or anything else.

**Line 10: `net_connect = ConnectHandler(`**ios1)**

The `ios1` syntax unpacks** the dictionary, passing each key as a keyword argument. This is equivalent to:

```python
net_connect = ConnectHandler(
    device_type='cisco_ios',
    ip='198.18.1.11',
    username='cisco',
    password='cisco'
)
```

Under the hood, Netmiko:

1. Opens a TCP connection to port 22
2. Performs the SSH handshake
3. Logs in with username and password
4. Waits for the device prompt (`#` or `>`)
5. Returns the connection object as `net_connect`

**Line 11: `output = net_connect.send_command('show version')`**

Sends `show version` to the device and waits for the output. Netmiko detects when the command output ends (prompt returns) and captures everything in between. Returns the output as a **string**.

**Line 12: `net_connect.disconnect()`**

Closes the SSH connection cleanly. Releases the VTY line on the device.

**Line 13: `print(output)`**

Print the captured output string to the terminal.

### Expected Output (abbreviated)

```python
Cisco IOS XE Software, Version 16.11.01
Cisco IOS Software [Gibraltar], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M),
Version 16.11.01, RELEASE SOFTWARE (fc5)
...
cisco CSR1000V (VXE) processor (revision VXE) with 2392579K/3075K bytes of memory.
...
1 Gigabit Ethernet interface
32768K bytes of non-volatile configuration memory.
...
```

### Python Concepts Used

| Concept | Where Used | Chapter |
| --- | --- | --- |
| Dictionary | ios1 = {...} | Ch 2 |
| ** unpacking | ConnectHandler(**ios1) | Ch 3/5 |
| Variable assignment | output = ... | Ch 2 |
| Method call | .send_command(...) | Ch 5 |
| print() | print(output) | Ch 1 |

## Best Practice: The with Statement

Script 1 works, but it has a problem: if `send_command()` raises an exception, `disconnect()` is never called — the SSH session leaks. The `with` statement (Chapter 4) solves this:

```python
#!/usr/bin/env python
# 1-netmiko-show-improved.py

from netmiko import ConnectHandler

ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}

# with statement: disconnect() called automatically when block exits
# Even if an exception occurs
with ConnectHandler(**ios1) as net_connect:
    output = net_connect.send_command('show version')
    print(output)

# net_connect.disconnect() called here automatically
print('Script complete.')
```

> **Note:** 📝
Note
💡
Best practice:
Always use
with ConnectHandler(...) as conn:
instead of manually calling
.disconnect()
. It is cleaner, safer, and consistent with professional Python style.

## Lab Script 2 — 2-netmiko-config.py

Sending configuration commands instead of show commands. One key difference: use `send_config_set()` instead of `send_command()`.

### The Full Script

```python
#!/usr/bin/env python
from netmiko import ConnectHandler

# SSH Connection Details
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}

# Establish SSH to device and run config command
net_connect = ConnectHandler(**ios1)
output = net_connect.send_config_set('logging host 10.1.1.1')
net_connect.disconnect()
print(output)
```

### What send_config_set() Does

Unlike `send_command()`, `send_config_set()`:

1. Enters `configure terminal` automatically
2. Sends your command(s)
3. Exits config mode automatically (`end`)

It accepts either a **string** (single command) or a **list** (multiple commands):

```python
# Single command — string
output = net_connect.send_config_set('logging host 10.1.1.1')

# Multiple commands — list (preferred)
config_commands = [
    'logging console',
    'logging host 10.1.1.3',
    'ntp server 10.1.1.4',
    'ip name-server 10.1.1.5',
    'no ip http server',
]
output = net_connect.send_config_set(config_commands)
```

### Expected Output

```python
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
CSR1(config)#logging host 10.1.1.1
CSR1(config)#end
CSR1#
```

### Saving the Configuration

Always save after config changes:

```python
with ConnectHandler(**ios1) as conn:
    output = conn.send_config_set('logging host 10.1.1.1')
    save_output = conn.save_config()   # Equivalent to 'write memory'
    print(output)
    print(save_output)
```

## Key Methods Summary

| Method | Purpose | Returns |
| --- | --- | --- |
| send_command(cmd) | Run a show command | String |
| send_command(cmd, use_textfsm=True) | Run + parse with TextFSM | List of dicts |
| send_command(cmd, use_genie=True) | Run + parse with Genie | Nested dict |
| send_config_set(cmds) | Push config commands | String |
| send_config_from_file(path) | Push commands from file | String |
| save_config() | write memory | String |
| find_prompt() | Get device prompt (e.g., CSR1# ) | String |
| disconnect() | Close SSH session | None |
| enable() | Enter enable mode | None |

## Running Multiple Show Commands

```python
from netmiko import ConnectHandler

ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}

show_commands = [
    'show version',
    'show ip interface brief',
    'show ip route summary',
    'show processes cpu sorted | head 10',
]

with ConnectHandler(**ios1) as conn:
    for command in show_commands:
        print(f'\n{"="*55}')
        print(f'Command: {command}')
        print('='*55)
        output = conn.send_command(command)
        print(output)
```

## Parsing and Filtering Telemetry with TextFSM

When we run show commands like `show version` or `show ip interface brief`, Netmiko returns the output as a plain Python string. While strings are easy to print, they are incredibly difficult to parse programmatically. If you wanted to find only the down interfaces, you would have to write complex regular expressions (`re` module) or iterate line-by-line using string manipulation methods like `.split()`, `.strip()`, and `.startswith()`.

Netmiko has a built-in integration with **TextFSM** (via the `ntc-templates` package) to solve this. By passing `use_textfsm=True` to `send_command()`, Netmiko automatically matches the command output against a pre-built parser template and returns a **structured list of dictionaries**.

### Real-World Use Case: Auto-Labeling Disconnected Interfaces

Let's look at a common, high-value operations task: finding all switch interfaces that are currently in a `notconnect` state and automatically applying a `NOT-CONNECTED` description to keep the interface database tidy.

Without automation, you would:

1. SSH into the switch.
2. Run `show interfaces status | include notconnect`.
3. Manually type `interface` and `description NOT-CONNECTED` for each matching interface.

Here is the complete Python solution utilizing Netmiko and TextFSM parsing:

```python
#!/usr/bin/env python
from netmiko import ConnectHandler
import json

# Device connection details
sw_01 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

with ConnectHandler(**sw_01) as connection:
    print("Collecting interface status telemetry...")
    # Executing show command with TextFSM parsing active
    output = connection.send_command('show interfaces status', use_textfsm=True)

    # TextFSM returns a list of dictionaries, for example:
    # [
    #   {'port': 'Gi0/0', 'name': '', 'status': 'connected', 'vlan': '10', ...},
    #   {'port': 'Gi0/2', 'name': '', 'status': 'notconnect', 'vlan': '1', ...}
    # ]

    # Use list comprehension to filter out ports with status 'notconnect'
    not_connect_interfaces = [
        item['port'] for item in output
        if item['status'] == 'notconnect'
    ]

    print(f"Found {len(not_connect_interfaces)} disconnected interfaces: {not_connect_interfaces}")

    if not_connect_interfaces:
        connection.enable()

        # Configure each disconnected interface
        for interface in not_connect_interfaces:
            commands = [
                f"interface {interface}",
                "description NOT-CONNECTED"
            ]
            print(f"Configuring description on interface {interface}...")
            config_output = connection.send_config_set(commands)
            print(config_output)

        print("Saving configuration...")
        connection.save_config()

print("Script complete.")
```

### Walkthrough of the Logic

- **`use_textfsm=True`**: This flag transforms Netmiko's output from a single string block into a list of structured key-value maps.
- **`not_connect_interfaces = [item['port'] for item in output if item['status'] == 'notconnect']`**: A clean, elegant Python list comprehension (Chapter 3) that filters our structured telemetry data and extracts only the interface port names that match our targeting criteria.
- **Iterative Configuration Loop**: Loops through the list of ports, constructs configuration command pairs, and runs them using `send_config_set()`.

This design separates **telemetry parsing** (reading state) from **state change execution** (configuring interfaces) seamlessly.

## Troubleshooting Common Issues

| Error | Cause | Fix |
| --- | --- | --- |
| NetmikoTimeoutException | Device unreachable | Check IP, firewall, SSH enabled |
| NetmikoAuthenticationException | Wrong credentials | Verify username/password |
| SSHException | SSH not enabled | ip ssh version 2 on device |
| ValueError: device_type not found | Typo in device_type | Use exact strings from the table above |
| Hanging indefinitely | Slow device / wrong prompt | Increase read_timeout parameter |

```python
# Increase timeout for slow devices
with ConnectHandler(**ios1, read_timeout=60, conn_timeout=30) as conn:
    output = conn.send_command('show running-config', read_timeout=120)
```

## Practice Exercises

Practice Exercises
1
Run script
1-netmiko-show.py
against your lab device. What IOS version is it running

1. Modify the script to run `show ip interface brief` instead of `show version`. What interfaces are shown

1. Rewrite script 1 using the `with` statement.

1. Run script `2-netmiko-config.py`. Verify the logging config was applied with `show running-config | include logging`.

1. Modify script 2 to push 4 configuration commands (your choice) as a list.


---


# Multi-Device Automation and File-Driven Inventory

> "The goal of automation is not to reduce jobs, but to reduce the time spent on work that machines do better than humans." — Inspirational

> **Note:** 📝
Note
*"The goal of automation is not to reduce jobs, but to reduce the time spent on work that machines do better than humans."*

## Chapter Goal

Scale from one device to your entire fleet. This chapter covers the transition from hardcoded single-device scripts to data-driven, file-based multi-device automation — the exact progression of lab scripts 3 and 4.

**Key Points:**

- Lists of dictionaries — your fleet as a Python data structure (lab script 3)
- Reading device inventories from files — the `device_list` and `config_commands` files (lab script 4)
- `send_config_from_file()` — pushing configuration from a template file
- Collecting credentials at runtime with `getpass`

## Lab Script 3 — 3-netmiko-config.py : Multiple Devices

### The Full Script

```python
#!/usr/bin/env python
from netmiko import ConnectHandler

# SSH Connection Details
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}

ios2 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.12',
    'username': 'cisco',
    'password': 'cisco',
}

devices = [ios1, ios2]

for device in devices:
    print('Connecting to device ' + device['ip'])
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set('logging host 10.1.1.2')
    net_connect.disconnect()
    print(output)
```

### Walkthrough: The List of Dictionaries Pattern

**`devices = [ios1, ios2]`**

This creates a list of dictionaries — each element is one complete connection dictionary. This is the same pattern from Chapter 2: a list where each item is a dictionary. The list holds your fleet.

**`for device in devices:`**

On the first iteration, `device` holds `ios1`. On the second, it holds `ios2`. The code inside the loop runs identically for each — the same six config commands go to every switch.

**`ConnectHandler(`**device)**

Each iteration creates a fresh connection. The `**device` unpacking works the same whether the variable is named `ios1` or `device` — it passes all keys as keyword arguments.

**Python Connection to Chapter 2:**

`device['ip']` accesses the `'ip'` key from the current device dictionary. This is direct dictionary access from Chapter 2.

### Expected Output

```python
Connecting to device 198.18.1.11
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
CSR1(config)#logging host 10.1.1.2
CSR1(config)#end

Connecting to device 198.18.1.12
configure terminal
...
CSR2(config)#logging host 10.1.1.2
CSR2(config)#end
```

## Lab Script 4 — 4-netmiko-config.py : File-Driven Inventory

### The Full Script

```python
#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

# SSH username and password provided by user
username = input('Enter your SSH username: ')
password = getpass('Enter your password: ')

# Sending device ip's stored in a file
with open('device_list') as f:
    device_list = f.read().splitlines()

# Iterate through device list and configure the devices
for device in device_list:
    print('Connecting to device ' + device)
    ip_address_of_device = device

    # SSH Connection details
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_from_file('config_commands')
    net_connect.disconnect()
    print(output)
```

### Walkthrough: All New Concepts

**`from getpass import getpass`**

Import the `getpass` function for secure password input (no echo).

**`username = input('Enter your SSH username: ')`**

`input()` prompts the user and returns what they type. Credentials collected at runtime — not hardcoded.

**`password = getpass('Enter your password: ')`**

Same as `input()` but characters are not echoed. The user sees only the prompt, not what they type.

**`with open('device_list') as f: device_list = f.read().splitlines()`**

Opens `device_list` file, reads it, splits on newlines. Result: `['198.18.1.11', '198.18.1.12']`

**`for device in device_list:`**

Loop through each IP string. On first iteration, `device = '198.18.1.11'`.

**`ios_device = {'device_type': 'cisco_ios', 'ip': ip_address_of_device, ...}`**

Build the connection dictionary inside the loop using the current IP. This is the key pattern: one dictionary built per device per iteration, using runtime data.

**`net_connect.send_config_from_file('config_commands')`**

Reads commands from the `config_commands` file and sends them all. This separates configuration data from automation logic.

### The device_list File

```python
198.18.1.11
198.18.1.12
```

One IP per line. No headers, no formatting. Clean and simple.

### The config_commands File

```python
logging console
logging host 10.1.1.3
ntp server 10.1.1.4
ip name-server 10.1.1.5
no ip http server
no ip http secure-server
snmp-server community cisco_public RO
snmp-server community cisco_private RW
snmp-server location dCloud
ip access-list extended TEST_ACL
 permit ip 1.1.1.0 0.0.0.255 any
 permit ip 2.2.2.0 0.0.0.255 any
 permit ip 3.3.3.0 0.0.0.255 any
interface loopback 10
 description Created by Python
router ospf 10
 network 0.0.0.0 0.0.0.0 area 0
```

This file is pushed verbatim to every device. Change the file content, re-run the script, and all devices get the updated configuration.

> **Note:** 📝
Note
🔑
Key Insight:
Script 4 establishes the architecture of professional network automation:
data files
(device_list, config_commands) contain the specifics;
the script
contains the logic. To target different devices, change the data file. To push different config, change the config file. The script never changes.

### Python Concepts Used

| Concept | Where | Chapter |
| --- | --- | --- |
| input() | Get username | Ch 1 |
| getpass() | Get password securely | Ch 4 |
| with open() as f: | File reading | Ch 4 |
| .splitlines() | Parse file lines | Ch 2 |
| for device in device_list: | Loop through IPs | Ch 3 |
| Dict inside loop | Build per-device params | Ch 2 |
| send_config_from_file() | Push from file | Netmiko |

## Building a Scalable Multi-Device Runner

Here is the pattern from script 4 refactored into a reusable function structure:

```python
#!/usr/bin/env python3
"""
multi_device_config.py
Refactored version of 4-netmiko-config.py with function organization.
"""

import os
from getpass import getpass
from netmiko import ConnectHandler

def load_device_list(filepath='device_list'):
    """Load device IPs from a file."""
    with open(filepath) as f:
        return f.read().splitlines()

def build_device_params(ip, username, password):
    """Build a Netmiko connection dictionary."""
    return {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
    }

def configure_device(device_params, config_file='config_commands'):
    """Connect to one device and push config from file."""
    net_connect = ConnectHandler(**device_params)
    output = net_connect.send_config_from_file(config_file)
    net_connect.save_config()
    net_connect.disconnect()
    return output

def main():
    username = os.getenv('NETMIKO_USERNAME') or input('Username: ')
    password = os.getenv('NETMIKO_PASSWORD') or getpass('Password: ')

    device_ips = load_device_list()
    print(f'Processing {len(device_ips)} devices...\n')

    for ip in device_ips:
        print(f'Connecting to {ip}...', end=' ')
        params = build_device_params(ip, username, password)
        output = configure_device(params)
        print('✅ Done')
        print(output)

if __name__ == '__main__':
    main()
```

## Practice Exercises

Practice Exercises
1
Create a
device_list
file with 2 or 3 IP addresses. Run script 4 against your lab devices (or simulate it by printing instead of connecting).

1. Create a `config_commands` file with 3 configuration commands. Verify they were applied with `show running-config`.

1. Refactor script 3 to use a list comprehension to build the device list — start from a list of IP strings and build the list of dicts inline.


---


# Production Scripts: Exceptions, Env Vars, and Show Commands

> Constructing clean, reliable networks through software.

## Chapter Goal

Add the three elements that separate development scripts from production scripts: comprehensive exception handling, secure credential management with environment variables, and multi-command show collection from files. Covers lab scripts 5, 6, and 7.

## Lab Script 5 — 5-netmiko-final.py : Full Exception Handling

### The Full Script

```python
#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException

# Collect login credentials
username = input('Enter your SSH username: ')
password = getpass('Enter your password: ')

# Read device list from file
with open('device_list') as f:
    device_list = f.read().splitlines()

# Iterate through device list and configure
for devices in device_list:
    print('Connecting to device ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (NetmikoAuthenticationException):
        print('Authentication failure: ' + ip_address_of_device)
        continue
    except (NetmikoTimeoutException):
        print('Timeout to device: ' + ip_address_of_device)
        continue
    except (EOFError):
        print('End of file while attempting device ' + ip_address_of_device)
        continue
    except (SSHException):
        print('SSH Issue. Are you sure SSH is enabled ' + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print('Some other error: ' + str(unknown_error))
        continue

    # Only runs if connection succeeded
    output  = net_connect.send_config_from_file('config_commands')
    output += net_connect.save_config()
    net_connect.disconnect()
    print(output)
```

### The Exception Architecture

Four specific exception types, each with a targeted message, followed by a catch-all:

| Exception | Meaning | Remediation |
| --- | --- | --- |
| NetmikoAuthenticationException | Wrong credentials | Check username/password, AAA config |
| NetmikoTimeoutException | Can't reach device | Check IP, firewall, SSH enabled |
| EOFError | Connection dropped mid-session | VTY limit, ACL blocking |
| SSHException | SSH protocol issue | Enable SSH v2, check key |
| Exception | Anything else | Log and skip |

**Why `continue`**

Without `continue`, a connection failure causes Python to try `send_config_from_file()` — which fails because there is no connection — and the script crashes. With `continue`, the failed device is skipped and the loop moves to the next IP.

**`output += net_connect.save_config()`**

`+=` appends the save output to the config output string. The combined output gives you a complete record of what happened on the device.

> **Note:** 📝
Note
🔑
Script 5 is the template for every production Netmiko script you will write.
Every element — file inventory, runtime credentials, specific exception handling, continue-on-failure, save config — is a production requirement.

## Lab Script 6 — 6-netmiko-final.py : Environment Variables

### The Full Script

```python
#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException

# Check environment variable for credentials; fall back to getpass
username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Enter username: ')
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# (rest of script identical to script 5)
with open('device_list') as f:
    device_list = f.read().splitlines()

for devices in device_list:
    print('Connecting to device ' + devices)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': devices,
        'username': username,
        'password': password
    }
    try:
        net_connect = ConnectHandler(**ios_device)
    except NetmikoAuthenticationException:
        print('Authentication failure: ' + devices)
        continue
    except NetmikoTimeoutException:
        print('Timeout to device: ' + devices)
        continue
    except EOFError:
        print('End of file: ' + devices)
        continue
    except SSHException:
        print('SSH Issue: ' + devices)
        continue
    except Exception as e:
        print('Unknown error: ' + str(e))
        continue

    output  = net_connect.send_config_from_file('config_commands')
    output += net_connect.save_config()
    net_connect.disconnect()
    print(output)
```

### The Credential Pattern

```python
username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Enter username: ')
```

This reads as: "If the environment variable NETMIKO_USERNAME is set, use it. Otherwise, prompt the user."

**Setting variables before running:**

```python
# Linux / Mac
export NETMIKO_USERNAME="cisco"
export NETMIKO_PASSWORD="cisco"
python 6-netmiko-final.py

# Windows PowerShell
$env:NETMIKO_USERNAME = "cisco"
$env:NETMIKO_PASSWORD = "cisco"
python 6-netmiko-final.py
```

**For automated runs (cron, CI/CD):**

The platform injects environment variables. GitLab CI sets them in Settings → CI/CD → Variables. Jenkins sets them in credentials. Ansible Tower uses the Vault. Your script works the same way — it just reads the environment.

## Lab Script 7 — 7-netmiko-final.py : Multiple Show Commands from File

### The Full Script

```python
#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException

username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Enter username: ')
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Read device IPs
with open('device_list') as f:
    device_list = f.read().splitlines()

# Read show commands from file
with open('show_command') as f:
    show_commands = f.readlines()

for devices in device_list:
    print('Connecting to device ' + devices)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': devices,
        'username': username,
        'password': password
    }
    try:
        net_connect = ConnectHandler(**ios_device)
    except NetmikoAuthenticationException:
        print('Authentication failure: ' + devices)
        continue
    except NetmikoTimeoutException:
        print('Timeout to device: ' + devices)
        continue
    except EOFError:
        print('End of file: ' + devices)
        continue
    except SSHException:
        print('SSH Issue: ' + devices)
        continue
    except Exception as e:
        print('Unknown error: ' + str(e))
        continue

    # Inner loop: run every show command on this device
    net_connect = ConnectHandler(**ios_device)
    for command in show_commands:
        output = net_connect.send_command(command)
        print(command + output + '\n')
    net_connect.disconnect()
```

### The show_command File

```python
show runn | in logging
show runn | in ntp
show runn | in snmp
show ip access-lists TEST_ACL
show ip ospf neighbor
show ip ospf interface brief
show ip interface brief
```

### The Nested Loop

```python
for devices in device_list:       # Outer: each device
    ...
    for command in show_commands:  # Inner: each command
        output = net_connect.send_command(command)
        print(command + output + '\n')
```

For 2 devices and 7 commands: 14 `send_command()` calls total. Every command runs on every device. This is the **pre/post change validation pattern** — run it before a change window, save the output, run it again after, compare.

**`f.readlines()` vs `f.read().splitlines()`:**

`readlines()` keeps the `\n` at the end of each line. `splitlines()` strips them. For `send_command()`, both work — Netmiko strips leading/trailing whitespace from commands automatically.

## Production Use Case: VLAN Configuration Standardization Across the Fleet

A common challenge in network operations is **configuration drift**. Over time, different administrators might configure the same VLANs across various switches using slightly different naming conventions (e.g., VLAN 10 named `MGMT` on one switch, `management` on another, and `VLAN0010` on a third). This drift breaks monitoring tools, audits, and automation.

Let's write a production-grade script to audit and standardize VLAN names across your entire fleet of switches based on a golden inventory map.

### The Operational Guardrails

To prevent outages or structural changes during automated runs, a production script must have precise boundaries:

1. **Never create new VLANs:** If a VLAN does not exist on a switch, do not configure it (to avoid introducing unnecessary broadcast domains to random ports).
2. **Never delete VLANs:** The script should only modify names of existing VLANs.
3. **Robust Connection Resiliency:** If one switch is offline or has invalid credentials, log the failure and continue processing the rest of the fleet.
4. **Hiding Secrets:** Pass credentials via environment variables.

### The Standardization Script

```python
#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException, NetmikoTimeoutException
from paramiko.ssh_exception import SSHException

# 1. Golden standard definition of VLANs
GOLDEN_VLANS = {
    '10': 'MGMT',
    '20': 'DATA',
    '30': 'ACTIVE_DIRECTORY',
    '31': 'WEB_SERVERS',
    '32': 'ADMIN_OOB',
    '33': 'NETWORK_CORE'
}

# 2. Secure credential collection
username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Enter SSH username: ')
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass('Enter SSH password: ')

# 3. Read target switches
with open('device_list') as f:
    device_list = f.read().splitlines()

print(f"Starting audit across {len(device_list)} switches...\n")

for ip in device_list:
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
    }

    print(f"Connecting to {ip}...")
    try:
        connection = ConnectHandler(**device_params)
    except NetmikoAuthenticationException:
        print(f"❌ Authentication failed for {ip}")
        continue
    except NetmikoTimeoutException:
        print(f"❌ Timeout reaching device {ip}")
        continue
    except (EOFError, SSHException) as e:
        print(f"❌ SSH protocol issue on {ip}: {str(e)}")
        continue
    except Exception as unknown_error:
        print(f"❌ Unexpected error on {ip}: {str(unknown_error)}")
        continue

    # Connection succeeded! Run audit logic inside try-finally to guarantee disconnect
    try:
        # Run show vlan and parse output into structured dictionary list
        parsed_vlans = connection.send_command('show vlan', use_textfsm=True)

        # Build local switch state mapping: {vlan_id: name}
        current_vlans = {}
        for item in parsed_vlans:
            current_vlans[item['vlan_id']] = item['name']

        print(f"Analyzing VLAN configurations on {ip}...")

        # Track pending config changes
        commands_to_send = []
        for vlan_id, golden_name in GOLDEN_VLANS.items():
            # RULE 1: VLAN must already exist on the switch
            # RULE 2: Current name must differ from our golden standard
            if vlan_id in current_vlans:
                current_name = current_vlans[vlan_id]
                if current_name != golden_name:
                    print(f"  ⚠️ Mismatch found on VLAN {vlan_id}: current='{current_name}', expected='{golden_name}'")
                    commands_to_send.extend([
                        f"vlan {vlan_id}",
                        f"name {golden_name}"
                    ])

        # Apply standardizations if mismatched items exist
        if commands_to_send:
            connection.enable()
            print(f"  ⚙️ Pushing {len(commands_to_send)//2} VLAN name updates to {ip}...")
            config_output = connection.send_config_set(commands_to_send)
            print(config_output)

            print("  💾 Saving configurations...")
            save_output = connection.save_config()
            print(f"  {save_output}")
        else:
            print(f"  ✅ {ip} is already fully standardized.")

    finally:
        print(f"Disconnecting from {ip}...\n")
        connection.disconnect()

print("VLAN fleet standardization audit complete!")
```

### Walkthrough of the Standardization Logic

- **The Golden Map (`GOLDEN_VLANS`)**: A dictionary defining the authoritative mapping of VLAN IDs to their correct names.
- **Telemetry to Local Dict (`current_vlans`)**:

This loop processes the TextFSM output (list of dicts) and builds a simple lookup mapping like `{'10': 'VLAN0010', '20': 'DATA'}`.

- **The Audit Comparison**:

The outer `if` satisfies the requirement to **never create new VLANs** (we only act if `vlan_id` already exists in `current_vlans`). The inner `if` detects a mismatch.

- **Clean Deconnection (`try ... finally`)**: Using a `finally` block guarantees that `connection.disconnect()` is executed even if a parsing error occurs mid-run, keeping VTY lines open for other operations.

## Production Use Case 2: Interactive Cisco Interface Repair Bot

A common day-to-day operations requirement is auditing interfaces across multiple switches to find ports that are down. When an administrator encounters ports that are **administratively down** (disabled manually by configuration), they often want to interactively confirm whether to re-enable them.

Let's look at a production-grade interactive troubleshooting bot. It reads its device configuration from a YAML-structured file (`devices.yaml`), establishes secure connections, prints ports that are down, and prompts you to bring them back online with an interactive CLI input.

### The Devices YAML File ( devices.yaml )

```python
devices:
  - name: "csr1"
    device_type: "cisco_ios"
    host: "198.18.1.11"
    username: "cisco"
    password: "cisco"
  - name: "csr2"
    device_type: "cisco_ios"
    host: "198.18.1.12"
    username: "cisco"
    password: "cisco"
```

### The Interface Checker Script

```python
#!/usr/bin/env python
from netmiko import ConnectHandler, NetmikoTimeoutException  # Import Netmiko classes
import yaml  # Import PyYAML to read YAML files

print("Cisco Interface Checker\n")  # Print a simple title for the script

# Load device list from YAML file
with open("devices.yaml") as file:  # Open the devices.yaml file
    data = yaml.safe_load(file)  # Read its content and convert it into a Python dictionary

devices = data["devices"]  # Get the list of devices from the dictionary

# Loop through each device in the list
for device in devices:
    print("Connecting to", device.get("name", "Unknown"))  # Print which device we are connecting to

    # Prepare the parameters Netmiko needs to connect
    netmiko_params = {
        "device_type": device.get("device_type"),  # Cisco IOS, etc.
        "host": device.get("host"),  # IP address of the device
        "username": device.get("username"),  # SSH username
        "password": device.get("password")  # SSH password
    }

    # Skip this device if any parameter is missing
    if None in netmiko_params.values():
        print(f"⚠️ Skipping {device.get('name', 'Unknown')} - missing host or credentials\n")
        continue  # Go to the next device in the loop

    # Try to connect to the device
    try:
        connection = ConnectHandler(**netmiko_params)  # Establish SSH connection
    except NetmikoTimeoutException:  # If connection times out
        print(f"⚠️ Could not connect to {device['name']} (timeout)\n")
        continue  # Skip this device and continue
    except Exception as e:  # Any other connection error
        print(f"⚠️ Could not connect to {device['name']}: {e}\n")
        continue

    # Get interface status
    output = connection.send_command("show ip interface brief")  # Run command to check all interfaces
    lines = output.splitlines()  # Split the output into lines

    print("\nInterfaces not UP:\n")  # Print a heading

    # Loop through each line (skip header at index 0)
    for line in lines[1:]:  # Skip the first line because it's the header
        parts = line.split()  # Split the line into individual words/columns
        if len(parts) < 6:  # If there are not enough columns, skip this line
            continue

        interface = parts[0]  # The first column is the interface name
        status = " ".join(parts[4:-1])  # Combine columns 4 to second-last to get status
        protocol = parts[-1]  # The last column is the protocol status

        # Only report interfaces that are not fully up
        if status.lower() != "up" or protocol.lower() != "up":
            print(f"{interface} is {status}/{protocol}")  # Print interface and its status

            # If interface is administratively down, ask user if they want to enable it
            if status.lower() == "administratively down":
                answer = input(f"Do you want to enable {interface} on {device['name']} (yes/no): ")  # Prompt user
                if answer.lower() in ["yes", "y"]:  # If user says yes
                    print(f"Enabling {interface}...")  # Print action
                    connection.send_config_set([f"interface {interface}", "no shutdown"])  # Send commands to enable
                    print(f"{interface} is now enabled!")  # Confirm to the user

    connection.disconnect()  # Disconnect from the device
    print(f"\nFinished checking, {device.get('name', 'Unknown')}")  # Print completion message for this device
    print("---------------------------------")  # Print a separator line
```

### Walkthrough of the Interactive Repair Logic

- **Structured YAML Inventory**: Rather than reading flat IP files, we use `yaml.safe_load(file)` to load descriptive multi-parameter dictionaries. This lets us map hostnames, device types, IPs, and passwords in a single structured schema.
- **Command Output Splitting**: We capture `show ip interface brief`, and use `.splitlines()` and `.split()` to parse the tabular output column-by-column without relying on external parsing libraries.
- **Interactive Remediation Loop**:

This is the first example of a **closed-loop human-in-the-loop repair system**. When a port mismatch is discovered, the script pauses execution, captures operator confirmation via `input()`, executes a localized target configuration change (`no shutdown`), and immediately prints a status confirmation before proceeding.


---


# Automated Backup and Inventory Reports

> Constructing clean, reliable networks through software.

## Chapter Goal

Build two of the highest-value automation tools in network operations: automated configuration backup and structured device inventory reporting. Covers lab scripts 8, 9, and 10.

## Lab Script 8 — 8-netmiko_backup.py : Configuration Backup

### The Full Script

```python
#!/usr/bin/env python
import os, time
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler

print(datetime.now())

# Credentials
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Enter username: ')

# Create backup folder
if not os.path.exists('backup/'):
    os.mkdir('backup')

# Read device list
with open('device_list') as f:
    device_list = f.read().splitlines()

# Iterate and backup each device
for devices in device_list:
    print('Connecting to device ' + devices)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': devices,
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**ios_device)

    # Get hostname from device prompt
    hostname = net_connect.find_prompt()[:-1]

    # Collect running config
    print(f'Initiating config backup on {hostname}..')
    output = net_connect.send_command("show run")

    # Save to file named after hostname
    with open(f'backup/{hostname}.cfg', 'w') as file:
        file.write(output)

    print('Finished config backup \n')
    net_connect.disconnect()
    time.sleep(3)

print(datetime.now())
```

### Key Patterns

**`print(datetime.now())`** (first and last lines)

Timestamps the run. When you look at the output later, you know exactly when it ran and how long it took.

**`if not os.path.exists('backup/'): os.mkdir('backup')`**

Create the backup directory only if it does not exist. Without the `if`, `os.mkdir()` raises `FileExistsError` on the second run.

**`hostname = net_connect.find_prompt()[:-1]`**

`find_prompt()` returns the current prompt, e.g., `CSR1#`. The `[:-1]` slice removes the last character (the `#`), leaving `CSR1`. This is how the script names each backup file after the device — no manual hostname mapping needed.

**`with open(f'backup/{hostname}.cfg', 'w') as file:`**

Creates `backup/CSR1.cfg` for device 1, `backup/CSR2.cfg` for device 2, etc.

**`time.sleep(3)`**

A 3-second pause between devices. Prevents overwhelming devices with rapid back-to-back connections and gives SSH sessions time to fully close.

### Output Files

```python
backup/
  CSR1.cfg     ← full running config of device 1
  CSR2.cfg     ← full running config of device 2
```

## Lab Script 9 — 9-netmiko-report.py : Genie Parsing Introduction

### The Full Script

```python
#!/usr/bin/env python
from netmiko import ConnectHandler
from pprint import pprint

ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.11',
    'username': 'cisco',
    'password': 'cisco',
}

# Connect and use Genie to parse 'show version'
net_connect = ConnectHandler(**ios1)
output = net_connect.send_command('show version', use_genie=True)
net_connect.disconnect()

print(output)
print()
pprint(output)
print()
```

### What use_genie=True Does

Without Genie:

```python
output = net_connect.send_command('show version')
type(output)   # 'str'>
# "Cisco IOS XE Software, Version 16.11.01\n..."
```

With Genie:

```python
output = net_connect.send_command('show version', use_genie=True)
type(output)   # 'dict'>
# {
#   'version': {
#     'hostname': 'CSR1',
#     'chassis': 'CSR1000V',
#     'chassis_sn': '9KIBQAQ3OPE',
#     'os': 'IOS-XE',
#     'version': '16.11.01',
#     ...
#   }
# }
```

**`pprint`** ("pretty print") formats nested dictionaries readably. Regular `print()` on a large dict produces one unreadable line.

## Lab Script 10 — 10-netmiko-report.py : Multi-Device Inventory Report

### The Full Script

```python
#!/usr/bin/env python
import os
import csv
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint
from tabulate import tabulate

password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Enter username: ')

# Initialize inventory with header row
inventory = []
title = ["Hostname", "Chassis", "Serial No", "os", "version"]
inventory.append(title)

# Read device list
with open('device_list') as f:
    device_list = f.read().splitlines()

# Collect data from each device
for devices in device_list:
    print('Connecting to device ' + devices)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': devices,
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_command('show version', use_genie=True)
    net_connect.disconnect()

    # Extract structured fields from Genie output
    hostname = output["version"]["hostname"]
    chassis  = output["version"]["chassis"]
    serial   = output["version"]["chassis_sn"]
    os_type  = output["version"]["os"]
    version  = output["version"]["version"]

    device_details = [hostname, chassis, serial, os_type, version]
    inventory.append(device_details)

# Print formatted table
print(tabulate(inventory, headers="firstrow", tablefmt="grid"))

# Save to CSV
with open("inventory.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(inventory)
```

### The Inventory Build Pattern

```python
# Start with a list containing the header row
inventory = [["Hostname", "Chassis", "Serial No", "os", "version"]]

# For each device, extract fields and append a row
device_details = [hostname, chassis, serial, os_type, version]
inventory.append(device_details)

# Result after 2 devices:
# [
#   ["Hostname", "Chassis", ...],     <- header
#   ["CSR1", "CSR1000V", ...],        <- device 1
#   ["CSR2", "CSR1000V", ...],        <- device 2
# ]
```

### Expected Table Output

```python
+----------+----------+--------------+--------+---------+
| Hostname | Chassis  | Serial No    | os     | version |
+==========+==========+==============+========+=========+
| CSR1     | CSR1000V | 9KIBQAQ3OPE  | IOS-XE | 16.11.01|
+----------+----------+--------------+--------+---------+
| CSR2     | CSR1000V | 9KIBQAQ3OPF  | IOS-XE | 16.11.01|
+----------+----------+--------------+--------+---------+
```

**`tabulate(inventory, headers="firstrow", tablefmt="grid")`:**

- `headers="firstrow"` — use the first list as column headers
- `tablefmt="grid"` — draw the border grid

> **Note:** 📝
Note
🔑
Business value:
This script is immediately demonstrable. "Press Enter, it SSHes to every device and gives you a spreadsheet of what is running where." From zero to actionable inventory in under 30 lines.

## Real-World Operations: Pre- and Post-Migration Telemetry Collection

In professional network administration, a fundamental rule is: **never perform a network change without collecting state snapshots before and after the change.**

If you migrate a switch or cut over a fiber link, you must verify that OSPF neighbors re-establish, the IP routing table remains identical, and MAC/ARP bindings are correct. Doing this manually for dozens of switches takes hours. Let's write an operational automation script that captures critical state telemetry, generating clean, host-specific, and timestamped reports that can be run instantly before and after a change window.

### The Telemetry Script

```python
#!/usr/bin/env python
import os
import time
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException, NetmikoTimeoutException

# 1. Verification command set
VERIFICATION_COMMANDS = [
    'show ip route summary',
    'show ip route',
    'show ip arp',
    'show ip ospf neighbor',
    'show ip interface brief'
]

# 2. Secure credentials
username = os.getenv("NETMIKO_USERNAME") if os.getenv("NETMIKO_USERNAME") else input('Username: ')
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass('Password: ')

# 3. Create telemetry directory
TELEMETRY_DIR = "telemetry_snapshots/"
if not os.path.exists(TELEMETRY_DIR):
    os.makedirs(TELEMETRY_DIR)

# 4. Read target switches
with open('device_list') as f:
    device_list = f.read().splitlines()

# 5. Timestamp for snapshot files
timestamp = time.strftime("%Y%m%d-%H%M%S")
print(f"Beginning telemetry snapshot run at {datetime.now()}...\n")

for ip in device_list:
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password
    }

    print(f"Connecting to {ip}...")
    try:
        connection = ConnectHandler(**device_params)
    except (NetmikoAuthenticationException, NetmikoTimeoutException) as e:
        print(f"❌ Connection failed for {ip}: {str(e)}")
        continue

    try:
        # Determine the host prompt cleanly (e.g. 'CSR1')
        hostname = connection.find_prompt()[:-1]

        # Unique timestamped output filename
        filename = f"{TELEMETRY_DIR}{timestamp}_{hostname}_snapshot.txt"
        print(f"  📸 Capturing state for '{hostname}' -> Saving to {filename}...")

        with open(filename, 'w') as file_writer:
            file_writer.write(f"====================================================\n")
            file_writer.write(f"NETWORK SNAPSHOT REPORT FOR {hostname} ({ip})\n")
            file_writer.write(f"Captured at: {datetime.now()}\n")
            file_writer.write(f"====================================================\n\n")

            for command in VERIFICATION_COMMANDS:
                file_writer.write(f"----------------------------------------------------\n")
                file_writer.write(f"COMMAND: {command}\n")
                file_writer.write(f"----------------------------------------------------\n")

                # Execute show command
                output = connection.send_command(command)
                file_writer.write(output + "\n\n")

        print(f"  ✅ Snapshot complete for {hostname}.\n")

    finally:
        connection.disconnect()

print("All device snapshots gathered successfully!")
```

### Walkthrough of the Snapshot Pattern

- **Unique File Names**: We construct a structured path like `telemetry_snapshots/20260517-120000_CSR1_snapshot.txt`. The date-time stamp ensures that pre-change run outputs never overwrite post-change run outputs.
- **Structured Snapshot Body**:

The script loops through our diagnostics list, executes each command, writes the command name header, and appends the raw output block.

- **Diffing Snapshots**: Because the output is saved in structured text, you can instantly compare two files using any standard diff utility:

This immediately highlights any missing routing table entries, down interfaces, or lost OSPF neighbors.
