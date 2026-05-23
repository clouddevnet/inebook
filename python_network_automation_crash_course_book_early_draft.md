# Python Network Automation Crash Course

## Preface

If you are a network engineer, you already automate more than you may realize.
Every time you follow a change plan, paste a known-good command sequence, check
the same output on multiple switches, or keep a personal checklist for a
maintenance window, you are describing a repeatable process.

Python gives that process a better home.

This book is for the engineer who knows the CLI but wants to stop being trapped
inside it. You will not be asked to forget how routers, switches, firewalls,
interfaces, routing tables, or configuration modes work. That knowledge is your
advantage. The purpose of this book is to take the Python learning path that has
worked so well for general beginners and rebuild it around the daily world of
network operations.

So instead of learning lists with random names, you will learn lists with device
inventories and command queues. Instead of learning dictionaries as abstract
key-value examples, you will model devices, interfaces, VLANs, API responses,
and parsed command output. Instead of waiting until the end to see why Python
matters, you will see the network use case from the first program.

The promise is simple: each chapter teaches one Python idea, then immediately
shows how that idea helps a network engineer.

## How This Book Works

The book starts gently. You will print messages, store device facts in
variables, and build lists of devices and commands. These early examples are
small on purpose. A script that prints a planned command is safer than a script
that logs into a router before you understand what the code is doing.

As the chapters progress, the examples grow into real automation patterns:

- building command strings from variables
- storing device inventory in lists and dictionaries
- looping over devices and commands
- validating operator input
- writing reusable functions
- modeling devices and sessions with classes
- reading and writing JSON, YAML, CSV, and text files
- testing automation logic before using it in a lab
- connecting to devices with Netmiko
- collecting show commands across many devices
- preparing safe configuration workflows
- generating reports
- using APIs
- finishing with capstone projects for backups, reports, and inventory-driven automation

The final projects will include practical scripts such as connecting to a
device and running a show command, pushing simple configuration safely, backing
up running configurations, building inventory reports, and eventually scaling
the same thinking with Nornir. But those scripts will not be treated as magic.
By the time you reach them, every line should feel like something you have
already met in a smaller form.

This is the rhythm of the book:

```text
learn one Python idea -> apply it to a network task -> make one safe change -> explain the result
```

If you follow that rhythm, Python will stop feeling like a separate career and
start feeling like another tool in your network engineering toolbox.

---

# Chapter 1: Getting Started in a Network Lab

## What This Chapter Teaches

In *Python Crash Course*, Chapter 1 is about getting Python running and printing
a tiny message. That can feel almost too small, but it is the most important
habit in programming: make a change, run the program, and look at what happened.

For a network engineer, that same habit becomes:

```text
write a small script -> run it -> inspect output -> change one value -> run it again
```

Before Python logs into a router, parses a firewall policy, or backs up a
switch, it must first do one humble thing: run correctly on your machine.

## Why Network Engineers Need Automation

The CLI is not going away. You still need to understand commands, prompts,
privilege levels, interfaces, routing tables, and device behavior. Automation
does not replace network knowledge. It rewards it.

What changes is how repeated work gets done.

CLI-only management works well when the task is small:

- Check one interface.
- Add one NTP server.
- Look at one routing table.
- Copy one running configuration.

But networks rarely stay that small. The same CLI workflow becomes fragile when
you need to repeat it across dozens or hundreds of devices:

- Did every device get the same command?
- Did you miss one switch?
- Did you paste the wrong config into one terminal?
- Did you save the output somewhere consistent?
- Can someone else prove what happened later?

Python helps because it turns a repeated manual process into a written process.
Once the process is written down as code, it can be reviewed, tested, improved,
and run the same way again.

## Why Python Is a Good First Language for Network Engineers

Python is popular in network automation for practical reasons:

- It reads close to plain English.
- It has a huge ecosystem of libraries.
- It works well with text, files, JSON, YAML, APIs, and SSH.
- It has mature network libraries such as Netmiko.
- It lets you start small before you build larger systems.

That last point matters. You do not need to start with a framework, a database,
or a controller. Your first useful automation can be as small as:

```python
print("Collect show version from edge-sw1")
```

That line does not touch a device yet, but it starts the habit: say clearly what
the script is supposed to do.

## Your First Network-Flavored Python Program

Create a file named `hello_network.py`:

```python
device_name = "edge-sw1"
mgmt_ip = "192.0.2.10"

print(f"Hello, {device_name}.")
print(f"I will manage you through {mgmt_ip}.")
```

Run it:

```text
python hello_network.py
```

Expected output:

```text
Hello, edge-sw1.
I will manage you through 192.0.2.10.
```

This program has three ideas:

1. `device_name` stores the name of a device.
2. `mgmt_ip` stores the management address.
3. `print()` shows you what Python knows.

That is already a network automation pattern. Later, the device name and
management IP will come from inventory files. For now, they are written directly
in the script so you can see the idea clearly.

## The First Rule: Output Is Feedback

Network engineers already think in feedback loops:

```text
run show command -> read output -> decide next step
```

Python uses the same loop:

```text
run script -> read output -> decide next change
```

When you are learning, print more than you think you need. Print the hostname.
Print the command you plan to run. Print the device list before looping over it.
Print the parsed result before writing a report.

Printing is not childish. It is visibility.

## From Hello World to Hello Device

The twin-bridges Python course begins with a tiny script:

```python
print("Hello world")
```

In this book, we translate that into a network engineer's first tiny script:

```python
hostname = "core-rtr1"
print(f"Hello, {hostname}")
```

Then one step more:

```python
hostname = "core-rtr1"
command = "show version"

print(f"{hostname}# {command}")
```

Expected output:

```text
core-rtr1# show version
```

This is not a real SSH session yet. It is a dry run. A dry run means the script
shows what it would do before it does it. That habit will protect you later
when your scripts can make real changes.

## Preview: What Netmiko Will Eventually Do

Netmiko is a Python library that knows how to connect to network devices over
SSH, send commands, and return output. A future script will look conceptually
like this:

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}

connection = ConnectHandler(**device)
output = connection.send_command("show version")
connection.disconnect()

print(output)
```

Do not worry if this looks like a lot. PacketSwitch's Netmiko introduction makes
the same point: even a short connection script contains several Python ideas,
including imports, dictionaries, strings, function calls, and the `**` unpacking
operator. This book teaches those pieces before asking you to depend on them.

For now, focus on the shape:

```text
device facts -> connection -> command -> output -> disconnect
```

That shape will appear again and again.

## Lab: Build a Run-Only Script

Create `chapter_01_lab.py`:

```python
lab_name = "network-automation-lab"
device = "edge-sw1"
command = "show ip interface brief"

print(f"Lab: {lab_name}")
print(f"Device: {device}")
print(f"Planned command: {command}")
print("Status: dry run only")
```

Run it. Then change only one thing:

- Change `device` to `edge-sw2`.
- Run the script again.
- Confirm that only the device line changes.

This is the smallest safe automation workflow:

```text
edit -> run -> inspect -> repeat
```

## Common Beginner Mistakes

**Mistake: Trying Netmiko before understanding Python basics.**

Netmiko examples are exciting because they touch real devices. But if you do not
understand variables, strings, dictionaries, lists, loops, and functions, every
error message will feel mysterious.

**Mistake: Hard-coding production credentials.**

Early examples often show passwords directly in code because it keeps the
example short. Real automation should use environment variables, prompts,
vaults, or other secret-management tools.

**Mistake: Skipping the dry run.**

Before a script sends config, make it print the planned config. Before it loops
over 100 devices, make it print the 100 device names.

## Chapter 1 Review

You learned:

- Python is useful for network engineers because it makes repeated work visible,
  repeatable, and reviewable.
- A script should start small and show output.
- `print()` is your first troubleshooting tool.
- A dry run is a safe way to build confidence before touching devices.
- Netmiko will eventually provide the bridge from Python to network devices.

## Practice Questions

1. Why is CLI knowledge still important when using Python?
2. What is the difference between running one CLI command manually and writing a script that prints the planned command?
3. Why should early scripts print their plan before connecting to devices?
4. What are the five broad steps in the Netmiko workflow preview?

## Practice Exercise

Write a script that prints a planned backup operation:

```text
Device: core-rtr1
Management IP: 192.0.2.20
Command: show running-config
Output file: core-rtr1.cfg
Mode: dry run
```

Do not use Netmiko yet. Make the script explain the work before it performs the
work.

---

# Chapter 2: Variables, Strings, and Device Facts

## What This Chapter Teaches

In *Python Crash Course*, Chapter 2 introduces variables, strings, numbers, and
comments. In network automation, these are not abstract programming ideas.
They are how you describe the network.

A device has facts:

- hostname
- management IP
- platform
- site
- role
- software version
- serial number

Python variables give names to those facts.

## Variables Are Labels

A variable is a label attached to a value:

```python
hostname = "edge-sw1"
mgmt_ip = "192.0.2.10"
platform = "cisco_ios"
```

Read this as:

```text
hostname means edge-sw1
mgmt_ip means 192.0.2.10
platform means cisco_ios
```

The power is not that Python can remember one value. The power is that the same
script can later use different values for different devices.

## Strings Are Network Text

A string is text. In network automation, most of your early data is text:

- hostnames
- interface names
- commands
- descriptions
- IP addresses
- file names
- device prompts

Examples:

```python
hostname = "dist-sw1"
interface = "GigabitEthernet1/0/24"
description = "Uplink to core-rtr1"
command = "show interface status"
```

The quotes tell Python, "this is text."

## Use Names That Explain the Network

This works:

```python
x = "edge-sw1"
y = "show version"
```

But this is better:

```python
hostname = "edge-sw1"
show_command = "show version"
```

Good variable names reduce mental effort. Network automation already has enough
complexity: device types, prompts, credentials, command output, failure modes.
Do not make the reader decode mysterious variable names too.

## Build Readable Output with f-Strings

An f-string lets you place variable values inside text:

```python
hostname = "edge-sw1"
mgmt_ip = "192.0.2.10"

print(f"{hostname} is managed at {mgmt_ip}.")
```

Output:

```text
edge-sw1 is managed at 192.0.2.10.
```

The `f` before the quote means "format this string." Anything inside `{}` is
evaluated by Python and inserted into the final text.

The twin-bridges string example uses IP address text and f-string formatting to
split and display octets. That is a perfect network example because IP addresses
look simple to humans but still need careful handling in code.

## Splitting an IP Address

An IPv4 address is often written as four octets separated by dots:

```python
ip_address = "192.0.2.10"
octets = ip_address.split(".")

print(octets)
```

Output:

```text
['192', '0', '2', '10']
```

The `.split(".")` method says:

```text
Take this string and cut it wherever you see a dot.
```

Now Python has a list of four strings. Later, you will use lists to process
multiple devices and multiple commands. For now, notice the bridge:

```text
network text -> Python string method -> structured pieces
```

## Building Commands from Variables

Hard-coded command:

```python
print("show running-config interface GigabitEthernet1/0/24")
```

Command built from variables:

```python
interface = "GigabitEthernet1/0/24"
command = f"show running-config interface {interface}"

print(command)
```

Output:

```text
show running-config interface GigabitEthernet1/0/24
```

The second version is more useful because `interface` can change.

```python
interface = "Vlan20"
command = f"show running-config interface {interface}"

print(command)
```

Output:

```text
show running-config interface Vlan20
```

This is the beginning of automation. You stop typing final commands manually
and start writing code that creates the correct command from facts.

## Comments Explain Intent

Comments begin with `#`:

```python
# This is a dry run. Do not connect to a device yet.
hostname = "edge-sw1"
command = "show version"

print(f"Would run {command} on {hostname}")
```

Comments should explain why the code exists or what safety boundary matters.
They should not repeat the obvious.

Weak comment:

```python
# Set hostname
hostname = "edge-sw1"
```

Better comment:

```python
# Use a lab hostname while learning. Production inventory comes later.
hostname = "edge-sw1"
```

## Device Facts as Variables

Here is a small device summary:

```python
hostname = "edge-sw1"
mgmt_ip = "192.0.2.10"
site = "dal"
role = "access"
platform = "cisco_ios"

print(f"{hostname} is an {role} switch in {site}.")
print(f"Management IP: {mgmt_ip}")
print(f"Netmiko platform: {platform}")
```

Output:

```text
edge-sw1 is an access switch in dal.
Management IP: 192.0.2.10
Netmiko platform: cisco_ios
```

The value `cisco_ios` matters because Netmiko uses device types to understand
how to interact with different platforms. You will not connect yet, but you are
already learning how a future connection dictionary will be built.

## Preview: The Future Connection Dictionary

A later Netmiko script will collect device facts into a dictionary:

```python
device = {
    "device_type": "cisco_ios",
    "host": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}
```

Every value in that dictionary starts as a simple Python value. Chapter 2 is
where those values become familiar.

For now, you can print the same facts safely:

```python
device_type = "cisco_ios"
host = "198.18.1.11"
username = "cisco"

print(f"Device type: {device_type}")
print(f"Host: {host}")
print(f"Username: {username}")
print("Password: not printed")
```

That last line is intentional. Do not train yourself to print secrets.

## Lab: Create a Device Fact Sheet

Create `chapter_02_device_facts.py`:

```python
hostname = "edge-sw1"
mgmt_ip = "192.0.2.10"
platform = "cisco_ios"
site = "dal"
role = "access"
software_version = "17.09"

summary = f"{hostname} is a {role} device in {site}."
netmiko_hint = f"Use device_type={platform} when connecting with Netmiko."
version_line = f"Expected software version: {software_version}"

print(summary)
print(f"Management IP: {mgmt_ip}")
print(netmiko_hint)
print(version_line)
```

Run it, then change:

- `hostname`
- `mgmt_ip`
- `site`

Run it again and confirm the output follows the new facts.

## Lab: Build a Show Command

Create `chapter_02_command_builder.py`:

```python
interface = "GigabitEthernet1/0/1"
command = f"show running-config interface {interface}"

print("Dry run command:")
print(command)
```

Then change `interface` to:

```python
interface = "Vlan20"
```

This is a tiny idea, but it scales. The same pattern later becomes:

```text
read interface list -> build command for each interface -> collect output
```

## Common Beginner Mistakes

**Mistake: Forgetting quotes around text.**

This is wrong:

```python
hostname = edge-sw1
```

Python will think `edge` is code, not text. Use quotes:

```python
hostname = "edge-sw1"
```

**Mistake: Printing secrets.**

It is fine to print a hostname, command, or management IP in a lab. Do not print
passwords, API tokens, or private keys.

**Mistake: Building unreadable f-strings.**

If an f-string becomes too long, break the problem into smaller variables.

## Chapter 2 Review

You learned:

- Variables label network facts.
- Strings hold hostnames, commands, interface names, and IP addresses.
- f-strings create readable output and command text.
- Comments should explain intent and safety.
- Chapter 2 values will later become Netmiko connection details.

## Practice Questions

1. Why is `hostname` a better variable name than `x`?
2. What does the `f` mean in an f-string?
3. Why should a script avoid printing passwords?
4. What does `"192.0.2.10".split(".")` produce?

## Practice Exercise

Write a script that stores these facts and prints a clean summary:

- hostname: `core-rtr1`
- management IP: `192.0.2.20`
- platform: `cisco_ios`
- role: `core`
- planned command: `show ip route`

Expected style:

```text
core-rtr1 is a core device.
Connect using platform cisco_ios at 192.0.2.20.
Dry run command: show ip route
```

---

# Chapter 3: Introducing Device Lists

## What This Chapter Teaches

In *Python Crash Course*, Chapter 3 introduces lists. In network automation,
lists are everywhere.

You use lists for:

- device names
- management IPs
- commands
- interfaces
- VLANs
- backup files
- failed devices
- report rows

The CLI trains you to think one device at a time. Lists train Python to think
many items at a time.

## What Is a List?

A list stores multiple values in order:

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]
```

Read it as:

```text
devices is a collection of device names.
```

Print the whole list:

```python
print(devices)
```

Print the first device:

```python
print(devices[0])
```

Output:

```text
edge-sw1
```

Python indexes start at `0`. The first item is index `0`, the second item is
index `1`, and so on.

## Accessing Devices by Position

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]

first_device = devices[0]
second_device = devices[1]
last_device = devices[-1]

print(first_device)
print(second_device)
print(last_device)
```

Output:

```text
edge-sw1
edge-sw2
core-rtr1
```

The index `-1` means "last item." This is useful when you do not know how long
the list is.

## Device Lists Are the First Step Toward Scale

The `labato_1010` capstone repo includes a file named `device_list`:

```text
198.18.1.11
198.18.1.12
```

Later, a backup script reads that file, turns each line into a device target,
connects to each device, and saves the running configuration.

You are not ready for the full backup script yet, but you are ready for the
core idea:

```python
devices = ["198.18.1.11", "198.18.1.12"]

print(devices[0])
print(devices[1])
```

That is the seed of multi-device automation.

## Changing a List

Networks change. Device lists change too.

```python
devices = ["edge-sw1", "edge-sw2"]
print(devices)

devices.append("core-rtr1")
print(devices)
```

Output:

```text
['edge-sw1', 'edge-sw2']
['edge-sw1', 'edge-sw2', 'core-rtr1']
```

The `.append()` method adds one item to the end.

## Removing a Device from a Work Queue

Sometimes a list is a queue: a set of things waiting to be handled.

```python
commands = ["show version", "show ip interface brief", "show vlan brief"]

next_command = commands.pop(0)

print(f"Run now: {next_command}")
print(f"Still waiting: {commands}")
```

Output:

```text
Run now: show version
Still waiting: ['show ip interface brief', 'show vlan brief']
```

`.pop(0)` removes and returns the first item. This is useful when a script
handles one task and leaves the rest for later.

## A List of Show Commands

The PacketSwitch Netmiko guide shows the natural next step: put multiple show
commands in a list, then send each one. You will learn loops in Chapter 4, but
you can already understand the data structure:

```python
show_commands = [
    "show ip route",
    "show interface description",
    "show clock",
]
```

This list is better than three unrelated variables:

```python
command1 = "show ip route"
command2 = "show interface description"
command3 = "show clock"
```

The list says, "these values belong together."

## A Labato-Style Command List

The `labato_1010` repo also includes a command file with operational checks:

```text
show runn | in logging
show runn | in ntp
show runn | in snmp
show ip access-lists TEST_ACL
show ip ospf neighbor
show ip ospf interface brief
show ip interface brief
```

As a Python list, that becomes:

```python
show_commands = [
    "show runn | in logging",
    "show runn | in ntp",
    "show runn | in snmp",
    "show ip access-lists TEST_ACL",
    "show ip ospf neighbor",
    "show ip ospf interface brief",
    "show ip interface brief",
]
```

Notice the pattern:

```text
manual checklist -> Python list -> repeatable automation plan
```

That is one of the most important transitions in the whole book.

## Lists Can Hold Different Kinds of Values

Python allows this:

```python
mixed = ["edge-sw1", 22, None]
```

But in network automation, prefer lists where each item represents the same
kind of thing:

Good:

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]
```

Good:

```python
vlans = [10, 20, 30]
```

Good:

```python
commands = ["show version", "show ip interface brief"]
```

Harder to understand:

```python
items = ["edge-sw1", 20, "show version", None]
```

Keep lists boring. Boring data is easier to automate.

## Sorting and Reviewing Lists

Before a script touches devices, inspect the list:

```python
devices = ["edge-sw2", "core-rtr1", "edge-sw1"]

print(sorted(devices))
print(devices)
```

`sorted(devices)` shows a sorted copy. It does not change the original list.
This is useful when you want clean output without changing the actual work
order.

## Lab: Create a Device List

Create `chapter_03_devices.py`:

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]

print("All devices:")
print(devices)

print("First device:")
print(devices[0])

print("Last device:")
print(devices[-1])
```

Run it. Then add:

```python
devices.append("wan-rtr1")
print(devices)
```

Run it again.

## Lab: Create a Command Queue

Create `chapter_03_commands.py`:

```python
commands = [
    "show version",
    "show ip interface brief",
    "show vlan brief",
]

next_command = commands.pop(0)

print(f"Next command: {next_command}")
print(f"Remaining commands: {commands}")
```

This prepares you for Chapter 4, where Python will loop through the remaining
commands automatically.

## Capstone Preview: From Lists to Backups

The final capstone will include a backup workflow inspired by
`labato_1010/8-netmiko_backup.py`.

At a high level, that script does this:

```text
read device list -> connect to each device -> run show run -> save output to file
```

Chapter 3 teaches the first piece:

```text
read or create a list of devices
```

Chapter 4 will teach:

```text
loop over each device
```

Chapter 10 will teach:

```text
read device lists from files and write backup files
```

Chapter 12 will bring in:

```text
Netmiko connection handling
```

By the time you reach the capstone, the script will not feel like magic. It will
feel like familiar pieces assembled in a useful order.

## Common Beginner Mistakes

**Mistake: Forgetting that indexes start at zero.**

The first item is `devices[0]`, not `devices[1]`.

**Mistake: Using a list when names matter.**

Lists are great for ordered collections. If each item needs labels such as
`hostname`, `mgmt_ip`, and `platform`, you will soon want dictionaries.

**Mistake: Changing a production list without printing it first.**

Before a loop runs against devices, print the device list. Make sure it contains
exactly what you think it contains.

## Chapter 3 Review

You learned:

- Lists store multiple related values.
- Device names, commands, VLANs, and interfaces are natural list data.
- Index `0` means the first item.
- Index `-1` means the last item.
- `.append()` adds an item.
- `.pop()` removes and returns an item.
- A command checklist can become a Python list.

## Practice Questions

1. Why are lists useful for network automation?
2. What is the output of `devices[-1]`?
3. What does `.append()` do?
4. What does `.pop(0)` do?
5. Why is a list of commands better than unrelated variables named `command1`, `command2`, and `command3`?

## Practice Exercise

Create a script with:

- a list of three device names
- a list of three show commands
- a print statement showing the first device
- a print statement showing the last command
- an `.append()` call that adds one more device

Do not use loops yet. That comes next.

---

# Chapter 4: Working Through Networks with Loops

## What This Chapter Teaches

Chapter 4 is where Python starts to feel useful. A list lets you store many
things, but a loop lets you do something with each thing.

The classic beginner pattern is a list of names:

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
```

The network version is a list of devices:

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]

for device in devices:
    print(f"Collect show version from {device}")
```

The idea is identical:

```text
for each item in this list, do this action
```

That sentence is the heart of network automation.

## Why Loops Matter to Network Engineers

Most CLI work is repeated work:

- Check every access switch.
- Verify every uplink.
- Back up every router.
- Apply the same logging server to every device.
- Run the same show command before and after a change.

When you do this manually, your brain becomes the loop. You connect to device 1,
run the command, copy output, disconnect, connect to device 2, and repeat.

Python lets the loop live in the program instead:

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]
command = "show ip interface brief"

for device in devices:
    print(f"Would run '{command}' on {device}")
```

Output:

```text
Would run 'show ip interface brief' on edge-sw1
Would run 'show ip interface brief' on edge-sw2
Would run 'show ip interface brief' on core-rtr1
```

This is still a dry run, but it is now a multi-device dry run.

## Understanding the `for` Loop

Look carefully at this line:

```python
for device in devices:
```

Read it as:

```text
For each device in the devices list...
```

The variable `device` is temporary. On the first loop, it means `"edge-sw1"`.
On the second loop, it means `"edge-sw2"`. On the third loop, it means
`"core-rtr1"`.

The indented lines underneath the `for` statement run once for each item:

```python
for device in devices:
    print(device)
    print("Check complete")
```

Indentation matters. In Python, indentation is not decoration. It tells Python
which lines belong to the loop.

## Classic Example, Network Translation

Classic beginner example:

```python
pizzas = ["pepperoni", "margherita", "veggie"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")
```

Network equivalent:

```python
show_commands = ["show version", "show ip interface brief", "show vlan brief"]

for command in show_commands:
    print(f"Planned command: {command}")

print("Command plan complete.")
```

The final `print()` is not indented, so it runs once after the loop is finished.

## Building Interface Names with `range()`

The classic Python example uses `range()` to generate numbers:

```python
for value in range(1, 6):
    print(value)
```

Output:

```text
1
2
3
4
5
```

Notice that `range(1, 6)` stops before `6`.

Network engineers can use the same pattern to build interface names:

```python
for port in range(1, 5):
    interface = f"GigabitEthernet1/0/{port}"
    print(interface)
```

Output:

```text
GigabitEthernet1/0/1
GigabitEthernet1/0/2
GigabitEthernet1/0/3
GigabitEthernet1/0/4
```

Now the loop is not just printing numbers. It is generating network objects.

## List Comprehensions, Gently

A list comprehension builds a new list in one line.

Classic example:

```python
squares = [value ** 2 for value in range(1, 6)]
print(squares)
```

Network equivalent:

```python
interfaces = [f"GigabitEthernet1/0/{port}" for port in range(1, 5)]
print(interfaces)
```

Output:

```text
['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'GigabitEthernet1/0/3', 'GigabitEthernet1/0/4']
```

Do not overuse comprehensions while learning. A normal loop is easier to read.
Use comprehensions when the pattern is simple and obvious.

## Netmiko Preview: Looping Over Commands

Later, you will use this same pattern with Netmiko:

```python
show_commands = ["show ip route", "show interface description", "show clock"]

for command in show_commands:
    output = connection.send_command(command)
    print(output)
```

For now, replace the real connection with a dry run:

```python
show_commands = ["show ip route", "show interface description", "show clock"]

for command in show_commands:
    print(f"Would send: {command}")
```

The important thing is the shape:

```text
list of commands -> loop -> one command handled at a time
```

## Lab: Multi-Device Dry Run

Create `chapter_04_device_loop.py`:

```python
devices = ["edge-sw1", "edge-sw2", "core-rtr1"]
command = "show ip interface brief"

for device in devices:
    print(f"Connecting to {device}")
    print(f"Would run: {command}")
    print("Disconnecting")
    print()
```

This is not connecting yet. It is rehearsing the workflow.

## Chapter 4 Review

You learned:

- A `for` loop repeats work for every item in a list.
- Indentation controls what belongs inside the loop.
- `range()` generates numbers.
- Loops can build interface names and command plans.
- A multi-device dry run is the safest first step toward real automation.

---

# Chapter 5: If Statements for Network Decisions

## What This Chapter Teaches

Loops repeat work. `if` statements make decisions.

Classic beginner example:

```python
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
```

Python checks each value and chooses what to do.

The network version checks device or interface facts:

```python
interfaces = ["up", "down", "administratively down"]

for status in interfaces:
    if status == "up":
        print("Interface is forwarding traffic.")
    else:
        print("Interface needs review.")
```

Automation is not only about doing things faster. It is about making the same
decision consistently.

## Conditions Are Questions

An `if` statement asks a question:

```python
status = "up"

if status == "up":
    print("Interface is healthy.")
```

The question is:

```text
Is status equal to "up"?
```

The double equals sign `==` compares two values. A single equals sign `=`
assigns a value.

```python
status = "up"      # assignment
status == "up"     # comparison
```

This distinction matters. Many beginner bugs come from mixing them up.

## Classic Example, Network Translation

Classic example:

```python
age = 17

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are too young to vote.")
```

Network equivalent:

```python
free_ports = 3

if free_ports >= 1:
    print("There is at least one available access port.")
else:
    print("No available access ports. Do not schedule the install yet.")
```

The Python idea is the same:

```text
look at a value -> compare it -> choose a branch
```

## Interface Status Decisions

A realistic network check often starts with a fact:

```python
interface = "GigabitEthernet1/0/10"
status = "notconnect"
```

Now decide what to do:

```python
if status == "connected":
    print(f"{interface} is active.")
elif status == "notconnect":
    print(f"{interface} may be available, but verify before reuse.")
else:
    print(f"{interface} needs manual review.")
```

`elif` means "else if." It lets you check another condition.

Use `else` as the catch-all branch. In networking, the catch-all branch is often
"do not change anything until a human reviews it."

## Checking Membership

Classic Python:

```python
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
```

Network equivalent:

```python
approved_vlans = [10, 20, 30]
requested_vlan = 20

if requested_vlan in approved_vlans:
    print(f"VLAN {requested_vlan} is approved.")
else:
    print(f"VLAN {requested_vlan} is not approved.")
```

This pattern is a guardrail. Before a script builds or sends configuration, it
can check whether the request is allowed.

## Change Window Guardrails

Network automation must respect operations.

```python
change_window_open = False
approval_received = True

if change_window_open and approval_received:
    print("Proceed with configuration.")
else:
    print("Stop. Do not configure.")
```

The word `and` means both conditions must be true.

This is the beginning of safe automation. The script is not just asking "can I
do this?" It is asking "should I do this now?"

## Netmiko Preview: Read Before Write

Before sending config with Netmiko, a script can make decisions:

```python
intended_logging_server = "10.1.1.1"
current_config = "logging host 10.1.1.1"

if intended_logging_server in current_config:
    print("Logging server already configured. No change needed.")
else:
    print(f"Would configure logging host {intended_logging_server}")
```

Later, the `current_config` value will come from:

```python
connection.send_command("show running-config | include logging")
```

For now, the string is fake so the decision is easy to see.

## Lab: Build a Safe VLAN Decision

Create `chapter_05_vlan_guard.py`:

```python
approved_vlans = [10, 20, 30]
requested_vlan = 40
change_window_open = True

if requested_vlan in approved_vlans and change_window_open:
    print(f"Approved: configure VLAN {requested_vlan}")
elif requested_vlan not in approved_vlans:
    print(f"Denied: VLAN {requested_vlan} is not approved.")
else:
    print("Denied: change window is closed.")
```

Change `requested_vlan` to `20` and run it again.

## Chapter 5 Review

You learned:

- `if` statements let Python make decisions.
- `==` compares values.
- `elif` checks another condition.
- `else` catches everything not matched earlier.
- `in` checks whether a value appears in a list.
- Guardrails are decision logic that prevent unsafe automation.

---

# Chapter 6: Dictionaries for Device Inventory

## What This Chapter Teaches

Lists are great when order matters. Dictionaries are better when meaning matters.

Classic beginner example:

```python
alien = {"color": "green", "points": 5}

print(alien["color"])
print(alien["points"])
```

A dictionary stores key-value pairs. The key is the label. The value is the
thing stored under that label.

Network equivalent:

```python
device = {
    "hostname": "edge-sw1",
    "mgmt_ip": "192.0.2.10",
    "platform": "cisco_ios",
}

print(device["hostname"])
print(device["mgmt_ip"])
```

This is the first structure that really looks like device inventory.

## Why Dictionaries Matter in Network Automation

A network device is not just one value. It has many facts:

```text
hostname: edge-sw1
management IP: 192.0.2.10
platform: cisco_ios
site: dal
role: access
```

A dictionary keeps those facts together:

```python
device = {
    "hostname": "edge-sw1",
    "mgmt_ip": "192.0.2.10",
    "platform": "cisco_ios",
    "site": "dal",
    "role": "access",
}
```

Now the code can ask for the exact fact it needs:

```python
print(device["platform"])
```

## Classic Example, Network Translation

Classic dictionary update:

```python
alien = {"color": "green"}
alien["points"] = 5

print(alien)
```

Network equivalent:

```python
device = {"hostname": "edge-sw1"}
device["mgmt_ip"] = "192.0.2.10"
device["platform"] = "cisco_ios"

print(device)
```

You can start with a small dictionary and add facts as you learn them.

## A Netmiko Connection Dictionary

Netmiko commonly uses a dictionary to describe a device:

```python
device = {
    "device_type": "cisco_ios",
    "host": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}
```

Later, this dictionary is passed to Netmiko:

```python
connection = ConnectHandler(**device)
```

The `**device` syntax unpacks the dictionary. It is like telling Python:

```text
Take each key-value pair in this dictionary and pass it as a named argument.
```

You do not need to master `**` yet, but you should understand why the dictionary
is useful: it keeps all connection facts in one place.

## Nesting Dictionaries

A real inventory has more than one device:

```python
inventory = {
    "edge-sw1": {
        "mgmt_ip": "192.0.2.10",
        "platform": "cisco_ios",
        "role": "access",
    },
    "core-rtr1": {
        "mgmt_ip": "192.0.2.20",
        "platform": "cisco_ios",
        "role": "core",
    },
}
```

Access one value:

```python
print(inventory["edge-sw1"]["mgmt_ip"])
```

Output:

```text
192.0.2.10
```

Read the brackets from left to right:

```text
in inventory -> find edge-sw1 -> then find mgmt_ip
```

## Looping Through a Dictionary

```python
for hostname, facts in inventory.items():
    print(f"{hostname} is a {facts['role']} device.")
```

Output:

```text
edge-sw1 is a access device.
core-rtr1 is a core device.
```

That output has awkward grammar, so improve the sentence:

```python
for hostname, facts in inventory.items():
    print(f"{hostname}: role={facts['role']}, ip={facts['mgmt_ip']}")
```

Readable output matters. A report that humans cannot scan is only half useful.

## Lab: Build a Small Inventory

Create `chapter_06_inventory.py`:

```python
inventory = {
    "edge-sw1": {
        "mgmt_ip": "192.0.2.10",
        "platform": "cisco_ios",
        "role": "access",
    },
    "edge-sw2": {
        "mgmt_ip": "192.0.2.11",
        "platform": "cisco_ios",
        "role": "access",
    },
}

for hostname, facts in inventory.items():
    print(f"{hostname} ({facts['platform']}) -> {facts['mgmt_ip']}")
```

Then add a third device.

## Chapter 6 Review

You learned:

- Dictionaries store key-value pairs.
- Device facts fit naturally in dictionaries.
- Netmiko connection details are commonly represented as dictionaries.
- Nested dictionaries can model a small inventory.
- `.items()` lets you loop through keys and values together.

---

# Chapter 7: Operator Input and While Loops

## What This Chapter Teaches

So far, your scripts have used values written directly in the code. Chapter 7
introduces interaction and repetition that continues until a condition changes.

Classic input example:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

Network equivalent:

```python
hostname = input("Device hostname: ")
print(f"Preparing dry run for {hostname}")
```

Use input carefully. In production automation, many values should come from
inventory or approved change data, not from typing at a prompt. But while
learning, `input()` helps you understand how scripts receive information.

## Converting Input

`input()` always returns a string.

```python
vlan = input("VLAN ID: ")
print(type(vlan))
```

Even if you type `20`, Python receives `"20"` as text. Convert it when you need
a number:

```python
vlan = int(input("VLAN ID: "))
print(vlan + 1)
```

For safe automation, validate before converting:

```python
vlan_text = input("VLAN ID: ")

if vlan_text.isdigit():
    vlan = int(vlan_text)
    print(f"VLAN {vlan} accepted.")
else:
    print("VLAN must be a number.")
```

## Classic While Loop

Classic example:

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

A `while` loop keeps running as long as its condition is true.

Network equivalent:

```python
attempt = 1

while attempt <= 3:
    print(f"Connection attempt {attempt}")
    attempt += 1
```

This pattern will later help with retries.

## Avoid Infinite Loops

An infinite loop never stops:

```python
attempt = 1

while attempt <= 3:
    print(f"Connection attempt {attempt}")
```

`attempt` never changes, so the condition never becomes false.

Always ask:

```text
What changes inside the loop so this eventually stops?
```

## Menu-Style Dry Run

```python
prompt = "\nChoose an action:"
prompt += "\n1. Show version"
prompt += "\n2. Show interface brief"
prompt += "\nq. Quit"
prompt += "\n> "

choice = ""

while choice != "q":
    choice = input(prompt)

    if choice == "1":
        print("Would run: show version")
    elif choice == "2":
        print("Would run: show ip interface brief")
    elif choice == "q":
        print("Goodbye.")
    else:
        print("Unknown option.")
```

This is still a dry run, but it teaches a real operational idea: let the
operator choose from known safe actions instead of typing arbitrary commands.

## Lab: Validate a VLAN

Create `chapter_07_vlan_input.py`:

```python
vlan_text = input("Enter VLAN ID: ")

if vlan_text.isdigit():
    vlan = int(vlan_text)

    if 1 <= vlan <= 4094:
        print(f"VLAN {vlan} is valid.")
    else:
        print("VLAN must be between 1 and 4094.")
else:
    print("VLAN must be numeric.")
```

This is more important than it looks. Automation should reject bad input before
it becomes bad configuration.

## Chapter 7 Review

You learned:

- `input()` receives text from the operator.
- Convert input when you need numbers.
- Validate input before using it.
- A `while` loop repeats while a condition is true.
- Every `while` loop needs a path to stop.

---

# Chapter 8: Functions for Reusable Automation

## What This Chapter Teaches

Functions let you name a block of code and reuse it.

Classic example:

```python
def greet_user(username):
    print(f"Hello, {username}!")

greet_user("jesse")
```

Network equivalent:

```python
def describe_device(hostname):
    print(f"Preparing automation for {hostname}")

describe_device("edge-sw1")
```

Functions are where scripts start becoming tools.

## Why Functions Matter

Without a function, repeated logic spreads everywhere:

```python
interface = "GigabitEthernet1/0/1"
print(f"show running-config interface {interface}")

interface = "GigabitEthernet1/0/2"
print(f"show running-config interface {interface}")
```

With a function:

```python
def build_interface_command(interface):
    return f"show running-config interface {interface}"

print(build_interface_command("GigabitEthernet1/0/1"))
print(build_interface_command("GigabitEthernet1/0/2"))
```

The idea has a name now: `build_interface_command`.

## Parameters and Arguments

In this function:

```python
def build_interface_command(interface):
    return f"show running-config interface {interface}"
```

`interface` is a parameter. It is a placeholder.

In this call:

```python
build_interface_command("Vlan20")
```

`"Vlan20"` is an argument. It is the real value passed into the function.

## Returning Data

Printing is useful while learning, but returning values makes functions more
flexible.

```python
def build_vlan_commands(vlan_id, name):
    commands = [f"vlan {vlan_id}", f"name {name}"]
    return commands

planned_commands = build_vlan_commands(20, "USERS")
print(planned_commands)
```

Output:

```text
['vlan 20', 'name USERS']
```

Later, that returned list can be passed to Netmiko's `send_config_set()`.

## Netmiko Preview: Function Around a Show Command

Do not run this yet unless you are in a lab, but read the shape:

```python
def collect_show_command(connection, command):
    output = connection.send_command(command)
    return output
```

This function does one thing: send one command through an existing connection.

Good functions are small. A function named `collect_show_command` should not
also parse CSV, send email, and update a ticket. Keep the name honest.

## Lab: Build Command Functions

Create `chapter_08_functions.py`:

```python
def build_show_command(interface):
    return f"show running-config interface {interface}"


def build_vlan_commands(vlan_id, vlan_name):
    return [f"vlan {vlan_id}", f"name {vlan_name}"]


print(build_show_command("GigabitEthernet1/0/1"))
print(build_vlan_commands(20, "USERS"))
```

Then call each function with a different value.

## Chapter 8 Review

You learned:

- Functions package reusable behavior.
- `def` starts a function definition.
- Parameters are placeholders.
- Arguments are real values.
- `return` sends a value back to the caller.
- Small command-building functions prepare you for safer Netmiko scripts.

---

# Chapter 9: Classes for Devices and Sessions

## What This Chapter Teaches

Classes let you model things. In general Python teaching, a common first class
is a dog:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(f"{self.name} is now sitting.")

my_dog = Dog("willie")
my_dog.sit()
```

The network equivalent is a device:

```python
class NetworkDevice:
    def __init__(self, hostname, mgmt_ip):
        self.hostname = hostname
        self.mgmt_ip = mgmt_ip

    def describe(self):
        print(f"{self.hostname} is managed at {self.mgmt_ip}.")

device = NetworkDevice("edge-sw1", "192.0.2.10")
device.describe()
```

Do not worry if classes feel bigger than functions. You can write useful
automation without creating many classes. But you need to understand them
because libraries such as Netmiko use objects.

## What `__init__` Does

`__init__` runs when a new object is created:

```python
device = NetworkDevice("edge-sw1", "192.0.2.10")
```

The values are stored on `self`:

```python
self.hostname = hostname
self.mgmt_ip = mgmt_ip
```

Read `self.hostname` as:

```text
this device object's hostname
```

## Methods Are Functions Attached to Objects

This is a method:

```python
def describe(self):
    print(f"{self.hostname} is managed at {self.mgmt_ip}.")
```

You call it from the object:

```python
device.describe()
```

In Netmiko, `connection.send_command()` and `connection.disconnect()` are
methods. The connection object knows how to perform those actions.

## Modeling a Dry-Run Session

```python
class DryRunSession:
    def __init__(self, hostname):
        self.hostname = hostname
        self.commands = []

    def send_config_set(self, commands):
        self.commands.extend(commands)
        print(f"{self.hostname}: queued {len(commands)} command(s)")


session = DryRunSession("edge-sw1")
session.send_config_set(["vlan 20", "name USERS"])
print(session.commands)
```

This class does not configure anything. It imitates the shape of a Netmiko
session so you can understand object behavior safely.

## Chapter 9 Review

You learned:

- A class is a blueprint.
- An object is one instance of that blueprint.
- `__init__` stores initial data.
- Methods are functions attached to objects.
- Netmiko connection objects use methods such as `send_command()` and `disconnect()`.

---

# Chapter 10: Files, Exceptions, and Network Data

## What This Chapter Teaches

Network automation becomes truly useful when scripts can read and write files.

Classic beginner file example:

```python
from pathlib import Path

path = Path("message.txt")
contents = path.read_text()
print(contents)
```

Network equivalent:

```python
from pathlib import Path

path = Path("device_list")
devices = path.read_text().splitlines()
print(devices)
```

Files are how scripts remember things beyond one run.

## Reading a Device List

Suppose `device_list` contains:

```text
198.18.1.11
198.18.1.12
```

Read it:

```python
from pathlib import Path

device_file = Path("device_list")
devices = device_file.read_text().splitlines()

print(devices)
```

Output:

```text
['198.18.1.11', '198.18.1.12']
```

The file is plain text. Python turns it into a list.

## Writing a Backup File

```python
from pathlib import Path

hostname = "edge-sw1"
running_config = "hostname edge-sw1\nlogging host 10.1.1.1\n"

backup_dir = Path("backup")
backup_dir.mkdir(exist_ok=True)

backup_file = backup_dir / f"{hostname}.cfg"
backup_file.write_text(running_config)

print(f"Wrote {backup_file}")
```

This is the safe version of a backup script. The config text is fake, but the
file-writing pattern is real.

## Exceptions: When Things Go Wrong

Classic example:

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

Network equivalent:

```python
from pathlib import Path

path = Path("missing_device_list")

try:
    devices = path.read_text().splitlines()
except FileNotFoundError:
    print(f"Could not find {path}. Check the filename.")
```

Network automation must expect failure. Files may be missing. Passwords may be
wrong. DNS may fail. Devices may be unreachable. Prompts may not match. A good
script handles expected failures clearly.

## JSON as Network Data

```python
import json

raw = '{"hostname": "edge-sw1", "mgmt_ip": "192.0.2.10"}'
device = json.loads(raw)

print(device["hostname"])
```

JSON turns text into Python dictionaries and lists. APIs often return JSON, so
this skill prepares you for controller and firewall management APIs.

## Capstone Preview: Backing Up Configurations

The later backup project follows this pattern:

```text
read device_list -> connect to each device -> run show run -> write hostname.cfg
```

Chapter 10 teaches two pieces:

```text
read device_list
write hostname.cfg
```

The Netmiko connection comes later.

## Chapter 10 Review

You learned:

- Files let scripts read inventory and write reports.
- `.splitlines()` turns file lines into a list.
- `Path` helps work with files and folders.
- Exceptions let scripts handle expected failures.
- JSON prepares you for API data.

---

# Chapter 11: Testing Network Automation

## What This Chapter Teaches

Tests prove that code behaves the way you expect.

Classic beginner function:

```python
def get_formatted_name(first, last):
    return f"{first} {last}".title()
```

Classic test idea:

```python
assert get_formatted_name("ada", "lovelace") == "Ada Lovelace"
```

Network equivalent:

```python
def build_vlan_commands(vlan_id, name):
    return [f"vlan {vlan_id}", f"name {name}"]

assert build_vlan_commands(20, "USERS") == ["vlan 20", "name USERS"]
```

Testing matters more in network automation than in many beginner projects
because mistakes can affect real infrastructure.

## Test the Logic Before the Network

Do not start by testing SSH to a real device. Start by testing pure Python
logic:

- command builders
- input validators
- parsers
- inventory checks
- report formatters

These tests do not need a network.

## Testing a VLAN Validator

```python
def valid_vlan(vlan_id):
    return 1 <= vlan_id <= 4094


assert valid_vlan(1)
assert valid_vlan(4094)
assert not valid_vlan(0)
assert not valid_vlan(5000)
```

If the script finishes silently, the assertions passed.

## Testing Required Device Keys

```python
def has_required_keys(device):
    required = {"hostname", "mgmt_ip", "platform"}
    return required.issubset(device)


good_device = {
    "hostname": "edge-sw1",
    "mgmt_ip": "192.0.2.10",
    "platform": "cisco_ios",
}

bad_device = {
    "hostname": "edge-sw2",
}

assert has_required_keys(good_device)
assert not has_required_keys(bad_device)
```

This protects later Netmiko code. If a device dictionary is missing required
fields, fail early before trying to connect.

## Testing a Parser

```python
def interface_is_up(status, protocol):
    return status == "up" and protocol == "up"


assert interface_is_up("up", "up")
assert not interface_is_up("administratively down", "down")
assert not interface_is_up("up", "down")
```

Small tests like this make bigger scripts safer.

## Lab: Create a Test File

Create `chapter_11_tests.py`:

```python
def build_show_command(interface):
    return f"show running-config interface {interface}"


def valid_vlan(vlan_id):
    return 1 <= vlan_id <= 4094


assert build_show_command("Vlan20") == "show running-config interface Vlan20"
assert valid_vlan(20)
assert not valid_vlan(5000)

print("All tests passed.")
```

Run it:

```text
python chapter_11_tests.py
```

Then intentionally break one expected value and run it again. Read the failure.
Learning to read test failures is part of learning to trust automation.

## Chapter 11 Review

You learned:

- Tests check expected behavior.
- `assert` is a simple way to start testing.
- Test pure Python logic before testing real network access.
- Validators, command builders, and parsers are excellent first test targets.
- Good tests create confidence before change windows.

---

# References for Chapters 1-11

- PacketSwitch, [Python For Network Engineers - Introduction](https://www.packetswitch.co.uk/python-for-network-engineers-introduction/)
- PacketSwitch, [Python - Netmiko](https://www.packetswitch.co.uk/python-netmiko/)
- PacketSwitch, [Python - Functions](https://www.packetswitch.co.uk/python-functions/)
- twin-bridges, [python_course_mar26](https://github.com/twin-bridges/python_course_mar26)
- twin-bridges, [netmiko_course](https://github.com/twin-bridges/netmiko_course)
- jagadnag, [labato_1010](https://github.com/jagadnag/labato_1010)
