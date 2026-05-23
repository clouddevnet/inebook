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

# Introduction: The Evolution You Cannot Ignore

> An engineer who only performs repeatable execution will eventually compete
> with tools that execute repeatable work. The engineer who learns to design,
> verify, and orchestrate those tools becomes far more valuable.

This book begins with a simple argument: network engineering is changing, and
the change is not optional.

That does not mean the CLI is useless. It does not mean protocol knowledge is
old-fashioned. It does not mean a network engineer should stop understanding
spanning tree, OSPF neighbors, BGP policy, VLAN design, ACL order, interface
counters, or the difference between configuration mode and operational mode.

It means the center of gravity is moving.

For years, the most visible part of network engineering was execution: open an
SSH session, type the command, read the output, paste the change, verify the
result, repeat on the next device. That work still matters, but it is no longer
where the highest leverage lives. The highest leverage now lives in designing
repeatable workflows, encoding operational knowledge into scripts, verifying
changes before they reach production, collecting evidence after they run, and
building systems that help the whole team work with more consistency.

This is why Python matters.

Python lets you take the process already in your head and write it down in a
form the computer can repeat. Python lets you turn a checklist into a dry-run
script, a dry-run script into a data collection tool, a data collection tool
into a backup workflow, and a backup workflow into a production automation
pattern with logging, error handling, and reports.

That is the journey this book takes.

## The Conversation Happening Right Now

Somewhere in your organization, a conversation is already underway.

A network engineer with years of experience is being asked whether automation
could handle the VLAN deployment process. Or whether switch backups could run
every night. Or whether a script could collect interface status from every
access switch before a maintenance window. Or whether the team can stop relying
on one person's terminal history to prove what changed.

The engineer pauses.

"I know how to SSH to every switch," they say.

And that is exactly the problem.

Not the knowledge. Not the discipline. Not the experience. The problem is that
the execution itself - the SSH sessions, the repeated commands, the manual
copying, the device-by-device verification - is exactly the kind of work that
software can perform more consistently.

If the task is:

- repeatable
- predictable
- based on known inputs
- expected to produce known outputs
- dangerous mainly because humans get tired or distracted

then it is a strong candidate for automation.

The engineers who understand this are already building the tools. The engineers
who do not are already being asked why the team is still doing everything by
hand.

This book is written for engineers who want to be on the right side of that
conversation.

## Why This Book Is Different

Many Python books teach programming with examples such as cats, dogs, favorite
foods, bicycles, cars, weather apps, or generic shopping carts. Those examples
can teach syntax, but they do not always help a network engineer connect the
idea to daily work.

This book takes a different path.

You will still learn the same fundamentals every Python beginner needs:
variables, strings, lists, dictionaries, loops, conditionals, functions,
classes, files, exceptions, tests, APIs, and project structure. But you will
learn them through the world you already know.

Instead of a list of pets, you will build a list of switches.

Instead of a dictionary that describes a person, you will build a dictionary
that describes a router, including its hostname, management IP, platform, site,
and role.

Instead of looping through pizza toppings, you will loop through show commands.

Instead of writing a toy weather app, you will write scripts that prepare dry
runs, validate inventory, collect device output, back up configurations, parse
results, and generate reports.

The goal is not to make the examples sound more serious. The goal is to make
the learning stick. When you learn a Python concept through a networking task,
you do not have to translate it later. You already know why the concept exists.

## Practical From Chapter 1

This book is practical from the first chapter, but practical does not mean
reckless.

In Chapter 1, you will not immediately push configuration to a production
router. That would be a poor way to learn. Instead, you will begin with safe,
visible scripts that print what they plan to do. You will learn to trust the
feedback loop:

```text
write a small script -> run it -> inspect output -> change one thing -> run it again
```

That habit matters more than the first script itself.

A beginner who can run small scripts, read output carefully, and make one safe
change at a time is already building the mindset required for production
automation. Production automation is not magic. It is the same habit with
better inputs, better guardrails, better logs, better tests, and better review.

This book builds that habit step by step.

At first, the scripts only print planned actions. Then they organize device
facts. Then they loop through commands. Then they read files. Then they handle
errors. Then they connect to lab devices with Netmiko. Then they scale across
multiple devices. Then they produce evidence: backups, reports, summaries,
parsed data, and audit-friendly output.

Every chapter asks the same question:

> How does this Python idea help a network engineer do real work more safely?

## The Journey This Book Takes You On

The journey is deliberate. Each stage gives you enough skill to understand the
next one.

### Stage 1: Python Fundamentals Through a Networking Lens

You begin with the basics:

- printing output
- assigning variables
- working with strings
- storing devices in lists
- modeling inventory with dictionaries
- making decisions with `if` statements
- repeating work with loops
- accepting user input
- writing functions
- organizing code into modules
- building classes when the problem needs structure

These are the same ideas every Python programmer learns. The difference is that
your examples come from network operations. A variable might hold a hostname. A
string might hold a show command. A list might hold access switches. A
dictionary might hold a Netmiko connection profile.

You are not learning Python in the abstract. You are learning Python as the
language of repeatable network work.

### Stage 2: Files, Errors, and Production Habits

Real scripts need to work with real data.

That means reading inventory from files, writing output to disk, saving device
backups, handling missing files, catching connection errors, and producing
logs that tell the next engineer what happened.

This is where many beginner scripts fail. They work only when everything goes
perfectly. Production code cannot assume perfection. Devices are offline.
Credentials expire. Command output changes. Files are missing. A switch prompt
looks different from what you expected.

This stage teaches you to expect those problems and write code that responds
calmly.

### Stage 3: Netmiko and Real Device Automation

Once the Python foundation is in place, you begin connecting to devices with
Netmiko.

Netmiko is useful because it understands the SSH behavior of many network
platforms. It knows how to connect, send commands, enter configuration mode,
return output, and disconnect cleanly.

But Netmiko should not feel like a mysterious leap. By the time you reach it,
you will already understand the pieces:

- a connection profile is a dictionary
- a command list is a list of strings
- a multi-device run is a loop
- a failed login is an exception
- a reusable workflow belongs in a function
- a backup directory is file handling
- a report is structured output

Netmiko becomes the tool that connects the Python concepts you have already
learned to the devices you already understand.

### Stage 4: Multi-Device Workflows

The power of automation appears when one correct workflow can run across many
devices.

This stage teaches you to think beyond a single SSH session. You will build
inventory-driven scripts, loop over devices, collect command output, separate
successful results from failures, and make your output easy to review.

This is where the network engineer starts to feel the shift. A task that once
required many terminal tabs becomes a controlled script. The script does not
forget a device. It does not get bored. It does not paste the wrong command
because someone interrupted it mid-change.

You still provide the judgment. Python provides the repeatability.

### Stage 5: Capstone Projects That Resemble Real Work

The book does not end with isolated syntax exercises. It builds toward
projects that look like work a network automation engineer might actually do:

- collect show commands from multiple devices
- back up running configurations
- create timestamped output directories
- validate inventory before connecting
- generate CSV or Markdown reports
- prepare safe configuration changes
- separate dry-run behavior from write behavior
- parse output into useful facts
- build reusable helper functions
- organize scripts so they can grow without becoming messy

These projects are not decorative. They are the bridge between learning Python
and using Python responsibly in a network environment.

### Stage 6: AI-Assisted Automation and Orchestration

The final direction of the journey is orchestration.

AI tools can now generate code, explain errors, summarize logs, analyze command
output, and help design workflows. That does not remove the need to understand
Python. It increases the need.

An engineer who understands Python can evaluate AI-generated code. They can
see when a script is missing exception handling. They can notice when a tool is
about to push configuration without a dry-run step. They can test small pieces
before trusting the whole workflow.

AI can help you build faster, but your judgment keeps the work safe.

The Python you learn in this book becomes the lens through which you review,
shape, and orchestrate AI-assisted network automation.

## The Three Waves of Network Engineering

Network engineering has already moved through major shifts. The next one is
underway.

### Wave 1: The CLI Era

In the CLI era, configuration was manual. Verification was manual. The engineer
who knew the right command, typed quickly, and interpreted output correctly was
the most valuable person in the room.

That era created deep technical skill. It taught engineers to understand device
behavior, protocol state, command output, and operational risk. This knowledge
is still the foundation. Automation without network knowledge is dangerous.

### Wave 2: The Automation Era

In the automation era, network vendors exposed APIs, Python became common in
operations teams, and tools such as Netmiko, Nornir, Ansible, and Terraform
became normal parts of the conversation.

The advantage moved from the engineer who could manually perform a task to the
engineer who could define the task clearly enough for a tool to perform it
reliably.

A VLAN change that once required many SSH sessions could become an
inventory-driven workflow. A backup process that depended on memory could
become a scheduled script. A manual verification checklist could become a
repeatable report.

### Wave 3: The AI-Assisted Era

The AI-assisted era changes the equation again.

AI can draft scripts, explain tracebacks, summarize documentation, generate
test data, parse noisy text, and propose troubleshooting steps. That creates a
new question for network engineers:

Can you judge the output?

If AI writes a Netmiko script, can you tell whether the connection dictionary
is correct? Can you tell whether the script disconnects cleanly? Can you tell
whether it handles authentication failure? Can you tell whether it is about to
make a configuration change when you only wanted a dry run?

The engineer who can answer those questions is not replaced by AI. That
engineer becomes more capable because AI speeds up the routine parts while the
engineer keeps control of design, validation, risk, and intent.

## Execution Is Being Commoditized

Here is the uncomfortable truth: many execution skills are becoming easier to
automate.

Remembering syntax is useful, but AI can often recall syntax. Finding a
starting script is useful, but AI can draft one. Pattern-matching common show
output is useful, but AI can often summarize it quickly.

This does not make network engineers less valuable. It changes which parts of
the job are most valuable.

The durable skills are:

- understanding why the network behaves the way it does
- framing the real problem
- knowing what must be verified before and after a change
- recognizing risky automation patterns
- designing guardrails
- reviewing generated code
- deciding when not to automate
- communicating results to the business

Deep network knowledge becomes more valuable, not less. It becomes the thing
that lets you tell whether the automation is correct.

## The Orchestrator Principle

Consider two engineers facing the same Monday morning task list.

Engineer A is the executor:

- SSH to 40 switches and push VLAN configuration manually.
- Check syslog for critical events by hand.
- Pull running configurations into a folder manually.
- Generate inventory spreadsheets from show commands.
- Verify last night's changes device by device.

Engineer B is the orchestrator:

- Review the VLAN provisioning workflow's audit log.
- Improve the syslog triage rules based on false positives.
- Expand the backup workflow to include new branch sites.
- Design verification checks for an upcoming operating system upgrade.
- Investigate the devices that automation flagged for human review.
- Decide whether a vendor API is safe to integrate.

Engineer A is doing repeatable execution. Engineer B is designing, reviewing,
and improving the system that performs repeatable execution.

This book helps move you from A toward B.

You will not become an orchestrator by skipping the basics. You become one by
understanding the basics so well that you can combine them into reliable
workflows.

## Why Python, Git, CI/CD, and AI Tools Matter

The stack this book points toward is not random.

Python is the language of network automation, scripting, APIs, data handling,
and many AI frameworks. It is readable enough for beginners and powerful enough
for production workflows.

Git is how automation becomes professional. A script that can change a network
is not just a personal note. It is an operational asset. It needs history,
review, rollback, and collaboration.

CI/CD is how teams add checks before automation runs. Even a simple pipeline
can lint code, run tests, validate inventory, or prevent unsafe changes from
moving forward.

AI tools can accelerate the work, but they should not replace understanding.
They are assistants, not accountability. You still own the outcome.

## What This Book Requires of You

You do not need a computer science degree. You do not need prior programming
experience. You do not need to already be a network automation engineer.

You do need patience, curiosity, and the willingness to type through examples.

Run the code. Break it. Read the error message. Change one thing. Run it again.
Build something small in your own environment before moving on.

This book is practical because practice is the point.

## How to Read This Book

Read the book sequentially the first time. Each chapter assumes the previous
ones. After that, the chapters can become a reference.

Run every example as you read. Reading code without running it is like reading
a routing table without asking what traffic will actually do.

When something fails, do not skip the failure. Read the traceback. Look at the
line number. Ask what Python expected and what it received. Troubleshooting code
is not separate from learning Python. It is learning Python.

When you finish a chapter, build one small variation:

- change the hostname
- add another command
- add another device
- write output to a file
- handle one more error case
- turn repeated code into a function

Small variations create real understanding.

The agents and automation systems are being built. The question is whether you
will only use them, or whether you will understand them well enough to design,
review, and orchestrate them.

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

# Part II: Applying Python to Network Automation

The first eleven chapters taught the core Python vocabulary: variables, strings,
lists, dictionaries, loops, functions, classes, files, exceptions, and tests.

Now the work becomes concrete. You will use those same ideas to connect to
devices, run commands, push small configuration changes, process multiple
devices, handle failures, collect backups, and generate reports.

This part of the book is intentionally practical. You are not learning a new
language now; you are using the language you just learned against real network
workflows.

---

# Chapter 12: Netmiko: SSHing to Your Network at Python Speed

## What This Chapter Teaches

Netmiko is the bridge between basic Python and real network devices.

Until now, the book has used dry runs:

```python
device = "edge-sw1"
command = "show version"

print(f"Would run {command} on {device}")
```

Netmiko lets Python actually make the SSH connection, send the command, collect
the output, and close the session.

The shape is simple:

```text
device dictionary -> ConnectHandler -> send_command() -> output -> disconnect()
```

Every piece of that shape comes from earlier chapters.

## The First Netmiko Script

Here is a first complete script:

```python
#!/usr/bin/env python
from netmiko import ConnectHandler

ios1 = {
    "device_type": "cisco_ios",
    "ip": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}

net_connect = ConnectHandler(**ios1)
output = net_connect.send_command("show version")
net_connect.disconnect()

print(output)
```

This is the real version of the dry run you have been practicing.

## Line-by-Line Walkthrough

The first line is the shebang:

```python
#!/usr/bin/env python
```

On Linux and macOS, this tells the operating system which interpreter should run
the file if you execute it directly. On Windows, it is harmless.

Next, import Netmiko's connection class:

```python
from netmiko import ConnectHandler
```

`ConnectHandler` is the object that knows how to open a network session. You do
not have to manually handle SSH negotiation, prompts, terminal width, or command
timing. Netmiko handles those details.

Then define the device:

```python
ios1 = {
    "device_type": "cisco_ios",
    "ip": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}
```

This is just a dictionary. Nothing magical is happening yet. The keys tell
Netmiko what kind of device to connect to, where it lives, and which credentials
to use.

Then connect:

```python
net_connect = ConnectHandler(**ios1)
```

The `**ios1` syntax unpacks the dictionary. It is similar to writing:

```python
net_connect = ConnectHandler(
    device_type="cisco_ios",
    ip="198.18.1.11",
    username="cisco",
    password="cisco",
)
```

Then send a show command:

```python
output = net_connect.send_command("show version")
```

The result comes back as a string. That means you can print it, save it to a
file, split it into lines, search it, or eventually parse it into structured
data.

Finally, disconnect:

```python
net_connect.disconnect()
```

Always close the session. A script that opens connections but does not close
them can leave stale sessions on the device.

## Using a Context Manager

The first script works, but there is a better pattern:

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}

with ConnectHandler(**device) as conn:
    output = conn.send_command("show version")

print(output)
```

The `with` statement automatically closes the connection when the indented block
finishes. This is the same idea you saw with files in Chapter 10.

```text
with open(...) as f:
    ...

with ConnectHandler(...) as conn:
    ...
```

The pattern means: open the resource, use it safely, clean up when done.

## Sending Configuration

Show commands are read-only. Configuration commands change the device.

Netmiko uses a different method for configuration:

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}

commands = ["logging host 10.1.1.1"]

with ConnectHandler(**device) as conn:
    output = conn.send_config_set(commands)

print(output)
```

`send_config_set()` enters configuration mode, sends the commands, and exits
configuration mode. A single command can be sent, but a list is usually better
because configuration changes often have more than one line.

Example:

```python
commands = [
    "vlan 20",
    "name USERS",
]
```

Before sending configuration, build the list and print it:

```python
for command in commands:
    print(f"Would configure: {command}")
```

That dry-run habit never goes away.

## Running Multiple Show Commands

You already know lists and loops, so this should look familiar:

```python
show_commands = [
    "show version",
    "show ip interface brief",
    "show clock",
]

with ConnectHandler(**device) as conn:
    for command in show_commands:
        print(f"\n--- {command} ---")
        output = conn.send_command(command)
        print(output)
```

This is the moment the earlier chapters pay off. Lists and loops are not
academic. They are how one connection becomes many commands.

## Practice Exercise

Rewrite the first Netmiko script using these steps:

1. Store the command in a variable named `command`.
2. Print `Connecting to 198.18.1.11`.
3. Run `show ip interface brief`.
4. Disconnect.
5. Print the output.

Then rewrite it again using a `with` statement.

---

# Chapter 13: Multi-Device Automation and File-Driven Inventory

## What This Chapter Teaches

One device is useful. Multiple devices are where automation becomes valuable.

The basic pattern is:

```text
list of devices -> loop -> connect -> run work -> disconnect -> next device
```

You already know every Python concept in that sentence.

## Two Devices as Dictionaries

Start with two device dictionaries:

```python
ios1 = {
    "device_type": "cisco_ios",
    "ip": "198.18.1.11",
    "username": "cisco",
    "password": "cisco",
}

ios2 = {
    "device_type": "cisco_ios",
    "ip": "198.18.1.12",
    "username": "cisco",
    "password": "cisco",
}

devices = [ios1, ios2]
```

`devices` is a list of dictionaries. This is one of the most important data
structures in network automation.

Now loop:

```python
from netmiko import ConnectHandler

for device in devices:
    print(f"Connecting to {device['ip']}")

    with ConnectHandler(**device) as conn:
        output = conn.send_command("show version")

    print(output)
```

On the first loop, `device` is `ios1`. On the second loop, `device` is `ios2`.
The same code runs for both.

## Reading Devices from a File

Hard-coding devices in a script is fine for learning, but real scripts should
separate data from logic.

Create a file named `device_list`:

```text
198.18.1.11
198.18.1.12
```

Read it:

```python
with open("device_list") as f:
    device_list = f.read().splitlines()
```

Now `device_list` is:

```python
["198.18.1.11", "198.18.1.12"]
```

Build the connection dictionary inside the loop:

```python
from getpass import getpass
from netmiko import ConnectHandler

username = input("Enter SSH username: ")
password = getpass("Enter SSH password: ")

with open("device_list") as f:
    device_list = f.read().splitlines()

for ip_address in device_list:
    device = {
        "device_type": "cisco_ios",
        "ip": ip_address,
        "username": username,
        "password": password,
    }

    print(f"Connecting to {ip_address}")

    with ConnectHandler(**device) as conn:
        output = conn.send_command("show ip interface brief")

    print(output)
```

This pattern is powerful because the script does not care how many devices are
in the file. Add a third line to `device_list`, and the loop processes a third
device.

## Reading Configuration from a File

You can separate configuration commands too.

Create a file named `config_commands`:

```text
logging host 10.1.1.1
ntp server 8.8.8.8
snmp-server location LAB
```

Then send it:

```python
with ConnectHandler(**device) as conn:
    output = conn.send_config_from_file("config_commands")
```

The benefit is operational clarity:

- The Python script controls *how* work is done.
- The command file controls *what* configuration is applied.

That separation makes review easier. A peer can inspect `config_commands`
without reading the whole Python script.

## A Scalable Runner

Here is a simple multi-device runner:

```python
from getpass import getpass
from netmiko import ConnectHandler

username = input("Username: ")
password = getpass("Password: ")

with open("device_list") as f:
    device_ips = f.read().splitlines()

for ip in device_ips:
    device = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": username,
        "password": password,
    }

    print(f"\nConnecting to {ip}")

    try:
        with ConnectHandler(**device) as conn:
            output = conn.send_command("show clock")
    except Exception as exc:
        print(f"Failed on {ip}: {exc}")
        continue

    print(output)
```

The `continue` statement matters. If one device fails, the script skips it and
continues with the next device instead of crashing the whole run.

## Practice Exercise

Create:

- `device_list` with two lab device IPs
- `config_commands` with three harmless lab configuration commands

Write a script that:

1. Prompts for username and password.
2. Reads the device list.
3. Connects to each device.
4. Sends the config file.
5. Prints success or failure for each device.

Keep the first version in a lab only.

---

# Chapter 14: Production Scripts: Exceptions, Env Vars, and Show Commands

## What This Chapter Teaches

A lab script can be short. A production script needs guardrails.

Production guardrails include:

- catching expected exceptions
- skipping failed devices without stopping the whole run
- keeping credentials out of code
- saving enough output to troubleshoot later
- separating device lists and commands from logic

This chapter turns a working script into an operational script.

## The Production Exception Pattern

Network connections fail for normal reasons:

- wrong password
- device unreachable
- SSH disabled
- DNS failure
- prompt mismatch
- slow command output

Your script should expect this.

```python
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import NetmikoTimeoutException

for device in devices:
    try:
        connection = ConnectHandler(**device)
    except NetmikoAuthenticationException:
        print(f"Authentication failed for {device['ip']}")
        continue
    except NetmikoTimeoutException:
        print(f"Timeout connecting to {device['ip']}")
        continue
    except Exception as exc:
        print(f"Unexpected failure on {device['ip']}: {exc}")
        continue

    try:
        output = connection.send_command("show version")
        print(output)
    finally:
        connection.disconnect()
```

This pattern has two important ideas.

First, failures are specific where possible. Authentication failure is different
from timeout. Timeout is different from an unexpected exception.

Second, `finally` disconnects even if something goes wrong after the connection
is open.

## Why `continue` Matters

Suppose you have 100 devices. If device 7 fails authentication, should the
script stop and skip devices 8 through 100?

Usually, no.

`continue` says:

```text
this device failed; move to the next device
```

That is the production mindset. A single failed node should be recorded, not
allowed to destroy the entire batch.

## Credentials from Environment Variables

Hard-coded credentials are easy to learn with and dangerous to keep.

Use environment variables:

```python
import os
from getpass import getpass

username = os.getenv("NETMIKO_USERNAME") or input("Username: ")
password = os.getenv("NETMIKO_PASSWORD") or getpass("Password: ")
```

This says:

```text
If the environment variable exists, use it.
Otherwise, prompt the operator.
```

On Linux or macOS:

```text
export NETMIKO_USERNAME="admin"
export NETMIKO_PASSWORD="your-password"
```

In PowerShell:

```powershell
$env:NETMIKO_USERNAME = "admin"
$env:NETMIKO_PASSWORD = "your-password"
```

Do not commit passwords to Git.

## Multiple Show Commands from a File

Create a file named `show_command`:

```text
show running-config | include logging
show running-config | include ntp
show ip ospf neighbor
show ip interface brief
```

Read it:

```python
with open("show_command") as f:
    show_commands = f.read().splitlines()
```

Run every command on every device:

```python
for device in devices:
    with ConnectHandler(**device) as conn:
        for command in show_commands:
            output = conn.send_command(command)
            print(f"\n--- {device['ip']} :: {command} ---")
            print(output)
```

This is the pre-check and post-check pattern:

```text
before change -> collect command outputs
after change -> collect command outputs
compare
```

## Production Use Case: VLAN Standardization

A common operations problem is configuration drift. VLAN 20 might be called
`USERS` on one switch, `DATA` on another, and `VLAN0020` somewhere else.

Define the desired state:

```python
golden_vlans = {
    "10": "VOICE",
    "20": "USERS",
    "30": "SERVERS",
}
```

The script should:

1. Collect current VLANs from the switch.
2. Compare current names to the golden names.
3. Build commands only for mismatches.
4. Print the plan.
5. Apply only after review.

The important lesson is not the exact parser. The lesson is the workflow:

```text
current state -> desired state -> diff -> planned commands -> guarded change
```

That is production network automation.

## Practice Exercise

Write a dry-run script that:

1. Defines a `golden_vlans` dictionary.
2. Defines a fake `current_vlans` dictionary.
3. Compares them.
4. Prints configuration commands only for mismatched VLAN names.

Do not connect to devices yet. Make the diff logic clear first.

---

# Chapter 15: Automated Backup and Inventory Reports

## What This Chapter Teaches

Backups and reports are ideal first production automation projects.

They are valuable because they save time and create audit history. They are also
safer than configuration changes because they are mostly read-only.

This chapter builds two major patterns:

```text
device list -> show running-config -> backup file
```

and:

```text
device list -> show version -> parsed facts -> table and CSV report
```

## Configuration Backup Pattern

A backup script does five things:

1. Get credentials.
2. Create a backup folder.
3. Read a device list.
4. Connect to each device.
5. Save `show running-config` to a file.

Here is the core workflow:

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

username = os.getenv("NETMIKO_USERNAME") or input("Username: ")
password = os.getenv("NETMIKO_PASSWORD") or getpass("Password: ")

if not os.path.exists("backup"):
    os.mkdir("backup")

with open("device_list") as f:
    device_list = f.read().splitlines()

for ip_address in device_list:
    device = {
        "device_type": "cisco_ios",
        "ip": ip_address,
        "username": username,
        "password": password,
    }

    with ConnectHandler(**device) as conn:
        hostname = conn.find_prompt()[:-1]
        output = conn.send_command("show running-config")

    with open(f"backup/{hostname}.cfg", "w") as f:
        f.write(output)

    print(f"Saved backup for {hostname}")
```

The line below is a neat trick:

```python
hostname = conn.find_prompt()[:-1]
```

If the prompt is `CSR1#`, `find_prompt()` returns `CSR1#`. The slice `[:-1]`
removes the final `#`, leaving `CSR1`. That gives the backup file a meaningful
name without hard-coding hostnames.

## Adding Timestamps

Backups should not overwrite each other forever. Add a timestamp:

```python
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
filename = f"backup/{hostname}_{timestamp}.cfg"
```

Now every run creates a unique file.

## Structured Parsing with Genie

Plain text is easy for humans but awkward for programs. Structured output is
easier to report on.

Netmiko can use Genie parsing:

```python
output = conn.send_command("show version", use_genie=True)
```

Instead of a long string, you receive a nested dictionary. Then you can extract
facts:

```python
hostname = output["version"]["hostname"]
chassis = output["version"]["chassis"]
serial = output["version"]["chassis_sn"]
os_name = output["version"]["os"]
version = output["version"]["version"]
```

This is why Chapter 6 mattered. Parsed network output is dictionaries and lists.

## Building an Inventory Report

Start with a header row:

```python
inventory = []
inventory.append(["Hostname", "Chassis", "Serial No", "OS", "Version"])
```

For each device, append a row:

```python
device_details = [hostname, chassis, serial, os_name, version]
inventory.append(device_details)
```

At the end, write CSV:

```python
import csv

with open("inventory.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(inventory)
```

This is a complete reporting pattern:

```text
collect -> parse -> extract fields -> append rows -> write report
```

## Pre- and Post-Change Telemetry

Before a maintenance window, collect a snapshot:

```text
show ip interface brief
show ip ospf neighbor
show running-config | include logging
show running-config | include ntp
```

After the change, collect the same snapshot again.

The goal is not just automation speed. The goal is evidence. If something
breaks, you have before-and-after data. If everything works, you have proof.

## Practice Exercise

Write a dry-run backup planner:

1. Create a list of two fake IP addresses.
2. For each IP, create a fake hostname.
3. Build the filename that would be used for backup.
4. Print the command `show running-config`.
5. Print the final planned file path.

Then modify it to include a timestamp in each filename.

---

# Part III: Twin-Bridges Mastery Lab Workbook

This section turns the twin-bridges course repositories into deliberate lab work. The goal is mastery through repetition: read the code, explain the code, dry-run the code, change one thing, and connect the pattern back to the chapter concepts.

Do not treat these as copy-paste recipes. Treat each lab as a small inspection exercise. A network automation engineer should be able to answer four questions about every script: What data goes in? What decision does the code make? What network action could happen? What evidence comes out?

Recommended rhythm for every lab:

1. Read the lab objective.
2. Read the source slowly.
3. Explain the code out loud in plain English.
4. Run only in a safe lab, or convert live network calls to dry-run `print()` statements.
5. Change one value and predict the outcome.
6. Write one operational guardrail you would add before production use.
---

## Lab Track 1: Getting Started in a Network Lab

**Concept focus:** run Python, print device context, and build the first lab-safe habit.

**Mental model:** `editor -> Python file -> simulated device fact -> printed result`

### TB-001: `python_course_mar26/class1/python_script/my_script.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
print("Hello world")
```

---

## Lab Track 2: Variables, Strings, and Device Facts

**Concept focus:** store hostnames, interfaces, versions, and command text.

**Mental model:** `raw fact -> variable name -> string method/f-string -> readable report`

### TB-002: `python_course_mar26/class1/strings/f_strings.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print

ip_addr = "142.251.141.110"
fields = ip_addr.split(".")
print(fields)

octet1, octet2, octet3, octet4 = fields

# f-string 15-wide columns (left-aligned by default)
print()
print(f"|{octet1:15}|{octet2:15}|{octet3:15}|{octet4:15}|")

# f-string 15-wide columns (right-aligned)
print()
print(f"|{octet1:>15}|{octet2:>15}|{octet3:>15}|{octet4:>15}|")

# f-string 15-wide columns (centered)
print()
print(f"|{octet1:^15}|{octet2:^15}|{octet3:^15}|{octet4:^15}|")

# Variable display trick
print()
print(f"{octet1=}")

# f-string expressions get evaluated
print()
var1 = 22
var2 = 42
print(f"Variable sum: {var1 + var2}")
```

### TB-003: `python_course_mar26/class1/strings/unicode_chars.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
"""
Character 	Unicode (Hex)	Description
ä	00E4	a-umlaut (small)
ö	00F6	o-umlaut (small)
ü	00FC	u-umlaut (small)
Ä	00C4	A-umlaut (capital)
Ö	00D6	O-umlaut (capital)
Ü	00DC	U-umlaut (capital)
ß	00DF	Eszett / Sharp s
ẞ	1E9E	Capital Sharp S
"""

print("\u00e4")
print("\u00c4")

print("\u00f6")
print("\u00d6")

print("\u00fc")
print("\u00dc")

print("\u00df")
print("\u1e9e")

some_str = """
ä
Ä
ö
Ö
ü
Ü
ß
ẞ
"""
print(some_str)
```

### TB-004: `python_course_mar26/class1/exercises/string_ex/strings_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Strings Exercise

Use the .split() method to divide the following:

1. 198.51.100.0/24 (divide the network from the mask and create a separate variable for each).
    * Further subdivide the IPv4 address into octets.
    * Print out the ipv4_network, ipv4_mask, and all four octets.
    * Use f-strings and 4 x 15-character columns to print out each octet.
    * Center the octets in their column.
2. 2001:db8:1:1::/64 (divide the network from the mask and create a separate variable for each).
    * Further subdivide the IPv6 address into hextets.
    * Print out the ipv6_network, ipv6_mask, and all four hextets.
    * Use f-strings and 4 x 15-character columns to print out each hextet.
    * Center the hextets in their column.

Example output
'''shell
$ python strings_ex1.py 

String Exercise1, part-1 (IPv4 .split())
----------------------------------------
IPv4 Network: 198.51.100.0
IPv4 Mask: 24

    octet1          octet2          octet3          octet4     
--------------- --------------- --------------- ---------------
      198             51              100              0       


String Exercise1, part-2 (IPv6 .split())
----------------------------------------
IPv6 Network: 2001:db8:1:1::
IPv6 Mask: 64

    hextet1         hextet2         hextet3         hextet4    
--------------- --------------- --------------- ---------------
     2001             db8              1               1       

'''
```

### TB-005: `python_course_mar26/class1/exercises/string_ex/strings_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print

ip_address = "198.51.100.0/24"
ipv6_address = "2001:db8:1:1::/64"

# Divide the network from the mask
ipv4_network, ipv4_mask = ip_address.split("/")

# Obtain the octets
octet1, octet2, octet3, octet4 = ipv4_network.split(".")

divider = "-" * 15
top_string = "String Exercise1, part-1 (IPv4 .split())"
top_divider = "-" * len(top_string)
print("\n" + top_string)
print(top_divider)
print(f"IPv4 Network: {ipv4_network}")
print(f"IPv4 Mask: {ipv4_mask}\n")
print(f"{'octet1':^15} {'octet2':^15} {'octet3':^15} {'octet4':^15}")
print(f"{divider:15} {divider:15} {divider:15} {divider:15}")
print(f"{octet1:^15} {octet2:^15} {octet3:^15} {octet4:^15}")

# Divide the network from the mask (IPv6)
ipv6_network, ipv6_mask = ipv6_address.split("/")

# Obtain the hextets
# _ indicates a junk variable (i.e. just discarded)
start_ipv6_network, _ = ipv6_network.split("::")
# Hard-coded length, in practice would (probably) use a list
hextet1, hextet2, hextet3, hextet4 = start_ipv6_network.split(":")

top_string = "String Exercise1, part-2 (IPv6 .split())"
top_divider = "-" * len(top_string)
print("\n\n" + top_string)
print(top_divider)
print(f"IPv6 Network: {ipv6_network}")
print(f"IPv6 Mask: {ipv6_mask}\n")
print(f"{'hextet1':^15} {'hextet2':^15} {'hextet3':^15} {'hextet4':^15}")
print(f"{divider:15} {divider:15} {divider:15} {divider:15}")
print(f"{hextet1:^15} {hextet2:^15} {hextet3:^15} {hextet4:^15}")
```

### TB-006: `python_course_mar26/class1/exercises/func_ex/func_ex3.md`

**Lab type:** Reading and design lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Function Exercise3

Construct a function named 'fw_func' that has three parameters: name, ip_addr, and os_version. The os_version parameter should have a default value of "R82".

The function body should use f-strings to print out the parameter name and corresponding value (for example, 'print(f"{name=}")' ).

The function body should also return the following string: f"{name}-{ipaddr}-{os_version}"

1. Call 'fw_func' using three positional arguments. Print out the function return value.
2. Call 'fw_func' using three named arguments. Print out the function return value.
3. Call 'fw_func' using two named arguments and the default os_version. Print out the function return value.
4. Call 'fw_func' using one positional argument and two named arguments. Print out the function return value.
on

Your program output should look similar to the following:

'''bash
$ python func_ex3.py 

Function call with positional arguments
------------------------------
name='chkpnt-pod99'
ipaddr='3.77.44.109'
os_version='R81.20'

ret_val='chkpnt-pod99-3.77.44.109-R81.20'


Function call with named arguments
------------------------------
name='chkpnt-pod1'
ipaddr='3.77.44.100'
os_version='R82'

ret_val='chkpnt-pod1-3.77.44.100-R82'


Function call with named arguments and a default value
------------------------------
name='chkpnt-pod1'
ipaddr='3.77.44.100'
os_version='R82'

ret_val='chkpnt-pod1-3.77.44.100-R82'


Function call with both positional and named arguments
------------------------------
name='chkpnt-pod2'
ipaddr='3.77.44.9'
os_version='R82.10'

ret_val='chkpnt-pod2-3.77.44.9-R82.10'

'''
```

---

## Lab Track 3: Introducing Device Lists

**Concept focus:** track device groups, command queues, and change windows.

**Mental model:** `device list -> index/slice/method -> selected maintenance target`

### TB-007: `python_course_mar26/class1/lists/list_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python

import ipdb  # noqa
from rich import print

my_list = ["zzz", "world", "foo", 22, None]
ipdb.set_trace()

print(type(my_list))
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[-1])

my_list[0] = "new value"
print(my_list)

some_list = [42, "a string"]
# my_list += some_list
my_list = my_list + some_list
print(my_list)

other_list = []

a_tuple = (42, 22, "hello")
print(type(a_tuple))
print(a_tuple)
```

### TB-008: `python_course_mar26/class1/lists/list_methods.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python

import ipdb  # noqa
from rich import print

my_list = ["zzz", "world", "foo", 22, None]
ipdb.set_trace()

print(my_list)
my_list.append(42)
print(my_list)

some_list = [0, "hello"]
my_list.extend(some_list)
print(my_list)

pop_val = my_list.pop()
print(f"{pop_val=}")
print(f"{my_list=}")

pop_val = my_list.pop(0)
print(f"{pop_val=}")
print(f"{my_list=}")

my_list.insert(0, "first val")
print(f"{my_list=}")

my_list.remove("foo")
print(f"{my_list=}")
```

---

## Lab Track 4: Working Through Networks with Loops

**Concept focus:** iterate over inventories and produce repeatable checks.

**Mental model:** `inventory -> for loop/comprehension -> repeated command plan`

### TB-009: `python_course_mar26/class1/loops/loop_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
import ipdb  # noqa

for loop_var in ["hello", "world", "something", "else"]:
    ipdb.set_trace()
    print(loop_var)
```

### TB-010: `python_course_mar26/class1/loops/loop_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
import ipdb  # noqa

my_list = ["hello", "world", "something", "else"]
for loop_var in my_list:
    print(loop_var)
    # Print the first letter
    print(loop_var[0])
    # Print the last letter
    print(loop_var[-1])
```

### TB-011: `python_course_mar26/class1/loops/loop_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
import ipdb  # noqa

my_list = ["hello", "world", "something", "else"]

for loop_var in my_list:
    if loop_var == "something":
        print("\n\nAll done!\n")
        break
    print(loop_var)
    print("...still in the loop")
```

### TB-012: `python_course_mar26/class1/loops/loop_ex4.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
import ipdb  # noqa

my_list = ["hello", "world", "something", "else"]

for loop_var in my_list:
    if loop_var == "something":
        print("<skip>")
        continue
    print(loop_var)
    print("...still in the loop")
```

### TB-013: `python_course_mar26/class1/loops/loop_ex5.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
import ipdb  # noqa

my_list = ["hello", "world", "something", "else"]
for idx, loop_var in enumerate(my_list):
    print(f"{idx} --> {loop_var}")
```

### TB-014: `python_course_mar26/class1/loops/loop_ex6.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
from rich import print

ftp_service = {
    "uid": "97aeb3d0-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Protocols/FTP",
    "color": "forest green",
}

print("\nLoop over the keys")
print("-" * 10)
for key in ftp_service.keys():
    print(key)

print("\nLoop over the values")
print("-" * 10)
# Loop over the values
for value in ftp_service.values():
    print(value)

print("\nLoop over the key-value")
print("-" * 10)
# Loop over the key-value
for k, v in ftp_service.items():
    print(f"{k} -> {v}")
```

### TB-015: `python_course_mar26/class1/loops/loop_ex7.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
from rich import print

ftp_service = {
    "uid": "97aeb3d0-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Protocols/FTP",
    "color": "forest green",
}

for k, v in ftp_service.items():
    if k == "domain":
        print()
        for inner_k, inner_v in v.items():
            print(f"{inner_k} -> {inner_v}")
        print()
```

### TB-016: `python_course_mar26/class1/loops/while_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, time, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import time
from rich import print

WAIT_TIME = 6

print()
start_time = time.time()
while time.time() - start_time < WAIT_TIME:
    print(time.time() - start_time)
    time.sleep(1)
    print("In loop...")

print("\nLoop over")
```

### TB-017: `python_course_mar26/class1/loops/while_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, time, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import time
from rich import print

WAIT_TIME = 6

print()
start_time = time.time()
while True:
    print("In loop...")
    time.sleep(1)
    cur_time = time.time()
    if (cur_time - start_time) > WAIT_TIME:
        break

print("\nLoop over")
```

### TB-018: `python_course_mar26/class1/loops/while_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, time, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import time
from rich import print

WAIT_TIME = 6

print()
check_var1 = "some string"
check_var2 = ""
while check_var1:
    print("In loop...")
    time.sleep(1)
    if not check_var2:
        break

print("\nLoop over")
```

### TB-019: `python_course_mar26/class1/exercises/loops_ex/loops_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It makes a decision from network data, such as whether to act, skip, retry, or report.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Loops Exercise1

Construct a list of five firewall pods: pod1-gaia, pod2-gaia, pod3-gaia, pod4-gaia, pod5-gaia.

Loop over this list and use 'rich.print' to print out the firewall name.

Loop over this list and check if the pod is 'pod5'. If so print the message of "Connecting to fw: pod5-gaia".
```

### TB-020: `python_course_mar26/class1/exercises/loops_ex/loops_ex2.md`

**Lab type:** Reading and design lab

**Objective:** It makes a decision from network data, such as whether to act, skip, retry, or report.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Loops Exercise2

Construct a list of seven firewall pods: pod1-gaia, pod2-gaia, pod3-gaia, pod4-gaia, pod5-gaia, pod98-gaia, and pod99-gaia.

Loop over this list of firewalls. If it 'pod4', then skip that pod (but keep looping over the list). If it is 'pod98', then break out of your loop.

If it is any of the other pods, then print out the firewall name.
```

### TB-021: `python_course_mar26/class1/exercises/loops_ex/loops_ex3.md`

**Lab type:** Reading and design lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Loops Exercise3

Construct a list of seven firewall pods: pod1-gaia, pod2-gaia, pod3-gaia, pod4-gaia, pod5-gaia, pod98-gaia, and pod99-gaia.

Loop over this list of firewalls while keeping track of both the firewall name and the loop index (remember your 'enumerate'). 

Use 'rich.print' and an f-string to print out both the loop index and the firewall name.
```

### TB-022: `python_course_mar26/class1/exercises/loops_ex/loops_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print

my_firewalls = [
    "pod1-gaia",
    "pod2-gaia",
    "pod3-gaia",
    "pod4-gaia",
    "pod5-gaia",
]

for fw in my_firewalls:
    print(fw)

for fw in my_firewalls:
    if fw == "pod5-gaia":
        print(f"\nConnecting to fw: {fw}\n")
```

### TB-023: `python_course_mar26/class1/exercises/loops_ex/loops_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print

my_firewalls = [
    "pod1-gaia",
    "pod2-gaia",
    "pod3-gaia",
    "pod4-gaia",
    "pod5-gaia",
    "pod98-gaia",
    "pod99-gaia",
]

for fw in my_firewalls:
    if fw == "pod4-gaia":
        continue
    if fw == "pod98-gaia":
        break
    print(fw)
```

### TB-024: `python_course_mar26/class1/exercises/loops_ex/loops_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print

my_firewalls = [
    "pod1-gaia",
    "pod2-gaia",
    "pod3-gaia",
    "pod4-gaia",
    "pod5-gaia",
    "pod98-gaia",
    "pod99-gaia",
]

for idx, fw in enumerate(my_firewalls):
    print(f"{idx} -> {fw}")
```

---

## Lab Track 5: If Statements for Network Decisions

**Concept focus:** decide whether an interface, device, or API version needs action.

**Mental model:** `network fact -> condition -> allow/deny/remediate branch -> action`

### TB-025: `python_course_mar26/class1/cond/api_support_versions.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
supported-versions:
- '1'
- '1.1'
- '1.2'
- '1.3'
- '1.4'
- '1.5'
- '1.6'
- '1.7'
- '1.8'
```

### TB-026: `python_course_mar26/class1/booleans/show_circuit.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print

# and: if the first condition is False, we are done.
check_cond = False
if check_cond and my_func():  # noqa
    print("Never printed")

# or: if the first condition is True, we are done.
skip_func = True
if skip_func or my_func():  # noqa
    print("Always printed")
```

### TB-027: `python_course_mar26/class1/cond/cond_ex4.py`

**Lab type:** Python fundamentals lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, yaml`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import yaml
# from rich import print


with open("api_support_versions.yml") as f:
    api_versions = yaml.safe_load(f)

supported_versions = api_versions["supported-versions"]

# ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8']
if "1.8" in supported_versions:
    api_version = "1.8"

api_version = "1.8"
if "1." in api_version:
    base_api = "v1"
elif "2." in api_version:
    base_api = "v2"
```

### TB-028: `python_course_mar26/class1/cond/cond_ex5.py`

**Lab type:** Python fundamentals lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, yaml, rich.print`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import yaml
from rich import print


with open("api_support_versions.yml") as f:
    api_versions = yaml.safe_load(f)

supported_versions = api_versions["supported-versions"]

# ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8']
if "1.8" in supported_versions:
    api_version = "1.8"

api_version = "1.8"
if "1." in api_version:
    base_api = "v1"
elif "2." in api_version:
    base_api = "v2"

if base_api == "v1" and float(api_version) >= 1.8:
    print("API Version 1.8 or later (not V2)")

if base_api == "v1" or base_api == "v2":
    print("API V1 or V2")
```

### TB-029: `python_course_mar26/class1/cond/cond_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, json, rich.print`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import json
from rich import print

with open("tcp_services.json") as f:
    services = json.load(f)

service_list = services["objects"]
print(len(service_list))

for service in service_list:
    service_name = service["name"]
    if service_name == "ftp":
        print("Found FTP Service")
    elif service_name == "domain-tcp":
        print("Found DNS (TCP)")
    else:
        print(service_name)
```

### TB-030: `python_course_mar26/class1/cond/cond_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, json, rich.print`.
3. It defines reusable function(s): `check_service`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import json
from rich import print


def check_service(service):
    """Just placeholder function."""
    pass


with open("tcp_services.json") as f:
    services = json.load(f)

service_list = services["objects"]
print(len(service_list))

for service in service_list:
    service_name = service["name"]
    if service_name == "ftp":
        print("Found FTP Service")
        check = check_service(service)
        if check:
            print("FTP service check passed")
    elif service_name == "domain-tcp":
        print("Found DNS (TCP)")
        check_service(service)
    else:
        print("Service not found")
        print("Nothing else to do")
```

### TB-031: `python_course_mar26/class1/cond/cond_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, json, rich.print`.
3. It defines reusable function(s): `check_service`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
import json
from rich import print


def check_service(service):
    """Just placeholder function."""
    pass


with open("tcp_services.json") as f:
    services = json.load(f)

service_list = services["objects"]
print(len(service_list))

for service in service_list:
    service_name = service["name"]
    if service_name == "ftp":
        print("Found FTP Service")
        check = check_service(service)
        if check:
            print("FTP service check passed")
    elif service_name == "domain-tcp":
        print("Found DNS (TCP)")
        check_service(service)
    else:
        print("Service not found")
        print("Nothing else to do")
```

### TB-032: `python_course_mar26/class1/booleans/truish.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print

# Strings
print("\nStrings:")
some_str = ""
print(bool(some_str))

# Numbers
print("\nNumbers:")
some_int = 0
print(bool(some_int))
some_float = 0.0
print(bool(some_float))

# Lists
print("\nLists:")
some_list = []
print(bool(some_list))

# Dict
print("\nDict:")
some_dict = {}
print(bool(some_dict))
```

### TB-033: `python_course_mar26/class1/cond/tcp_services.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "objects": [
        {
            "uid": "97aeb44f-9aea-11d5-bd16-0090272ccb30",
            "name": "AOL",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "5190",
            "icon": "Services/TCPService",
            "color": "red"
        },
        {
            "uid": "97aeb3e9-9aea-11d5-bd16-0090272ccb30",
            "name": "AP-Defender",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "2626",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3ea-9aea-11d5-bd16-0090272ccb30",
            "name": "AT-Defender",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "2626",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "96759a8d-aab8-43d9-bbfc-b459ce66ac87",
            "name": "Backage",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "411",
            "icon": "Services/TCPService",
            "color": "pink"
        },
        {
            "uid": "1fceea78-d378-44b4-8939-019b68f48518",
            "name": "BGP",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "179",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "86077a7d-a8da-4b5b-919c-366fe91ad1da",
            "name": "Bionet-Setup",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "5000",
            "icon": "Services/TCPService",
            "color": "magenta"
        },
        {
            "uid": "11da2773-a070-4f68-a3c2-9ce5dc158683",
            "name": "CheckPointExchangeAgent",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18301",
            "icon": "Protocols/MailProtocolEnvelope",
            "color": "black"
        },
        {
            "uid": "986bad5a-94d2-4a8c-81aa-de98d3ecb5c6",
            "name": "Citrix_ICA",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "1494",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "97aeb451-9aea-11d5-bd16-0090272ccb30",
            "name": "ConnectedOnLine",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "16384",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "97aeb3ad-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_Exnet_PK",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18262",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3ae-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_Exnet_resolve",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18263",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3a9-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_redundant",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18221",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb397-9aea-11d5-bd16-0090272ccb30",
```

_Source excerpt shown: first 160 of 657 lines. Use the repository file for the full data/output sample._

### TB-034: `python_course_mar26/class1/exercises/cond_ex/cond_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Conditional Exercise1

Use 'input' to prompt for a pod number. From this construct a "fw_name" variable that refers to a pod (for example, "chkpnt-pod1").

Construct a conditional that prints out "Found pod1" and "Found pod99" if the "fw_name" is "chkpnt-pod1" or "chkpnt-pod99". If neither of those conditions are matched, then print out the message "Not my pod".
```

### TB-035: `python_course_mar26/class1/exercises/cond_ex/cond_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print

pod_numb = input("Enter pod number: ")
fw_name = f"chkpnt-pod{pod_numb}"

if fw_name == "chkpnt-pod1":
    print("Found pod1")
elif fw_name == "chkpnt-pod99":
    print("Found pod99")
else:
    print("Not my pod")
```

---

## Lab Track 6: Dictionaries for Device Inventory

**Concept focus:** model devices, interfaces, services, and firewall objects.

**Mental model:** `real network object -> dict keys/values -> lookup/update/report`

### TB-036: `python_course_mar26/class1/dict/tcp_services.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "objects": [
        {
            "uid": "97aeb44f-9aea-11d5-bd16-0090272ccb30",
            "name": "AOL",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "5190",
            "icon": "Services/TCPService",
            "color": "red"
        },
        {
            "uid": "97aeb3e9-9aea-11d5-bd16-0090272ccb30",
            "name": "AP-Defender",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "2626",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3ea-9aea-11d5-bd16-0090272ccb30",
            "name": "AT-Defender",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "2626",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "96759a8d-aab8-43d9-bbfc-b459ce66ac87",
            "name": "Backage",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "411",
            "icon": "Services/TCPService",
            "color": "pink"
        },
        {
            "uid": "1fceea78-d378-44b4-8939-019b68f48518",
            "name": "BGP",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "179",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "86077a7d-a8da-4b5b-919c-366fe91ad1da",
            "name": "Bionet-Setup",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "5000",
            "icon": "Services/TCPService",
            "color": "magenta"
        },
        {
            "uid": "11da2773-a070-4f68-a3c2-9ce5dc158683",
            "name": "CheckPointExchangeAgent",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18301",
            "icon": "Protocols/MailProtocolEnvelope",
            "color": "black"
        },
        {
            "uid": "986bad5a-94d2-4a8c-81aa-de98d3ecb5c6",
            "name": "Citrix_ICA",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "1494",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "97aeb451-9aea-11d5-bd16-0090272ccb30",
            "name": "ConnectedOnLine",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "16384",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "97aeb3ad-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_Exnet_PK",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18262",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3ae-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_Exnet_resolve",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18263",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3a9-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_redundant",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18221",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb397-9aea-11d5-bd16-0090272ccb30",
```

_Source excerpt shown: first 160 of 657 lines. Use the repository file for the full data/output sample._

### TB-037: `python_course_mar26/class2/complex_dstruct/network_objects.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "objects": [
        {
            "uid": "eff32e1a-d4ed-4df9-a6e6-398c5d88b34d",
            "name": "CP_default_Office_Mode_addresses_pool",
            "type": "network",
            "domain": {
                "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                "name": "SMC User",
                "domain-type": "domain"
            },
            "subnet4": "172.16.10.0",
            "mask-length4": 24,
            "subnet-mask": "255.255.255.0",
            "icon": "NetworkObjects/network",
            "color": "black"
        },
        {
            "uid": "6796b2f5-d449-44dc-9cf8-75b33c4ca493",
            "name": "hq_net_128",
            "type": "network",
            "domain": {
                "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                "name": "SMC User",
                "domain-type": "domain"
            },
            "subnet4": "172.31.128.0",
            "mask-length4": 24,
            "subnet-mask": "255.255.255.0",
            "icon": "NetworkObjects/network",
            "color": "light green"
        },
        {
            "uid": "caee1116-8087-4310-9208-b422d3628a7e",
            "name": "IPv6_Link_Local_Hosts",
            "type": "network",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "subnet6": "fe80::",
            "mask-length6": 64,
            "icon": "NetworkObjects/network",
            "color": "black"
        }
    ],
    "from": 1,
    "to": 3,
    "total": 3
}
```

### TB-038: `python_course_mar26/class2/complex_dstruct/tcp_services.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "objects": [
        {
            "uid": "97aeb44f-9aea-11d5-bd16-0090272ccb30",
            "name": "AOL",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "5190",
            "icon": "Services/TCPService",
            "color": "red"
        },
        {
            "uid": "97aeb3e9-9aea-11d5-bd16-0090272ccb30",
            "name": "AP-Defender",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "2626",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3ea-9aea-11d5-bd16-0090272ccb30",
            "name": "AT-Defender",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "2626",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "96759a8d-aab8-43d9-bbfc-b459ce66ac87",
            "name": "Backage",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "411",
            "icon": "Services/TCPService",
            "color": "pink"
        },
        {
            "uid": "1fceea78-d378-44b4-8939-019b68f48518",
            "name": "BGP",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "179",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "86077a7d-a8da-4b5b-919c-366fe91ad1da",
            "name": "Bionet-Setup",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "5000",
            "icon": "Services/TCPService",
            "color": "magenta"
        },
        {
            "uid": "11da2773-a070-4f68-a3c2-9ce5dc158683",
            "name": "CheckPointExchangeAgent",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18301",
            "icon": "Protocols/MailProtocolEnvelope",
            "color": "black"
        },
        {
            "uid": "986bad5a-94d2-4a8c-81aa-de98d3ecb5c6",
            "name": "Citrix_ICA",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "1494",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "97aeb451-9aea-11d5-bd16-0090272ccb30",
            "name": "ConnectedOnLine",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "16384",
            "icon": "Services/TCPService",
            "color": "black"
        },
        {
            "uid": "97aeb3ad-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_Exnet_PK",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18262",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3ae-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_Exnet_resolve",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18263",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb3a9-9aea-11d5-bd16-0090272ccb30",
            "name": "CP_redundant",
            "type": "service-tcp",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "port": "18221",
            "icon": "Services/TCPService",
            "color": "firebrick"
        },
        {
            "uid": "97aeb397-9aea-11d5-bd16-0090272ccb30",
```

_Source excerpt shown: first 160 of 657 lines. Use the repository file for the full data/output sample._

### TB-039: `python_course_mar26/class1/dict/dict_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb, rich.print`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import ipdb  # noqa
from rich import print

ftp_service = {
    "uid": "97aeb3d0-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Protocols/FTP",
    "color": "forest green",
}
ipdb.set_trace()
print()
```

### TB-040: `python_course_mar26/class2/complex_dstruct/complex_ds2.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json, rich.print, ipdb`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json
from rich import print
import ipdb  # noqa

with open("network_objects.json") as f:
    net_objects = json.load(f)

ipdb.set_trace()
print(net_objects)
```

### TB-041: `python_course_mar26/class2/complex_dstruct/complex_ds3.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json, rich.print, ipdb`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json
from rich import print
import ipdb  # noqa

with open("tcp_services.json") as f:
    tcp_services = json.load(f)

ipdb.set_trace()
print(tcp_services)
```

### TB-042: `python_course_mar26/class2/complex_dstruct/complex_ds.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json, rich.print, ipdb`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json
from rich import print
import ipdb  # noqa

with open("sessions.json") as f:
    sessions = json.load(f)

ipdb.set_trace()
print(sessions)
```

### TB-043: `python_course_mar26/class2/complex_dstruct/sessions.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
[
    {
        "uid": "62408b66-24ea-4ca6-a7ef-4d4984f535d4",
        "type": "session",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
        },
        "state": "open",
        "user-name": "admin",
        "description": "",
        "last-login-time": {
            "posix": 1770759402157,
            "iso-8601": "2026-02-10T22:36+0100"
        },
        "expired-session": false,
        "application": "WEB_API",
        "changes": 0,
        "in-work": true,
        "ip-address": "127.0.0.1",
        "locks": 0,
        "email": "",
        "phone-number": "",
        "connection-mode": "read write",
        "session-timeout": 600,
        "workflow-state": "open",
        "workflow-history": "",
        "comments": "",
        "color": "black",
        "icon": "Objects/worksession",
        "tags": [],
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1770759402177,
                "iso-8601": "2026-02-10T22:36+0100"
            },
            "last-modifier": "admin",
            "creation-time": {
                "posix": 1770759402151,
                "iso-8601": "2026-02-10T22:36+0100"
            },
            "creator": "admin"
        },
        "read-only": false,
        "available-actions": {
            "edit": "true",
            "delete": "false",
            "clone": "false"
        }
    },
    {
        "uid": "1c49ab5c-e9de-440b-aadb-532e935a99ce",
        "type": "session",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
        },
        "state": "open",
        "user-name": "admin",
        "description": "",
        "last-login-time": {
            "posix": 1770759378466,
            "iso-8601": "2026-02-10T22:36+0100"
        },
        "expired-session": false,
        "application": "WEB_API",
        "changes": 0,
        "in-work": true,
        "ip-address": "127.0.0.1",
        "locks": 0,
        "email": "",
        "phone-number": "",
        "connection-mode": "read write",
        "session-timeout": 600,
        "workflow-state": "open",
        "workflow-history": "",
        "comments": "",
        "color": "black",
        "icon": "Objects/worksession",
        "tags": [],
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1770759378473,
                "iso-8601": "2026-02-10T22:36+0100"
            },
            "last-modifier": "admin",
            "creation-time": {
                "posix": 1770759378457,
                "iso-8601": "2026-02-10T22:36+0100"
            },
            "creator": "admin"
        },
        "read-only": false,
        "available-actions": {
            "edit": "true",
            "delete": "false",
            "clone": "false"
        }
    },
    {
        "uid": "8f1a2bc1-a67f-4750-a474-17fa71acd331",
        "type": "session",
        "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
        },
        "state": "open",
        "user-name": "admin",
        "description": "",
        "last-login-time": {
            "posix": 1770759368604,
            "iso-8601": "2026-02-10T22:36+0100"
        },
        "expired-session": false,
        "application": "WEB_API",
        "changes": 0,
        "in-work": true,
        "ip-address": "127.0.0.1",
        "locks": 0,
        "email": "",
        "phone-number": "",
        "connection-mode": "read write",
        "session-timeout": 600,
        "workflow-state": "open",
        "workflow-history": "",
        "comments": "",
        "color": "black",
        "icon": "Objects/worksession",
        "tags": [],
        "meta-info": {
            "lock": "unlocked",
            "validation-state": "ok",
            "last-modify-time": {
                "posix": 1770759368611,
                "iso-8601": "2026-02-10T22:36+0100"
            },
            "last-modifier": "admin",
            "creation-time": {
                "posix": 1770759368598,
                "iso-8601": "2026-02-10T22:36+0100"
            },
            "creator": "admin"
        },
        "read-only": false,
        "available-actions": {
            "edit": "true",
            "delete": "false",
            "clone": "false"
        }
    },
    {
        "uid": "0d0f74ab-6f4c-47ef-b3f7-8d0bc2ec0ebb",
        "type": "session",
```

_Source excerpt shown: first 160 of 262 lines. Use the repository file for the full data/output sample._

### TB-044: `python_course_mar26/class1/exercises/dict_ex/dict_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Dictionary Exercise1

1. Read the file "net_object_net128.json" in as JSON. Create a variable named 'network_obj' from this data (this should be a dictionary).
2. Print the dictionary
3. Retrieve the 'name', 'subnet4' and 'mask-length4' fields (store these into variables).
4. Print these three variables out.
5. Retrieve the network_obj['domain']['uid'] field (nested dictionary) and save to a variable named 'domain_uid'. Print out this value.
6. Add a new key 'location' to the dictionary (set this value to "Munich").
7. Change the 'location' key to "Cologne".
8. Delete the 'color' key.
9. Print your dictionary
```

### TB-045: `python_course_mar26/class1/exercises/dict_ex/dict_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `json, rich.print`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import json
from rich import print

with open("net_object_net128.json") as f:
    network_obj = json.load(f)

# Print the dictionary
print(network_obj)

# Retrieve the 'name', 'subnet4' and 'mask-length4' fields (store into variables)
name = network_obj["name"]
network = network_obj["subnet4"]
netmask = network_obj["mask-length4"]

# Print these three variables out.
print(f"Network Object: {name} ({network}/{netmask})")

# Retrieve the network_obj['domain']['uid'] field (nested dictionary) and save to a variable.
domain_uid = network_obj["domain"]["uid"]
print(f"Domain UID: {domain_uid}")

# Add a new key 'location' to the dictionary (set the value to "Munich").
network_obj["location"] = "Munich"

# Change the 'location' key to "Cologne"
network_obj["location"] = "Cologne"

# Delete the 'color' key
network_obj.pop("color")

# Print your dictionary
print(network_obj)
```

### TB-046: `python_course_mar26/class2/exercises/complex_ds_ex/complex_ds_ex2.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Complex Data Structures Exercise2

Convert your Complex Data Structures Exercise1 into a Python script.

The script should have a function named 'read_json' which takes a 'filename' argument and returns the JSON data from the file.

The script should also have a function named 'extract_fields' which takes a task dictionary as an argument. The function should extract the "task-id", "status", and "lock" fields (note, "lock" is embedded inside "meta-info"). 

This 'task' dictionary is the final dictionary that we were extracting "task-id" and "status" from in Exercise1. The function should return: '(task_id, status, lock)' as a tuple.

Your main program should read the "show_tasks.json" file using your function, perform the initial data processing to retrieve the "tasks" list, and loop over the "tasks" list to obtain the "task" dictionary.

Finally, your main program should call the "extract_fields" function and print out the returned data.

Your output should look similar to the following:

'''bash
$ python complex_ds_ex2.py 

d1313671-7c40-4c95-be76-a2ac451705e7 --> succeeded lock='unlocked'
37b26077-b9bb-40c7-a522-45ad0bee23c3 --> succeeded lock='unlocked'
ffb1b55b-1436-40e1-9076-83ebe54b5c68 --> succeeded lock='unlocked'

'''
```

---

## Lab Track 7: Operator Input and While Loops

**Concept focus:** collect operator intent safely and retry bounded workflows.

**Mental model:** `operator input -> validate -> while loop -> planned network action`

### TB-047: `python_course_mar26/class1/exercises/loops_ex/while_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### While-loop Exercise1

Construct a while loop such that you wait in the while loop for WAIT_TIME seconds (set this to a value of 8).

You should use time.time() to record both the start_time and the cur_time. The amount of seconds waited will be cur_time - start_time.

Inside your while loop use time.sleep(1) to sleep 1 second and also print a message stating "Sleeping 1s".

When WAIT_TIME has elapsed, you should exit your while loop. You should also print the message "All done..."

Your output should look similar to the following:

'''bash
$ python while_ex1.py 
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
All done...
'''

And your program should take roughly 8 seconds to run (8 seconds and a bit).
```

### TB-048: `python_course_mar26/class1/exercises/loops_ex/while_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print, time`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
import time

WAIT_TIME = 8

start_time = time.time()
while True:
    cur_time = time.time()
    if cur_time - start_time < WAIT_TIME:
        print("Sleeping 1s")
        time.sleep(1)
    else:
        print("All done...")
        break
```

### TB-049: `python_course_mar26/class1/try_except/try_except_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}

# Try to access a key that doesn't exist
fw_service["service_type"]

# Gracefully handle with try/except
try:
    print("before KeyError")
    fw_service["service_type"]
    print("after KeyError")
except KeyError:
    print("Inside exception handler")
```

### TB-050: `python_course_mar26/class1/try_except/try_except_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}

# Gracefully handle with try/except with finally
try:
    print("before KeyError")
    fw_service["service_type"]
    print("after KeyError")
except KeyError:
    print("Inside exception handler")
finally:
    print("Always happens")
```

### TB-051: `python_course_mar26/class1/try_except/try_except_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}

# Gracefully handle with try/except with finally
try:
    print("before KeyError")
    fw_service["service_type"]
    print("after KeyError")
except KeyError:
    print("Inside exception handler")
finally:
    print("Always happens")
```

### TB-052: `python_course_mar26/class1/try_except/try_except_ex4.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}
fw_service_keys = list(fw_service.keys())

# Gracefully handle with try/except with finally
try:
    print("before Error")
    # fw_service["service_type"]
    # Try to access list element that doesn't exist
    fw_service_keys[100]
    print("after Error")
except KeyError:
    print("KeyError exception handler")
except IndexError:
    print("IndexError exception handler")
finally:
    print("Always happens")
```

### TB-053: `python_course_mar26/class1/try_except/try_except_ex5.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}
fw_service_keys = list(fw_service.keys())

# Gracefully handle with try/except with finally
try:
    print("before Error")
    # fw_service["service_type"]
    # Try to access list element that doesn't exist
    fw_service_keys[100]
    print("after Error")
except (KeyError, IndexError):
    print("Handle both KeyError and IndexError")
finally:
    print("Always happens")
```

### TB-054: `python_course_mar26/class1/try_except/try_except_ex6.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}
fw_service_keys = list(fw_service.keys())

# Gracefully handle with try/except with finally
try:
    print("before Error")
    # fw_service["service_type"]
    # Try to access list element that doesn't exist
    fw_service_keys[100]
    print("after Error")
except Exception:
    print("Very generic exception handler.")
    print("...be careful here.")
finally:
    print("Always happens")
```

### TB-055: `python_course_mar26/class1/try_except/try_except_ex7.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}
fw_service_keys = list(fw_service.keys())

# Gracefully handle with try/except using 'as e'
try:
    print("before Error")
    # fw_service["service_type"]
    # Try to access list element that doesn't exist
    fw_service_keys[100]
    print("after Error")
except IndexError as e:
    print(f"Exception message: {e}")
```

### TB-056: `python_course_mar26/class1/try_except/try_except_ex8.py`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. It runs from top to bottom: create values, transform them, and print or return a result.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}
fw_service_keys = list(fw_service.keys())

msg = "Something went wrong"
raise ValueError(msg)
```

---

## Lab Track 8: Functions for Reusable Automation

**Concept focus:** turn repeated checks, command builders, and parsers into functions.

**Mental model:** `arguments -> function body -> return/report -> reuse across devices`

### TB-057: `python_course_mar26/class1/functions/func_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `my_func`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def my_func(x, y):
    print(x)
    print(y)
    return x + y


ret_val = my_func(7, 2)
print(f"{ret_val=}")
```

### TB-058: `python_course_mar26/class1/functions/func_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `my_func`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def my_func(x, y):
    print(f"{x=}")
    print(f"{y=}")
    return x + y


print()
ret_val = my_func(x=7, y=2)
print(f"{ret_val=}")

print()
ret_val = my_func(y=42, x=0)
print(f"{ret_val=}")
```

### TB-059: `python_course_mar26/class1/functions/func_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `my_func`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def my_func(x, y, z=100):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    return x + y + z


ret_val = my_func(x=7, y=2)
print(f"{ret_val=}")
```

### TB-060: `python_course_mar26/class1/functions/func_ex4.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `my_func`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def my_func(x, y, z=100):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    return x + y + z


my_list = [1, 7, 99]
ret_val = my_func(*my_list)
print(ret_val)
```

### TB-061: `python_course_mar26/class1/functions/func_ex5.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `my_func`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def my_func(x, y, z=100):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    return x + y + z


my_dict = {
    "x": 11,
    "y": 22,
    "z": 33,
}
ret_val = my_func(**my_dict)
print(ret_val)
```

### TB-062: `python_course_mar26/class2/gaia_func/gaia_funcs.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, json`.
2. It defines class blueprint(s): `GaiaAuthError, GaiaLogoutError`.
3. It defines reusable function(s): `login, api_call, logout`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import json


class GaiaAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class GaiaLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


def login(url, username, password):
    """Login and return the session_id."""
    headers = {"Content-Type": "application/json"}
    ssl_verify = False
    login_payload = {"user": username, "password": password}

    response = requests.post(
        url,
        data=json.dumps(login_payload),
        headers=headers,
        verify=ssl_verify,
    )
    resp_struct = response.json()
    return resp_struct["sid"]


def api_call(url, headers, payload=None, ssl_verify=False):
    if payload is None:
        payload = {}
    if "X-chkp-sid" not in headers:
        msg = """
Session ID not set, please call '.login()' method and properly
authenticate to the API.
"""
        raise GaiaAuthError(msg)

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(url, headers):
    """Removes 'X-chkp-sid' from headers and returns headers dict."""
    res = api_call(url, headers)
    if res.status_code == 200:
        msg = res.json()["message"]
    if res.status_code == 200 and msg == "OK":
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")
            return headers
    else:
        msg = "Failed to 'logout' from Gaia API"
        raise GaiaLogoutError(msg)
```

### TB-063: `python_course_mar26/class3/mgmt_func/mgmt_funcs.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, json`.
2. It defines class blueprint(s): `MgmtAuthError, MgmtLogoutError`.
3. It defines reusable function(s): `login, api_call, logout`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import json


class MgmtAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class MgmtLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


def login(url, username, password):
    """Login and return the session_id."""
    headers = {"Content-Type": "application/json"}
    ssl_verify = False
    login_payload = {"user": username, "password": password}

    response = requests.post(
        url,
        data=json.dumps(login_payload),
        headers=headers,
        verify=ssl_verify,
    )
    resp_struct = response.json()
    return resp_struct["sid"]


def api_call(url, headers, payload=None, ssl_verify=False):
    if payload is None:
        payload = {}
    if "X-chkp-sid" not in headers:
        msg = """
Session ID not set, please call '.login()' method and properly
authenticate to the API.
"""
        raise MgmtAuthError(msg)

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(url, headers):
    """Removes 'X-chkp-sid' from headers and returns headers dict."""
    res = api_call(url, headers)
    if res.status_code == 200:
        msg = res.json()["message"]
    if res.status_code == 200 and msg == "OK":
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")
            return headers
    else:
        msg = "Failed to 'logout' from Mgmt API"
        raise MgmtLogoutError(msg)
```

### TB-064: `python_course_mar26/work/gaia_funcs.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, json`.
2. It defines class blueprint(s): `GaiaAuthError, GaiaLogoutError`.
3. It defines reusable function(s): `login, api_call, logout`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import json


class GaiaAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class GaiaLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


def login(url, username, password):
    """Login and return the session_id."""
    headers = {"Content-Type": "application/json"}
    ssl_verify = False
    login_payload = {"user": username, "password": password}

    response = requests.post(
        url,
        data=json.dumps(login_payload),
        headers=headers,
        verify=ssl_verify,
    )
    resp_struct = response.json()
    return resp_struct["sid"]


def api_call(url, headers, payload=None, ssl_verify=False):
    if payload is None:
        payload = {}
    if "X-chkp-sid" not in headers:
        msg = """
Session ID not set, please call '.login()' method and properly
authenticate to the API.
"""
        raise GaiaAuthError(msg)

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(url, headers):
    """Removes 'X-chkp-sid' from headers and returns headers dict."""
    res = api_call(url, headers)
    if res.status_code == 200:
        msg = res.json()["message"]
    if res.status_code == 200 and msg == "OK":
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")
            return headers
    else:
        msg = "Failed to 'logout' from Gaia API"
        raise GaiaLogoutError(msg)
```

### TB-065: `python_course_mar26/work/mgmt_funcs.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, json`.
2. It defines class blueprint(s): `MgmtAuthError, MgmtLogoutError`.
3. It defines reusable function(s): `login, api_call, logout`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import json


class MgmtAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class MgmtLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


def login(url, username, password):
    """Login and return the session_id."""
    headers = {"Content-Type": "application/json"}
    ssl_verify = False
    login_payload = {"user": username, "password": password}

    response = requests.post(
        url,
        data=json.dumps(login_payload),
        headers=headers,
        verify=ssl_verify,
    )
    resp_struct = response.json()
    return resp_struct["sid"]


def api_call(url, headers, payload=None, ssl_verify=False):
    if payload is None:
        payload = {}
    if "X-chkp-sid" not in headers:
        msg = """
Session ID not set, please call '.login()' method and properly
authenticate to the API.
"""
        raise MgmtAuthError(msg)

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(url, headers):
    """Removes 'X-chkp-sid' from headers and returns headers dict."""
    res = api_call(url, headers)
    if res.status_code == 200:
        msg = res.json()["message"]
    if res.status_code == 200 and msg == "OK":
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")
            return headers
    else:
        msg = "Failed to 'logout' from Mgmt API"
        raise MgmtLogoutError(msg)
```

### TB-066: `python_course_mar26/class3/exercises/fw_policy_ex2/fw_policy_edit_rule.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Edit firewall rule exercise

Expand on your Firewall Policy Exercise1 implementation.

Change the allowed services in the 'corp_fw_rule' to also include "ssh".

Update the firewall rule using the Mgmt API and your functions. After the rule has been updated, then "publish" and "install" the firewall policy.

Note, ideally you will want to be able to share the same functions for your "fw_policy_ex1" code and for this code. You should avoid copying/duplicating the functions, if possible. 

In order to simplify things, you can location both "fw_policy_ex1" code and this code in the same directory.
```

---

## Lab Track 9: Classes for Devices and Sessions

**Concept focus:** model devices, API clients, and SSH sessions.

**Mental model:** `class blueprint -> device/session instance -> methods -> automation behavior`

### TB-067: `python_course_mar26/class3/exercises/class_api_ex/chkpt_api_ex.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `rich.print, ipdb`.
2. It defines class blueprint(s): `ChkptAPI`.
3. It defines reusable function(s): `__init__`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print  # noqa
import ipdb  # noqa


class ChkptAPI:
    def __init__(
        self,
        host,
        username,
        password,
        mode="web_api",
        api_version=None,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password

        if api_version is None:
            if mode == "web_api":
                api_version = "2"
            elif mode == "gaia_api":
                api_version = "1.8"

        self.ssl_verify = ssl_verify
        self.headers = {"Content-Type": "application/json"}
        self.base_url = f"https://{host}/{mode}/v{api_version}/"


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    user = "admin"
    admin_pass = "testpass"

    # Test Gaia API
    api_client = ChkptAPI(
        host=host, username=user, password=admin_pass, mode="gaia_api"
    )
    print("Testing ChkptAPI Class (Gaia API)")
    print(api_client.base_url)
    print()

    # Test Mgmt API
    api_client = ChkptAPI(
        host=host, username=user, password=admin_pass, mode="web_api"
    )
    print("Testing ChkptAPI Class (Mgmt API)")
    print(api_client.base_url)
    print()
```

### TB-068: `python_course_mar26/class3/gaia_class/gaia_class.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, json, rich.print, dotenv.load_dotenv, ipdb`.
2. It defines class blueprint(s): `GaiaAuthError, GaiaLogoutError, GaiaAPI`.
3. It defines reusable function(s): `__init__, login, logout, call`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class GaiaAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class GaiaLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class GaiaAPI:
    def __init__(self, host, username, password, api_version="1.8", ssl_verify=False):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/gaia_api/v{api_version}/"
        self.headers = {"Content-Type": "application/json"}
        self.ssl_verify = ssl_verify

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Gaia API"
            raise GaiaLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise GaiaAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = GaiaAPI(host=host, username=user, password=admin_pass)
    api_client.login()

    res = api_client.call(endpoint="show-version")
    print(res.json())

    api_client.logout()
```

### TB-069: `python_course_mar26/class3/gaia_class/gaia_class_cfg.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, json, rich.print, dotenv.load_dotenv, ipdb`.
2. It defines class blueprint(s): `GaiaAuthError, GaiaLogoutError, GaiaAPI`.
3. It defines reusable function(s): `__init__, login, logout, call`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class GaiaAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class GaiaLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class GaiaAPI:
    def __init__(self, host, username, password, api_version="1.8", ssl_verify=False):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/gaia_api/v{api_version}/"
        self.headers = {"Content-Type": "application/json"}
        self.ssl_verify = ssl_verify

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Gaia API"
            raise GaiaLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise GaiaAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = GaiaAPI(host=host, username=user, password=admin_pass)
    api_client.login()

    # Static Routes
    payload = {
        "address": "172.31.128.0",
        "mask-length": 21,
        "type": "gateway",
        "next-hop": {"gateway": "172.31.128.1"},
    }
    endpoint = "set-static-route"
    res = api_client.call(endpoint=endpoint, payload=payload)
    print(res.json())
    res = api_client.call(endpoint="show-static-routes")
    print(res.json())

    # DNS
    payload = {
        "primary": "172.31.0.2",
        "secondary": "8.8.8.8",
        "tertiary": "8.8.4.4",
        "suffix": "lasthop.io",
    }
    endpoint = "set-dns"
    res = api_client.call(endpoint=endpoint, payload=payload)
    res = api_client.call(endpoint="show-dns")
    print(res.json())

    api_client.logout()
```

### TB-070: `python_course_mar26/class3/mgmt_class/mgmt_class.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, json, rich.print, dotenv.load_dotenv, ipdb`.
2. It defines class blueprint(s): `MgmtAuthError, MgmtLogoutError, MgmtAPI`.
3. It defines reusable function(s): `__init__, login, logout, call`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class MgmtAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class MgmtLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class MgmtAPI:
    def __init__(
        self,
        host,
        username,
        password,
        api_version="2",
        read_only=False,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/web_api/v{api_version}/"
        self.headers = {"Content-Type": "application/json"}
        self.read_only = False
        self.ssl_verify = ssl_verify

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        if self.read_only:
            # Less overhead if read-only
            login_payload["enter-last-published-session"] = True
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        print(resp_struct)
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Mgmt API"
            raise MgmtLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise MgmtAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = MgmtAPI(host=host, username=user, password=admin_pass, read_only=True)
    api_client.login()

    res = api_client.call(endpoint="show-networks")
    print(res.json())

    api_client.logout()
```

### TB-071: `python_course_mar26/class3/mgmt_class/mgmt_class_cfg.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, json, rich.print, dotenv.load_dotenv, ipdb`.
2. It defines class blueprint(s): `MgmtAuthError, MgmtLogoutError, MgmtPublishError, MgmtAPI`.
3. It defines reusable function(s): `__init__, login, publish, logout, call`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class MgmtAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class MgmtLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class MgmtPublishError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class MgmtAPI:
    def __init__(
        self,
        host,
        username,
        password,
        api_version="2",
        read_only=False,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/web_api/v{api_version}/"
        self.headers = {"Content-Type": "application/json"}
        self.read_only = False
        self.ssl_verify = ssl_verify

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        if self.read_only:
            # Less overhead if read-only
            login_payload["enter-last-published-session"] = True
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        print(resp_struct)
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def publish(self):
        endpoint = "publish"
        res = self.call(endpoint)
        if res.status_code != 200:
            msg = "Publish operation failed!"
            raise MgmtPublishError(msg)

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Mgmt API"
            raise MgmtLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise MgmtAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = MgmtAPI(host=host, username=user, password=admin_pass, read_only=True)
    api_client.login()

    payload = {
        "name": "hq_net_128",
        "subnet": "172.31.128.0",
        "mask-length": 24,
        "color": "green",
    }
    api_client.call(endpoint="add-network", payload=payload)
    api_client.publish()
    res = api_client.call(endpoint="show-networks")
    print(res.json())

    api_client.logout()
```

### TB-072: `python_course_mar26/class3/exercises/class_api_ex/chkpt_api_ex_old.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, json, rich.print, ipdb`.
2. It defines class blueprint(s): `ChkptAuthError, ChkptLogoutError, ChkptAPI`.
3. It defines reusable function(s): `__init__, login, logout, call`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import json
from rich import print  # noqa
import ipdb  # noqa


class ChkptAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class ChkptLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class ChkptAPI:
    def __init__(
        self,
        host,
        username,
        password,
        mode="web_api",
        api_version=None,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password

        if api_version is None:
            if mode == "web_api":
                api_version = "2"
            elif mode == "gaia_api":
                api_version = "1.8"

        self.ssl_verify = ssl_verify
        self.headers = {"Content-Type": "application/json"}
        self.base_url = f"https://{host}/{mode}/v{api_version}/"

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Check Point API"
            raise ChkptLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise ChkptAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response
```

### TB-073: `python_course_mar26/class3/exercises/class_api_ex/test_chkpt_class.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, chkpt_api_ex.ChkptAPI, ipdb`.
2. It defines reusable function(s): `gaia_test, mgmt_test`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from chkpt_api_ex import ChkptAPI
import ipdb  # noqa


def gaia_test():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = ChkptAPI(
        host=host, username=user, password=admin_pass, mode="gaia_api"
    )
    api_client.login()

    endpoint = "show-static-routes"
    res = api_client.call(endpoint=endpoint)

    print()
    print("*" * 40)
    print("--- Gaia Class Test ---")
    print(res.json())
    print("*" * 40)
    print()

    api_client.logout()


def mgmt_test():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = ChkptAPI(host=host, username=user, password=admin_pass, mode="web_api")
    api_client.login()

    endpoint = "show-networks"
    res = api_client.call(endpoint=endpoint)

    print()
    print("*" * 40)
    print("--- Mgmt Class Test ---")
    print(res.json())
    print("*" * 40)
    print()

    api_client.logout()


if __name__ == "__main__":
    gaia_test()
    mgmt_test()
```

---

## Lab Track 10: Files, Exceptions, and Network Data

**Concept focus:** load inventories, handle bad data, and write audit artifacts.

**Mental model:** `file/API data -> read/parse -> handle errors -> save report`

### TB-074: `python_course_mar26/class1/files/read_json.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json, rich.print`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json
from rich import print

with open("gaia_api.json") as f:
    data = json.load(f)

print(data)
```

### TB-075: `python_course_mar26/class1/files/read_yaml.py`

**Lab type:** Python fundamentals lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. First, it brings in helper tools: `yaml, rich.print`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import yaml
from rich import print

with open("gaia_api.yaml") as f:
    data = yaml.safe_load(f)

print(data)
```

### TB-076: `python_course_mar26/class1/files/write_json.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json

data = {
    "current-version": "1.8",
    "supported-versions": ["1", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8"],
}

with open("gaia_api.json", "w") as f:
    json.dump(data, f, indent=4)
```

### TB-077: `python_course_mar26/class1/files/my_file.txt`

**Lab type:** Testing lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
aiofiles==24.1.0
aiohappyeyeballs==2.6.1
aiohttp==3.13.0
aiohttp-swagger==1.0.16
aiosignal==1.4.0
ansible==11.10.0
ansible-compat==25.8.2
ansible-core==2.18.10
ansible-lint==26.1.0
ansible-pylibssh==1.3.0
astroid==3.3.11
asttokens==3.0.0
async-lru==2.0.5
attrs==25.4.0
backcall==0.2.0
bcrypt==5.0.0
black==25.9.0
bracex==2.6
cachetools==6.2.0
certifi==2025.10.5
cffi==2.0.0
chardet==4.0.0
charset-normalizer==3.4.3
ciscoconfparse==1.5.46
click==8.3.0
colorama==0.4.6
cryptography==46.0.2
decorator==5.2.1
dict2xml==1.7.7
dill==0.4.0
distlib==0.4.0
distro==1.9.0
dnspython==2.8.0
et_xmlfile==2.0.0
executing==2.2.1
f5-icontrol-rest==1.3.13
filelock==3.19.1
flake8==7.3.0
frozenlist==1.8.0
future==1.0.0
genie==23.11
genie.libs.clean==23.11
genie.libs.conf==23.11
genie.libs.filetransferutils==23.11
genie.libs.health==23.11
genie.libs.ops==23.11
genie.libs.parser==23.11
genie.libs.sdk==23.11
gitdb==4.0.12
GitPython==3.1.45
grpcio==1.75.1
idna==3.10
importlib_metadata==8.7.0
iniconfig==2.1.0
invoke==2.2.0
ipdb==0.13.13
ipython==7.31.1
ipython_pygments_lexers==1.1.1
isort==6.1.0
jedi==0.19.2
Jinja2==3.1.6
jsonpickle==4.1.1
jsonrpclib==0.2.1
jsonschema==4.25.1
jsonschema-specifications==2025.9.1
junit-xml==1.9
junos-eznc==2.7.5
loguru==0.7.3
lxml==6.0.2
markdown-it-py==4.0.0
MarkupSafe==3.0.3
matplotlib-inline==0.1.7
mccabe==0.7.0
mdurl==0.1.2
multidict==6.7.0
mypy_extensions==1.1.0
napalm==5.0.0
ncclient==0.7.0
netaddr==1.3.0
netmiko==4.6.0
netutils==1.15.0
nornir==3.5.0
nornir-ansible==2023.12.28
nornir-jinja2==0.2.0
nornir-netbox==0.3.0
nornir-netmiko==1.0.1
nornir-utils==0.2.0
nornir_napalm==0.5.0
ntc_templates==8.1.0
nxapi_plumbing==0.5.2
openpyxl==3.1.5
packaging==25.0
paramiko==4.0.0
parso==0.8.5
passlib==1.7.4
pathspec==0.12.1
pdbr==0.9.2
pep8==1.7.1
pexpect==4.9.0
pickleshare==0.7.5
platformdirs==4.4.0
pluggy==1.6.0
ply==3.11
prettytable==3.16.0
prompt_toolkit==3.0.52
propcache==0.4.0
protobuf==6.32.1
psutil==7.1.0
ptyprocess==0.7.0
pure_eval==0.2.3
pyasn1==0.4.8
pyats==23.11
pyats.aereport==23.11
pyats.aetest==23.11
pyats.async==23.11
pyats.connections==23.11
pyats.datastructures==23.11
pyats.easypy==23.11
pyats.kleenex==23.11
pyats.log==23.11
pyats.reporter==23.11
pyats.results==23.11
pyats.tcl==23.11
pyats.topology==23.11
pyats.utils==23.11
pycodestyle==2.14.0
pycparser==2.23
pydocstyle==6.3.0
pyeapi==1.0.4
pyflakes==3.4.0
pyftpdlib==2.1.0
pygal==3.0.5
Pygments==2.19.2
pylama==8.4.1
pylint==3.3.9
PyNaCl==1.6.0
pynetbox==7.5.0
pyparsing==3.2.5
pyproject-api==1.9.1
pyserial==3.5
pysmi-lextudio==1.4.3
pysnmp==7.1.21
pysnmp-lextudio==5.0.29
pysnmpcrypto==0.0.4
pytest==8.4.2
python-engineio==3.14.2
python-socketio==4.6.1
pytokens==0.1.10
PyYAML==6.0.3
referencing==0.36.2
requests==2.32.5
resolvelib==1.0.1
rest.connector==23.11
rich==14.1.0
rpds-py==0.27.1
ruamel.yaml==0.18.15
ruamel.yaml.clib==0.2.14
scp==0.15.0
six==1.17.0
smmap==5.0.2
```

_Source excerpt shown: first 160 of 185 lines. Use the repository file for the full data/output sample._

### TB-078: `python_course_mar26/class1/files/file_cm.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python

# Context manager automatically close the file (when done)
with open("my_file.txt") as f:
    data = f.read()

print(data)
```

### TB-079: `python_course_mar26/class1/files/gaia_api.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "current-version": "1.8",
    "supported-versions": [
        "1",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
        "1.8"
    ]
}
```

### TB-080: `python_course_mar26/class1/files/gaia_api.yaml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
current-version: '1.8'
supported-versions:
- '1'
- '1.1'
- '1.2'
- '1.3'
- '1.4'
- '1.5'
- '1.6'
- '1.7'
- '1.8'
```

### TB-081: `python_course_mar26/class1/files/new_file.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
--> hello world <--
something else
one last line
```

### TB-082: `python_course_mar26/class1/files/read_file.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print

# Open file
f = open("my_file.txt", "r")

# Read entire file contents
data = f.read()
print(data)

# Go back to start of the file
f.seek(0)

# Read the entire file, but as a list of lines
data = f.readlines()
print(type(data))
print(data)

# Go back to start of the file
f.seek(0)

# Loop over the file (haven't covered loops yet)
print("Looping over file")
for line in f:
    # Eliminate double enter
    line = line.strip()
    print(repr(line))

# Cloes file
f.close()
```

### TB-083: `python_course_mar26/class1/files/write_file.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `ipdb`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python

import ipdb

ipdb.set_trace()

f = open("new_file.txt", "w")
f.write("hello world\n")
f.write("something else\n")
f.write("one last line\n")
print()

f.close()
```

### TB-084: `python_course_mar26/class1/files/write_file_cm.py`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python

with open("new_file.txt", "w") as f:
    f.write("--> hello world <--\n")
    f.write("something else\n")
    f.write("one last line\n")
```

### TB-085: `python_course_mar26/class1/files/write_yaml.py`

**Lab type:** Python fundamentals lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. First, it brings in helper tools: `yaml`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import yaml

data = {
    "current-version": "1.8",
    "supported-versions": ["1", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8"],
}

with open("gaia_api.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)
```

### TB-086: `python_course_mar26/class2/exercises/linux_python_ex/firewalls.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
- mun-fw1
- mun-fw2 
- col-fw1 
- col-fw2
```

### TB-087: `python_course_mar26/class2/exercises/linux_python_ex/pathlib_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Pathlib Exercise

Use the following to import pathlib

'''python
from pathlib import Path
'''

Create the following Path object:

'''python
home = Path.home()
firewalls_file = (
    home / "python_course_mar26/class2/exercises/linux_python_ex/firewalls.yml"
)
'''

Next using your Pathlib Path object, verify the 'firewalls_file' exists and is a file.

Extract the parent directory (i.e. the directory that contains the file 'firewalls.yml') and verify this directory exists and is a directory.

Use the 'yaml' library to read in the contents of this 'firewalls_file' as YAML. Print the contents of this file (it should be a list of firewalls).

Next use pathlib to create the following directory. You can use code similar to the following:

'''python
work_dir = home / "tmp_work"
if not work_dir.exists():
    print(f"Creating {work_dir}")
    work_dir.mkdir()
'''

Now add on the following two firewalls to your list of firewalls: ["ber-fw1", "ber-fw2"] 

Finally, create a new "firewalls.yml" file inside your new 'work_dir'. Once again use pathlib and the YAML library to accomplish this.
```

### TB-088: `python_course_mar26/class2/exercises/linux_python_ex/pathlib_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, rich.print, yaml`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
from rich import print
import yaml

# Pathlib home
home = Path.home()
firewalls_file = (
    home / "python_course_mar26/class2/exercises/linux_python_ex/firewalls.yml"
)

print(f"\n{firewalls_file=}")
print(f"Exists: {firewalls_file.exists()}")
print(f"Is file: {firewalls_file.is_file()}")

parent_dir = firewalls_file.parent
print(f"\n{parent_dir=}")
print(f"Parent exists: {parent_dir.exists()}")
print(f"Is dir: {parent_dir.is_dir()}")

## Read file as YAML
with open(firewalls_file) as f:
    fw_list = yaml.safe_load(f)

print(f"\n{fw_list=}\n")

# Create temp work dir
work_dir = home / "tmp_work"
if not work_dir.exists():
    print(f"Creating {work_dir}")
    work_dir.mkdir()

# Add new entries to firewall list
fw_list += ["ber-fw1", "ber-fw2"]

new_fw_file = work_dir / "firewalls.yml"
print(fw_list)
with open(new_fw_file, "w") as f:
    yaml.dump(fw_list, f, default_flow_style=False)
```

### TB-089: `python_course_mar26/class2/linux_python/os_system_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `os`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import os

cmd = "ping -c 4 google.com"
os.system(cmd)
```

### TB-090: `python_course_mar26/class2/linux_python/pathlib_ex.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, rich.print, ipdb`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
from rich import print
import ipdb  # noqa

# Pathlib home
home = Path.home()
netmiko_yml_file = home / ".netmiko.yml"

print(netmiko_yml_file)

# Read file
with open(netmiko_yml_file) as f:
    netmiko_yml_data = f.read()
print(netmiko_yml_data)

# Alternate read (pathlib magic)
netmiko_yml_data = netmiko_yml_file.read_text()
print(netmiko_yml_data)

# More difficult path
home = Path.home()
sessions_file = (
    home / "python_course_mar26" / "class2" / "complex_dstruct" / "sessions.json"
)

ipdb.set_trace()
sessions_file.exists()
sessions_file.is_file()
sessions_file.is_dir()

# Get the parent dir
sessions_file.name
parent_dir = sessions_file.parent
ipdb.set_trace()
print(parent_dir)

# Creating directories
# Path("./test1/2026/check_point").mkdir(parents=True, exist_ok=True)

# Find all JSONs in this folder
home = Path.home()
course_dir = home / "python_course_mar26"
# Recursive search
print()
for f in course_dir.rglob("*.json"):
    print(f)
```

### TB-091: `python_course_mar26/class2/linux_python/subprocess_ping.py`

**Lab type:** Scale and concurrency lab

**Objective:** It runs the same network task across multiple devices without waiting for one device at a time.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `subprocess, ipdb`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import subprocess
import ipdb  # noqa

command = ["ping", "-c", "4", "google.com"]

# run() execute the command; wait to finish
result = subprocess.run(
    command,
    capture_output=True, 
    text=True
)

ipdb.set_trace()
print(result.stdout)
print(result.stderr)
print(result.returncode)
```

### TB-092: `python_course_mar26/class2/linux_python/subprocess_popen.py`

**Lab type:** Scale and concurrency lab

**Objective:** It runs the same network task across multiple devices without waiting for one device at a time.

**What to notice:**

1. First, it brings in helper tools: `subprocess, pathlib.Path`.
2. It defines reusable function(s): `subprocess_runner`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import subprocess
from pathlib import Path


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


if __name__ == "__main__":
    cmd_list = ["ls", "-a", "-l"]
    print("Executing ls -al:")
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")
    print(std_out)
    print(std_err)

    home = Path.home()
    script = home / "python_course_mar26" / "class2" / "gaia_ssh" / "show_version.py"
    python = home / "VENV/py3_venv/bin/python"

    if script.is_file() and python.is_file():
        print("Executing Python script:")
        cmd_list = [python, script]
        std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")
        print(std_out)
        print(std_err)
```

### TB-093: `python_course_mar26/class1/exercises/file_ex/files_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Files exercise1

1. Read in the file named "network_objects.json" as text. Print out the type of the variable that you saved this data into (should be a string).
2. Read in the file named "network_objects.json" as JSON. Print out the type of the variable that you saved this data into (should be a dictionary). Print out the type of "data['objects']" field (should be a list).

Output should look similar to the following:

'''shell
$ python files_ex1.py 

Read in file(network_objects.json) as a string
Type 'data' var: <class 'str'>

Read in file(network_objects.json) as a data structure (dictionary)
Type 'data' var: <class 'dict'>
Type data['objects'] field: <class 'list'>
'''
```

### TB-094: `python_course_mar26/class1/exercises/file_ex/files_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `json, rich.print`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import json
from rich import print

filename = "network_objects.json"

# Read in file as text
with open(filename) as f:
    data = f.read()

# rich.print is misleading here as it would make it look like a data structure
print(f"\nRead in file({filename}) as a string")
print(f"Type 'data' var: {type(data)}")

# Read in file as JSON
with open(filename) as f:
    data = json.load(f)
print(f"\nRead in file({filename}) as a data structure (dictionary)")
print(f"Type 'data' var: {type(data)}")
print(f"Type data['objects'] field: {type(data['objects'])}")
print()
```

---

## Lab Track 11: Testing Network Automation

**Concept focus:** test parsers, command builders, inventory validation, and policy logic.

**Mental model:** `expected network behavior -> test case -> run test -> fix automation`

### TB-095: `python_course_mar26/class3/exercises/pytest_ex/test_funcs_ex.md`

**Lab type:** Reading and design lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### pytest exercise1

You will need to use pip to install pytest into your Python virtual environment.

'''bash
pip install pytest==9.0.2
'''

Create a Python file named 'simple_funcs.py'. Inside this file, define the following function:

'''python
def split_ip_addr(ip_addr):
    octets = ip_addr.split(".")
    if len(octets) != 4:
        raise ValueError("Invalid ip_addr, split('.') didn't return 4 octets")

    return octets
'''

In the same directory, create a "test_funcs_ex.py". This file will import the "split_ip_addr" function and then use pytest to test it.

Construct the following test case:

'''python
def test_split_ip(ip_addr, result):
    assert split_ip_addr(ip_addr) == result
'''

Use the `parametrize` decorator and then test the following IP addresses:

'''python
"1.1.1.1"
"182.227.100.10"
"127.0.0.1"
'''

Verify each one of the above IP addresses passes the test properly.


Next construct a test that verifies each of the following three invalid IP addresses properly raises a ValueError exception: "137.1.1", "37.1", "198.1.1.10.17".

Finally construct the following test:

'''python
def test_skip():
    assert split_ip_addr("1.1.1.1") == ["1", "1", "1", "1"]
'''

This test should be skipped if 'sys.platform == "linux"'.

Run py.test to make sure all of the above tests pass or are skipped.

Your output should look similar to the following:

'''shell
$ py.test -s -v test_funcs_ex.py 
============== test session starts =======================
platform linux -- Python 3.13.12, pytest-9.0.2
cachedir: .pytest_cache
rootdir: /home/kbyers/python_course_mar26/class3/exercises/pytest_ex
collected 7 items

test_funcs_ex.py::test_split_ip[1.1.1.1-result0] PASSED
test_funcs_ex.py::test_split_ip[182.227.100.10-result1] PASSED
test_funcs_ex.py::test_split_ip[127.0.0.1-result2] PASSED
test_funcs_ex.py::test_invalid_ip[137.1.1] PASSED
test_funcs_ex.py::test_invalid_ip[37.1] PASSED
test_funcs_ex.py::test_invalid_ip[198.1.1.10.17] PASSED
test_funcs_ex.py::test_skip SKIPPED (Skip test on Linux)

========== 6 passed, 1 skipped in 0.02s ==================
'''
```

### TB-096: `python_course_mar26/class3/test_pytest_ex/test_mgmt_api.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `ipdb, rich.print`.
2. It defines reusable function(s): `test_blocked_ips_group, test_host_objects, test_ansible_host`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import ipdb  # noqa
from rich import print  # noqa


def test_blocked_ips_group(web_api_session):
    # api_session is the logged-in client object from the fixture
    endpoint = "show-group"
    payload = {"name": "Blocked IPs"}
    response = web_api_session.api_call(endpoint, payload=payload)

    assert response.success is True

    group_name = response.data["name"]
    assert "Blocked IPs" == group_name

    # Membership check
    members = response.data["members"]
    assert len(members) == 10


def test_host_objects(web_api_session):
    minimum_host_objects = 10
    endpoint = "show-hosts"
    response = web_api_session.api_call(endpoint)

    host_objects = response.data["objects"]
    assert len(host_objects) >= minimum_host_objects


def test_ansible_host(web_api_session):
    host_name = "Ansible Server"
    ip_addr = "3.125.34.232"

    endpoint = "show-host"
    payload = {"name": host_name}
    response = web_api_session.api_call(endpoint, payload=payload)

    host_obj = response.data
    ipv4_addr = host_obj["ipv4-address"]

    assert host_name == host_obj["name"]
    assert ip_addr == ipv4_addr
```

### TB-097: `python_course_mar26/class3/test_pytest_ex/test_some_funcs.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pytest, sys, some_funcs.simple_sum, some_funcs.simple_div`.
2. It defines reusable function(s): `test_sums, test_negative_sums, test_addition, test_sums2, test_exception, test_skip_example`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import pytest
import sys
from some_funcs import simple_sum, simple_div


def test_sums():
    assert simple_sum(1, 7) == 8
    assert simple_sum(0, 0) == 0


def test_negative_sums():
    assert simple_sum(-1, -1) == -2


@pytest.mark.parametrize(
    "val1, val2, result", [(10, 5, 15), (-1, 1, 0), (0, 0, 0), (100, 200, 300)]
)
def test_addition(val1, val2, result):
    assert simple_sum(val1, val2) == result


@pytest.mark.slow
def test_sums2():
    assert simple_sum(100, 1) == 101
    assert simple_sum(1001, 1) == 1002
    assert simple_sum(1, 1) == 2


def test_exception():
    with pytest.raises(ZeroDivisionError):
        simple_div(10, 0)


@pytest.mark.skipif(
    sys.version_info.major == 3 and sys.version_info.minor == 13,
    reason="Skip test on PY3.13",
)
def test_skip_example():
    assert simple_sum(-7, 7) == 0
```

### TB-098: `python_course_mar26/class3/exercises/pytest_ex/test_funcs_ex.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pytest, sys, simple_funcs.split_ip_addr`.
2. It defines reusable function(s): `test_split_ip, test_invalid_ip, test_skip`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import pytest
import sys
from simple_funcs import split_ip_addr


@pytest.mark.parametrize(
    "ip_addr, result",
    [
        ("1.1.1.1", ["1", "1", "1", "1"]),
        ("182.227.100.10", ["182", "227", "100", "10"]),
        ("127.0.0.1", ["127", "0", "0", "1"]),
    ],
)
def test_split_ip(ip_addr, result):
    assert split_ip_addr(ip_addr) == result


@pytest.mark.parametrize(
    "bogus_ip_addr",
    [
        "137.1.1",
        "37.1",
        "198.1.1.10.17",
    ],
)
def test_invalid_ip(bogus_ip_addr):
    with pytest.raises(ValueError):
        split_ip_addr(bogus_ip_addr)


@pytest.mark.skipif(sys.platform == "linux", reason="Skip test on Linux")
def test_skip():
    assert split_ip_addr("1.1.1.1") == ["1", "1", "1", "1"]
```

### TB-099: `python_course_mar26/class3/test_pytest_ex/test_simple_exc.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pytest, some_funcs.simple_div`.
2. It defines reusable function(s): `test_exception`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import pytest
from some_funcs import simple_div


def test_exception():
    with pytest.raises(ZeroDivisionError):
        simple_div(10, 0)
```

### TB-100: `python_course_mar26/class4/exercises/main_project/tests/test_mgmt_cfg.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `ipdb, rich.print, host_objects.smart_console_private, host_objects.smart_console_public, host_objects.ansible_server, chkpt_policy_funcs.extract_fw_name`.
2. It defines reusable function(s): `test_host_objects, test_blocked_ips_group, test_firewall_rules`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import ipdb  # noqa
from rich import print  # noqa
from host_objects import smart_console_private, smart_console_public, ansible_server
from chkpt_policy_funcs import extract_fw_name
from gen_fw_rules import gen_blockedip_fw_rules, gen_mgmt_fw_rules


def test_host_objects(mgmt_api):

    api_client = mgmt_api
    api_endpoint = "show-host"

    mgmt_host_objects = [smart_console_private, smart_console_public, ansible_server]

    for host_obj in mgmt_host_objects:
        payload = {"name": host_obj["name"]}
        api_res = api_client.api_call(command=api_endpoint, payload=payload)
        assert api_res.success is True
        assert api_res.data["name"] == host_obj["name"]
        assert api_res.data["ipv4-address"] == host_obj["ipv4-address"]


def test_blocked_ips_group(mgmt_api):

    api_client = mgmt_api
    api_endpoint = "show-group"

    group_name = "Blocked IPs"
    payload = {"name": group_name}
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    assert api_res.success is True
    assert group_name == api_res.data["name"]
    members = api_res.data["members"]
    assert len(members) == 10


def test_firewall_rules(mgmt_api):
    api_client = mgmt_api
    fw_name = extract_fw_name(api_client.server)

    fw_rules = gen_mgmt_fw_rules(fw_name) + gen_blockedip_fw_rules()

    for fw_rule in fw_rules:
        payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
        api_res = api_client.api_call(command="show-access-rule", payload=payload)
        assert api_res.success is True
        source_objs = api_res.data["source"]
        dest_objs = api_res.data["destination"]
        source_names = [obj["name"] for obj in source_objs]
        destination_names = [obj["name"] for obj in dest_objs]
        # Mgmt API always returns a list even for single source
        if isinstance(fw_rule["source"], list):
            assert fw_rule["source"] == source_names
        else:
            assert [fw_rule["source"]] == source_names
        # Mgmt API always returns a list even for single destination
        if isinstance(fw_rule["destination"], list):
            assert fw_rule["destination"] == destination_names
        else:
            assert [fw_rule["destination"]] == destination_names

        services = api_res.data["service"]
        assert len(services) == 1
        service_name = services[0]["name"]
        assert fw_rule["service"].lower() == service_name.lower()
        assert fw_rule["action"] == api_res.data["action"]["name"]
```

### TB-101: `python_course_mar26/class3/test_pytest_ex/test_simple.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `some_funcs.simple_sum`.
2. It defines reusable function(s): `test_sums, test_negative_sums`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from some_funcs import simple_sum


def test_sums():
    assert simple_sum(1, 7) == 8
    assert simple_sum(0, 0) == 0


def test_negative_sums():
    assert simple_sum(-1, -1) == -2
```

### TB-102: `python_course_mar26/class4/exercises/main_project/tests/test_gaia_cfg.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `ipdb, rich.print`.
2. It defines reusable function(s): `test_dns_config, test_static_route_cfg`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import ipdb  # noqa
from rich import print  # noqa


def test_dns_config(gaia_api):

    api_client = gaia_api

    api_endpoint = "show-dns"
    api_res = api_client.api_call(command=api_endpoint)

    assert api_res.success is True
    dns_dict = api_res.data
    pri_dns = dns_dict["primary"]
    sec_dns = dns_dict["secondary"]
    ter_dns = dns_dict["tertiary"]
    suffix = dns_dict["suffix"]

    assert pri_dns == "172.31.0.2"
    assert sec_dns == "8.8.8.8"
    assert ter_dns == "8.8.4.4"
    assert suffix == "lasthop.io"


def test_static_route_cfg(gaia_api):

    api_client = gaia_api

    api_endpoint = "show-static-route"
    payload = {
        "address": "172.31.128.0",
        "mask-length": 21,
    }
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    assert api_res.success is True

    static_route = api_res.data
    network = static_route["address"]
    mask = static_route["mask-length"]
    next_hop_dict = static_route["next-hop"][0]
    next_hop = next_hop_dict["gateway"]
    gw_type = static_route["type"]

    assert network == "172.31.128.0"
    assert mask == 21
    assert next_hop == "172.31.128.1"
    assert gw_type == "gateway"
```

### TB-103: `python_course_mar26/class4/ssh_session/test_mgmt_cli_auth.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `os, pytest, mgmt_cli_session.mgmt_cli_auth, dotenv.load_dotenv`.
2. It defines reusable function(s): `test_mgmt_cli_auth`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import pytest
from mgmt_cli_session import mgmt_cli_auth
from dotenv import load_dotenv


def test_mgmt_cli_auth(ssh_conn):

    load_dotenv()
    admin_pass = os.environ["CHKP_ADMIN"]

    # Intentionally fail
    with pytest.raises(KeyError):
        mgmt_cli_auth(ssh_conn, username="admin", password="invalid")

    session_id = mgmt_cli_auth(ssh_conn, username="admin", password=admin_pass)
    assert len(session_id) == 43
```

### TB-104: `python_course_mar26/class3/test_pytest_ex/conftest.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pytest, os, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `web_api_session`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import pytest
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


@pytest.fixture(scope="session")
def web_api_session():

    api_server = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=True, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # Object that is passed to the tests
        yield api_client
```

### TB-105: `python_course_mar26/class3/exercises/object_func_ex/test_object_funcs.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `object_funcs.cfg_host_object, object_funcs.cfg_network_object, object_funcs.cfg_group_object`.
2. It defines reusable function(s): `test_host_object_creation, test_network_object_creation, test_group_object_creation`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from object_funcs import cfg_host_object, cfg_network_object, cfg_group_object


def test_host_object_creation(web_api_session):

    test_host_obj = {
        "name": "Test Host1",
        "ipv4-address": "10.31.10.101",
        "color": "black",
    }

    (api_res, status) = cfg_host_object(web_api_session, test_host_obj)
    assert api_res.success is True
    assert status in ["created", "updated"]


def test_network_object_creation(web_api_session):

    test_network_obj = {
        "name": "Test Network1",
        "subnet": "10.31.10.0",
        "color": "green",
        "mask-length": 24,
    }

    (api_res, status) = cfg_network_object(web_api_session, test_network_obj)
    assert api_res.success is True
    assert status in ["created", "updated"]


def test_group_object_creation(web_api_session):

    test_group_obj = {
        "name": "Test Group1",
        "members": [
            "Test Network1",
        ],
        "color": "blue",
    }

    (api_res, status) = cfg_group_object(web_api_session, test_group_obj)
    assert api_res.success is True
    assert status in ["created", "updated"]
```

### TB-106: `python_course_mar26/class3/exercises/pytest_ex/simple_funcs.py`

**Lab type:** Testing lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `split_ip_addr`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def split_ip_addr(ip_addr):
    octets = ip_addr.split(".")
    if len(octets) != 4:
        raise ValueError("Invalid ip_addr, split('.') didn't return 4 octets")

    return octets
```

### TB-107: `python_course_mar26/class3/test_pytest_ex/some_funcs.py`

**Lab type:** Testing lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `simple_sum, simple_div`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def simple_sum(x, y):
    return x + y


def simple_div(x, y):
    return x / y
```

### TB-108: `netmiko_course/tests/test_class2.py`

**Lab type:** Testing lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `time, pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_runner_collateral_exception, test_class2_ex1, test_class2_ex2, test_class2_ex3, test_class2_ex4`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import time
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class2/collateral/netmiko_log.py",
    "../class2/collateral/conn_mult_devices.py",
    "../class2/collateral/show_command.py",
    "../class2/collateral/expect_str.py",
    "../class2/collateral/read_timeout/traceroute_working.py",
]

TEST_COLLATERAL_EXC = [
    "../class2/collateral/read_timeout/traceroute_timeout.py",
    "../class2/collateral/read_timeout/traceroute_long.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXC)
def test_runner_collateral_exception(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "raise ReadTimeout" in std_err


def test_class2_ex1():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("10.220.88.1") == 4


def test_class2_ex2():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "cisco3>" in std_out
    assert "cisco3#" in std_out


def test_class2_ex3():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Program failed" in std_out
    assert "Execution time" in std_out
    # Let show tech-support complete
    time.sleep(120)


def test_class2_ex4():
    base_path = "../class2/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Resource" in std_out
    assert "Execution time" in std_out


# def test_class2_ex3():
#    base_path = "../class2/exercises/"
#    cmd_list = ["python", "exercise3.py"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    assert return_code == 0
#    assert std_err == ""
#    assert "cisco3>" in std_out
#    assert "cisco3#" in std_out
#    assert "cisco4>" in std_out
#    assert "cisco4#" in std_out
```

### TB-109: `netmiko_course/tests/test_class3.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_runner_collateral_exception, test_class3_ex1, test_class3_ex2, test_class3_ex3, test_class3_ex4, test_class3_ex5`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class3/collateral/show_timing.py",
    "../class3/collateral/show_textfsm.py",
    "../class3/collateral/show_genie.py",
    "../class3/collateral/show_genie_nxos.py",
    "../class3/collateral/show_ttp.py",
    "../class3/collateral/read_timeout_timing/traceroute_working.py",
]

TEST_COLLATERAL_EXC = [
    "../class3/collateral/read_timeout_timing/traceroute_timeout.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXC)
def test_runner_collateral_exception(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "raise ReadTimeout" in std_err


def test_class3_ex1():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "cisco3>" in std_out
    assert "cisco3#" in std_out
    assert "cisco4>" in std_out
    assert "cisco4#" in std_out


def test_class3_ex2():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Resource" in std_out
    assert "Exec time" in std_out


def test_class3_ex3():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "VLAN ID: 7" in std_out
    assert "VLAN0007" in std_out


def test_class3_ex4():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("nxos2") == 4
    assert std_out.count("10.0.2.16") == 4


def test_class3_ex5():
    base_path = "../class3/exercises/"
    cmd_list = ["python", "exercise5.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "VLAN ID: 7" in std_out
    assert "VLAN0007" in std_out
```

### TB-110: `python_course_mar26/class2/gaia_func/test_gaia_funcs.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, gaia_funcs.login, gaia_funcs.api_call, gaia_funcs.logout`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from gaia_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"
    base_url = f"https://{host}/gaia_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(f"{session_id=}")

    headers["X-chkp-sid"] = session_id

    url = base_url + "show-version"
    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
```

### TB-111: `python_course_mar26/class3/mgmt_func/test_mgmt_funcs.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, mgmt_funcs.login, mgmt_funcs.api_call, mgmt_funcs.logout`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from mgmt_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"
    endpoint = "login"
    base_url = f"https://{host}/web_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(f"{session_id=}")

    headers["X-chkp-sid"] = session_id

    url = base_url + "show-networks"
    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
```

### TB-112: `python_course_mar26/work/test_gaia_funcs.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, gaia_funcs.login, gaia_funcs.api_call, gaia_funcs.logout`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from gaia_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"
    base_url = f"https://{host}/gaia_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(f"{session_id=}")

    headers["X-chkp-sid"] = session_id

    url = base_url + "show-connections"  # No
    url = base_url + "show-arp"  # Yes
    url = base_url + "show-allowed-clients"  # Yes
    url = base_url + "show-nat-pools"  # No
    url = base_url + "show-cluster-state"  # No
    url = base_url + "show-cluster-members"  # No
    url = base_url + "show-param"  # No
    # url = base_url + "set-initial-setup" # Looks very interesting
    # url = base_url + "run-reboot" # Looks interesting
    url = base_url + "show-serial-number"  # Yes
    url = base_url + "show-asset"  # Yes
    url = base_url + "show-diagnostics"  # Looks interesting / requires payload
    # add-secheduled-job / set- / show- / Looks very interesting
    # lightshot -- Lightweight snapshot
    # scheduled backups
    # scheduled snapshots
    # custom intelligence feeds
    # user management
    # run-script    / Definitely do this!!!
    # Interfaces
    # Licensing

    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
```

### TB-113: `python_course_mar26/work/test_mgmt_funcs.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `os, json, rich.print, dotenv.load_dotenv, mgmt_funcs.login, mgmt_funcs.api_call`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import json
from rich import print
from dotenv import load_dotenv
from mgmt_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"
    endpoint = "login"
    base_url = f"https://{host}/web_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(f"{session_id=}")

    headers["X-chkp-sid"] = session_id

    # url = base_url + "show-networks"
    # revert-to-revision
    # show-session
    # show-sessions
    # show-list-published-session
    # assign session ownershipa
    # take over session
    # switch session    # looks interesting
    # url = base_url + "show-sessions"
    url = base_url + "show-gateway-capabilities"
    # show-login-message
    # set-login-message
    # show-gateway-capabilities
    # Services / Applications
    # Access Rule
    # NAT
    # Threat prevention(?)
    # HTTPS Inspection / Rule
    # Policy / install-policy & verify-policy
    # Multi domain
    # Smart Tasks
    # Repository scripts?
    # You can create python repository scripts | this could be interesting
    # Package deployment -- sounds interesting
    # url = base_url + "show-repository-packages"
    # url = base_url + "show-tasks"
    # payload = {
    #    "task-id": "37b26077-b9bb-40c7-a522-45ad0bee23c3",
    #    "details-level": "full"
    # }
    # res = api_call(url, headers, payload=payload)
    # User
    # High-availability
    # Administrators
    # url = base_url + "show-logs"    # Interesting
    # Cloud services
    # Misc
    #   where-used
    #   show-changes
    #   show-gateways-and-servers
    #   show-unused-objects

    res = api_call(url, headers)
    print(res.json())
    with open("output.json", "w") as f:
        json.dump(res.json(), f, indent=4)

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
```

### TB-114: `netmiko_course/tests/test_class7.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral_except, test_runner_collateral, test_class7_ex1, test_class7_ex2, test_class7_ex3, test_class7_ex4`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL_EXCEPT = [
    "../class7/collateral/tcp_conn_fail.py",
    "../class7/collateral/dns_fail.py",
    "../class7/collateral/auth_fail.py",
    "../class7/collateral/auth_fail_keys.py",
    # "../class7/collateral/banner_fail.py",
]

TEST_COLLATERAL = [
    "../class7/collateral/auth_retry.py",
    "../class7/collateral/auth_retry_func.py",
    "../class7/collateral/handle_failures.py",
    "../class7/collateral/conn_log.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL_EXCEPT)
def test_runner_collateral_except(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 1
    assert "Traceback" in std_err


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


def test_class7_ex1():
    base_path = "../class7/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Address         Age       MAC Address     Interface       Flags" in std_out


def test_class7_ex2():
    base_path = "../class7/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Connection failed" in std_out
    assert "Initial connection failed...retrying" in std_out
    assert "Authenticated successfully" in std_out
    assert "Address         Age       MAC Address     Interface       Flags" in std_out


def test_class7_ex3():
    base_path = "../class7/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Successfully connected to device" in std_out
    assert "nxos2#" in std_out


def test_class7_ex4():
    base_path = "../class7/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Successfully connected to device" in std_out
    assert "nxos2#" in std_out
```

### TB-115: `python_course_mar26/class4/exercises/main_project/tests/test_users_and_password_pol.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `ipdb, rich.print`.
2. It defines reusable function(s): `test_users, test_password_policy`.
3. It uses assertions/tests to say, `this result must be true`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import ipdb  # noqa
from rich import print  # noqa


def test_users(gaia_api):

    api_client = gaia_api

    CHECK_USERS = {"admin", "monitor"}

    api_endpoint = "show-users"
    api_res = api_client.api_call(command=api_endpoint)

    users = api_res.data["objects"]
    audit_users = []
    for user in users:
        username = user["name"]
        # user_roles = user["roles"]
        audit_users.append(username)

    # CHECKS #####
    audit_users = set(audit_users)
    assert audit_users == CHECK_USERS


def test_password_policy(gaia_api):

    MAX_FAILED_ATTEMPTS = 10
    MIN_LOCKOUT_DURATION = 600
    MAX_INACTIVE_DAYS = 365
    LOCK_INACTIVE_ACCOUNTS = True
    MIN_PWD_CHAR_COMPLEXITY = 3
    MIN_PWD_LENGTH = 10

    api_client = gaia_api

    api_endpoint = "show-password-policy"
    api_res = api_client.api_call(command=api_endpoint)

    password_policy = api_res.data
    password_lock = password_policy["lock-settings"]
    password_strength = password_policy["password-strength"]

    failed_attempts = password_lock["failed-attempts-settings"][
        "failed-attempts-allowed"
    ]
    lockout_duration = password_lock["failed-attempts-settings"][
        "failed-lock-duration-seconds"
    ]
    inactivity_days = password_lock["inactivity-settings"]["inactivity-threshold-days"]
    lock_inactive_accounts = password_lock["inactivity-settings"][
        "lock-unused-accounts-enabled"
    ]
    password_complexity = password_strength["complexity"]
    password_min_length = password_strength["minimum-length"]

    # CHECKS #####
    assert failed_attempts <= MAX_FAILED_ATTEMPTS
    assert lockout_duration >= MIN_LOCKOUT_DURATION
    assert inactivity_days <= MAX_INACTIVE_DAYS
    assert lock_inactive_accounts == LOCK_INACTIVE_ACCOUNTS
    assert password_complexity >= MIN_PWD_CHAR_COMPLEXITY
    assert password_min_length >= MIN_PWD_LENGTH
```

### TB-116: `netmiko_course/tests/test_class4.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. After that, it sends a show command and saves the text that comes back from the device.
3. It defines reusable function(s): `test_runner_collateral, test_class4_ex1, test_class4_ex2, test_class4_ex3, test_class4_ex4`.
4. It uses assertions/tests to say, `this result must be true`.
5. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class4/collateral/send_command_prompting.py",
    "../class4/collateral/send_command_timing_prompting.py",
    "../class4/collateral/send_multiline/mline_pattern.py",
    # "../class4/collateral/send_multiline/file_delete_pattern.py",
    # "../class4/collateral/send_multiline_timing/file_delete_timing.py",
    "../class4/collateral/send_multiline_timing/mline_time.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


def test_class4_ex1():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "copy flash" in std_out
    assert "Copy in progress" in std_out
    assert "bytes copied" in std_out


def test_class4_ex2():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "copy flash" in std_out
    assert "Copy in progress" in std_out
    assert "bytes copied" in std_out


def test_class4_ex3():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 180


def test_class4_ex4():
    base_path = "../class4/exercises/"
    cmd_list = ["python", "exercise4.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Target IP" in std_out
    assert "8.8.8.8" in std_out
    assert std_out.count("!") >= 180
```

### TB-117: `netmiko_course/tests/test_class1.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class1_ex1, test_class1_ex2, test_class1_ex3`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class1/collateral/simple_conn.py",
    "../class1/collateral/simple_conn_slog.py",
    "../class1/collateral/simple_conn_dict.py",
    "../class1/collateral/simple_conn_cm.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


def test_class1_ex1():
    base_path = "../class1/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "nxos1#" in std_out


def test_class1_ex2():
    base_path = "../class1/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "nxos1#" in std_out


def test_class1_ex3():
    base_path = "../class1/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "nxos1#" in std_out
```

### TB-118: `netmiko_course/tests/test_class10.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class10_ex1, test_class10_ex2, test_class10_ex3`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class10/collateral/detect_platform.py",
    "../class10/collateral/snmp_detect.py",
    "../class10/collateral/telnet_example.py",
    "../class10/collateral/write_read.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


def test_class10_ex1():
    base_path = "../class10/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco_xe") == 2
    assert std_out.count("cisco_nxos") == 2
    assert std_out.count("juniper_junos") == 2


def test_class10_ex2():
    base_path = "../class10/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco_xe") == 2
    assert std_out.count("cisco_nxos") == 2
    assert std_out.count("juniper_junos") == 2
    assert "Creating devices.yaml file" in std_out


def test_class10_ex3():
    base_path = "../class10/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco3") == 3
    assert "Trying 10.220.88.22" in std_out
```

### TB-119: `netmiko_course/tests/test_class12.py`

**Lab type:** Testing lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `re, pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class12_ex1, test_class12_ex2, test_class12_ex3`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import re
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class12/collateral/fast_cli.py",
    "../class12/collateral/enable.py",
    "../class12/collateral/config_mode.py",
    "../class12/collateral/commit.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


def test_class12_ex1():
    base_path = "../class12/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 1
    assert "ReadTimeout" in std_err
    assert "Fast CLI state" in std_out
    assert "Global Delay Factor state" in std_out
    assert "Command execution time" in std_out


def test_class12_ex2():
    base_path = "../class12/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco4") == 3
    assert re.search(r"cisco4.*\(config\)#", std_out)
    assert "cisco4-testing#" in std_out


def test_class12_ex3():
    base_path = "../class12/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Send configuration commands to device" in std_out
    assert "Commit change...operation is slow" in std_out
    assert "commit complete" in std_out
    assert "Configuration change using Netmiko (ktb)" in std_out
```

### TB-120: `netmiko_course/tests/test_class5.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, time, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class5_ex1, test_class5_ex2, test_class5_ex3`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from pathlib import Path
import pytest
import time

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class5/collateral/config_vlans.py",
    "../class5/collateral/config_file.py",
    "../class5/collateral/disable_cmd_verify.py",
    # "../class5/collateral/config_rm_user.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):
    # Arista's seem to have an issue where device's get overloaded?
    time.sleep(3)
    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    print(std_err)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


def test_class5_ex1():
    base_path = "../class5/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("ip domain-lookup") == 2
    assert std_out.count("ip domain-name bogus.com") == 2


def test_class5_ex2():
    base_path = "../class5/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("vlan 501") == 2
    assert std_out.count("vlan 502") == 2


def test_class5_ex3():
    base_path = "../class5/exercises/"
    cmd_list = ["python", "exercise3.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Changing the terminal width" in std_out
    assert "Setting the hostname to a very long value" in std_out
    assert "Testing long command that should now fail" in std_out
    assert "long command failed with an exception" in std_out
    assert "Restoring hostname to original value" in std_out
```

### TB-121: `netmiko_course/tests/test_class6.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, os, subprocess, utilities.subprocess_runner`.
2. It defines reusable function(s): `run_ssh_agent, test_runner_collateral, test_class6_ex1`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
import pytest
import os
import subprocess

from utilities import subprocess_runner


def run_ssh_agent():
    # Check for already running ssh-agent
    cmd_list = ["ps", "auwx"]
    # cmd_list = "ps auwx | grep ssh-agent | grep -v grep"
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")
    ssh_agent_running = False
    for line in std_out.splitlines():
        if "ssh-agent" in line:
            if "grep" in line:
                continue
            else:
                ssh_agent_running = True
                break

    # Retrieve the current environment
    env = os.environ.copy()
    if not ssh_agent_running:
        # Start the SSH Agent
        cmd_list = ["ssh-agent"]
        std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")

        # Set the environment variables
        for line in std_out.splitlines():
            if "SSH_AUTH_SOCK" in line or "SSH_AGENT_PID" in line:
                cmd_list = line.split(";")
                # Filter blank lines
                cmd_list = [cmd for cmd in cmd_list if cmd]
                for cmd in cmd_list:
                    if "=" in cmd:
                        env_var, env_value = cmd.split("=")
                        env[env_var] = env_value
                        break

    # And ssh-add ~/.ssh/test_rsa
    cmd_list = ["ssh-add", "~/.ssh/test_rsa"]
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, shell=True
    ) as proc:
        std_out, std_err = proc.communicate()
    print(std_err)

    cmd_list = ["ssh-add", "-l"]
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, shell=True
    ) as proc:
        std_out, std_err = proc.communicate()
    print(std_err)

    return env


TEST_COLLATERAL = [
    "../class6/collateral/ssh_keys.py",
    # "../class6/collateral/ssh_keys_encr.py",
    "../class6/collateral/ssh_config_file.py",
    "../class6/collateral/ssh_proxy_jump.py",
    # "../class6/collateral/ssh_keys_agent.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""
    assert "Traceback" not in std_out


# Close, but not quite working :-(
# def test_ssh_agent():
#
#     # Setup the SSH Agent
#     env = run_ssh_agent()
#
#     test_case = "../class6/collateral/ssh_keys_agent.py"
#     path_obj = Path(test_case)
#     script = path_obj.name
#     script_dir = path_obj.parents[0]
#
#     cmd_list = ["python", script]
#     with subprocess.Popen(
#         cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=script_dir
#     ) as proc:
#         std_out, std_err = proc.communicate()
#     print(std_out)
#     print(std_err)
#     # assert return_code == 0
#     assert std_err == ""


def test_class6_ex1():
    base_path = "../class6/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("10.220.88.1 ") == 2


# Will fail in the lab environment as things are missing (SSH keyfile, SSH trust)
# def test_class6_ex3():
#    base_path = "../class6/exercises/"
#    cmd_list = ["python", "exercise3.py"]
#    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
#    assert return_code == 0
#    assert std_err == ""
#    assert std_out.count("Line") == 1
#    assert std_out.count("Location") == 1
```

### TB-122: `netmiko_course/tests/test_class8.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class8_ex1, test_class8_ex2`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class8/collateral/cf_threads.py",
    "../class8/collateral/cf_threads_asc.py",
    "../class8/collateral/cf_processes.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


def test_class8_ex1():
    base_path = "../class8/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("Address") == 14


def test_class8_ex2():
    base_path = "../class8/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("Address") == 14
```

### TB-123: `netmiko_course/tests/test_class9.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class9_ex1, test_class9_ex2`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    "../class9/collateral/get_file.py",
    "../class9/collateral/get_progress_bar.py",
    "../class9/collateral/put_file.py",
    "../class9/collateral/put_progress_bar.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


def test_class9_ex1():
    base_path = "../class9/exercises/"
    cmd_list = ["python", "exercise1.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("Name servers are correct") == 2
    assert std_out.count("Domain name is correct") == 2


def test_class9_ex2():
    base_path = "../class9/exercises/"
    cmd_list = ["python", "exercise2.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert "Redirecting" in std_out
    assert "Verifying" in std_out
    assert "Retrieving" in std_out
    assert "file successfully transferred" in std_out
```

### TB-124: `netmiko_course/tests/test_class11.py`

**Lab type:** Testing lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `pathlib.Path, pytest, utilities.subprocess_runner`.
2. It defines reusable function(s): `test_runner_collateral, test_class11_ex1`.
3. It uses assertions/tests to say, `this result must be true`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from pathlib import Path
import pytest

from utilities import subprocess_runner


TEST_COLLATERAL = [
    # Require terminal server password
    #    "../class11/collateral/term_server1.py",
    #    "../class11/collateral/term_server2.py",
    #    "../class11/collateral/term_server3.py",
    #    "../class11/collateral/term_server4.py",
    #    "../class11/collateral/redispatch1.py",
]


@pytest.mark.parametrize("test_case", TEST_COLLATERAL)
def test_runner_collateral(test_case):

    path_obj = Path(test_case)
    script = path_obj.name
    script_dir = path_obj.parents[0]

    cmd_list = ["python", script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=script_dir)
    assert return_code == 0
    assert std_err == ""


def test_class11_ex1():
    base_path = "../class11/exercises/"
    cmd_list = ["python", "exercise1_final.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_err == ""
    assert std_out.count("cisco3") == 4
    assert std_out.count("netmiko.cisco.cisco_ios.CiscoIosSSH") == 1
    assert std_out.count("arista4") == 2
    assert std_out.count("netmiko.arista.arista.AristaSSH") == 1
    assert std_out.count("Use redispatch to switch the class") == 1
    assert std_out.count("completely close SSH session") == 1
```

### TB-125: `netmiko_course/tests/utilities.py`

**Lab type:** Scale and concurrency lab

**Objective:** It runs the same network task across multiple devices without waiting for one device at a time.

**What to notice:**

1. First, it brings in helper tools: `subprocess`.
2. It defines reusable function(s): `subprocess_runner, subprocess_runner_stdin`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def subprocess_runner_stdin(cmd_list, stdin_responses, exercise_dir):
    """Wrapper to execute subprocess including handling stdin."""
    if isinstance(stdin_responses, list):
        stdin_responses = "\n".join(stdin_responses)

    # universal_newlines will cause it to accept and return strings, not bytes
    proc = subprocess.Popen(
        cmd_list,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True,
        cwd=exercise_dir,
    )
    std_out, std_err = proc.communicate(input=stdin_responses)
    return (std_out, std_err, proc.returncode)
```

---

## Lab Track 12: Starting a Netmiko Project

**Concept focus:** connect to a lab device, find a prompt, and disconnect cleanly.

**Mental model:** `device dict -> ConnectHandler -> prompt/show command -> disconnect`

### TB-126: `netmiko_course/class1/collateral/simple_conn.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler


# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

net_connect = ConnectHandler(
    device_type="cisco_ios",
    # device_type="invalid",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
)
print(net_connect.find_prompt())
```

### TB-127: `netmiko_course/class1/collateral/simple_conn_cm.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    print(net_connect.find_prompt())

print("Hello")
```

### TB-128: `netmiko_course/class1/collateral/simple_conn_dict.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
print(net_connect.find_prompt())
net_connect.disconnect()
```

### TB-129: `netmiko_course/class1/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

net_connect = ConnectHandler(
    device_type="cisco_nxos",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
)

print(net_connect.find_prompt())
```

### TB-130: `netmiko_course/class1/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.disconnect()
```

### TB-131: `netmiko_course/class1/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "nxos1.out",
}
with ConnectHandler(**device) as net_connect:
    print(net_connect.find_prompt())
```

### TB-132: `netmiko_course/class1/collateral/simple_conn_slog.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
import time
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

time.sleep(4)

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    session_log="cisco3.out",
)
print(net_connect.find_prompt())
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect()
```

---

## Lab Track 13: Collecting Show Commands Across a Fleet

**Concept focus:** run operational commands against many devices and track results.

**Mental model:** `device fleet -> command loop -> per-device output -> result dictionary`

### TB-133: `netmiko_course/class2/collateral/read_timeout/traceroute_long.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    # "session_log": "traceroute.out",
}

command = "traceroute 8.8.8.8"

with ConnectHandler(**device) as ssh_conn:
    try:
        start_time = datetime.now()
        output = ssh_conn.send_command(command, read_timeout=60 * 1)
        # output = ssh_conn.send_command(command)
        print(output)
    finally:
        end_time = datetime.now()
        print()
        print("-" * 50)
        print(f"\n\nExecution time: {end_time - start_time}\n\n")
        print("-" * 50)
        print()
```

### TB-134: `netmiko_course/class2/collateral/read_timeout/traceroute_timeout.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    # "session_log": "traceroute.out",
}

command = "traceroute 8.8.8.8"

with ConnectHandler(**device) as ssh_conn:
    try:
        start_time = datetime.now()
        output = ssh_conn.send_command(command, read_timeout=20)
    finally:
        end_time = datetime.now()
        print()
        print("-" * 50)
        print(f"\n\nExecution time: {end_time - start_time}\n\n")
        print("-" * 50)
        print()
```

### TB-135: `netmiko_course/class2/collateral/read_timeout/traceroute_working.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    # "session_log": "traceroute.out",
}

command = "traceroute 10.220.88.28"

with ConnectHandler(**device) as ssh_conn:
    start_time = datetime.now()
    output = ssh_conn.send_command(command, read_timeout=20)
    end_time = datetime.now()
    print()
    print("-" * 50)
    print(output)
    print(f"\n\nExecution time: {end_time - start_time}\n\n")
    print("-" * 50)
    print()
```

### TB-136: `netmiko_course/class2/collateral/conn_mult_devices.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (cisco3, nxos1, arista1):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()
```

### TB-137: `netmiko_course/class2/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


cisco3 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

with ConnectHandler(**cisco3) as net_connect:
    # Intentionally do something that will break
    start_prompt = net_connect.find_prompt()

    # Will fail
    # net_connect.send_command("disable")

    # Working with expect_string
    net_connect.send_command("disable", expect_string=r">")

    end_prompt = net_connect.find_prompt()
    print(f"\nStarting prompt: {start_prompt}")
    print(f"\nEnding prompt: {end_prompt}")
    print()
```

### TB-138: `netmiko_course/class2/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, logging`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista3 = {
    "device_type": "arista_eos",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista4 = {
    "device_type": "arista_eos",
    "host": "arista4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (arista1, arista2, arista3, arista4):
    with ConnectHandler(**device) as net_connect:
        device_name = net_connect.find_prompt()
        output = net_connect.send_command("show ip arp")
        print(f"\nDevice: {device_name}:")
        print(output)
        print()
```

### TB-139: `netmiko_course/class2/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, datetime.datetime, getpass.getpass, netmiko.ConnectHandler, netmiko.ReadTimeout`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler, ReadTimeout

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}

try:
    ssh_conn = ConnectHandler(**device)
    start = datetime.now()
    show_tech = ssh_conn.send_command("show tech-support", read_timeout=5)
except ReadTimeout:
    end = datetime.now()
    print("\nProgram failed with ReadTimeout Exception.\n")
    print(f"Execution time: {end - start}")
    print("\n")
```

### TB-140: `netmiko_course/class2/exercises/exercise4.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, datetime.datetime, getpass.getpass, netmiko.ConnectHandler, netmiko.ReadTimeout`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler, ReadTimeout

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}

try:
    ssh_conn = ConnectHandler(**device)
    start = datetime.now()
    show_tech = ssh_conn.send_command("show tech-support", read_timeout=180)
    print("\nCommand Succeeded.\n")
except ReadTimeout:
    print("\nProgram failed with ReadTimeout Exception.\n")
finally:
    end = datetime.now()

try:
    ssh_conn.disconnect()
except Exception:
    pass

print("\n\n")
print("-" * 60)
print(show_tech)
print("-" * 60)
print("\n\n")
print(f"Execution time: {end - start}")
print("\n")
```

### TB-141: `netmiko_course/class2/collateral/expect_str.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)

output = net_connect.send_command("show ip int brief", expect_string=r"#")
print(output)
net_connect.disconnect()
```

### TB-142: `netmiko_course/class2/collateral/show_command.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)

output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect()
```

### TB-143: `netmiko_course/class2/collateral/netmiko_log.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass, logging`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
print(net_connect.find_prompt())
net_connect.disconnect()
```

---

## Lab Track 14: Configuration, Validation, and Rollback Thinking

**Concept focus:** prepare config sets, apply changes, verify state, and plan rollback.

**Mental model:** `intended state -> config commands -> verification command -> rollback notes`

### TB-144: `netmiko_course/class12/collateral/commit.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Then it sends configuration commands, which is the part that can change a real device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    vmx2 = {
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "output.txt",
    }

    with ConnectHandler(**vmx2) as net_connect:

        print("\n\nSend configuration commands to device:")
        cfg_commands = [
            "set system syslog archive size 110k files 3",
            "set system time-zone America/New_York",
        ]
        output = net_connect.send_config_set(cfg_commands)

        divider = "-" * 20
        print(f"\n{divider}\n{output}\n{divider}\n")

        print("Commit change...operation is slow")

        # Standard Commit
        output = net_connect.commit()

        # Commit with a comment
        # output = net_connect.commit(comment="Configuration change using Netmiko")

        # Commit confirm
        # output = net_connect.commit(confirm=True, confirm_delay=3)
        # wait_here = input("Hit enter to continue: ")
        # output = net_connect.commit()

        print(f"\n{divider}\n{output}\n{divider}\n")
        print()
```

### TB-145: `netmiko_course/class4/collateral/send_multiline/file_delete_pattern.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
}

with ConnectHandler(**device) as net_connect:

    # cisco3#del flash:/ex1.cfg
    # Delete filename [ex1.cfg]?
    # Delete bootflash:/ex1.cfg? [confirm]y
    # cisco3#

    filename = "test_cf.txt"
    cmd_list = [
        [f"del flash:/{filename}", r"Delete filename"],
        ["\n", r"confirm"],
        ["y", r"#"],
    ]

    output = net_connect.send_multiline(cmd_list)
    print(output)
```

### TB-146: `netmiko_course/class4/collateral/send_multiline/mline_pattern.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler, logging`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
cisco3#traceroute
Protocol [ip]:
Target IP address: 10.220.88.28
Ingress traceroute [n]:
Source address or interface: 10.220.88.22
DSCP Value [0]:
Numeric display [n]: y
Timeout in seconds [3]:
Probe count [3]:
Minimum Time to Live [1]:
Maximum Time to Live [30]:
Port Number [33434]:
Loose, Strict, Record, Timestamp, Verbose[none]:
Type escape sequence to abort.
Tracing the route to 10.220.88.28
VRF info: (vrf in name/id, vrf out name/id)
"""
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}

dest_ip = "10.220.88.28"
probes = "3"
commands = [
    ["traceroute", r"Protocol"],
    ["\n", r"Target IP address"],
    [dest_ip, r"Ingress traceroute"],
    ["\n", r"Source address or interface"],
    ["10.220.88.22", r"DSCP Value"],
    ["\n", r"Numeric display"],
    ["y", r"Timeout in seconds"],
    ["\n", r"Probe count"],
    [probes, r"Minimum Time to Live"],
    ["\n", r"Maximum"],
    ["\n", r"Port Number"],
    ["\n", r"Loose"],
    ["\n", ""],
]

start_time = datetime.now()
with ConnectHandler(**device) as ssh_conn:
    print("\n\n")
    print(ssh_conn.find_prompt())
    print("-" * 50)
    output = ssh_conn.send_multiline(commands)
    print(output)
    print("-" * 50)
    print("\n\n")
end_time = datetime.now()
print(f"Execution time: {end_time - start_time}")
```

### TB-147: `netmiko_course/class4/collateral/send_multiline_timing/file_delete_timing.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
}

with ConnectHandler(**device) as net_connect:

    # cisco3#del flash:/ex1.cfg
    # Delete filename [ex1.cfg]?
    # Delete bootflash:/ex1.cfg? [confirm]y
    # cisco3#

    filename = "test1_vlan.txt"
    cmd_list = [
        f"del flash:/{filename}",
        "\n",
        "y",
    ]

    output = net_connect.send_multiline_timing(cmd_list)
    print(output)
```

### TB-148: `netmiko_course/class4/collateral/send_multiline_timing/mline_time.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
cisco3#traceroute
Protocol [ip]:
Target IP address: 10.220.88.28
Ingress traceroute [n]:
Source address or interface: 10.220.88.22
DSCP Value [0]:
Numeric display [n]: y
Timeout in seconds [3]:
Probe count [3]:
Minimum Time to Live [1]:
Maximum Time to Live [30]:
Port Number [33434]:
Loose, Strict, Record, Timestamp, Verbose[none]:
Type escape sequence to abort.
Tracing the route to 10.220.88.28
VRF info: (vrf in name/id, vrf out name/id)
"""
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}

commands = [
    "traceroute",
    "\n",
    "10.220.88.28",
    "\n",
    "10.220.88.22",
    "\n",
    "y",
    "\n",
    "20",
    "\n",
    "\n",
    "\n",
    "\n",
]

start_time = datetime.now()
with ConnectHandler(**device) as ssh_conn:
    print("\n\n")
    print(ssh_conn.find_prompt())
    print("-" * 50)
    output = ssh_conn.send_multiline_timing(commands)
    print(output)
    print("-" * 50)
    print("\n\n")
end_time = datetime.now()
print(f"Execution time: {end_time - start_time}")
```

### TB-149: `netmiko_course/class5/collateral/config_file.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, yaml, netmiko.ConnectHandler, time`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Then it sends configuration commands, which is the part that can change a real device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It defines reusable function(s): `load_devices`.
7. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from getpass import getpass
import yaml
from netmiko import ConnectHandler
import time


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


if __name__ == "__main__":

    # Code so automated tests will run properly
    # Check for environment variable, if that fails, use getpass().
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    device_dict = load_devices()

    arista1 = device_dict["arista1"]
    arista2 = device_dict["arista2"]
    arista3 = device_dict["arista3"]
    arista4 = device_dict["arista4"]

    for device in (arista1, arista2, arista3, arista4):
        device["password"] = password
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_from_file("vlans.txt")
        output += net_connect.save_config()
        print(f"\n{output}\n\n")
        net_connect.disconnect()
        time.sleep(2)
```

### TB-150: `netmiko_course/class5/collateral/config_vlans.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, yaml, netmiko.ConnectHandler, time`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Then it sends configuration commands, which is the part that can change a real device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It defines reusable function(s): `load_devices`.
7. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from getpass import getpass
import yaml
from netmiko import ConnectHandler
import time


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


if __name__ == "__main__":

    # Code so automated tests will run properly
    # Check for environment variable, if that fails, use getpass().
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    device_dict = load_devices()

    arista1 = device_dict["arista1"]
    arista2 = device_dict["arista2"]
    arista3 = device_dict["arista3"]
    arista4 = device_dict["arista4"]

    cfg_changes = ["vlan 500", "name gold500"]

    for device in (arista1, arista2, arista3, arista4):
        device["password"] = password
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(cfg_changes)
        output += net_connect.save_config()
        print(f"\n{output}\n\n")
        net_connect.disconnect()
        time.sleep(2)
```

### TB-151: `netmiko_course/class5/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, netmiko.ReadTimeout, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Then it sends configuration commands, which is the part that can change a real device.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler, ReadTimeout
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    # "fast_cli": False,
    "session_log": "nxos1.out",
}

with ConnectHandler(**nxos1) as net_connect:

    print("\n\nChanging the terminal width...")
    output = net_connect.send_command("terminal width 80")

    print("\nSetting the hostname to a very long value...")
    output = net_connect.send_config_set("hostname verylonghostnamefornxos")

    # Will fail
    print("\nTesting long command that should now fail due to line-wrap issues")
    try:
        cmd = "show ip interface brief vrf management | include management"
        output = net_connect.send_command(cmd)
        print(f"\n{output}\n")
    except ReadTimeout:
        print("...long command failed with an exception")

    # Try again but disable cmd_verify
    banner = "-" * 12
    print("\n\nTrying again with cmd_verify disabled...should work:")
    output = net_connect.send_command(cmd, cmd_verify=False)
    print(f"{banner}\n{output}\n{banner}")

    # Try again but disable global_cmd_verify
    net_connect.global_cmd_verify = False
    print("Trying again with global_cmd_verify disabled...should work:")
    output = net_connect.send_command(cmd)
    print(f"{banner}\n{output}\n{banner}")

    print("\n\nRestoring hostname to original value...\n")
    net_connect.set_base_prompt()
    output = net_connect.send_config_set("hostname nxos1")
    net_connect.set_base_prompt()
```

### TB-152: `netmiko_course/class12/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Then it sends configuration commands, which is the part that can change a real device.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    device = {
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "output.txt",
    }

    net_connect = ConnectHandler(**device)

    print("\n\nSend configuration commands to device:")
    cfg_commands = [
        "set system syslog archive size 110k files 3",
        "set system time-zone America/New_York",
    ]
    output = net_connect.send_config_set(cfg_commands)

    divider = "-" * 20
    print(f"\n{divider}\n{output}\n{divider}\n")

    print("Commit change...operation is slow")

    # Commit with a comment. The and_quit=True causes the device to exit config mode post-commit
    output = net_connect.commit(
        comment="Configuration change using Netmiko (ktb)", and_quit=True
    )

    print(f"\n{divider}\n{output}\n{divider}\n")
    print()

    commit_history = net_connect.send_command("show system commit")
    commit_history = commit_history.strip()
    commit_list = commit_history.splitlines()
    last_commit = commit_list[:2]
    last_commit = "\n".join(last_commit)
    print(last_commit)
```

### TB-153: `netmiko_course/class4/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
Reference ping output:

cisco3#ping
Protocol [ip]:
Target IP address: 8.8.8.8
Repeat count [5]: 100
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 100, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/4 ms
"""
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}

commands = [
    "ping",
    "\n",
    "8.8.8.8",
    "100",
    "\n",
    "\n",
    "\n",
    "\n",
]
for device in (cisco3, cisco4):
    with ConnectHandler(**device) as ssh_conn:
        print("\n\n")
        print(ssh_conn.find_prompt())
        print("-" * 50)
        output = ssh_conn.send_multiline_timing(commands)
        print(output)
        print("-" * 50)
        print("\n\n")
```

### TB-154: `netmiko_course/class4/exercises/exercise4.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
Reference ping output:

cisco3#ping
Protocol [ip]:
Target IP address: 8.8.8.8
Repeat count [5]: 100
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 100, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/4 ms
"""
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
}

commands = [
    ("ping", "Protocol"),
    ("\n", "Target"),
    ("8.8.8.8", "Repeat count"),
    ("100", "Datagram size"),
    ("\n", "Timeout"),
    ("\n", "Extended commands"),
    ("\n", "Sweep range"),
    ("\n", "#"),
]
for device in (cisco3, cisco4):
    with ConnectHandler(**device) as ssh_conn:
        print("\n\n")
        print(ssh_conn.find_prompt())
        print("-" * 50)
        output = ssh_conn.send_multiline(commands)
        print(output)
        print("-" * 50)
        print("\n\n")
```

### TB-155: `netmiko_course/class5/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Then it sends configuration commands, which is the part that can change a real device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}
nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}

config_cmds = ["ip domain-lookup", "ip domain-name bogus.com"]

for device in (nxos1, nxos2):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_set(config_cmds)
        print(f"\n{output}\n")
```

### TB-156: `netmiko_course/class5/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Then it sends configuration commands, which is the part that can change a real device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}
nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": False,
}

for device in (nxos1, nxos2):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_from_file("vlans.txt")
        print(f"\n{output}\n")
```

### TB-157: `netmiko_course/class12/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, datetime.datetime`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True,
}

net_connect = ConnectHandler(**my_device)

try:
    # Command that send_command will fail on
    print(f"\n\nFast CLI state: {net_connect.fast_cli}")
    print(f"Global Delay Factor state: {net_connect.global_delay_factor}")
    start_time = datetime.now()
    output = net_connect.send_command("conf t")
finally:
    end_time = datetime.now()
    print(f"\nCommand execution time: {end_time - start_time}\n")
```

### TB-158: `netmiko_course/class12/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    debug = True
    device = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**device)
    print(f"\nCurrent Prompt:\n{net_connect.find_prompt()}\n")

    print("Enter into configuration mode:")
    output = net_connect.config_mode()
    net_connect.clear_buffer()
    print(f"\nCurrent Prompt:\n{net_connect.find_prompt()}\n")

    new_hostname = "cisco4-testing"
    net_connect.write_channel(f"hostname {new_hostname}\n")

    print("Exit configuration mode:")
    output = net_connect.exit_config_mode()

    # Should reset Netmiko's base prompt if you change the hostname
    net_connect.set_base_prompt()

    print(f"\nCurrent Prompt:\n{net_connect.find_prompt()}\n")
```

### TB-159: `netmiko_course/class4/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
    # If using send_command_timing, always set fast_cli=False
    "fast_cli": False,
}

net_connect = ConnectHandler(**my_device)

src_file = "testx.txt"
dest_file = "test-ktb.txt"
copy_cmd = f"copy flash:/{src_file} flash:/{dest_file}"

output = net_connect.send_command_timing(
    command_string=copy_cmd, strip_prompt=False, strip_command=False
)
if "Destination filename" in output:
    output += net_connect.send_command_timing(
        command_string="\n", strip_prompt=False, strip_command=False
    )
# If the destination file already exists, it will prompt you to 'confirm'.
if "Do you want to over write" in output:
    output += net_connect.send_command_timing(
        command_string="y", strip_prompt=False, strip_command=False
    )

print(output)
net_connect.disconnect()
```

### TB-160: `netmiko_course/class4/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

net_connect = ConnectHandler(**my_device)

src_file = "testx.txt"
dest_file = "test-ktb.txt"
copy_cmd = f"copy flash:/{src_file} flash:/{dest_file}"

output = net_connect.send_command(
    command_string=copy_cmd,
    expect_string=r"Destination filename",
    strip_prompt=False,
    strip_command=False,
)
output += net_connect.send_command(
    command_string="\n",
    expect_string=r"(confirm|\#)",
    strip_prompt=False,
    strip_command=False,
)
# If the destination file already exists, it will prompt you to 'confirm'.
if "confirm" in output:
    output += net_connect.send_command(
        command_string="y", expect_string=r"\#", strip_prompt=False, strip_command=False
    )

print(output)
net_connect.disconnect()
```

### TB-161: `netmiko_course/class5/collateral/disable_cmd_verify.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, yaml, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Then it sends configuration commands, which is the part that can change a real device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It defines reusable function(s): `load_devices`.
7. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from getpass import getpass
import yaml
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


if __name__ == "__main__":

    # Code so automated tests will run properly
    # Check for environment variable, if that fails, use getpass().
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    device_dict = load_devices()

    arista1 = device_dict["arista1"]

    cfg_changes = ["vlan 500", "name gold500"]

    for device in (arista1,):
        device["password"] = password
        net_connect = ConnectHandler(**device)
        # Disable cmd_verify
        output = net_connect.send_config_set(cfg_changes, cmd_verify=False)
        output += net_connect.save_config()
        print(output)
        net_connect.disconnect()
```

### TB-162: `netmiko_course/class5/exercises/vlans.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
vlan 501
  name blue501
vlan 502
  name blue502
```

### TB-163: `netmiko_course/class12/collateral/config_mode.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


if __name__ == "__main__":

    debug = True
    cisco4 = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    vmx2 = {
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    my_device = vmx2

    with ConnectHandler(**my_device) as net_connect:

        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")

        print("Enter into configuration mode:")
        output = net_connect.config_mode()
        if debug:
            divider = "-" * 20
            print(f"\n{divider}\n{output}\n{divider}\n")
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        print()

        print("Exit configuration mode:")
        output = net_connect.exit_config_mode()
        if debug:
            divider = "-" * 20
            print(f"\n{divider}\n{output}\n{divider}\n")
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        print()
```

### TB-164: `netmiko_course/class12/collateral/enable.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `lower_privileges, show_current_priv`.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


def lower_privileges(net_connect):
    net_connect.exit_enable_mode()
    print("*" * 40)
    print()
    print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
    show_current_priv(net_connect)


def show_current_priv(net_connect):
    output = net_connect.send_command("show priv")
    print(f"Current Privilege Level: {output}")


if __name__ == "__main__":

    my_device = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": password,
        "secret": password,
    }

    with ConnectHandler(**my_device) as net_connect:

        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        show_current_priv(net_connect)

        # Drop to privilege level1
        lower_privileges(net_connect)

        # Use 'enable()' method to raise privileges. This will automatically handle the password
        # must have 'secret' argument set in the device dictionary.
        net_connect.enable()
        print("*" * 40)
        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        show_current_priv(net_connect)

        # Try again - go back to priv level1
        lower_privileges(net_connect)

        # Now call 'enable', but feed in a 'cmd'
        net_connect.enable(cmd="enable 15")
        print("*" * 40)
        print()
        print(f"Current Prompt:\n{net_connect.find_prompt()}\n")
        show_current_priv(net_connect)
```

### TB-165: `netmiko_course/class12/collateral/fast_cli.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True,
}

with ConnectHandler(**my_device) as net_connect:

    print(f"\n\n{net_connect.find_prompt()}\n\n")
    print(f"Fast CLI state: {net_connect.fast_cli}")
    print(f"Global Delay Factor state: {net_connect.global_delay_factor}")

    output = net_connect.send_command("show ip int brief")
    print()
    print("-" * 20)
    print(output)
    print()
```

### TB-166: `netmiko_course/class4/collateral/send_command_prompting.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

with ConnectHandler(**my_device) as net_connect:

    filename = "file_ex_3.txt"
    cmd = f"del flash:/{filename}"

    output = net_connect.send_command(
        cmd, expect_string=r"Delete filename", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "\n", expect_string=r"confirm", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command(
        "y", expect_string=r"#", strip_prompt=False, strip_command=False
    )
    print(output)
```

### TB-167: `netmiko_course/class4/collateral/send_command_timing_prompting.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "cisco3.out",
}

with ConnectHandler(**my_device) as net_connect:

    filename = "cisco3-cfg-May-16-11-15-40.259-113"
    cmd = f"del flash:/{filename}"

    output = net_connect.send_command_timing(
        cmd, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "y", strip_prompt=False, strip_command=False
    )
    print(output)
```

### TB-168: `netmiko_course/class5/collateral/config_rm_user.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, yaml, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It defines reusable function(s): `load_devices`.
7. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
import yaml
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


if __name__ == "__main__":

    # Code so automated tests will run properly
    # Check for environment variable, if that fails, use getpass().
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    device_dict = load_devices()

    cisco3 = device_dict["cisco3"]

    for device in (cisco3,):
        device["password"] = password
        net_connect = ConnectHandler(**device)

        cmd = "no username my_user"
        output = net_connect.config_mode()
        output += net_connect.send_command_timing(
            cmd, strip_prompt=False, strip_command=False
        )
        if "confirm" in output:
            output += net_connect.send_command_timing(
                "y", strip_prompt=False, strip_command=False
            )
        output += net_connect.exit_config_mode()
        output += net_connect.save_config()
        print(output)
        net_connect.disconnect()
```

### TB-169: `netmiko_course/class5/collateral/lab_devices.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass
```

### TB-170: `netmiko_course/class5/collateral/vlans.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
vlan 500
 name gold500
vlan 501
 name gold501
vlan 502
 name gold502
vlan 503
 name gold503
vlan 504
 name gold504
```

---

## Lab Track 15: Generating Network Reports

**Concept focus:** summarize interface status, VLAN counts, latency, and compliance.

**Mental model:** `raw command output -> parsed records -> aggregate -> report`

### TB-171: `netmiko_course/class3/exercises/show_vlan.ttp`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
<vars>
# Definition of port field regular expression
PORT = "\S+.*"
</vars>

<group>
{{ vlan_id | DIGIT }} {{ vlan_name }} {{ vlan_status }} {{ ports | re("PORT") }}
</group>
```

### TB-172: `netmiko_course/class3/collateral/show_genie.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass, pprint.pprint`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command("show ip int brief", use_genie=True)
    # output = net_connect.send_command("show ip arp", use_genie=True)
    pprint(output)
```

### TB-173: `netmiko_course/class3/collateral/show_ttp.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass, pprint.pprint`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)

output = net_connect.send_command(
    "show run", use_ttp=True, ttp_template="show_run_intf.ttp"
)
pprint(output)
net_connect.disconnect()
```

### TB-174: `netmiko_course/class3/exercises/exercise5.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass, pprint.pprint`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
output = net_connect.send_command(
    "show vlan", use_ttp=True, ttp_template="show_vlan.ttp"
)
net_connect.disconnect()

print()
print("VLAN Table:")
print("-" * 18)
pprint(output)
print()

# Strip outer lists
data = output[0][0]
for vlan_dict in data:
    if vlan_dict["vlan_id"] == "7":
        print()
        print(f"VLAN ID: {vlan_dict['vlan_id']}")
        print(f"VLAN name: {vlan_dict['vlan_name']}")
        print()
```

### TB-175: `netmiko_course/class3/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


cisco3 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

cisco4 = {
    "device_type": "cisco_xe",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (cisco3, cisco4):
    with ConnectHandler(**device) as net_connect:
        start_prompt = net_connect.find_prompt()
        net_connect.send_command_timing("disable")
        end_prompt = net_connect.find_prompt()
        print(f"\nStarting prompt: {start_prompt}")
        print(f"\nEnding prompt: {end_prompt}")
        print()
```

### TB-176: `netmiko_course/class3/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    "session_log": "traceroute.out",
}

command = "show tech-support"
ssh_conn = ConnectHandler(**device)

# Gather the entire output
start_time = datetime.now()
output = ssh_conn.send_command_timing(
    command, last_read=10, read_timeout=180, strip_prompt=False
)
end_time = datetime.now()
ssh_conn.disconnect()

print("\n\n")
print("-" * 80)
print(output)
print("-" * 80)
print("\n\n")
print(f"Exec time: {end_time - start_time}")
print("\n\n")
```

### TB-177: `netmiko_course/class3/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, pprint.pprint, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**arista1) as net_connect:
    show_vlan = net_connect.send_command("show vlan", use_textfsm=True)

    print()
    print("VLAN Table:")
    print("-" * 18)
    pprint(show_vlan)
    print()

    for vlan_dict in show_vlan:
        if vlan_dict["vlan_id"] == "7":
            print()
            print(f"VLAN ID: {vlan_dict['vlan_id']}")
            print(f"VLAN name: {vlan_dict['vlan_name']}")
            print()
```

### TB-178: `netmiko_course/class3/exercises/exercise4.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command("show lldp neighbors detail", use_genie=True)
    output = output["interfaces"]
    for intf_name, v in output.items():
        print()
        print(f"Local Intf: {intf_name}")
        print("-" * 12)
        neighbor_dict = v["port_id"][intf_name]["neighbors"]
        for neighbor_name, neighbor_data in neighbor_dict.items():
            remote_port = neighbor_data["port_description"]
            mgmt_ip = neighbor_data["management_address_v4"]
            print(f"Neighbor: {neighbor_name}")
            print(f"  Remote Port: {remote_port}")
            print(f"  MGMT IP: {mgmt_ip}")
            print("-" * 12)
```

### TB-179: `netmiko_course/class3/collateral/read_timeout_timing/traceroute_timeout.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    # "session_log": "traceroute.out",
}

command = "traceroute 8.8.8.8"

with ConnectHandler(**device) as ssh_conn:
    try:
        start_time = datetime.now()
        # output = ssh_conn.send_command_timing(command)
        output = ssh_conn.send_command_timing(command, last_read=5, read_timeout=15)
    finally:
        end_time = datetime.now()
        print()
        print("-" * 50)
        print(f"\n\nExecution time: {end_time - start_time}\n\n")
        print("-" * 50)
        print()
```

### TB-180: `netmiko_course/class3/collateral/read_timeout_timing/traceroute_working.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, datetime.datetime, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_xe",
    # "session_log": "traceroute.out",
}

command = "traceroute 10.220.88.28"

with ConnectHandler(**device) as ssh_conn:
    start_time = datetime.now()
    output = ssh_conn.send_command_timing(command)
    end_time = datetime.now()

    print()
    print("-" * 50)
    print(output)
    print(f"\n\nExecution time: {end_time - start_time}\n\n")
    print("-" * 50)
    print()
```

### TB-181: `netmiko_course/class3/collateral/show_genie_nxos.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass, pprint.pprint`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

with ConnectHandler(**my_device) as net_connect:
    output = net_connect.send_command("show version", use_genie=True)
    pprint(output)
```

### TB-182: `netmiko_course/class3/collateral/show_run_intf.ttp`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
interface {{ interface }}
 ip address {{ ip }} {{ mask }}
 description {{ description }}
```

### TB-183: `netmiko_course/class3/collateral/show_textfsm.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass, pprint.pprint`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)

output = net_connect.send_command("show ip int brief", use_textfsm=True)
pprint(output)
net_connect.disconnect()
```

### TB-184: `netmiko_course/class3/collateral/show_timing.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)

output = net_connect.send_command_timing("show ip int brief")
print(output)
net_connect.disconnect()
```

### TB-185: `python_course_mar26/class3/list_comprehenson/list_comp_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x**2 for x in my_list]
print(squares)

cubes = [x**3 for x in my_list]
print(cubes)

evens = [x for x in my_list if x % 2 == 0]
print(evens)

odds = [x for x in my_list if x % 2 == 1]
print(odds)

sentence = "This is a test sentence."
words = sentence.split()
print(words)

capital_words = [word.upper() for word in words]
print(capital_words)
```

---

## Lab Track 16: Inventories, YAML, JSON, and Real-World Data

**Concept focus:** load inventories and transform external data into device actions.

**Mental model:** `YAML/JSON/source of truth -> parse -> clean -> command plan`

### TB-186: `netmiko_course/class10/exercises/devices.yaml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
cisco3:
  device_type: cisco_xe
  hostname: cisco3.lasthop.io
cisco4:
  device_type: cisco_xe
  hostname: cisco4.lasthop.io
nxos1:
  device_type: cisco_nxos
  hostname: nxos1.lasthop.io
nxos2:
  device_type: cisco_nxos
  hostname: nxos2.lasthop.io
vmx1:
  device_type: juniper_junos
  hostname: vmx1.lasthop.io
vmx2:
  device_type: juniper_junos
  hostname: vmx2.lasthop.io
```

### TB-187: `netmiko_course/class10/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, yaml, getpass.getpass, netmiko.SSHDetect, concurrent.futures.ThreadPoolExecutor, concurrent.futures.as_completed`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. It defines reusable function(s): `find_device_type`.
4. It reads or writes files, which is how automation remembers inventory, commands, or reports.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import yaml
from getpass import getpass
from netmiko import SSHDetect
from concurrent.futures import ThreadPoolExecutor, as_completed


# Code so automated tests will run properly
PASSWORD = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


def find_device_type(hostname):

    base_device = {
        "device_type": "autodetect",
        "username": "pyclass",
        "password": PASSWORD,
    }

    device = base_device.copy()
    device["host"] = hostname
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    return (hostname, best_match)


if __name__ == "__main__":

    hosts_file = "my_hosts.txt"
    with open(hosts_file) as f:
        hosts = f.readlines()

    pool = ThreadPoolExecutor(20)
    future_list = []
    for hostname in hosts:
        hostname = hostname.strip()
        future = pool.submit(find_device_type, hostname)
        future_list.append(future)

    # Display the results
    my_devices = {}
    print()
    for future in as_completed(future_list):
        hostname, device_type = future.result()
        print(f"{hostname} -> {device_type}")
        name = hostname.split(".")[0]
        my_devices[name] = {}
        my_devices[name]["hostname"] = hostname
        my_devices[name]["device_type"] = device_type
    print()

    # Write external YAML file
    print("\nCreating devices.yaml file\n\n")
    with open(r"devices.yaml", "w") as f:
        yaml.dump(my_devices, f)
```

### TB-188: `netmiko_course/class10/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.SSHDetect, concurrent.futures.ThreadPoolExecutor, concurrent.futures.as_completed`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. It defines reusable function(s): `find_device_type`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import SSHDetect
from concurrent.futures import ThreadPoolExecutor, as_completed


# Code so automated tests will run properly
PASSWORD = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()


def find_device_type(hostname):

    base_device = {
        "device_type": "autodetect",
        "username": "pyclass",
        "password": PASSWORD,
    }

    device = base_device.copy()
    device["host"] = hostname
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    return (hostname, best_match)


if __name__ == "__main__":

    hosts = [
        "cisco3.lasthop.io",
        "cisco4.lasthop.io",
        "nxos1.lasthop.io",
        "nxos2.lasthop.io",
        "vmx1.lasthop.io",
        "vmx2.lasthop.io",
    ]

    pool = ThreadPoolExecutor(20)

    future_list = []
    for hostname in hosts:
        future = pool.submit(find_device_type, hostname)
        future_list.append(future)

    # Display the results
    print()
    print("{:20} {:20}".format("hostname", "device_type"))
    print("{:20} {:20}".format("--------", "-----------"))
    for future in as_completed(future_list):
        hostname, device_type = future.result()
        print(f"{hostname:20} {device_type:20}")
    print()
```

### TB-189: `netmiko_course/class10/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It defines reusable function(s): `read_device`.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
import time
from getpass import getpass
from netmiko import ConnectHandler


def read_device(net_connect, sleep=1):
    """Sleep and read channel."""
    time.sleep(sleep)
    output = net_connect.read_channel()
    print(output)
    return output


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_device = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "output.txt",
    }

    with ConnectHandler(**my_device) as net_connect:

        print()
        print(net_connect.find_prompt())

        cmd = "telnet 10.220.88.22\n"
        net_connect.write_channel(cmd)
        output = read_device(net_connect, sleep=1)

        if "sername" in output:
            net_connect.write_channel(my_device["username"] + "\n")
        output = read_device(net_connect, sleep=1)

        if "ssword" in output:
            net_connect.write_channel(password + "\n")
        read_device(net_connect, sleep=1)

        net_connect.write_channel("exit\n")
        read_device(net_connect, sleep=1)
        print()
```

### TB-190: `netmiko_course/class10/exercises/my_hosts.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
cisco3.lasthop.io
cisco4.lasthop.io
nxos1.lasthop.io
nxos2.lasthop.io
vmx1.lasthop.io
vmx2.lasthop.io 
```

### TB-191: `netmiko_course/class10/collateral/detect_platform.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.SSHDetect, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import SSHDetect, ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

base_device = {"device_type": "autodetect", "username": "pyclass", "password": password}

hosts = [
    "cisco3.lasthop.io",
    "nxos1.lasthop.io",
    "vmx1.lasthop.io",
    "arista1.lasthop.io",
]

for hostname in hosts:
    device = base_device.copy()
    device["host"] = hostname
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    # Name of the best device_type to use further
    print(best_match)

# Connect to the very last device
device["device_type"] = best_match
with ConnectHandler(**device) as connection:
    print()
    print("Full SSH Connection:")
    print(connection.find_prompt())
```

### TB-192: `netmiko_course/class10/collateral/snmp_detect.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.snmp_autodetect.SNMPDetect`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko.snmp_autodetect import SNMPDetect

snmp_key = os.getenv("SNMP_COMMUNITY")
if not snmp_key:
    snmp_key = getpass("Enter SNMP community: ")

# Had to change from a hostname to an IP address due to a Netmiko bug
# in the SNMP autodetect code.
my_snmp = SNMPDetect(
    "184.105.247.70",
    snmp_version="v3",
    user="pysnmp",
    auth_key=snmp_key,
    encrypt_key=snmp_key,
    auth_proto="sha",
    encrypt_proto="aes128",
)

device_type = my_snmp.autodetect()
print(f"\n{device_type}\n")
```

### TB-193: `netmiko_course/class10/collateral/telnet_example.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco1 = {
    "device_type": "cisco_ios_telnet",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**cisco1)
print(net_connect.find_prompt())
net_connect.disconnect()
```

### TB-194: `netmiko_course/class10/collateral/write_read.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
import time
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "output.txt",
}

with ConnectHandler(**my_device) as net_connect:

    # Send command down the channel - don't forget the enter!
    net_connect.write_channel("show ip int brief\n")

    # You probably can't read right away - your Python program is faster than the device (so sleep)
    time.sleep(1)
    output = net_connect.read_channel()
    print(output)
    print()

    print("-" * 20)
    print()

    # You can do multiple interactions
    net_connect.write_channel("config term\n")
    time.sleep(1)
    output = net_connect.read_channel()
    net_connect.write_channel("end\n")
    time.sleep(1)
    output += net_connect.read_channel()
    print(output)
```

### TB-195: `python_course_mar26/class1/exercises/dict_ex/net_object_net128.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "uid": "6796b2f5-d449-44dc-9cf8-75b33c4ca493",
    "name": "hq_net_128",
    "type": "network",
    "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
    },
    "subnet4": "172.31.128.0",
    "mask-length4": 24,
    "subnet-mask": "255.255.255.0",
    "icon": "NetworkObjects/network",
    "color": "light green"
}
```

### TB-196: `python_course_mar26/class1/exercises/file_ex/network_objects.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "objects": [
        {
            "uid": "eff32e1a-d4ed-4df9-a6e6-398c5d88b34d",
            "name": "CP_default_Office_Mode_addresses_pool",
            "type": "network",
            "domain": {
                "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                "name": "SMC User",
                "domain-type": "domain"
            },
            "subnet4": "172.16.10.0",
            "mask-length4": 24,
            "subnet-mask": "255.255.255.0",
            "icon": "NetworkObjects/network",
            "color": "black"
        },
        {
            "uid": "6796b2f5-d449-44dc-9cf8-75b33c4ca493",
            "name": "hq_net_128",
            "type": "network",
            "domain": {
                "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                "name": "SMC User",
                "domain-type": "domain"
            },
            "subnet4": "172.31.128.0",
            "mask-length4": 24,
            "subnet-mask": "255.255.255.0",
            "icon": "NetworkObjects/network",
            "color": "light green"
        },
        {
            "uid": "caee1116-8087-4310-9208-b422d3628a7e",
            "name": "IPv6_Link_Local_Hosts",
            "type": "network",
            "domain": {
                "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                "name": "Check Point Data",
                "domain-type": "data domain"
            },
            "subnet6": "fe80::",
            "mask-length6": 64,
            "icon": "NetworkObjects/network",
            "color": "black"
        }
    ],
    "from": 1,
    "to": 3,
    "total": 3
}
```

### TB-197: `python_course_mar26/class2/exercises/complex_ds_ex/show_tasks.json`

**Lab type:** Data lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```json
{
    "tasks": [
        {
            "task-id": "d1313671-7c40-4c95-be76-a2ac451705e7",
            "task-name": "chkpnt-pod99 - is_ve-CMD",
            "status": "succeeded",
            "progress-percentage": 100,
            "suppressed": true,
            "comments": "Completed",
            "meta-info": {
                "lock": "unlocked",
                "validation-state": "ok",
                "last-modify-time": {
                    "posix": 1769728500793,
                    "iso-8601": "2026-01-30T00:15+0100"
                },
                "last-modifier": "WEB_API",
                "creation-time": {
                    "posix": 1769728500373,
                    "iso-8601": "2026-01-30T00:15+0100"
                },
                "creator": "WEB_API"
            }
        },
        {
            "task-id": "37b26077-b9bb-40c7-a522-45ad0bee23c3",
            "task-name": "Getting information for this software package: all",
            "status": "succeeded",
            "progress-percentage": 100,
            "suppressed": true,
            "comments": "",
            "meta-info": {
                "lock": "unlocked",
                "validation-state": "ok",
                "last-modify-time": {
                    "posix": 1771002543999,
                    "iso-8601": "2026-02-13T18:09+0100"
                },
                "last-modifier": "admin",
                "creation-time": {
                    "posix": 1771002542681,
                    "iso-8601": "2026-02-13T18:09+0100"
                },
                "creator": "admin"
            }
        },
        {
            "task-id": "ffb1b55b-1436-40e1-9076-83ebe54b5c68",
            "task-name": "Trusted CA's update",
            "status": "succeeded",
            "progress-percentage": 100,
            "suppressed": false,
            "comments": "Trusted CA's Package has been updated. Please install policy for the changes to take effect",
            "meta-info": {
                "lock": "unlocked",
                "validation-state": "ok",
                "last-modify-time": {
                    "posix": 1769648413434,
                    "iso-8601": "2026-01-29T02:00+0100"
                },
                "last-modifier": "System",
                "creation-time": {
                    "posix": 1769648405040,
                    "iso-8601": "2026-01-29T02:00+0100"
                },
                "creator": "System"
            }
        }
    ],
    "from": 1,
    "to": 3,
    "total": 3
}
```

### TB-198: `python_course_mar26/class2/exercises/complex_ds_ex/complex_ds_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json, rich.print, ipdb`.
2. It defines reusable function(s): `read_json, extract_fields`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json
from rich import print
import ipdb  # noqa


def read_json(filename):
    data = None
    with open(filename) as f:
        data = json.load(f)

    return data


def extract_fields(task):
    task_id = task["task-id"]
    status = task["status"]
    lock = task["meta-info"]["lock"]

    return (task_id, status, lock)


if __name__ == "__main__":
    filename = "show_tasks.json"
    tasks_ds = read_json(filename)

    # Remove outermost key
    tasks = tasks_ds["tasks"]

    print()
    for task in tasks:
        task_id, status, lock = extract_fields(task)
        print(f"{task_id} --> {status} {lock=}")
    print()
```

### TB-199: `python_course_mar26/class1/exercises/list_ex/list_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `yaml, rich.print`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
import yaml
from rich import print

filename = "locations.yml"

# Read in file as YAML
with open(filename) as f:
    locations = yaml.safe_load(f)

print()

# Print the list
print(locations)

# Print first element of list
print(f"First element: {locations[0]}")

# Print last element of list
print(f"Last element: {locations[-1]}")

# Print length of the list
print(f"List length: {len(locations)}")

# Add element to the list
locations.append("Leipzig")

# Change the fourth element of the list to be 'Stuttgart'
locations[3] = "Stuttgart"

# Print the current list
print(locations)

# Use list concatentation to add the following list ["Dortmund", "Essen"]
# Could also do: locations += ["Dortmund", "Essen"]
locations = locations + ["Dortmund", "Essen"]

# Print the current list
print(locations)

# Pop the first element of the list into a variable
city1 = locations.pop(0)

# Pop the last element of the list into a variable
city_n = locations.pop()

# Print 'city1', 'city_n', and current 'locations' list
print(f"{city1=}")
print(f"{city_n=}")
print(f"{locations=}")
```

### TB-200: `python_course_mar26/class2/exercises/complex_ds_ex/complex_ds_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `json, rich.print, ipdb`.
2. It reads or writes files, which is how automation remembers inventory, commands, or reports.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import json
from rich import print
import ipdb  # noqa

with open("show_tasks.json") as f:
    tasks_ds = json.load(f)

ipdb.set_trace()
print(tasks_ds)
print(type(tasks_ds))
print(tasks_ds.keys())

# Remove outermost key
tasks = tasks_ds["tasks"]
ipdb.set_trace()
print(type(tasks))
print(len(tasks))

ipdb.set_trace()
for task in tasks:
    task_id = task["task-id"]
    status = task["status"]
    print(f"{task_id} --> {status}")
```

### TB-201: `python_course_mar26/class1/exercises/list_ex/list_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### List Exercise1

1. Read in the file "locations.yml" as YAML (this should return a list). Use 'yaml.safe_load(f)' to do this.
2. Print out this list.
3. Print first element of the list.
4. Print last element of the list.
5. Print length of the list.
6. Append "Leipzig" to the end of the list.
7. Change the fourth element of the list to be 'Stuttgart'.
8. Print out the current list.
9. Use list concatentation to add the following list: ["Dortmund", "Essen"]
10. Print out the current list.
11. Pop the first element of the list into a variable named 'city1'.
12. Pop the last element of the list into a variable named 'city_n'.
13. Print out 'city1', 'city_n', and current 'locations' list.
```

### TB-202: `python_course_mar26/class2/exercises/complex_ds_ex/complex_ds_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Complex Data Structures Exercise1

Read "show_tasks.json" as JSON and save this data as a variable named 'tasks_ds'.

Use ipdb and ipdb.set_trace() and print 'tasks_ds', print 'type(tasks_ds)', and print 'tasks_ds.keys()'.

Next drill into the 'tasks_ds' data structure one-level and retrieve the "tasks" key; save this as a new variable named 'tasks'. In other words: tasks = tasks_ds["tasks"].

As this point the 'tasks' variable should be a list. Verify this by using 'type(tasks)' and 'len(tasks)'.

Use a for-loop to loop over the 'tasks'. Each entry in the 'tasks' list will be a task-dictionary. From this inner dictionary retrieve the "task-id" and "status" fields.

Your loop code should look similar to the following:

'''python
for task in tasks:
    task_id = task["task-id"]
    status = task["status"]
    print(f"{task_id} --> {status}")
'''
```

---

## Lab Track 17: Network APIs

**Concept focus:** authenticate, request network data, paginate, and process API responses.

**Mental model:** `API endpoint -> request/session -> JSON dicts -> object/config action`

### TB-203: `python_course_mar26/class4/sdk_api_query/sdk_api_query.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=True, context="web_api"
    )
    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        api_endpoint = "show-services-tcp"
        api_res = api_client.api_call(api_endpoint)

        tcp_services = api_res.data["objects"]
        print(len(tcp_services))

        tcp_services_total = api_res.data["total"]
        tcp_services_from = api_res.data["from"]
        tcp_services_to = api_res.data["to"]

        print(f"{tcp_services_total=}")
        print(f"{tcp_services_from=}")
        print(f"{tcp_services_to=}")

        api_res = api_client.api_query(api_endpoint, details_level="standard")
        ipdb.set_trace()
        # print(api_res)

        # No more "objects" / "total" / "from" / "to" keys--just a list.
        tcp_services = api_res.data
        print(f"\nServices returned: {len(tcp_services)}\n")


if __name__ == "__main__":
    main()
```

### TB-204: `python_course_mar26/class4/exercises/api_pages_ex/api_pages_ex.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=True, context="web_api"
    )
    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        udp_services = []
        offset = 0
        while True:
            api_endpoint = "show-services-udp"
            payload = {"offset": offset}
            api_res = api_client.api_call(api_endpoint, payload)

            udp_services = udp_services + api_res.data["objects"]

            udp_services_from = api_res.data["from"]
            udp_services_to = api_res.data["to"]
            udp_services_total = api_res.data["total"]
            print(f"{udp_services_from=}")
            print(f"{udp_services_to=}")
            print(f"{udp_services_total=}")

            offset = udp_services_to
            # Keep retrieving data until all have been retrieved
            if len(udp_services) >= udp_services_total:
                break

        print(len(udp_services))
        # print(udp_services)


if __name__ == "__main__":
    main()
```

### TB-205: `python_course_mar26/class4/exercises/main_project/03_mgmt_api_cfg.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `cfg_std_mgmt_hosts, cfg_blocked_ips, main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print  # noqa
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from chkpt_object_funcs import cfg_host_objects, cfg_group_object, delete_host_objects
from blocked_ip_funcs import (
    read_blocked_ips_file,
    gen_host_object,
    get_current_blocked_ips,
)
from chkpt_policy_funcs import cfg_fw_rules, install_fw_policy, extract_fw_name
from host_objects import smart_console_private, smart_console_public, ansible_server
from gen_fw_rules import gen_blockedip_fw_rules, gen_mgmt_fw_rules

DEBUG = False


def cfg_std_mgmt_hosts(api_client):
    print("[green][Mgmt API Config][/green] Configure Management Hosts")
    mgmt_host_objects = [smart_console_private, smart_console_public, ansible_server]
    cfg_host_objects(api_client, host_objects=mgmt_host_objects)


def cfg_blocked_ips(api_client):
    """
    Configure 'Blocked IPs' from blocked_ips.txt file.

    Add new blocked IP host objects
    Upgraded 'Blocked IPs' group membership
    Remove obsolete blocked IP host objects
    """

    group_name = "Blocked IPs"
    current_blocked_ips = get_current_blocked_ips(api_client, group_name)
    new_blocked_ips = read_blocked_ips_file()

    # Compare new versus currently configured blocked IPs
    if set(current_blocked_ips) == set(new_blocked_ips):
        # Nothing to do, current and new already match.
        print("[green][Mgmt API Config][/green] No Blocked IP Changes")
        return
    else:
        add_blocked_ips = set(new_blocked_ips) - set(current_blocked_ips)
        remove_blocked_ips = set(current_blocked_ips) - set(new_blocked_ips)
        if DEBUG:
            print(f"{add_blocked_ips=}")
            print(f"{remove_blocked_ips=}")

    # Convert to host object dict using list comprehension
    blocked_ip_objs = [gen_host_object(ip) for ip in add_blocked_ips]
    delete_ip_objs = [gen_host_object(ip) for ip in remove_blocked_ips]

    # Configure host objects for blocked IPs
    print("[green][Mgmt API Config][/green] Configure Blocked IP Host Objects")
    cfg_host_objects(api_client, blocked_ip_objs)

    # Update group membership
    blocked_ip_group = {
        "name": "Blocked IPs",
        "members": new_blocked_ips,
    }
    print("[green][Mgmt API Config][/green] Configure Blocked IPs Group")
    cfg_group_object(api_client, blocked_ip_group)

    # Remove unused host objects (must come after group membership update)
    print("[green][Mgmt API Config][/green] Remove Old Blocked IP Host Objects")
    delete_host_objects(api_client, delete_ip_objs)


def main():
    host = "chkpnt-pod99.lasthop.io"
    fw_name = extract_fw_name(host)

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_std_mgmt_hosts(api_client)
        cfg_blocked_ips(api_client)

        fw_rules = gen_mgmt_fw_rules(fw_name)
        fw_rules = gen_blockedip_fw_rules() + fw_rules
        print("[green][Mgmt API Config][/green] Configure Firewall Rules")
        cfg_fw_rules(api_client, fw_rules=fw_rules)

        print("[green][Mgmt API Config][/green] Publish")
        api_client.api_call(command="publish")
        # install_fw_policy(api_client, targets=fw_name)


if __name__ == "__main__":
    main()
```

### TB-206: `python_course_mar26/class4/exercises/api_pages_ex/api_query_ex.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=True, context="web_api"
    )
    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        api_endpoint = "show-services-udp"
        api_res = api_client.api_query(api_endpoint, details_level="standard")

        # No more "objects" / "total" / "from" / "to" keys--just a list.
        # Retrieve all 96 services using api_query
        udp_services = api_res.data
        print(f"\nServices returned: {len(udp_services)}\n")


if __name__ == "__main__":
    main()
```

### TB-207: `python_course_mar26/class4/sdk_api_query/sdk_gen_api_query.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=True, context="web_api"
    )
    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        api_endpoint = "show-services-tcp"
        query = api_client.gen_api_query(api_endpoint, details_level="standard")

        # Retrieve pages of data
        for chunk in query:
            ipdb.set_trace()
            # print(chunk)

            tcp_services = chunk.data["objects"]
            print(len(tcp_services))

            # tcp_services_total = api_res.data["total"]
            # tcp_services_from = api_res.data["from"]
            # tcp_services_to = api_res.data["to"]

            # print(f"{tcp_services_total=}")
            # print(f"{tcp_services_from=}")
            # print(f"{tcp_services_to=}")


if __name__ == "__main__":
    main()
```

### TB-208: `python_course_mar26/class2/exercises/gaia_api_ex/gaia_auth_ex.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Gaia API Auth Exercise

Create a Python script that authenticates to the Gaia API in your pod.

After you have authenticated extract the session ID and reuse this session ID to execute the following API command: "show-api-versions"

Print the returned JSON from that API command to standard output.

Bonus: Do the above, but create the following functions to assist you: 'login', 'api_call', 'logout'.

The 'login' function should handle the login and return the response (or alternatively return the session ID).

The 'api_call' function should handle API calls to the Gaia API and return the response. My reference function signature looks as follows:

'''python
def api_call(base_url, endpoint, headers, payload=None, ssl_verify=False):
'''

The 'logout' function should gracefully log you out of the Gaia API.
```

### TB-209: `python_course_mar26/class3/exercises/chkpnt_sdk_ex/group_net_objects_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, ipdb`.
2. It defines class blueprint(s): `ChkPntConfigError`.
3. It defines reusable function(s): `cfg_group_objects, main`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


def cfg_group_objects(api_client):
    """Use mgmt API to configure network object group."""

    group_params = {
        "name": "hq_net",
        "members": [
            "hq_net_128",
            "hq_net_129",
            "hq_net_130",
            "hq_net_131",
            "hq_net_132",
            "hq_net_133",
            "hq_net_134",
            "hq_net_135",
        ],
        "color": "blue",
    }

    for params in (group_params,):
        # ipdb.set_trace()
        # Check if object already exists
        obj_exists = False
        payload = {"name": params["name"]}
        api_res = api_client.api_call(command="show-group", payload=payload)

        if api_res.success:
            obj_exists = True
        if obj_exists:
            # object already exists, update parameters
            print(f"Updating object: {params}")
            api_res = api_client.api_call(command="set-group", payload=params)
        else:
            print(f"Configuring object: {params}")
            api_res = api_client.api_call(command="add-group", payload=params)

        if not api_res.success:
            msg = f"Failed to configure object: {params}"
            raise ChkPntConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_group_objects(api_client)
        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
```

### TB-210: `python_course_mar26/class3/exercises/chkpnt_sdk_ex/mgmt_cfg_hostobj_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, ipdb`.
2. It defines class blueprint(s): `ChkPntConfigError`.
3. It defines reusable function(s): `cfg_host_objects, main`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb # noqa

class ChkPntConfigError(Exception):
    pass

def cfg_host_objects(api_client):
    """Use mgmt API to configure Ansible and SmartConsole host objects."""
    smart_console_private = {
        "name": "Windows SmartConsole",
        "ipv4-address": "172.31.12.101",
        "color": "red",
    }
    smart_console_public = {
        "name": "Windows SmartConsole Public",
        "ipv4-address": "3.71.9.240",
        "color": "red",
    }
    ansible_server = {
        "name": "Ansible Server",
        "ipv4-address": "3.125.34.232",
        "color": "black",
    }
    for host_params in (smart_console_private, smart_console_public, ansible_server):

        # Check if host already exists
        # ipdb.set_trace()
        host_exists = False
        host_name = host_params["name"]
        payload = {"name": host_name}
        api_res = api_client.api_call(command="show-host", payload=payload)

        if api_res.success:
            host_exists = True
        if host_exists:
            # Host already exists, update parameters
            print(f"Updating host object: {host_params}")
            api_res = api_client.api_call(command="set-host", payload=host_params)
        else:
            print(f"Configuring host object: {host_params}")
            api_res = api_client.api_call(command="add-host", payload=host_params)

        if not api_res.success:
            msg = f"Failed to configure host object: {host_params}"
            raise ChkPntConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_host_objects(api_client)
        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
```

### TB-211: `python_course_mar26/class3/exercises/chkpnt_sdk_ex/mgmt_cfg_netobj_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, ipdb`.
2. It defines class blueprint(s): `ChkPntConfigError`.
3. It defines reusable function(s): `cfg_net_objects, main`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


def cfg_net_objects(api_client):
    """Use mgmt API to configure network objects."""
    hq_net_128 = {
        "name": "hq_net_128",
        "subnet": "172.31.128.0",
    }
    hq_net_129 = {
        "name": "hq_net_129",
        "subnet": "172.31.129.0",
    }
    hq_net_130 = {
        "name": "hq_net_130",
        "subnet": "172.31.130.0",
    }
    hq_net_131 = {
        "name": "hq_net_131",
        "subnet": "172.31.131.0",
    }
    hq_net_132 = {
        "name": "hq_net_132",
        "subnet": "172.31.132.0",
    }
    hq_net_133 = {
        "name": "hq_net_133",
        "subnet": "172.31.133.0",
    }
    hq_net_134 = {
        "name": "hq_net_134",
        "subnet": "172.31.134.0",
    }
    hq_net_135 = {
        "name": "hq_net_135",
        "subnet": "172.31.135.0",
    }

    for params in (
        hq_net_128,
        hq_net_129,
        hq_net_130,
        hq_net_131,
        hq_net_132,
        hq_net_133,
        hq_net_134,
        hq_net_135,
    ):
        # Set common params
        params["mask-length"] = 24
        params["color"] = "green"

        # ipdb.set_trace()
        # Check if object already exists
        obj_exists = False
        payload = {"name": params["name"]}
        api_res = api_client.api_call(command="show-network", payload=payload)

        if api_res.success:
            obj_exists = True
        if obj_exists:
            # object already exists, update parameters
            print(f"Updating object: {params}")
            api_res = api_client.api_call(command="set-network", payload=params)
        else:
            print(f"Configuring object: {params}")
            api_res = api_client.api_call(command="add-network", payload=params)

        if not api_res.success:
            msg = f"Failed to configure object: {params}"
            raise ChkPntConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_net_objects(api_client)
        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
```

### TB-212: `python_course_mar26/class2/exercises/gaia_api_ex/gaia_auth_ex.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, json, rich.print, dotenv.load_dotenv, ipdb`.
2. It defines reusable function(s): `login, api_call, logout`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


def login(base_url, user, password, ssl_verify=False):

    url = base_url + "login"
    headers = {"Content-Type": "application/json"}
    login_payload = {"user": user, "password": password}

    response = requests.post(
        url, data=json.dumps(login_payload), headers=headers, verify=ssl_verify
    )
    return response


def api_call(base_url, endpoint, headers, payload=None, ssl_verify=False):

    if payload is None:
        payload = {}
    url = base_url + endpoint
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(base_url, headers, ssl_verify=False):

    # Call 'logout'
    endpoint = "logout"
    response = api_call(base_url, endpoint, headers, ssl_verify=ssl_verify)
    # If successful, remove the session ID from the headers
    if response.status_code == 200:
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")

    return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    base_url = f"https://{host}/gaia_api/v{api_version}/"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    response = login(base_url, user, admin_pass)
    resp_struct = response.json()
    session_id = resp_struct["sid"]

    headers = {"Content-Type": "application/json"}
    headers["X-chkp-sid"] = session_id

    endpoint = "show-api-versions"
    response = api_call(base_url, endpoint, headers)
    print(response.json())

    logout(base_url, headers)
```

### TB-213: `python_course_mar26/class3/chkpnt_sdk/api_notes.txt`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
    
    def __init__(self, api_client_args=None):
        self.server = api_client_args.server
        # web-api versus gaia-api
        self.context = api_client_args.context 
        self.api_version = api_client_args.api_version
        self.unsafe = api_client_args.unsafe
        self.fingerprint = api_client_args.fingerprint
        self.sid = api_client_args.sid

    # Context manager
    def __enter__(self):
    def __exit__(self, exc_type, exc_value, traceback):

    # Toggle to unsafe=False and will prompt you for fingerprint the first time.
    # Verification is hard
    def get_server_fingerprint(self):
    def check_fingerprint(self):
    def save_fingerprint_to_file(server, fingerprint, filename="fingerprints.txt"):
    def read_fingerprint_from_file(server, filename="fingerprints.txt"):

    def login(self, username, password, continue_last_session=False, domain=None, read_only=False,
    def login_with_api_key(self, api_key, continue_last_session=False, domain=None, read_only=False, payload=None):
    def login_as_root(self, domain=None, payload=None):

### Main API Call ###
    def api_call(self, command, payload=None, sid=None, wait_for_task=True, timeout=-1, method="POST"):

### API Call when pagination / multiple api calls are required
    def api_query(self, command, details_level="standard", container_key="objects", include_container_key=False,

    def check_tasks_status(task_result):
    def ask_yes_no_question(question):

    def close_connection(self):
```

### TB-214: `python_course_mar26/class3/exercises/mgmt_api_ex/mgmt_api_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Mgmt API Exercise

Reusing the code you created for the Gaia API authentication exercise (with slight modifications of the base_url), connect and authentication to the Mgmt API of your pod.

After authenticating connect to the "show-gateway-capabilities" endpoint and retrieve the JSON payload from this reponse.

From the returned data structure extract and print out the Supported OS Versions and also extract and print out the LightSpeed supported hardware.

Your output should look similar to the following:

'''bash
$ python mgmt_api_ex1.py 

R81 Supported OS Versions: 
--------------------
['R81', 'R81.10', 'R81.20']


LightSpeed Supported Hardware: 
--------------------
[
    'QLS250 Quantum LightSpeed',
    'QLS450 Quantum LightSpeed',
    'QLS650 Quantum LightSpeed',
    'QLS800 Quantum LightSpeed',
    'MLS200 Maestro LightSpeed',
    'MLS400 Maestro LightSpeed'
]

'''
```

### TB-215: `python_course_mar26/class3/exercises/mgmt_api_ex/mgmt_api_ex1.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, mgmt_funcs.login, mgmt_funcs.api_call, mgmt_funcs.logout`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from mgmt_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"
    endpoint = "login"
    base_url = f"https://{host}/web_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    # Login
    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    headers["X-chkp-sid"] = session_id

    endpoint = "show-gateway-capabilities"
    url = base_url + endpoint
    res = api_call(url, headers)
    capabilities = res.json()

    supported_os_versions = capabilities["supported-versions"]["versions"]
    r81_supported_versions = []
    for os_version in supported_os_versions:
        if "R81" in os_version:
            r81_supported_versions.append(os_version)

    supported_hw = capabilities["supported-hardware"]["hardware"]
    supported_hw_lightspeed = []
    for hardware in supported_hw:
        if "lightspeed" in hardware.lower():
            supported_hw_lightspeed.append(hardware)

    print("\nR81 Supported OS Versions: ")
    print("-" * 20)
    print(r81_supported_versions)
    print()

    print("\nLightSpeed Supported Hardware: ")
    print("-" * 20)
    print(supported_hw_lightspeed)
    print()

    # Logout
    url = base_url + "logout"
    headers = logout(url, headers)
```

### TB-216: `python_course_mar26/class3/exercises/mgmt_api_ex/mgmt_funcs.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, json`.
2. It defines class blueprint(s): `MgmtAuthError, MgmtLogoutError`.
3. It defines reusable function(s): `login, api_call, logout`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import requests
import json


class MgmtAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class MgmtLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


def login(url, username, password):
    """Login and return the session_id."""
    headers = {"Content-Type": "application/json"}
    ssl_verify = False
    login_payload = {"user": username, "password": password}

    response = requests.post(
        url,
        data=json.dumps(login_payload),
        headers=headers,
        verify=ssl_verify,
    )
    resp_struct = response.json()
    return resp_struct["sid"]


def api_call(url, headers, payload=None, ssl_verify=False):
    if payload is None:
        payload = {}
    if "X-chkp-sid" not in headers:
        msg = """
Session ID not set, please call '.login()' method and properly
authenticate to the API.
"""
        raise MgmtAuthError(msg)

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(url, headers):
    """Removes 'X-chkp-sid' from headers and returns headers dict."""
    res = api_call(url, headers)
    if res.status_code == 200:
        msg = res.json()["message"]
    if res.status_code == 200 and msg == "OK":
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")
            return headers
    else:
        msg = "Failed to 'logout' from Mgmt API"
        raise MgmtLogoutError(msg)
```

### TB-217: `python_course_mar26/class4/exercises/api_pages_ex/api_pagination.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Pagination exercise

Using a standard SDK api_call, query "show-services-udp" use the "total", "to", and "from" fields and
the payload "offset" field to paginate through the results using api_call.

Verify that you correctly received all 96 of the UDP services.

Create a second Python script that uses "api_query" to automatically retrieve all of the objects and to handle any required pagination.

Verify "api_query" successfully retrieved all 96 of the UDP services.
```

### TB-218: `python_course_mar26/class3/chkpnt_sdk/gaia_intf.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#
# show physical interface.py
# version 1.0
#
# The purpose of this script is to show a server's physical interfaces
#
# written by: Check Point software technologies inc.
# April 2019
# modified by: Kirk Byers (Feb 2026)

import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    api_server = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=True, context="gaia_api"
    )

    with APIClient(client_args) as client:
        login_res = client.login(username, password)
        if login_res.success is False:
            print(f"Login failed: {login_res.error_message}")
            exit(1)

        interface_name = input("Enter interface name: ")
        api_endpoint = "show-physical-interface"
        api_args = {"name": interface_name}
        print(api_args)
        api_res = client.api_call(api_endpoint, api_args)
        if api_res.success:
            intf_name = api_res.data["name"]
            ip_addr = (api_res.data["ipv4-address"],)
            mtu = (api_res.data["mtu"],)
            resp = f"""
Physical interface name is '{intf_name}' , ipv4 address is '{ip_addr}', 
interface mtu is '{mtu}' 
"""
            print(resp)
        else:
            print(f"Failed to get physical interface data '{api_res.data}'")


if __name__ == "__main__":
    main()
```

### TB-219: `python_course_mar26/class3/chkpnt_sdk/gaia_intf_fingerprint.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#
# show physical interface.py
# version 1.0
#
# The purpose of this script is to show a server's physical interfaces
#
# written by: Check Point software technologies inc.
# April 2019
# modified by: Kirk Byers (Feb 2026)

import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    api_server = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=False, context="gaia_api", fingerprint="4B:80:47:51:7E:36:78:93:0A:0D:76:98:91:6F:6C:2A"
    )

    with APIClient(client_args) as client:
        login_res = client.login(username, password)
        if login_res.success is False:
            print(f"Login failed: {login_res.error_message}")
            exit(1)

        interface_name = input("Enter interface name: ")
        api_endpoint = "show-physical-interface"
        api_args = {"name": interface_name}
        print(api_args)
        api_res = client.api_call(api_endpoint, api_args)
        if api_res.success:
            intf_name = api_res.data["name"]
            ip_addr = (api_res.data["ipv4-address"],)
            mtu = (api_res.data["mtu"],)
            resp = f"""
Physical interface name is '{intf_name}' , ipv4 address is '{ip_addr}', 
interface mtu is '{mtu}' 
"""
            print(resp)
        else:
            print(f"Failed to get physical interface data '{api_res.data}'")


if __name__ == "__main__":
    main()
```

### TB-220: `python_course_mar26/class3/chkpnt_sdk/mgmt_cfg_netobj.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # DNS
        payload = {
            "name": "hq_net_128",
            "subnet": "172.31.128.0",
            "mask-length": 24,
            "color": "green",
        }
        api_res = api_client.api_call(command="add-network", payload=payload)
        print(api_res)
        api_res = api_client.api_call(command="publish")
        print(api_res)
        api_res = api_client.api_call(command="show-networks")
        print(api_res)


if __name__ == "__main__":
    main()
```

### TB-221: `python_course_mar26/class2/api/gaia_auth.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, json, rich.print, dotenv.load_dotenv, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb # noqa

if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    base_url = f"https://{host}/gaia_api/v{api_version}/"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = f"{base_url}{endpoint}"
    headers = {"Content-Type": "application/json"}
    login_payload = {"user": user, "password": admin_pass}
    ssl_verify = False

    # CheckPoint uses POST even for information retrieval operations
    response = requests.post(
        url, data=json.dumps(login_payload), headers=headers, verify=ssl_verify
    )

    print(f"\n{base_url}\n")

    print(response)
    print(response.status_code)
    resp_struct = response.json()
    session_id = resp_struct["sid"]
    print(session_id)

    headers["X-chkp-sid"] = session_id
    print(headers)

    #endpoint = "show-version"
    endpoint = "show-api-versions"
    url = f"{base_url}{endpoint}"
    payload = {}

    print(url)
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    print(response.json())
    ipdb.set_trace()

    endpoint = "logout"
    url = f"{base_url}{endpoint}"
    payload = {}

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    print(response)
```

### TB-222: `python_course_mar26/class3/exercises/class_api_ex/chkpt_api_ex.md`

**Lab type:** Reading and design lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Check Point Class Exercise

Create a class named 'ChkptAPI'.

The class should only have one method (dunder-init).

The dunder-init method should have the following signature:

'''python
    def __init__(
        self,
        host,
        username,
        password,
        mode="web_api",
        api_version=None,
        ssl_verify=False,
    ):
'''

The 'mode' variable can either be 'web_api' or 'gaia_api'.

Inside your dunder-init method, initialize the following attribites: self.host, self.username, self.password, and self.ssl_verify.

Your dunder-init method should also set the following:

'''python
self.headers = {"Content-Type": "application/json"}
'''

Your dunder-init method should also create a 'base_url' attribute (self.base_url) and base_url should be constructed using the 'mode' variable (i.e. 'web_api' or 'gaia_api' and should also properly specify the API version.

If 'web_api', then api_version should be '2'. If 'gaia_api', then api_version should be '1.8'.

The base_url should be the proper url to use with the Gaia API or Mgmt API.

You should test your class using the following two test cases.

Test case1 (gaia_api):

'''python
host = "chkpnt-pod99.lasthop.io"
user = "admin"
admin_pass = "testpass"

api_client = ChkptAPI(
    host=host, username=user, password=admin_pass, mode="gaia_api"
)
print("Testing ChkptAPI Class (Gaia API)")
print(api_client.base_url)
print()
'''

Test case2 (web_api):

'''python
host = "chkpnt-pod99.lasthop.io"
user = "admin"
admin_pass = "testpass"

api_client = ChkptAPI(
    host=host, username=user, password=admin_pass, mode="web_api"
)
print("Testing ChkptAPI Class (Mgmt API)")
print(api_client.base_url)
print()
'''

Executing your test code should produce results similar to the following:

'''bash
$ python chkpt_api_ex.py 
Testing ChkptAPI Class (Gaia API)
https://chkpnt-pod99.lasthop.io/gaia_api/v1.8/

Testing ChkptAPI Class (Mgmt API)
https://chkpnt-pod99.lasthop.io/web_api/v2/
'''

You should verify that your 'base_url' is correct.
```

### TB-223: `python_course_mar26/work/clear_sessions.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, ipdb`.
2. It defines class blueprint(s): `chkp_exception`.
3. It defines reusable function(s): `cfg_host_object, cfg_fw_rule, main`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


class chkp_exception(Exception):
    pass


def cfg_host_object(api_client, host_object):

    payload = {"name": host_object["name"]}
    api_res = api_client.api_call(command="show-host", payload=payload)

    payload = host_object
    if api_res.success:
        api_res = api_client.api_call(command="set-host", payload=payload)

    else:
        api_res = api_client.api_call(command="add-host", payload=payload)

    if not api_res.success:
        msg = api_res.error_message
        raise chkp_exception(f"Error creating/updating host object: {msg}")

    return api_res


def cfg_fw_rule(api_client, corp_fw_rule):

    payload = {"name": corp_fw_rule["name"], "layer": corp_fw_rule["layer"]}
    api_res = api_client.api_call(command="show-access-rule", payload=payload)

    payload = corp_fw_rule
    if api_res.success:
        api_res = api_client.api_call(command="set-access-rule", payload=payload)
    else:
        api_res = api_client.api_call(command="add-access-rule", payload=payload)

    if not api_res.success:
        msg = api_res.error_message
        raise chkp_exception(f"Error creating/updating access rule: {msg}")

    return api_res


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        payload = {"details-level": "full"}
        response = api_client.api_call(command="show-sessions", payload=payload)
        sessions = response.data
        print(f"Number of sessions with locks: {sessions['total']}")
        import ipdb

        ipdb.set_trace()

        for session in sessions["objects"]:
            if session["locks"] > 0:
                import ipdb

                ipdb.set_trace()
                uid = session["uid"]
                payload = {"uid": f"{uid}"}
                api_client.api_call(command="take-over-session", payload=payload)
                api_client.api_call(command="discard", payload=None)

        response = api_client.api_call(command="show-sessions", payload=payload)
        sessions = response.data
        print(f"Number of sessions with locks: {sessions['total']}")


if __name__ == "__main__":
    main()
```

### TB-224: `python_course_mar26/class3/chkpnt_sdk/gaia_cfg_dns.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # DNS
        payload = {
            "primary": "172.31.0.2",
            "secondary": "8.8.8.8",
            "tertiary": "8.8.4.4",
            "suffix": "lasthop.io",
        }

        api_endpoint = "set-dns"
        api_res = api_client.api_call(command=api_endpoint, payload=payload)
        print(api_res)

        api_res = api_client.api_call(command="show-dns")
        print(api_res)


if __name__ == "__main__":
    main()
```

### TB-225: `python_course_mar26/class3/chkpnt_sdk/mgmt_show_networks.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=True, context="web_api"
    )
    with APIClient(client_args) as api_client:
        res = api_client.login(username, password)
        print(res)

        # api_endpoint = "show-hosts"
        api_endpoint = "show-networks"
        api_args = {}
        api_res = api_client.api_call(api_endpoint, api_args)
        print(api_res)


if __name__ == "__main__":
    main()
```

### TB-226: `python_course_mar26/class2/api/awx_auth.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `requests, os, ipdb, dotenv.load_dotenv, rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import requests
import os
import ipdb  # noqa
from dotenv import load_dotenv
from rich import print

awx_host = "54.241.198.61"
port = "32309"
base_url = f"http://{awx_host}:{port}/api/v2/"
url = f"{base_url}tokens/"

# This looks for a .env file and loads it
load_dotenv()
user = "admin"
admin_pass = os.environ["AWX_ADMIN"]
creds = (user, admin_pass)

res = requests.post(url, auth=creds, json={"description": "Testing auth"}, verify=False)
json_resp = res.json()
token = json_resp["token"]
print()
print(url)
print(res)

# Retrieve some data using existing token
headers = {"Authorization": f"Bearer {token}"}
endpoint = "projects/"
url = f"{base_url}{endpoint}"

res = requests.get(url, headers=headers, verify=False)
print()
print(url)
print(res)
print(res.json())

# Delete the token
endpoint = f"tokens/{token}/"
url = f"{base_url}{endpoint}"
requests.delete(url, headers=headers, verify=False)
print()
print(url)
print(res)
```

### TB-227: `python_course_mar26/class2/exercises/gaia_api_ex/gaia_proc.py`

**Lab type:** API automation lab

**Objective:** It treats network facts as structured data, so code can look up exact fields instead of reading text by eye.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, gaia_auth_ex.login, gaia_auth_ex.api_call, gaia_auth_ex.logout`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from gaia_auth_ex import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    base_url = f"https://{host}/gaia_api/v{api_version}/"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    response = login(base_url, user, admin_pass)
    resp_struct = response.json()
    session_id = resp_struct["sid"]

    headers = {"Content-Type": "application/json"}
    headers["X-chkp-sid"] = session_id

    # Gather and display dynamic ARP data
    endpoint = "show-arp"
    arp_response = api_call(base_url, endpoint, headers)
    arp_table = arp_response.json()
    dynamic_arp = arp_table["dynamic"]

    print()
    for arp_entry in dynamic_arp:
        ip_addr = arp_entry['ipv4-address']
        mac_addr = arp_entry['mac-address']
        print(f"{ip_addr} -> {mac_addr}")
    print()

    logout(base_url, headers)
```

### TB-228: `python_course_mar26/class2/exercises/gaia_api_ex/gaia_proc.md`

**Lab type:** Reading and design lab

**Objective:** It runs the same network task across multiple devices without waiting for one device at a time.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Gaia 'show arp' Exercise

Repeat the Gaia authentication code from the Gaia authentication exercise.

In this script, use your authenticated Gaia session to execute 'show-arp'. Retreive the ARP response from the firewall and process the ARP table.

From the ARP response, you should extract both the 'mac-address' and the 'ipv4-address'. You should then print this data to standard output.

Your output should look similar to the following:

'''python
$ python gaia_proc.py 

172.31.32.1 -> 0a:61:33:92:44:55
172.31.128.1 -> 0a:15:04:3a:87:eb
172.31.144.1 -> 0a:be:1f:c0:c1:03
172.31.145.1 -> 0a:ce:8f:94:04:c9

'''
```

### TB-229: `python_course_mar26/class2/gaia_ssh/api_status.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    # "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    print(ssh_conn.find_prompt())

    # Enter expert mode
    ssh_conn.enable()
    print(ssh_conn.find_prompt())

    cmd = "gaia_api status"
    data = ssh_conn.send_command(cmd)
    print(data)

    data = ssh_conn.exit_enable_mode()
    print(ssh_conn.find_prompt())
```

### TB-230: `python_course_mar26/class3/exercises/fw_policy_ex2/fw_policy_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `chkpt_exceptions.ChkPntConfigError, chkpt_exceptions.ChkPntPolicyInstallError, rich.print, ipdb`.
2. It defines reusable function(s): `extract_fw_name, display_fw_policy, install_fw_policy, cfg_fw_rule, cfg_fw_rules`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from chkpt_exceptions import ChkPntConfigError, ChkPntPolicyInstallError
from rich import print
import ipdb  # noqa


def extract_fw_name(fqdn):
    # Extract the fw_name from the DNS name
    if "." in fqdn:
        fw_name = fqdn.split(".")[0]
        return fw_name
    else:
        raise ValueError("Invalid firewall name: {fqdn}")


def display_fw_policy(api_client, layer="Network"):
    payload = {"name": layer}
    api_res = api_client.api_call(command="show-access-rulebase", payload=payload)
    fw_rules = api_res.data["rulebase"]
    print(fw_rules)


def install_fw_policy(api_client, policy_package="Standard", targets=None):
    """
    Install the firewall policy on firewall.

    This code ASSUMES all-in-one firewall i.e. target firewall is web_api host by default.
    """
    if targets is None:
        fw_name = extract_fw_name(api_client.server)
        targets = [fw_name]

    payload = {"policy-package": policy_package, "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
    if not api_res.success:
        msg = f"Failed to install firewall policy: {payload}"
        raise ChkPntPolicyInstallError(msg)


def cfg_fw_rule(api_client, fw_rule, delete_rule=False):
    """Use mgmt API to configure a firewall rule."""

    # Check if fw_rule already exists
    obj_exists = False
    payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
    api_res = api_client.api_call(command="show-access-rule", payload=payload)

    if api_res.success:
        obj_exists = True

    if delete_rule and obj_exists:
        print(f"Deleting firewall rule: {fw_rule['name']}")
        api_res = api_client.api_call(command="delete-access-rule", payload=payload)
    else:
        if obj_exists:
            print(f"Updating firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="set-access-rule", payload=fw_rule)
        else:
            print(f"Configuring firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="add-access-rule", payload=fw_rule)

    if not api_res.success:
        msg = f"Failed to configure firewall rule: {fw_rule}"
        raise ChkPntConfigError(msg)


def cfg_fw_rules(api_client, fw_rules):
    """Use mgmt API to configure firewall policy rules."""
    for fw_rule in fw_rules:
        cfg_fw_rule(api_client, fw_rule)
```

### TB-231: `python_course_mar26/class3/exercises/chkpnt_sdk_ex/mgmt_cfg_hostobj_ex.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Chkpnt SDK Exercise1

Connect to the Mgmt API using the Chkpnt SDK. You should read your API credentials in using the .env file and load_dotenv().

Create a function named 'cfg_host_objects'  that takes one argument (api_client). In this function configure the following three host objects:

'''python
    smart_console_private = {
        "name": "Windows SmartConsole",
        "ipv4-address": "172.31.12.101",
        "color": "red",
    }
    smart_console_public = {
        "name": "Windows SmartConsole Public",
        "ipv4-address": "3.71.9.240",
        "color": "red",
    }
    ansible_server = {
        "name": "Ansible Server",
        "ipv4-address": "3.125.34.232",
        "color": "black",
    }
'''

Your function should do the following:
1. Use the 'show-host' endpoint and the object name to see if the object already exists.
2. If the object already exists, then use the 'set-host' endpoint to update the host object (using the dictionaries provided above).
3. If the object doesn't exist, then use the 'add-host' endpoint to create the given host object.

You should use the ".success" attribute of the response object to ensure your object was created or updated successfully.

You should raise an exception if the 'add-host' or 'set-host' operation was not successful.

Once your object has been created, you will need to 'publish' it. You can do this by invoking the following:

'''python
api_client.api_call(command="publish")
'''
```

### TB-232: `python_course_mar26/class3/fw_policy/fw_policy.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, ipdb`.
2. It defines class blueprint(s): `ChkPntConfigError, ChkPntPolicyInstallError`.
3. It defines reusable function(s): `extract_fw_name, display_fw_policy, install_fw_policy, cfg_fw_policy, main`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


class ChkPntPolicyInstallError(Exception):
    pass


def extract_fw_name(api_client):
    # Extract the fw_name from the DNS name
    fqdn = api_client.server
    if "." in fqdn:
        fw_name = fqdn.split(".")[0]
        return fw_name
    else:
        raise ValueError("Invalid firewall name: {fqdn}")


def display_fw_policy(api_client, layer="Network"):
    payload = {"name": layer}
    api_res = api_client.api_call(command="show-access-rulebase", payload=payload)
    fw_rules = api_res.data["rulebase"]
    print(fw_rules)


def install_fw_policy(api_client, policy_package="Standard", targets=None):
    """
    Install the firewall policy on firewall.

    This code ASSUMES all-in-one firewall i.e. target firewall is web_api host by default.
    """
    if targets is None:
        fw_name = extract_fw_name(api_client)
        targets = [fw_name]

    payload = {"policy-package": policy_package, "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
    if not api_res.success:
        msg = f"Failed to install firewall policy: {payload}"
        raise ChkPntPolicyInstallError(msg)


def cfg_fw_policy(api_client):
    """Use mgmt API to configure firewall policy rules."""

    fw_name = extract_fw_name(api_client)
    management_rules = [
        {
            "layer": "Network",
            "name": "Ansible Management Access",
            "source": [
                "Ansible Server",
                "Windows SmartConsole",
                "Windows SmartConsole Public",
            ],
            "destination": fw_name,
            "service": "Any",
            "action": "Accept",
            "position": 2,
        },
        {
            "layer": "Network",
            "name": "SSH Access",
            "source": "Any",
            "destination": fw_name,
            "service": "SSH",
            "action": "Accept",
            "position": 3,
        },
    ]

    for fw_rule in management_rules:
        # Check if fw_rule already exists
        import ipdb; ipdb.set_trace()
        obj_exists = False
        payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
        api_res = api_client.api_call(command="show-access-rule", payload=payload)

        if api_res.success:
            obj_exists = True
        if obj_exists:
            print(f"Updating firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="set-access-rule", payload=fw_rule)
        else:
            print(f"Configuring firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="add-access-rule", payload=fw_rule)

        if not api_res.success:
            msg = f"Failed to configure firewall rule: {fw_rule}"
            raise ChkPntConfigError(msg)


def main():
    # CHANGE (for each pod) #####
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        import ipdb; ipdb.set_trace()
        cfg_fw_policy(api_client)
        api_client.api_call(command="publish")

        # install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
```

### TB-233: `python_course_mar26/class3/exercises/chkpnt_sdk_ex/group_net_objects_ex.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Chkpnt SDK Exercise3

Connect to the Mgmt API using the Chkpnt SDK. Read your credentials in using the .env file and load_dotenv().

Create a new function named 'cfg_group' that is based upon your previously created 'cfg_net_objects' function.

This function should create the following group object:

'''python
    group_params = {
        "name": "hq_net",
        "members": [
            "hq_net_128",
            "hq_net_129",
            "hq_net_130",
            "hq_net_131",
            "hq_net_132",
            "hq_net_133",
            "hq_net_134",
            "hq_net_135",
        ],
        "color": "blue",
    }

'''

Once again your function should check if the group object exists (using the 'show-group' endpoint). If the object does already exist, then you should update the group using the 'set-group' endpoint.

If the object doesn't exist, then you should add it using the 'add-group' endpoint.

You should use the ".success" attribute of the response object to ensure your object was created or updated successfully.

You should raise an exception if the 'add-group' or 'set-group' operation was not successful.

Once your object has been created, you will need to 'publish' it. You can do this by invoking the following:

'''python
api_client.api_call(command="publish")
'''
```

### TB-234: `python_course_mar26/class3/exercises/chkpnt_sdk_ex/mgmt_cfg_netobj_ex.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Chkpnt SDK Exercise2

Connect to the Mgmt API using the Chkpnt SDK. Read your credentials in using the .env file and load_dotenv().

Create a new function named 'cfg_net_objects' that is based upon your previously created 'cfg_host_objects' function.

This function should create the following network objects:

'''python
    hq_net_128 = {
        "name": "hq_net_128",
        "subnet": "172.31.128.0",
    }
    hq_net_129 = {
        "name": "hq_net_129",
        "subnet": "172.31.129.0",
    }
    hq_net_130 = {
        "name": "hq_net_130",
        "subnet": "172.31.130.0",
    }
    hq_net_131 = {
        "name": "hq_net_131",
        "subnet": "172.31.131.0",
    }
    hq_net_132 = {
        "name": "hq_net_132",
        "subnet": "172.31.132.0",
    }
    hq_net_133 = {
        "name": "hq_net_133",
        "subnet": "172.31.133.0",
    }
    hq_net_134 = {
        "name": "hq_net_134",
        "subnet": "172.31.134.0",
    }
    hq_net_135 = {
        "name": "hq_net_135",
        "subnet": "172.31.135.0",
    }
'''

For each of these networks you should also specify the following (i.e. the mask-length for these networks is always a /24 and the object color is always green).

'''python
        network_obj["mask-length"] = 24
        network_obj["color"] = "green"
'''

Once again your function should check if the given network object exists (using the 'show-network' endpoint). If the object does already exist, then you should update the network object using the 'set-network' endpoint.

If the network object doesn't exist, then you should add the object using the 'add-network' endpoint.

You should use the ".success" attribute of the response object to ensure your object was created or updated successfully.

You should raise an exception if the 'add-network' or 'set-network' operation was not successful.

Once your object has been created, you will need to 'publish' it. You can do this by invoking the following:

'''python
api_client.api_call(command="publish")
'''
```

### TB-235: `python_course_mar26/class3/exercises/fw_policy_ex1/fw_policy_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `chkpt_exceptions.ChkPntConfigError, chkpt_exceptions.ChkPntPolicyInstallError, rich.print, ipdb`.
2. It defines reusable function(s): `extract_fw_name, display_fw_policy, install_fw_policy, cfg_fw_rule, cfg_fw_rules`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from chkpt_exceptions import ChkPntConfigError, ChkPntPolicyInstallError
from rich import print
import ipdb  # noqa


def extract_fw_name(fqdn):
    # Extract the fw_name from the DNS name
    if "." in fqdn:
        fw_name = fqdn.split(".")[0]
        return fw_name
    else:
        raise ValueError("Invalid firewall name: {fqdn}")


def display_fw_policy(api_client, layer="Network"):
    payload = {"name": layer}
    api_res = api_client.api_call(command="show-access-rulebase", payload=payload)
    fw_rules = api_res.data["rulebase"]
    print(fw_rules)


def install_fw_policy(api_client, policy_package="Standard", targets=None):
    """
    Install the firewall policy on firewall.

    This code ASSUMES all-in-one firewall i.e. target firewall is web_api host by default.
    """
    if targets is None:
        fw_name = extract_fw_name(api_client.server)
        targets = [fw_name]

    payload = {"policy-package": policy_package, "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
    if not api_res.success:
        msg = f"Failed to install firewall policy: {payload}"
        raise ChkPntPolicyInstallError(msg)


def cfg_fw_rule(api_client, fw_rule):
    """Use mgmt API to configure a firewall rule."""

    # Check if fw_rule already exists
    obj_exists = False
    payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
    api_res = api_client.api_call(command="show-access-rule", payload=payload)

    if api_res.success:
        obj_exists = True
    if obj_exists:
        print(f"Updating firewall rule: {fw_rule}")
        api_res = api_client.api_call(command="set-access-rule", payload=fw_rule)
    else:
        print(f"Configuring firewall rule: {fw_rule}")
        api_res = api_client.api_call(command="add-access-rule", payload=fw_rule)

    if not api_res.success:
        msg = f"Failed to configure firewall rule: {fw_rule}"
        raise ChkPntConfigError(msg)


def cfg_fw_rules(api_client, fw_rules):
    """Use mgmt API to configure firewall policy rules."""
    for fw_rule in fw_rules:
        cfg_fw_rule(api_client, fw_rule)
```

### TB-236: `python_course_mar26/class4/exercises/main_project/tests/conftest.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pytest, os, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `gaia_api, mgmt_api`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import pytest
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


@pytest.fixture(scope="session")
def gaia_api():

    api_server = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=True, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # Object that is passed to the tests
        yield api_client


@pytest.fixture(scope="session")
def mgmt_api():

    api_server = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=True, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # Object that is passed to the tests
        yield api_client
```

### TB-237: `python_course_mar26/lib_class4/chkpt_policy_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `chkpt_exceptions.ChkPntConfigError, chkpt_exceptions.ChkPntPolicyInstallError, rich.print, ipdb`.
2. It defines reusable function(s): `extract_fw_name, display_fw_policy, install_fw_policy, cfg_fw_rule, cfg_fw_rules`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from chkpt_exceptions import ChkPntConfigError, ChkPntPolicyInstallError
from rich import print
import ipdb  # noqa

DEBUG = False

def extract_fw_name(fqdn):
    # Extract the fw_name from the DNS name
    if "." in fqdn:
        fw_name = fqdn.split(".")[0]
        return fw_name
    else:
        raise ValueError("Invalid firewall name: {fqdn}")


def display_fw_policy(api_client, layer="Network"):
    payload = {"name": layer}
    api_res = api_client.api_call(command="show-access-rulebase", payload=payload)
    fw_rules = api_res.data["rulebase"]
    print(fw_rules)


def install_fw_policy(api_client, policy_package="Standard", targets=None):
    """
    Install the firewall policy on firewall.

    This code ASSUMES all-in-one firewall i.e. target firewall is web_api host by default.
    """
    if targets is None:
        fw_name = extract_fw_name(api_client.server)
        targets = [fw_name]

    payload = {"policy-package": policy_package, "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
    if not api_res.success:
        msg = f"Failed to install firewall policy: {payload}"
        raise ChkPntPolicyInstallError(msg)


def cfg_fw_rule(api_client, fw_rule):
    """Use mgmt API to configure a firewall rule."""

    # Check if fw_rule already exists
    obj_exists = False
    payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
    api_res = api_client.api_call(command="show-access-rule", payload=payload)

    if api_res.success:
        obj_exists = True
    if obj_exists:
        DEBUG and print(f"Updating firewall rule: {fw_rule}")
        api_res = api_client.api_call(command="set-access-rule", payload=fw_rule)
    else:
        DEBUG and print(f"Configuring firewall rule: {fw_rule}")
        api_res = api_client.api_call(command="add-access-rule", payload=fw_rule)

    if not api_res.success:
        msg = f"Failed to configure firewall rule: {fw_rule}"
        raise ChkPntConfigError(msg)


def cfg_fw_rules(api_client, fw_rules):
    """Use mgmt API to configure firewall policy rules."""
    for fw_rule in fw_rules:
        cfg_fw_rule(api_client, fw_rule)
```

### TB-238: `python_course_mar26/class3/chkpnt_sdk/fingerprints.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
{
    "chkpnt-pod99.lasthop.io": "C15B266CC5738613FA6BDE99AC61F535AFB45909"
}
```

### TB-239: `python_course_mar26/lib_class4/chkpt_object_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `chkpt_exceptions.ChkPntConfigError, ipdb`.
2. It defines reusable function(s): `cfg_object, cfg_host_object, delete_host_object, delete_host_objects, cfg_group_object, cfg_host_objects`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from chkpt_exceptions import ChkPntConfigError
import ipdb  # noqa

DEBUG = False

def cfg_object(api_client, obj_type, obj_params, delete_obj=False):

    # Check if object already exists
    object_exists = False
    payload = {"name": obj_params["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if delete_obj:
        if object_exists:
            payload = {"name": obj_params["name"]}
            api_res = api_client.api_call(command=f"delete-{obj_type}", payload=payload)
        else:
            # Nothing to do, object to delete doesn't exist
            pass
        return

    if object_exists:
        # Object already exists, update parameters
        DEBUG and print(f"Updating {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=obj_params)
    else:
        DEBUG and print(f"Configuring {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=obj_params)

    if not api_res.success:
        # Ternary operator (could just use conditional)
        action = "delete" if delete_obj else "configure"
        msg = f"Failed to {action} {obj_type} object: {obj_params}"
        raise ChkPntConfigError(msg)


def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    cfg_object(api_client, obj_type=obj_type, obj_params=host_object)


def delete_host_object(api_client, host_object):
    """Wrapper for better naming."""
    obj_type = "host"
    cfg_object(api_client, obj_type=obj_type, obj_params=host_object, delete_obj=True)


def delete_host_objects(api_client, host_objects):
    """Delete a list/interable of host objects."""
    for host_obj in host_objects:
        delete_host_object(api_client, host_obj)


def cfg_group_object(api_client, group_object):
    """Create/update a host object."""
    obj_type = "group"
    cfg_object(api_client, obj_type=obj_type, obj_params=group_object)


def cfg_host_objects(api_client, host_objects):
    """Takes a list / iterator of host_objects and create/update them."""

    for host_obj in host_objects:
        cfg_host_object(api_client, host_obj)
```

### TB-240: `python_course_mar26/class3/exercises/object_func_ex/object_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `ipdb`.
2. It defines class blueprint(s): `ChkPntConfigError`.
3. It defines reusable function(s): `cfg_object, cfg_host_object, cfg_network_object, cfg_group_object`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


def cfg_object(api_client, obj_type, obj_params):

    # Check if object already exists
    object_exists = False
    status = ""
    payload = {"name": obj_params["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=obj_params)
        status = "updated"
    else:
        print(f"Configuring {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=obj_params)
        status = "created"

    if not api_res.success:
        msg = f"Failed to configure {obj_type} object: {obj_params}"
        raise ChkPntConfigError(msg)

    return (api_res, status)


def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    return cfg_object(api_client, obj_type=obj_type, obj_params=host_object)


def cfg_network_object(api_client, network_object):
    """Create/update a network object."""
    obj_type = "network"
    return cfg_object(api_client, obj_type=obj_type, obj_params=network_object)


def cfg_group_object(api_client, group_object):
    """Create/update a group object."""
    obj_type = "group"
    return cfg_object(api_client, obj_type=obj_type, obj_params=group_object)
```

### TB-241: `python_course_mar26/work/gaia_intf_work.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, sys, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#
# show physical interface.py
# version 1.0
#
# The purpose of this script is to show a server's physical interfaces
#
# written by: Check Point software technologies inc.
# April 2019
# modified by: Kirk Byers (Feb 2026)

import os
import sys
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    api_server = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"

    client_args = APIClientArgs(
        server="chkpnt-pod99.lasthop.io",
        api_version="1.8",
        unsafe=True,
        context="gaia_api",
    )

    with APIClient(client_args) as client:
        login_res = client.login(username, password)
        if login_res.success is False:
            print(f"Login failed: {login_res.error_message}")
            sys.exit(1)

        interface_name = input("Enter interface name: ")
        api_endpoint = "show-physical-interface"
        api_args = {"name": interface_name}
        api_res = client.api_call(api_endpoint, api_args)
        if api_res.success:
            intf_name = api_res.data["name"]
            ip_addr = (api_res.data["ipv4-address"],)
            mtu = (api_res.data["mtu"],)
            resp = f"""
Physical interface name is '{intf_name}' , ipv4 address is '{ip_addr}', 
interface mtu is '{mtu}' 
"""
            print(resp)
        else:
            print(f"Failed to get physical interface data '{api_res.data}'")


if __name__ == "__main__":
    main()
```

### TB-242: `python_course_mar26/class3/exercises/fw_policy_ex1/fw_policy_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, fw_policy_funcs.cfg_fw_rule, fw_policy_funcs.install_fw_policy`.
2. It defines reusable function(s): `main`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from fw_policy_funcs import (
    cfg_fw_rule,
    install_fw_policy,
    display_fw_policy,
)
from object_funcs import cfg_host_object
from rich import print  # noqa
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"

    corp_web_server = {
        "name": "Corp Web Server",
        "ipv4-address": "172.31.144.220",
        "color": "dark green",
    }

    corp_fw_rule = {
        "layer": "Network",
        "name": "Corp Web Server Access",
        "source": "Any",
        "destination": "Corp Web Server",
        "service": ["http", "https"],
        "action": "Accept",
        "position": 1,
    }

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_host_object(api_client, corp_web_server)
        cfg_fw_rule(api_client, fw_rule=corp_fw_rule)
        api_client.api_call(command="publish")
        install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
```

### TB-243: `python_course_mar26/class3/exercises/fw_policy_ex2/fw_policy_edit_rule.py`

**Lab type:** API automation lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, fw_policy_funcs.cfg_fw_rule, fw_policy_funcs.install_fw_policy`.
2. It defines reusable function(s): `main`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
# Edit an existing firewall rule
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from fw_policy_funcs import (
    cfg_fw_rule,
    install_fw_policy,
    display_fw_policy,
)
from object_funcs import cfg_host_object
from rich import print  # noqa
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"

    corp_web_server = {
        "name": "Corp Web Server",
        "ipv4-address": "172.31.144.220",
        "color": "dark green",
    }

    corp_fw_rule = {
        "layer": "Network",
        "name": "Corp Web Server Access",
        "source": "Any",
        "destination": "Corp Web Server",
        "service": ["http", "https", "ssh"],
        "action": "Accept",
        "position": 1,
        "comments": "Test rule for Python training session",
    }

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_host_object(api_client, corp_web_server)
        cfg_fw_rule(api_client, fw_rule=corp_fw_rule)
        api_client.api_call(command="publish")
        install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
```

### TB-244: `python_course_mar26/class3/exercises/fw_policy_ex2/fw_policy_delete_rule.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, fw_policy_funcs.cfg_fw_rule, fw_policy_funcs.install_fw_policy`.
2. It defines reusable function(s): `main`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
# Edit an existing firewall rule
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from fw_policy_funcs import (
    cfg_fw_rule,
    install_fw_policy,
    display_fw_policy,
)
from rich import print  # noqa
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"

    corp_web_rule = {
        "layer": "Network",
        "name": "Corp Web Server Access",
        "source": "Any",
        "destination": "Corp Web Server",
        "service": ["http", "https", "ssh"],
        "action": "Accept",
        "position": 1,
    }

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_fw_rule(api_client, fw_rule=corp_web_rule, delete_rule=True)
        api_client.api_call(command="publish")
        install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
```

### TB-245: `python_course_mar26/class4/exercises/show_changes_ex/show_changes.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs, datetime.datetime`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from datetime import datetime, timedelta, timezone
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        now = datetime.now(timezone.utc)
        two_days_ago = now - timedelta(hours=48)

        # ISO 8601
        from_date = two_days_ago.strftime('%Y-%m-%dT%H:%M:%S')
        to_date = now.strftime('%Y-%m-%dT%H:%M:%S')

        payload = {"from-date": from_date, "to-date": to_date}

        api_res = api_client.api_call(command="show-changes", payload=payload)
        print(api_res)

        changes = api_res.data['tasks'][0]['task-details'][0]['changes']
        for change in changes:
            operations = change['operations']
            added = operations['added-objects']
            modified = operations['modified-objects']
            deleted = operations['deleted-objects']
            if added:
                print(added)
            if modified:
                print(modified)
            if deleted:
                print(deleted)
            ipdb.set_trace()

        print(changes)


if __name__ == "__main__":
    main()
```

### TB-246: `python_course_mar26/class3/exercises/object_func_ex/conftest.py`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. First, it brings in helper tools: `pytest, os, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `web_api_session`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import pytest
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


@pytest.fixture(scope="session")
def web_api_session():

    api_server = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=True, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # Object that is passed to the tests
        yield api_client
```

### TB-247: `python_course_mar26/class3/exercises/fw_policy_ex1/object_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `chkpt_exceptions.ChkPntConfigError, ipdb`.
2. It defines reusable function(s): `cfg_host_object`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from chkpt_exceptions import ChkPntConfigError
import ipdb  # noqa


def cfg_host_object(api_client, host_object):

    obj_type = "host"

    # Check if host already exists
    object_exists = False
    payload = {"name": host_object["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {host_object}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=host_object)
    else:
        print(f"Configuring {obj_type} object: {host_object}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=host_object)

    if not api_res.success:
        msg = f"Failed to configure {obj_type} object: {host_object}"
        raise ChkPntConfigError(msg)
```

### TB-248: `python_course_mar26/class3/exercises/fw_policy_ex2/object_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `chkpt_exceptions.ChkPntConfigError, ipdb`.
2. It defines reusable function(s): `cfg_host_object`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
from chkpt_exceptions import ChkPntConfigError
import ipdb  # noqa


def cfg_host_object(api_client, host_object):

    obj_type = "host"

    # Check if host already exists
    object_exists = False
    payload = {"name": host_object["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {host_object}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=host_object)
    else:
        print(f"Configuring {obj_type} object: {host_object}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=host_object)

    if not api_res.success:
        msg = f"Failed to configure {obj_type} object: {host_object}"
        raise ChkPntConfigError(msg)
```

### TB-249: `python_course_mar26/class3/exercises/fw_policy_ex1/fw_policy_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Firewall Policy Exercise1

### The management rules for the Ansible Server must be installed prior to this exercise.

Connect to the Mgmt API using the Chkpnt SDK. Read your credentials in using the .env file and load_dotenv().

Re-use or re-implement your function named 'cfg_host_objects' that you previously created in the "./class3/exercise/chkpnt_sdk_ex" exercises. 

Note, in my reference function I added a second argument, 'host_object'. Consequently, I now pass the 'api_client' and the 'host_object' into the function. The 'host_object' is the host dictionary I am configuring.

'''python
def cfg_host_object(api_client, host_object):
'''

This function should create the following host object:

'''python
corp_web_server = {
    "name": "Corp Web Server",
    "ipv4-address": "172.31.144.220",
    "color": "dark green",
}
'''

Next create a 'cfg_fw_rule' function. This function should be similar to your previous 'cfg_host_object' function.

Once again your function should check if the given firewall rule exists (using 'show-access-rule). If the rule does already exist, then your script should update the firewall rule using 'set-access-rule'.

If the firewall rule doesn't exist, then it should add the rule using 'add-access-rule'.

You should use the ".success" attribute of the response object to ensure your firewall rule was created or updated successfully.

You should raise an exception if the 'add-access-rule' or 'set-access-rule' operation was not successful.

Note, for the 'show-access-rule' call you only need to pass the "layer" field and the "name" field in the API call payload (see the Mgmt API documentation for additional details).

Your firewall rule should be the following:

'''python
    corp_fw_rule = { 
        "layer": "Network",
        "name": "Corp Web Server Access",
        "source": "Any",
        "destination": "Corp Web Server",
        "service": ["http", "https"],
        "action": "Accept",
        "position": 1,
    } 
'''

After you have pushed both the host object and the new firewall rule, you will to both publish and install the firewall policy. In order to do this, you will need to make the following API call.

In order to publish, you can simply invoke the following:

'''python
api_client.api_call(command="publish")
'''

And in order to install the firewall policy, you will need to do something similar to the following:

'''python
    payload = {"policy-package": "Standard", "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
'''

Where 'targets' is your firewall name. So for 'pod99' (host = 'chkpnt-pod99.lasthop.io'), the firewall targets will be:

'''python
targets = ["chkpnt-pod99"]
'''

You can decide whether you want to create a function for 'install_fw_policy' or whether you want directly implement it in your main program.
```

### TB-250: `python_course_mar26/class3/exercises/object_func_ex/common_object_function.md`

**Lab type:** Reading and design lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Exercise on creating a common object function.

In the Check Point SDK exercises from Wednesday, we created host objects, network objects, and a group object.

This code had a common pattern of use f"show-{obj_type}" to check for the existence of an object (based on the name of the object).

If the object exists, then use f"set-{obj_type}" to update the existing object.

If the object doesn't exist, then use f"add-{obj_type}" to add the existing object.

Given the above, you should be able to create a common function to implement this logic. This common function would support host objects, network objects, and group objects.

Your function signature should look as follows:

'''python
def cfg_object(api_client, obj_type, obj_params):
'''

If your "set" or "add" operation fails, then you should raise the following exception.

'''python
msg = f"Failed to configure {obj_type} object: {obj_params}"
raise ChkPntConfigError(msg)
'''

You should return the '(api_resp, status)' from the 'cfg_object' function unless an exception was raised. 'status' will either be 'updated' or 'created' depending on the action the function took.

Once the 'cfg_object' function has been created, you should be able to create the following three wrapper functions.

'''python
def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    return cfg_object(api_client, obj_type=obj_type, obj_params=host_object)
'''

'''python
def cfg_network_object(api_client, network_object):
    """Create/update a network object."""
    obj_type = "network"
    return cfg_object(api_client, obj_type=obj_type, obj_params=network_object)
'''

'''python
def cfg_group_object(api_client, group_object):
    """Create/update a group object."""
    obj_type = "group"
    return cfg_object(api_client, obj_type=obj_type, obj_params=group_object)
'''
```

### TB-251: `python_course_mar26/class3/exercises/object_func_ex/object_function_tests.md`

**Lab type:** Reading and design lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Test object functions

Use the referenced 'conftest.py' file as a test fixture. You will need to change the 'api_server' variable in this file to match your pod.

'''python
# Change to your pod
api_server = "chkpnt-pod99.lasthop.io"
'''

Create a 'test_object_funcs.py' file. This file should import the three object creation functions.

'''python
from object_funcs import cfg_host_object, cfg_network_object, cfg_group_object
'''

You should create the following three tests:

'''python
def test_host_object_creation(web_api_session):
'''

'''python
def test_network_object_creation(web_api_session):
'''

'''python
def test_group_object_creation(web_api_session):
'''

Each of these three tests should create a test object of the given type and then verify the following:

'''python
assert api_res.success is True
assert status in ["created", "updated"]
'''

Use 'pytest' to run these tests and verify your tests properly pass.
```

---

## Lab Track 18: Building a Network Automation Tool

**Concept focus:** shape scripts into a small tool with clear inputs, outputs, and modules.

**Mental model:** `operator request -> validation -> automation function -> rendered report`

### TB-252: `python_course_mar26/class4/exercises/main_project/blocked_ip_funcs.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `ipdb, rich.print`.
2. It defines reusable function(s): `read_blocked_ips_file, gen_host_object, get_current_blocked_ips`.
3. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import ipdb  # noqa
from rich import print  # noqa


def read_blocked_ips_file():
    # Retrieve the 'new' blocked IPs
    with open("blocked_ips.txt") as f:
        new_blocked_ips = f.readlines()
        # strip trailing newline w/ list comprehension
        new_blocked_ips = [ip.strip() for ip in new_blocked_ips]
        return new_blocked_ips


def gen_host_object(ip_addr):
    return {
        "name": ip_addr,
        "ipv4-address": ip_addr,
        "color": "black",
    }


def get_current_blocked_ips(api_client, group_name):
    """Retrieve current Blocked IPs group membership."""
    current_blocked_ips = []
    api_res = api_client.api_call(command="show-group", payload={"name": group_name})
    if api_res.success:
        current_blocked_ips = api_res.data["members"]

    # Retrieve only names / use list comprehension
    cur_blocked_ip_names = [bl_obj["name"] for bl_obj in current_blocked_ips]
    return cur_blocked_ip_names
```

### TB-253: `python_course_mar26/class4/exercises/main_project/run_scripts.sh`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. This is a shell helper script.
2. It strings together command-line steps so the same setup or test can be repeated.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```bash
#!/bin/bash
python 01_gaia_cfg_settings.py
python 02_gaia_ssh_cfg.py
python 03_mgmt_api_cfg.py
```

### TB-254: `python_course_mar26/class4/exercises/main_project/main_project.md`

**Lab type:** Reading and design lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
# Main Project

### Gaia Configuration using API

DNS Config (endpoint: set-dns)

'''yaml
primary: 172.31.0.2
secondary: 8.8.8.8
tertiary: 8.8.4.4
suffix: lasthop.io
'''

Static Route (endpoint: set-static-route)

'''yaml
network: 172.31.128.0/21
next_hop_gateway: 172.31.128.1
'''

### Gaia Configuration using Netmiko-SSH

'''bash
set password-controls complexity 3
set password-controls deny-on-nonuse enable on
set password-controls min-password-length 10
'''

Call the Netmiko .save_config() method to ensure that you properly save these changes.

### Mgmt API Object Configuration

Host Objects

'''python
smart_console_private = { 
    "name": "Windows SmartConsole",
    "ipv4-address": "172.31.12.101",
    "color": "red",
}
smart_console_public = { 
    "name": "Windows SmartConsole Public",
    "ipv4-address": "3.71.9.240",
    "color": "red",
}
ansible_server = { 
    "name": "Ansible Server",
    "ipv4-address": "3.125.34.232",
    "color": "black",
}
'''

### Mgmt API Blocked IP Configuration

Create a Python script that uses the Mgmt API and configures a set of blocked IPs from a "blocked_ips.txt" file.

The script should do the following:
1. Retrieves the current "Blocked IPs" group and extracts all the member hosts. This query must handle the case then the "Blocked IPs" group doesn't exist.
2. Compares the currently configured blocked IPs (the group members) to the new blocked IPs (from the text file).
3. Adds any missing new blocked IPs as host objects. You should use the IP address as the host object name.
4. Updates the group membership to match the blocked IPs from the text file.
5. Remove any blocked IP host objects that are no longer used (previous group members, but no longer in the "blocked_ips.txt" file).

Publish your changes.


### Mgmt API FW Policy Configuration

Add the following firewall policy rules via the Mgmt API (publish, but do NOT install them)

'''python
fw_rules = [ 
    {   
        "layer": "Network",
        "name": "Blacklisted IPs",
        "source": "Blocked IPs",
        "destination": "Any",
        "service": "Any",
        "action": "Drop",
        "position": 1,
    },
    {   
        "layer": "Network",
        "name": "Ansible Management Access",
        "source": [
            "Ansible Server",
            "Windows SmartConsole",
            "Windows SmartConsole Public",
        ],  
        "destination": fw_name,
        "service": "Any",
        "action": "Accept",
        "position": 2,
    },  
    {   
        "layer": "Network",
        "name": "SSH Access",
        "source": "Any",
        "destination": fw_name,
        "service": "SSH",
        "action": "Accept",
        "position": 3,
    },  
]
'''

## Verifications of Current Configuration using Pytest.

### Pytest Fixtures

Create three pytest fixtures:
1. pytest fixture that establishes a Gaia Api connection.
2. pytest fixture that establishes a Mgmt Api connection.
3. pytest fixture that establishes a Netmiko-SSH connection.


### Pytest Tests (Gaia API)

1. User checks (uses "show-users" endpont):
    * The only configured users are: admin and monitor
2. Password policy checks (uses "show-password-policy"):
    * Maximum failed login attempts is <= 10.
    * Minimum account lockout duration is >= 600s.
    * Maximum inactive days is <= 365.
    * Lock inactive accounts is set to True.
    * Minimum password character complexity is >= 3.
    * Minimum password length is >= 10.
3. DNS settings match the items you configured earlier in this lab.
4. The static route you configured exists and has the correct next hop.


### Pytest Tests (Mgmt API)
1. All the host objects are properly configured.
2. The "Blocked IPs" group is properly configured and has ten members.
3. The three firewall rules are properly configured.


### Install the Firewall Policy
```

### TB-255: `python_course_mar26/class4/exercises/main_project/01_gaia_cfg_settings.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines class blueprint(s): `GaiaConfigError`.
3. It defines reusable function(s): `config_dns, config_static_route, main`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
import ipdb  # noqa
from rich import print  # noqa
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


class GaiaConfigError(Exception):
    pass


def config_dns(api_client):

    # DNS
    payload = {
        "primary": "172.31.0.2",
        "secondary": "8.8.8.8",
        "tertiary": "8.8.4.4",
        "suffix": "lasthop.io",
    }

    api_endpoint = "set-dns"
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    if not api_res.success:
        msg = f"{api_endpoint} configuration failed. "
        if hasattr(api_res, "data"):
            msg += api_res.data["errors"]
        raise GaiaConfigError(msg)


def config_static_route(api_client):

    payload = {
        "address": "172.31.128.0",
        "mask-length": 28,
        "next-hop": [{"gateway": "172.31.128.1", "priority": "default"}],
        "type": "gateway",
    }

    api_endpoint = "set-static-route"
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    if not api_res.success:
        msg = f"{api_endpoint} configuration failed. "
        if hasattr(api_res, "data"):
            msg += api_res.data["errors"]
        raise GaiaConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        print("[green][Gaia Config][/green] Configure DNS Settings")
        config_dns(api_client)
        print("[green][Gaia Config][/green] Configure Static Route")
        config_static_route(api_client)


if __name__ == "__main__":
    main()
```

### TB-256: `python_course_mar26/class4/exercises/main_project/02_gaia_ssh_cfg.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. Then it sends configuration commands, which is the part that can change a real device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    # "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    cfg_commands = [
        "set password-controls complexity 3",
        "set password-controls deny-on-nonuse enable on",
        "set password-controls min-password-length 10",
    ]

    print("[green][Gaia Config SSH][/green] Configure Password Policy")
    data = ssh_conn.send_config_set(cfg_commands)
    data += ssh_conn.save_config()
    # print(data)
```

### TB-257: `python_course_mar26/class4/exercises/main_project/blocked_ips.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
10.242.1.2
10.242.1.3
10.242.1.4
10.242.1.11
10.242.1.110
10.242.1.111
10.242.1.112
10.242.1.113
10.242.1.114
10.242.1.115
```

### TB-258: `python_course_mar26/class4/exercises/main_project/gaia_check_password_policy.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, ipdb, operator, rich.print, dotenv.load_dotenv, cpapi.APIClient`.
2. It defines reusable function(s): `condition_check, check_password_policy, check_users, main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import ipdb  # noqa
import operator
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def condition_check(cond1, cond2, comparator):
    """Function to consolidate the condition check code."""

    CHECK_PASSED = True
    operations = {
        "==": operator.eq,
        "!=": operator.ne,
        "<=": operator.le,
        ">=": operator.ge,
        "<": operator.lt,
        ">": operator.gt,
    }

    if comparator not in operations:
        raise ValueError(f"Invalid comparator: {comparator}")

    if operations[comparator](cond1, cond2):
        print("[green]pass[/green]")
    else:
        CHECK_PASSED = False
        print("[red]fail[/red]")

    return CHECK_PASSED


def check_password_policy(api_client):
    api_endpoint = "show-password-policy"
    api_res = api_client.api_call(command=api_endpoint)

    password_policy = api_res.data
    password_lock = password_policy["lock-settings"]
    password_strength = password_policy["password-strength"]

    failed_attempts = password_lock["failed-attempts-settings"][
        "failed-attempts-allowed"
    ]
    lockout_duration = password_lock["failed-attempts-settings"][
        "failed-lock-duration-seconds"
    ]
    inactivity_days = password_lock["inactivity-settings"]["inactivity-threshold-days"]
    lock_inactive_accounts = password_lock["inactivity-settings"][
        "lock-unused-accounts-enabled"
    ]
    password_complexity = password_strength["complexity"]
    password_min_length = password_strength["minimum-length"]

    MAX_FAILED_ATTEMPTS = 10
    MIN_LOCKOUT_DURATION = 600
    MAX_INACTIVE_DAYS = 365
    LOCK_INACTIVE_ACCOUNTS = True
    MIN_PWD_CHAR_COMPLEXITY = 3
    MIN_PWD_LENGTH = 10

    # CHECKS #####
    print()
    print("Password Policy Checks")

    print(f".failed login attempts <= {MAX_FAILED_ATTEMPTS}...", end="")
    condition_check(failed_attempts, MAX_FAILED_ATTEMPTS, comparator="<=")

    print(f".account lockout duration >= {MIN_LOCKOUT_DURATION}...", end="")
    condition_check(lockout_duration, MIN_LOCKOUT_DURATION, comparator=">=")

    print(f".max inactive days <= {MAX_INACTIVE_DAYS}...", end="")
    condition_check(inactivity_days, MAX_INACTIVE_DAYS, comparator="<=")

    print(f".lock inactive accounts is {LOCK_INACTIVE_ACCOUNTS}...", end="")
    condition_check(lock_inactive_accounts, LOCK_INACTIVE_ACCOUNTS, comparator="==")

    print(f".password char complexity >= {MIN_PWD_CHAR_COMPLEXITY}...", end="")
    condition_check(password_complexity, MIN_PWD_CHAR_COMPLEXITY, comparator=">=")

    print(f".minimum password length >= {MIN_PWD_LENGTH}...", end="")
    condition_check(password_min_length, MIN_PWD_LENGTH, comparator=">=")


def check_users(api_client):

    CHECK_USERS = {"admin", "monitor"}
    # Set False if any test fails (and return)
    CHECK_PASSED = True

    api_endpoint = "show-users"
    api_res = api_client.api_call(command=api_endpoint)

    users = api_res.data["objects"]

    audit_users = []
    for user in users:
        username = user["name"]
        # user_roles = user["roles"]
        audit_users.append(username)

    # CHECKS #####
    print()
    print("User checks:")
    print(f".only allowed users configured: {CHECK_USERS}...", end="")
    audit_users = set(audit_users)
    if audit_users == CHECK_USERS:
        print("[green]pass[/green]")
    else:
        CHECK_PASSED = False
        print("[red]fail[/red]")

    return CHECK_PASSED


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        check_users(api_client)
        check_password_policy(api_client)


if __name__ == "__main__":
    main()
```

### TB-259: `python_course_mar26/class4/exercises/main_project/gen_fw_rules.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. It defines reusable function(s): `gen_blockedip_fw_rules, gen_mgmt_fw_rules`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
def gen_blockedip_fw_rules():
    blacklisted_ips = [
        {
            "layer": "Network",
            "name": "Blacklisted IPs",
            "source": "Blocked IPs",
            "destination": "Any",
            "service": "Any",
            "action": "Drop",
            "position": 1,
        },
    ]

    return blacklisted_ips


def gen_mgmt_fw_rules(fw_name):
    management_rules = [
        {
            "layer": "Network",
            "name": "Ansible Management Access",
            "source": [
                "Ansible Server",
                "Windows SmartConsole",
                "Windows SmartConsole Public",
            ],
            "destination": fw_name,
            "service": "Any",
            "action": "Accept",
            "position": 2,
        },
        {
            "layer": "Network",
            "name": "SSH Access",
            "source": "Any",
            "destination": fw_name,
            "service": "SSH",
            "action": "Accept",
            "position": 3,
        },
    ]

    return management_rules
```

### TB-260: `python_course_mar26/class4/exercises/main_project/host_objects.py`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. It runs from top to bottom: create values, transform them, and print or return a result.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
smart_console_private = {
    "name": "Windows SmartConsole",
    "ipv4-address": "172.31.12.101",
    "color": "red",
}
smart_console_public = {
    "name": "Windows SmartConsole Public",
    "ipv4-address": "3.71.9.240",
    "color": "red",
}
ansible_server = {
    "name": "Ansible Server",
    "ipv4-address": "3.125.34.232",
    "color": "black",
}
```

### TB-261: `python_course_mar26/class4/run_script/run_script_gaia.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, base64, rich.print, dotenv.load_dotenv, cpapi.APIClient, cpapi.APIClientArgs`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import base64
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        payload = {
            # "script": "ls -al"
            # "script": "cat None"
            # "script": "fw stat"
            # "script": "cphaprob state"
            # "script": "cpstat os -f memory"
            "script": 'clish -c "show interfaces"'
        }

        api_endpoint = "run-script"
        api_res = api_client.api_call(command=api_endpoint, payload=payload)

        if api_res.success:
            tasks = api_res.data["tasks"]
            for task in tasks:
                if task["status"] == "succeeded":
                    b64_result = task["task-details"][0]["output"]
                    bytes_str = base64.b64decode(b64_result)
                    data_str = bytes_str.decode("utf-8")
                    print(data_str)


if __name__ == "__main__":
    main()
```

### TB-262: `python_course_mar26/class4/run_script/run_script_mgmt.py`

**Lab type:** Python fundamentals lab

**Objective:** It talks to a network API, which means Python asks a controller or firewall manager for data or changes.

**What to notice:**

1. First, it brings in helper tools: `os, base64, ipdb, rich.print, dotenv.load_dotenv, cpapi.APIClient`.
2. It defines reusable function(s): `main`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
import base64
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    fw_name = "chkpnt-pod99"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        payload = {
            # "script": "ls -al"
            # "script": "cat None"
            # "script": "fw stat"
            # "script": "cphaprob state"
            # "script": "cpstat os -f memory"
            "script": 'clish -c "show interfaces"',
            "script-name": "Testing Python Automation",
            "targets": [fw_name],
        }

        api_endpoint = "run-script"
        api_res = api_client.api_call(command=api_endpoint, payload=payload)

        if api_res.success:
            tasks = api_res.data["tasks"]
            for task in tasks:
                if task["status"] == "succeeded":
                    b64_result = task["task-details"][0]["responseMessage"]
                    bytes_str = base64.b64decode(b64_result)
                    data_str = bytes_str.decode("utf-8")
                    print(data_str)


if __name__ == "__main__":
    main()
```

---

## Lab Track 19: Credentials, Ownership, and Guardrails

**Concept focus:** separate secrets, authorization, device ownership, and approval checks.

**Mental model:** `operator identity -> permissions -> owned device set -> protected action`

### TB-263: `netmiko_course/class6/collateral/ssh_keys.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "student1",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
    "disable_sha2_fix": True,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-264: `netmiko_course/class6/collateral/ssh_keys_agent.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

# Key file is now encrypted
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "testuser",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa_encr",
    "allow_agent": True,
    "disable_sha2_fix": True,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-265: `netmiko_course/class6/collateral/ssh_keys_encr.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

# Key file is now encrypted
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "testuser",
    # Just make the password be the key passphrase
    "password": "cisco123",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa_encr",
    "disable_sha2_fix": True,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-266: `netmiko_course/class7/collateral/auth_fail.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "invalid",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-267: `netmiko_course/class7/collateral/auth_fail_keys.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "testuser",
    "use_keys": True,
    "key_file": "~/.ssh/id_rsa",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-268: `netmiko_course/class7/collateral/auth_retry.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.NetmikoAuthenticationException`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException


# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "invalid",
}

output = ""
try:
    net_connect = ConnectHandler(**cisco3)
    output = net_connect.send_command("show ip arp")
except NetmikoAuthenticationException:
    print("Initial auth failed")
    cisco3["password"] = password
    net_connect = ConnectHandler(**cisco3)
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-269: `netmiko_course/class7/collateral/auth_retry_func.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.NetmikoAuthenticationException`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `try_passwords`.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException


def try_passwords(device, passwords=None):
    """
    Retry using all of the passwords provided.

    passwords is an iterator of passwords to try.
    """
    if passwords is None:
        passwords = []
    for passwd in passwords:
        device["password"] = passwd
        try:
            net_connect = ConnectHandler(**device)
            break
        except NetmikoAuthenticationException:
            continue
    else:
        # nobreak
        raise NetmikoAuthenticationException("No valid password found.")
    return net_connect


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
    }

    real_password = password
    password_list = ["invalid1", "invalid2", real_password]

    net_connect = try_passwords(cisco3, password_list)
    output = net_connect.send_command("show ip arp")

    print(f"\n{output}\n")
```

### TB-270: `python_course_mar26/class4/ssh_session/mgmt_cli_session.md`

**Lab type:** Reading and design lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Part1: Mgmt CLI Exercise

Using your pod and Netmiko SSH connect to your pod and enter expert mode.

Create a function named 'mgmt_cli_auth' with the following function signature:

'''python
def mgmt_cli_auth(ssh_conn, username, password):
'''

This function should execute the following to login to the mgmt_cli:

'''bash
cmd = f'mgmt_cli login user "{username}" password "{password}" --format json'
'''

Use Netmiko to send this command to the remote pod. Retrieve the response and process it as JSON.

From the returned data structure extract the session ID ("sid" key).

Your function should return this session ID.


### Part2: py.test testing of the 'mgmt_cli_auth' function.

Create a conftest.py file and a fixture named 'ssh_conn'. Your fixture should establish a Netmiko SSH connection to your pod and then "yield" that connection.

Next create pytest test file named "test_mgmt_cli_auth.py". In this test file you should test the 'mgmt_cli_auth' function.

You should test the following test cases:
1. If you provide an invalid username and password, then you should receive a KeyError exception.
2. If you provide valid credentials, then you should receive a session_id that is 43 characters long.

You should ensure your tests pass successfully.
```

### TB-271: `python_course_mar26/class2/gaia_ssh/mgmt_cli_sessions.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, json, sys, time, ipdb, rich.print`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
import json
import sys
import time
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# mS values for various times
ONE_DAY_MS = 86_400_000
ONE_HOUR_MS = 3_600_000

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    # Enter expert mode
    ssh_conn.enable()
    print(ssh_conn.find_prompt())

    # Capture Session ID
    print("Capture Session ID using 'mgmt_cli'")
    cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
    # cmd = f'''mgmt_cli login -r true --format json'''
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    sid = d_struct["sid"]

    # Capture current session
    cmd = f'mgmt_cli show-session --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    my_session_uid = d_struct["uid"]

    cmd = f'mgmt_cli show-sessions details-level "full" --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)

    sessions = d_struct["objects"]
    print(f"Sessions: {len(sessions)}")
    ipdb.set_trace()

    # Enable debugger and quit to accumulate stale sessions
    # ipdb.set_trace()

    print(f"Session Count: {len(sessions)}")
    for session in sessions:
        session_timeout = session["session-timeout"]
        session_uid = session["uid"]

        if session_uid == my_session_uid:
            print("Skipping Current Session...")
            continue

        if meta_info := session.get("meta-info"):
            create_time = meta_info["creation-time"]["iso-8601"]
            epoch_create_time = meta_info["creation-time"]["posix"]
            session_user = meta_info["creator"]
            session_lock = meta_info["lock"]
            msg = f"""
Session User:   {session_user}
Lock: {session_lock}
Session Create Time: {create_time}
Session Timeout: {session_timeout}
"""
            print(msg)

            # *1000 to get current_time the same scale as Chkpnt (i.e. mS)
            current_time = int(time.time() * 1000)

            # Check for sessions under a day old (older sessions are probably SmartConsole)
            if current_time - epoch_create_time < ONE_DAY_MS:
                # Take over the session
                cmd = f'''mgmt_cli take-over-session uid "{session_uid}" --session-id "{sid}" disconnect-active-session true --format json'''
                data = ssh_conn.send_command(cmd, read_timeout=30)
                print(data)
                print("\n>>> Discarding Session >>>")
                print(session_uid)
                print(data)
                print(msg)
                # Discard the session
                cmd = 'mgmt_cli discard\n'
                data = ssh_conn.write_channel(cmd)
                sys.exit(0)
            else:
                print("Session over 24 hours old...retaining")

    # Restore the original session
    cmd = '''mgmt_cli take-over-session uid "{my_session_uid}" --format json'''
    data = ssh_conn.send_command(cmd)
    cmd = f'mgmt_cli logout --session-id "{sid}" --format json'
    data += ssh_conn.send_command(cmd)
    print(data)
```

### TB-272: `python_course_mar26/class4/ssh_session/conftest.py`

**Lab type:** Testing lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `pytest, os, dotenv.load_dotenv, netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. It defines reusable function(s): `ssh_conn`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import pytest
import os
from dotenv import load_dotenv
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def ssh_conn():

    load_dotenv()
    secret = os.environ["CHKP_EXPERT"]

    test_device = {
        "host": "chkpnt-pod99.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "secret": secret,
    }

    with ConnectHandler(**test_device) as ssh_conn:
        ssh_conn.enable()

        # Object that is passed to the tests
        yield ssh_conn
```

### TB-273: `python_course_mar26/class4/ssh_session/mgmt_cli_session.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `os, json, rich.print, netmiko.ConnectHandler, dotenv.load_dotenv`.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `mgmt_cli_auth, main`.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
#!/usr/bin/env python
import os
import json
from rich import print
from netmiko import ConnectHandler

from dotenv import load_dotenv


def mgmt_cli_auth(ssh_conn, username, password):
    """Use 'mgmt_cli' to authenticate and return the session_id."""

    cmd = f'mgmt_cli login user "{username}" password "{password}" --format json'
    auth_data = ssh_conn.send_command(cmd)

    auth_dict = json.loads(auth_data)
    return auth_dict["sid"]


def main():

    load_dotenv()
    secret = os.environ["CHKP_EXPERT"]
    admin_pass = os.environ["CHKP_ADMIN"]

    pod99 = {
        "host": "chkpnt-pod99.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "secret": secret,
    }

    with ConnectHandler(**pod99) as ssh_conn:
        ssh_conn.enable()
        session_id = mgmt_cli_auth(ssh_conn, username="admin", password=admin_pass)

        print(session_id)


if __name__ == "__main__":
    main()
```

### TB-274: `netmiko_course/class6/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

base_device = {
    "device_type": "cisco_ios",
    "username": "student1",
    "password": "cisco123",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
    "disable_sha2_fix": True,
}

cisco3 = base_device.copy()
cisco3["host"] = "cisco3.lasthop.io"
cisco4 = base_device.copy()
cisco4["host"] = "cisco4.lasthop.io"

for device in (cisco3, cisco4):
    with ConnectHandler(**device) as net_connect:
        print()
        print(net_connect.find_prompt())
        print("-" * 12)
        output = net_connect.send_command("show ip arp")
        print(f"{output}\n")
```

### TB-275: `netmiko_course/class6/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

# Keyfile should be encrypted at this point
# note, the passphrase is not provided as we are using an SSH Agent
base_device = {
    "device_type": "cisco_ios",
    "username": "student1",
    "use_keys": True,
    "key_file": "~/.ssh/student_key",
    "allow_agent": True,
    "disable_sha2_fix": True,
}

cisco3 = base_device.copy()
cisco3["host"] = "cisco3.lasthop.io"
cisco4 = base_device.copy()
cisco4["host"] = "cisco4.lasthop.io"

for device in (cisco3, cisco4):
    with ConnectHandler(**device) as net_connect:
        print()
        print(net_connect.find_prompt())
        print("-" * 12)
        output = net_connect.send_command("show ip arp")
        print(f"{output}\n")
```

### TB-276: `netmiko_course/class6/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
3. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
4. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
5. After that, it sends a show command and saves the text that comes back from the device.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "ssh_config_file": "./my_ssh_config",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show users")

print(output)
```

### TB-277: `netmiko_course/class6/exercises/my_ssh_config`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
host jumphost
  IdentitiesOnly yes
  IdentityFile ~/.ssh/my_ssh_key
  User student1
  HostName localhost

host * !jumphost
  User pyclass
  # Force usage of this SSH config file
  ProxyCommand ssh -F ~/netmiko_course/class6/exercises/my_ssh_config -W %h:%p jumphost
```

### TB-278: `netmiko_course/class7/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.NetmikoAuthenticationException`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `netmiko_connect`.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, NetmikoAuthenticationException


def netmiko_connect(device):
    """
    Successful connection returns: (True, connect_obj)

    Failed authentication returns: (False, None)
    """
    try:
        net_connect = ConnectHandler(**device)
        return (True, net_connect)
    except NetmikoAuthenticationException:
        return (False, None)


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    nxos2 = {
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
    }

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if not connect_status:
        print("\nAuthentication failed...retrying\n\n")
        nxos2["password"] = password

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if connect_status:
        print("\nAuthenticated successfully")
        output = net_connect.send_command("show ip arp vrf management")
        print(f"\n{output}\n")

    print()
```

### TB-279: `netmiko_course/class7/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.NetmikoTimeoutException, netmiko.NetmikoAuthenticationException`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `netmiko_connect`.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException


def netmiko_connect(device):
    """
    Successful connection returns: (True, connect_obj)

    Failed authentication returns: (False, None)
    """
    try:
        net_connect = ConnectHandler(**device)
        return (True, net_connect)
    except NetmikoAuthenticationException:
        print("\nAuthentication failed")
        return (False, None)
    except NetmikoTimeoutException:
        print("\nConnection failed")
        return (False, None)


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    nxos2 = {
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
        "port": 8022,
    }

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if not connect_status:
        print("\nInitial connection failed...retrying\n\n")
        nxos2["password"] = password
        nxos2["port"] = 22

    (connect_status, net_connect) = netmiko_connect(nxos2)
    if connect_status:
        print("\nAuthenticated successfully")
        output = net_connect.send_command("show ip arp vrf management")
        print(f"\n{output}\n")

    print()
```

### TB-280: `netmiko_course/class7/exercises/exercise3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.NetmikoTimeoutException, netmiko.NetmikoAuthenticationException, logging`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It defines reusable function(s): `netmiko_connect`.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

import logging

logging.basicConfig(
    filename="netmiko_class7.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)


def netmiko_connect(device_name, device):
    """
    Successful connection returns: (True, connect_obj)

    Failed authentication returns: (False, None)
    """
    hostname = device["host"]
    port = device.get("port", 22)
    msg = ""

    try:
        net_connect = ConnectHandler(**device)
        msg = f"Netmiko connection succesful to {hostname}:{port}"
        logger.info(msg)
        return (True, net_connect)
    except NetmikoAuthenticationException:
        msg = f"Authentication failure to: {device_name} {hostname}:{port}"
    except NetmikoTimeoutException as e:
        if "DNS failure" in str(e):
            msg = (
                f"Device {device_name} failed due to a DNS failure, hostname {hostname}"
            )
        elif "TCP connection to device failed" in str(e):
            msg = f"Netmiko was unable to reach the provided host and port: {hostname}:{port}"

    logger.error(msg)
    return (False, None)


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    # DNS failure
    vmx1 = {
        "name": "vmx1",
        "device_type": "juniper_junos",
        "host": "invalid.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Invalid Port
    vmx2 = {
        "name": "vmx2",
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "port": 8022,
    }

    # Invalid password
    nxos1 = {
        "name": "nxos1",
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
    }

    # Valid - should connect
    nxos2 = {
        "name": "nxos2",
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Create a list containing the successful connections
    connections = []
    for device in (vmx1, vmx2, nxos1, nxos2):
        device_name = device.pop("name")
        conn_status, net_connect = netmiko_connect(device_name, device)
        if conn_status:
            connections.append(net_connect)

    for net_connect in connections:
        print("\nSuccessfully connected to device:")
        print("-" * 20)
        print(net_connect.find_prompt())
        print("\n\n")
```

### TB-281: `netmiko_course/class7/exercises/exercise4.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnLogOnly`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnLogOnly


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    # DNS failure
    vmx1 = {
        "name": "vmx1",
        "device_type": "juniper_junos",
        "host": "invalid.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Invalid Port
    vmx2 = {
        "name": "vmx2",
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "port": 8022,
    }

    # Invalid password
    nxos1 = {
        "name": "nxos1",
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": "invalid",
    }

    # Valid - should connect
    nxos2 = {
        "name": "nxos2",
        "device_type": "cisco_nxos",
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    for device in (vmx1, vmx2, nxos1, nxos2):
        device_name = device.pop("name")
        net_connect = ConnLogOnly(**device)
        if net_connect:
            print("\nSuccessfully connected to device:")
            print("-" * 20)
            print(net_connect.find_prompt())
            print("\n\n")
```

### TB-282: `python_course_mar26/class2/exercises/gaia_ssh_ex/gaia_ssh_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Gaia SSH Exercise1

Connect to your lab pod using Netmiko. You will need to use an SSH key to connect. This connection will require the following Netmiko arguments:

'''python
chkpt_fw = {
    "host": "chkpnt-podN.lasthop.io",       # REPLACE with your pod
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,       # NEEDED for SSH Key
    "key_file": "/home/studentN/.ssh/eu-sshkey.pem",    # REPLACE with your student
}
'''

Using this SSH connection, execute "show arp dynamic all" and print this response out to standard output.

Your output should look similar to the following:

'''bash
$ python gaia_ssh_ex1.py 
Dynamic Arp Parameters

IP Address                 Mac Address                
172.31.32.1             0a:61:33:92:44:55
172.31.128.1            0a:15:04:3a:87:eb
172.31.144.1            0a:be:1f:c0:c1:03
172.31.145.1            0a:ce:8f:94:04:c9

'''
```

### TB-283: `python_course_mar26/class2/exercises/gaia_ssh_ex/gaia_ssh_ex1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `rich.print, netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from rich import print
from netmiko import ConnectHandler

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "session_log": "output.log",
}

with ConnectHandler(**chkpt_fw) as nc:

    cmd = "show arp dynamic all"
    data = nc.send_command(cmd)
    print(data)
```

### TB-284: `python_course_mar26/class2/exercises/gaia_ssh_ex/mgmt_cli_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```markdown
### mgmt_cli SSH Exercise1

Connect to your lab pod using Netmiko. You will once again need to use an SSH key to connect.

You will also need to provide the Check Point "expert" credentials. I recommend you do this by using .env file and the following pattern.

'''python
from dotenv import load_dotenv

# This looks for a .env file and loads it
load_dotenv()
secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]
'''

You will then use this 'secret' variable in your Netmiko ConnectHandler arguments.

Once connected, call the .enable() method to elevate privileges (this should cause you to enter 'expert' mode).

Now execute the following:

'''python
cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
data = ssh_conn.send_command(cmd)
'''

This will cause you to login using 'mgmt_cli'.

Now extract the session ID from the reponse.

'''
# Requires the 'json' library be imported
d_struct = json.loads(data)
sid = d_struct["sid"]
'''

At this point, you should be able to execute mgmt_cli commands using your session ID.

'''
cmd = f'mgmt_cli show-objects type "address-range" --session-id "{sid}" --format json'
data = ssh_conn.send_command(cmd)
'''

Capture the above address range objects and extract them from the returned data structure. The mgmt_cli is returning a JSON string which can convert to Python data structures using 'json.loads(data)'.

Extract the following fields from each of the address range objects: name, ipv4-address-first, ipv4-address-last. 

Finally, print out these three variables to standard output. Your output should look similar to the following:

'''bash
$ python mgmt_cli_ex1.py 
Capture Session ID using 'mgmt_cli'

Address Ranges:
------------------------------
All_Internet -> 0.0.0.0 to 255.255.255.255
LocalMachine_Loopback -> 127.0.0.1 to 127.255.255.255
------------------------------

'''
```

### TB-285: `python_course_mar26/class2/exercises/gaia_ssh_ex/mgmt_cli_ex1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, json, time, ipdb, rich.print, dotenv.load_dotenv`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
import json
import time
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()
secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    # Enter expert mode
    ssh_conn.enable()

    # Capture Session ID
    print("Capture Session ID using 'mgmt_cli'")
    cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    sid = d_struct["sid"]

    # Capture address range objects
    cmd = f'mgmt_cli show-objects type "address-range" --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)

    # Convert JSON-string to data structure
    d_struct = json.loads(data)
    address_ranges = d_struct["objects"]

    print()
    print("Address Ranges:")
    print("-" * 30)
    for addr_range in address_ranges:
        ar_name = addr_range["name"]
        start_ip = addr_range['ipv4-address-first']
        end_ip = addr_range['ipv4-address-last']
        print(f"{ar_name} -> {start_ip} to {end_ip}")
    print("-" * 30)
    print()
```

### TB-286: `netmiko_course/class6/collateral/lab_devices.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
# Dictionaries are devices
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass

# Any list is group of devices
cisco:
  - cisco3
  - cisco4

arista:
  - arista1
  - arista2
  - arista3
  - arista4

juniper:
  - vmx1
  - vmx2

nxos:
  - nxos1
  - nxos2
```

### TB-287: `netmiko_course/class6/collateral/ssh_config_file.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
3. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
4. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
5. After that, it sends a show command and saves the text that comes back from the device.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
#!/usr/bin/env python
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "ssh_config_file": "~/.ssh/ssh_config",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show users")

print(output)
```

### TB-288: `netmiko_course/class6/collateral/ssh_notes.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
# Encrypt an existing SSH key
ssh-keygen -o -p -f ./test_rsa

# Run SSH Agent
ssh-agent 

# Obviously, with the right values 
SSH_AUTH_SOCK=/tmp/ssh-7PGNJNwQ9OgN/agent.30115; export SSH_AUTH_SOCK;
SSH_AGENT_PID=30116; export SSH_AGENT_PID;

# Add keys to SSH Agent
ssh-add ~/.ssh/test_rsa
ssh-add -l

# Paramiko will automatically look for:
# Any “id_rsa”, “id_dsa” or “id_ecdsa” key discoverable in ~/.ssh/
```

### TB-289: `netmiko_course/class6/collateral/ssh_proxy_jump.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `os, netmiko.ConnectHandler, getpass.getpass`.
3. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
4. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
5. After that, it sends a show command and saves the text that comes back from the device.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "ssh_config_file": "/home/kbyers/.ssh/ssh_config_proxyjump",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show users")

print(output)
```

### TB-290: `netmiko_course/class7/collateral/banner_fail.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "testuser",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa",
    "banner_timeout": 1,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-291: `netmiko_course/class7/collateral/conn_log.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `logging, netmiko.ConnLogOnly, devices.cisco3, devices.cisco4, devices.arista1, devices.arista2`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import logging
from netmiko import ConnLogOnly
from devices import cisco3, cisco4, arista1, arista2


log_level = logging.INFO
log_file = "my_output.log"

for device in (cisco3, cisco4, arista1, arista2):
    net_connect = ConnLogOnly(log_file=log_file, log_level=log_level, **device)
    if net_connect:
        print(net_connect.find_prompt())
```

### TB-292: `netmiko_course/class7/collateral/devices.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from getpass import getpass

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_xe",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "invalid",
}

cisco4 = {
    "device_type": "cisco_xe",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "port": 8022,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
}
```

### TB-293: `netmiko_course/class7/collateral/dns_fail.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "invalid.lasthop.io",
    "username": "testuser",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa",
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-294: `netmiko_course/class7/collateral/handle_failures.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, yaml, getpass.getpass, netmiko.ConnectHandler, netmiko.NetmikoAuthenticationException, netmiko.NetmikoTimeoutException`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. It defines reusable function(s): `load_devices, netmiko_conn`.
5. It reads or writes files, which is how automation remembers inventory, commands, or reports.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
import yaml
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def netmiko_conn(device):
    try:
        conn = ConnectHandler(**device)
        return conn
    except NetmikoTimeoutException as e:
        if "DNS failure" in str(e):
            print("DNS failure")
        elif "TCP connection to device failed" in str(e):
            print("TCP connection failure")
        else:
            raise
    except NetmikoAuthenticationException:
        print("Authentication failure")
    except SSHException as e:
        if "Error reading SSH protocol banner" in str(e):
            print("SSH banner error")
        else:
            raise

    return None


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )
    my_devices = load_devices()

    for device_name, device in my_devices.items():
        device["password"] = password
        conn = netmiko_conn(device)
        if conn is None:
            continue
        print(conn.find_prompt())
```

### TB-295: `netmiko_course/class7/collateral/lab_devices.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
cisco3:
  device_type: cisco_xe
  host: invalid.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass
  port: 8022

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass
  password: invalid

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass
```

### TB-296: `netmiko_course/class7/collateral/tcp_conn_fail.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "testuser",
    "use_keys": True,
    "key_file": "~/.ssh/test_rsa",
    "port": 8022,
    "conn_timeout": 8,
}

with ConnectHandler(**cisco3) as net_connect:
    output = net_connect.send_command("show ip arp")

print(f"\n{output}\n")
```

### TB-297: `python_course_mar26/class2/gaia_ssh/cfg_domain_name.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. Then it sends configuration commands, which is the part that can change a real device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:

    print(ssh_conn.find_prompt())

    cmd = "set domainname lasthop.io"
    data = ssh_conn.send_config_set(cmd)
    data += ssh_conn.save_config()
    print(data)
```

### TB-298: `python_course_mar26/class2/gaia_ssh/retrieve_fingerprint.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, rich.print, dotenv.load_dotenv, netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    # "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    print(ssh_conn.find_prompt())

    # Enter expert mode
    ssh_conn.enable()
    print(ssh_conn.find_prompt())

    cmd = "fwm fingerprint localhost 443"
    fingerprint = ssh_conn.send_command(cmd)
    # print(f"{fingerprint=}")

    for line in fingerprint.splitlines():
        if "#FINGER" in line:
            print(line)

    data = ssh_conn.exit_enable_mode()
```

### TB-299: `python_course_mar26/class2/gaia_ssh/show_version.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "session_log": "output.log",
}

with ConnectHandler(**chkpt_fw) as nc:
    print(nc.find_prompt())

    cmd = "show version all"
    data = nc.send_command(cmd)
    print(data)
```

### TB-300: `python_course_mar26/class4/concurrency/ssh_procs_ascompleted.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `concurrent.futures.ProcessPoolExecutor, concurrent.futures.as_completed, datetime.datetime, netmiko.ConnectHandler, my_devices.device_list`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. It defines reusable function(s): `ssh_conn`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4

    pool = ProcessPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    # Process as completed
    for future in as_completed(future_list):
        print("Result: " + future.result())

    end_time = datetime.now()
    print(end_time - start_time)
```

### TB-301: `python_course_mar26/class4/concurrency/ssh_procs_ascompleted_cm.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `concurrent.futures.ProcessPoolExecutor, concurrent.futures.as_completed, datetime.datetime, netmiko.ConnectHandler, my_devices.device_list`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. It defines reusable function(s): `ssh_conn`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4

    # Use context manager to gracefully cleanup the pool
    with ProcessPoolExecutor(max_threads) as pool:
        future_list = []
        for a_device in device_list:
            future = pool.submit(ssh_conn, a_device)
            future_list.append(future)

        # Process as completed
        for future in as_completed(future_list):
            print("Result: " + future.result())

        end_time = datetime.now()
        print(end_time - start_time)
```

### TB-302: `python_course_mar26/class4/concurrency/ssh_threads_ascompleted.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `concurrent.futures.ThreadPoolExecutor, concurrent.futures.as_completed, datetime.datetime, netmiko.ConnectHandler, my_devices.device_list`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. It defines reusable function(s): `ssh_conn`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    # Process as completed
    for future in as_completed(future_list):
        print("Result: " + future.result())

    end_time = datetime.now()
    print(end_time - start_time)
```

### TB-303: `python_course_mar26/class4/concurrency/ssh_threads_ascompleted_cm.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `concurrent.futures.ThreadPoolExecutor, concurrent.futures.as_completed, datetime.datetime, netmiko.ConnectHandler, my_devices.device_list`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. It defines reusable function(s): `ssh_conn`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4

    # Use context manager to gracefully cleanup the pool
    with ThreadPoolExecutor(max_threads) as pool:
        future_list = []
        for a_device in device_list:
            future = pool.submit(ssh_conn, a_device)
            future_list.append(future)

        # Process as completed
        for future in as_completed(future_list):
            print("Result: " + future.result())

        end_time = datetime.now()
        print(end_time - start_time)
```

### TB-304: `python_course_mar26/class4/concurrency/ssh_threads_wait.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `concurrent.futures.ThreadPoolExecutor, concurrent.futures.wait, datetime.datetime, netmiko.ConnectHandler, my_devices.device_list`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. It defines reusable function(s): `ssh_conn`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    return net_connect.find_prompt()


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        print("Result: " + future.result())

    end_time = datetime.now()
    print(end_time - start_time)
```

### TB-305: `python_course_mar26/work/ssh_conn_ex.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler, rich.print`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It defines reusable function(s): `main`.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler
from rich import print


def main():

    pod1 = {
        "host": "chkpnt-pod1.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "session_log": "output.log",
    }
    pod99 = {
        "host": "chkpnt-pod99.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "session_log": "output.log",
    }

    for device in (pod1, pod99):
        with ConnectHandler(**device) as ssh_conn:
            print(f"Our device is: {device['host']}:")
            cmd = "show interfaces all"
            data = ssh_conn.send_command(cmd)

            intf_dict = {}
            intf_name = ""
            ip_addr = ""
            for line in data.splitlines():
                if line.startswith("Interface"):
                    fields = line.split()
                    intf_name = fields[1]
                if "ipv4-address" in line:
                    fields = line.split()
                    ip_addr = fields[1]

                if intf_name and ip_addr:
                    intf_dict[intf_name] = ip_addr

            print(intf_dict)
            print()


if __name__ == "__main__":
    main()
```

---

## Lab Track 20: Operating and Deploying Automation

**Concept focus:** package scripts, run checks, log sessions, and prepare production workflows.

**Mental model:** `local script -> config/logging/tests -> scheduled run -> operational report`

### TB-306: `netmiko_course/class9/collateral/get_file.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.file_transfer`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "test2.txt"
dest_file = "test2.txt"
direction = "get"
file_system = "flash:"

ssh_conn = ConnectHandler(**cisco3)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    # Overwrite the target file (if it already exists)
    overwrite_file=True,  # default "will not overwrite"
    # verify_file=True,     # default "will verify"
)
print(transfer_dict)
ssh_conn.disconnect()
```

### TB-307: `netmiko_course/class9/collateral/put_file.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.file_transfer`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "test2.txt"
dest_file = "test2.txt"
direction = "put"
file_system = "flash:"

ssh_conn = ConnectHandler(**cisco3)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,  # default "will not overwrite"
    inline_transfer=True,
)
ssh_conn.disconnect()
print(transfer_dict)
```

### TB-308: `netmiko_course/deploy.sh`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. This is a shell helper script.
2. It strings together command-line steps so the same setup or test can be repeated.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```bash
#mkdir class2/collateral
#mkdir class2/exercises
#touch class2/collateral/empty.txt
#touch class2/exercises/empty.txt

mkdir class3/collateral
mkdir class3/exercises
touch class3/collateral/empty.txt
touch class3/exercises/empty.txt

mkdir class4/collateral
mkdir class4/exercises
touch class4/collateral/empty.txt
touch class4/exercises/empty.txt

mkdir class5/collateral
mkdir class5/exercises
touch class5/collateral/empty.txt
touch class5/exercises/empty.txt

mkdir class6/collateral
mkdir class6/exercises
touch class6/collateral/empty.txt
touch class6/exercises/empty.txt

mkdir class7/collateral
mkdir class7/exercises
touch class7/collateral/empty.txt
touch class7/exercises/empty.txt

mkdir class8/collateral
mkdir class8/exercises
touch class8/collateral/empty.txt
touch class8/exercises/empty.txt

mkdir class9/collateral
mkdir class9/exercises
touch class9/collateral/empty.txt
touch class9/exercises/empty.txt
```

### TB-309: `netmiko_course/tests.sh`

**Lab type:** Testing lab

**Objective:** It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure.

**What to notice:**

1. This is a shell helper script.
2. It strings together command-line steps so the same setup or test can be repeated.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```bash
#!/bin/bash

RETURN_CODE=0

echo "pylama ." \
&& pylama . \
&& echo "black" \
&& black --check . \
&& echo "running pytest..." \
&& cd tests \
&& py.test -x -s -v test_class1.py \
&& py.test -x -s -v test_class2.py \
&& py.test -x -s -v test_class3.py \
&& py.test -x -s -v test_class4.py \
&& py.test -x -s -v test_class5.py \
&& py.test -x -s -v test_class6.py \
&& py.test -x -s -v test_class7.py \
&& py.test -x -s -v test_class8.py \
&& py.test -x -s -v test_class9.py \
&& py.test -x -s -v test_class10.py \
&& py.test -x -s -v test_class11.py \
&& py.test -x -s -v test_class12.py \
\
|| RETURN_CODE=1

exit $RETURN_CODE
```

### TB-310: `netmiko_course/class9/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.file_transfer`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Finally, it disconnects so the network session is not left hanging open.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}
cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "cfg_name_servers.txt"
dest_file = "cfg_name_servers.txt"
direction = "put"
file_system = "flash:"

for device in (cisco3, cisco4):
    ssh_conn = ConnectHandler(**device)
    print("\n\n")
    print("-" * 20)
    print(f"\nTransferring configuration file: {device['host']}")
    transfer_dict = file_transfer(
        ssh_conn,
        source_file=source_file,
        dest_file=dest_file,
        file_system=file_system,
        direction=direction,
        overwrite_file=True,  # default "will not overwrite"
    )
    file_exists = transfer_dict["file_exists"]
    md5_verify = transfer_dict["file_verified"]

    # Merge configuration change
    if file_exists and md5_verify:
        cmd = f"copy {file_system}/{ dest_file } system:running-config"
        output = ssh_conn.send_command_timing(
            cmd, strip_prompt=False, strip_command=False
        )
        # Device will prompt to verify: Destination filename [running-config]?
        if "Destination filename" in output and "running-config" in output:
            output += ssh_conn.send_command_timing(
                "\n", strip_prompt=False, strip_command=False
            )
        print(output)

    # Verify
    name_srv = ssh_conn.send_command("show run | inc name-server").strip()
    if len(name_srv.split()) != 4:
        # Checks there aren't extra name-servers
        print(f"\nThe name servers are not configured properly:\n>>> {name_srv}")
    if "8.8.8.8" in name_srv and "8.8.4.4" in name_srv:
        print("\nName servers are correct.")
    domain_name = ssh_conn.send_command("show run | inc domain")
    if "lasthop.io" in domain_name:
        print("\nDomain name is correct")
    ssh_conn.disconnect()
```

### TB-311: `netmiko_course/class9/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.file_transfer`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `redirect_output, more_file`.
6. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": "output.txt",
}


def redirect_output(ssh_conn, cmd):
    print("\n\nRedirecting 'show interfaces' output to flash:")
    output = ssh_conn.send_command_timing(cmd, strip_prompt=False, strip_command=False)

    # Command will prompt for confirmation if the file already exists
    if "confirm" in output:
        output += ssh_conn.send_command_timing(
            "y", strip_prompt=False, strip_command=False
        )
    return output


def more_file(ssh_conn, cmd):
    """Verify file was saved into flash:"""

    print("\nVerifying 'show interfaces' file exists on flash:")
    output_verify = ssh_conn.send_command(cmd)
    if "GigabitEthernet0/0/0" not in output_verify:
        raise ValueError(f"{cmd} does not contain expected value in output")
    return output_verify


if __name__ == "__main__":

    # Secure copy server must be enable on the device ('ip scp server enable')
    source_file = "show_interfaces_ktb.txt"
    dest_file = source_file
    direction = "get"
    file_system = "flash:"

    with ConnectHandler(**cisco3) as ssh_conn:

        # show interfaces | redirect flash:/show_interfaces_ktb.txt
        cmd = f"show interfaces | redirect {file_system}/{source_file}"
        redirect_output(ssh_conn, cmd)

        # more flash:/show_interfaces_ktb.txt
        cmd = f"more {file_system}/{source_file}"
        more_file(ssh_conn, cmd)

        # SCP Get the file
        print("\nRetrieving the file using SCP Get")
        transfer_dict = file_transfer(
            ssh_conn,
            source_file=source_file,
            dest_file=dest_file,
            file_system=file_system,
            direction=direction,
            # Overwrite the target file (if it already exists)
            overwrite_file=True,
        )
        file_exists = transfer_dict["file_exists"]
        md5_verify = transfer_dict["file_verified"]
        if file_exists and md5_verify:
            print("\n'show interfaces' file successfully transferred")
        else:
            raise ValueError("Error in transferring the file.")
```

### TB-312: `netmiko_course/class9/collateral/get_progress_bar.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.file_transfer, netmiko.progress_bar`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer, progress_bar

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "testx.txt"
dest_file = "testx.txt"
direction = "get"
file_system = "flash:"

ssh_conn = ConnectHandler(**cisco3)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
    progress4=progress_bar,
)
print(transfer_dict)
ssh_conn.disconnect()
```

### TB-313: `netmiko_course/class9/collateral/put_progress_bar.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.file_transfer, netmiko.progress_bar`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, file_transfer, progress_bar

# Code so automated tests will run properly
password = os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()

# Need a privilege15 account (no enable call)
cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

# Secure copy server must be enable on the device ('ip scp server enable')
source_file = "testx.txt"
dest_file = "testx.txt"
direction = "put"
file_system = "flash:"

ssh_conn = ConnectHandler(**cisco3)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,  # default "will not overwrite"
    progress4=progress_bar,
)
ssh_conn.disconnect()
print(transfer_dict)
```

### TB-314: `netmiko_course/class11/exercises/exercise1_final.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.redispatch`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, redispatch


if __name__ == "__main__":

    debug = True
    arista4_internal_ip = "10.220.88.31"
    ssh_cmd = f"ssh -l pyclass {arista4_internal_ip}"

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "output.txt",
    }

    # Connect to Cisco3 using Netmiko
    print()
    print(f"Connecting to: {cisco3['host']}")
    net_connect = ConnectHandler(**cisco3)

    # Ensure connected to cisco3
    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    if "cisco3" not in prompt:
        raise ValueError(f"Expecting 'cisco3' in prompt: {prompt}")
    if "CiscoIosSSH" not in str(net_connect):
        raise ValueError(
            f"Expecting CiscoIosSSH class at this point: {str(net_connect)}"
        )
    print(f"Current class: {str(net_connect)}")

    # SSH to Arista4 from Cisco3
    print("\nSSH from Cisco3 to Arista4:")
    output = net_connect.send_command(
        ssh_cmd, expect_string=r"ssword", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        password, strip_prompt=False, strip_command=False
    )
    if debug:
        print(">>>>")
        print(output)
        print(">>>>")

    prompt = net_connect.find_prompt()
    if "arista4" not in prompt:
        raise ValueError(f"Expecting 'arista4' in prompt: {prompt}")

    # Use redispatch to switch the Netmiko class
    print("\nUse redispatch to switch the class.")
    redispatch(net_connect, device_type="arista_eos")
    print(f"Current class: {str(net_connect)}")

    if "AristaSSH" not in str(net_connect):
        raise ValueError(f"Expecting AristaSSH class at this point: {str(net_connect)}")

    # Exit Arista device
    print("\nExit from 'arista4'")
    output = net_connect.send_command_timing("exit\n")

    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    if "cisco3" not in prompt:
        raise ValueError(f"Expecting 'cisco3' in prompt: {prompt}")

    # Exit Cisco device
    print("\nExit from 'cisco3' device; completely close SSH session.")
    output = net_connect.send_command_timing("exit\n")
```

### TB-315: `netmiko_course/class11/exercises/exercise1a.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.redispatch`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, redispatch


if __name__ == "__main__":

    debug = True
    arista4_internal_ip = "10.220.88.31"
    ssh_cmd = f"ssh -l pyclass {arista4_internal_ip}"

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Connect to Cisco3 using Netmiko
    print()
    print(f"Connecting to: {cisco3['host']}")
    net_connect = ConnectHandler(**cisco3)

    # Ensure connected to cisco3
    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    print(f"Current class: {str(net_connect)}")

    # SSH to Arista4 from Cisco3
    print("\nSSH from Cisco3 to Arista4:")
    output = net_connect.send_command(
        ssh_cmd, expect_string=r"ssword", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        password, strip_prompt=False, strip_command=False
    )
    if debug:
        print(">>>>")
        print(output)
        print(">>>>")

    prompt = net_connect.find_prompt()

    # Use redispatch to switch the Netmiko class
    print("\nUse redispatch to switch the class.")
    redispatch(net_connect, device_type="arista_eos")
    print(f"Current class: {str(net_connect)}")
```

### TB-316: `netmiko_course/class11/exercises/exercise1b.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.redispatch`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, redispatch


if __name__ == "__main__":

    debug = True
    arista4_internal_ip = "10.220.88.31"
    ssh_cmd = f"ssh -l pyclass {arista4_internal_ip}"

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Connect to Cisco3 using Netmiko
    print()
    print(f"Connecting to: {cisco3['host']}")
    net_connect = ConnectHandler(**cisco3)

    # Ensure connected to cisco3
    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    if "cisco3" not in prompt:
        raise ValueError(f"Expecting 'cisco3' in prompt: {prompt}")
    if "CiscoIosSSH" not in str(net_connect):
        raise ValueError(
            f"Expecting CiscoIosSSH class at this point: {str(net_connect)}"
        )
    print(f"Current class: {str(net_connect)}")

    # SSH to Arista4 from Cisco3
    print("\nSSH from Cisco3 to Arista4:")
    output = net_connect.send_command(
        ssh_cmd, expect_string=r"ssword", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        password, strip_prompt=False, strip_command=False
    )
    if debug:
        print(">>>>")
        print(output)
        print(">>>>")

    prompt = net_connect.find_prompt()
    if "arista4" not in prompt:
        raise ValueError(f"Expecting 'arista4' in prompt: {prompt}")

    # Use redispatch to switch the Netmiko class
    print("\nUse redispatch to switch the class.")
    redispatch(net_connect, device_type="arista_eos")
    print(f"Current class: {str(net_connect)}")

    if "AristaSSH" not in str(net_connect):
        raise ValueError(f"Expecting AristaSSH class at this point: {str(net_connect)}")
```

### TB-317: `netmiko_course/class11/exercises/exercise1c.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler, netmiko.redispatch`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
from getpass import getpass
from netmiko import ConnectHandler, redispatch


if __name__ == "__main__":

    debug = True
    arista4_internal_ip = "10.220.88.31"
    ssh_cmd = f"ssh -l pyclass {arista4_internal_ip}"

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    # Connect to Cisco3 using Netmiko
    print()
    print(f"Connecting to: {cisco3['host']}")
    net_connect = ConnectHandler(**cisco3)

    # Ensure connected to cisco3
    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    if "cisco3" not in prompt:
        raise ValueError(f"Expecting 'cisco3' in prompt: {prompt}")
    if "CiscoIosSSH" not in str(net_connect):
        raise ValueError(
            f"Expecting CiscoIosSSH class at this point: {str(net_connect)}"
        )
    print(f"Current class: {str(net_connect)}")

    # SSH to Arista4 from Cisco3
    print("\nSSH from Cisco3 to Arista4:")
    output = net_connect.send_command(
        ssh_cmd, expect_string=r"ssword", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        password, strip_prompt=False, strip_command=False
    )
    if debug:
        print(">>>>")
        print(output)
        print(">>>>")

    prompt = net_connect.find_prompt()
    if "arista4" not in prompt:
        raise ValueError(f"Expecting 'arista4' in prompt: {prompt}")

    # Use redispatch to switch the Netmiko class
    print("\nUse redispatch to switch the class.")
    redispatch(net_connect, device_type="arista_eos")
    print(f"Current class: {str(net_connect)}")

    if "AristaSSH" not in str(net_connect):
        raise ValueError(f"Expecting AristaSSH class at this point: {str(net_connect)}")

    # Exit Arista device
    print("\nExit from 'arista4'")
    output = net_connect.send_command_timing("exit\n")

    prompt = net_connect.find_prompt()
    if debug:
        print(f"\nCurrent prompt: {prompt}")
    if "cisco3" not in prompt:
        raise ValueError(f"Expecting 'cisco3' in prompt: {prompt}")

    # Exit Cisco device
    print("\nExit from 'cisco3' device; completely close SSH session.")
    output = net_connect.send_command_timing("exit\n")
```

### TB-318: `netmiko_course/class8/exercises/exercise1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, concurrent.futures.ThreadPoolExecutor, concurrent.futures.wait, getpass.getpass, utilities.load_devices, utilities.ssh_conn`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from concurrent.futures import ThreadPoolExecutor, wait
from getpass import getpass

# Store certain functions in another module so the can be used across multiple exercises.
from utilities import load_devices, ssh_conn


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    device_list = my_devices["all"]
    pool = ThreadPoolExecutor(20)

    cmd_dict = {"cisco_nxos": "show ip arp vrf management", "juniper_junos": "show arp"}

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        platform = device_dict["device_type"]

        # If cmd is not in cmd_dict, default to "show ip arp"
        cmd = cmd_dict.get(platform, "show ip arp")
        future = pool.submit(
            ssh_conn, device_name=device_name, device_dict=device_dict, cmd=cmd
        )
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    # Display the results
    for future in future_list:
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()
```

### TB-319: `netmiko_course/class8/exercises/exercise2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, concurrent.futures.ProcessPoolExecutor, concurrent.futures.as_completed, getpass.getpass, utilities.load_devices, utilities.ssh_conn`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from getpass import getpass

# Store certain functions in another module so the can be used across multiple exercises.
from utilities import load_devices, ssh_conn


if __name__ == "__main__":

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    device_list = my_devices["all"]
    pool = ProcessPoolExecutor(20)

    cmd_dict = {"cisco_nxos": "show ip arp vrf management", "juniper_junos": "show arp"}

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        platform = device_dict["device_type"]

        # If cmd is not in cmd_dict, default to "show ip arp"
        cmd = cmd_dict.get(platform, "show ip arp")
        future = pool.submit(
            ssh_conn, device_name=device_name, device_dict=device_dict, cmd=cmd
        )
        future_list.append(future)

    # Display the results
    for future in as_completed(future_list):
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()

    # There is an odd concurrent futures exception if you don't cleanup the pool gracefully.
    del pool
```

### TB-320: `netmiko_course/class8/exercises/lab_devices.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass


# Any list is group of devices
cisco:
  - cisco3
  - cisco4

arista:
  - arista1
  - arista2
  - arista3
  - arista4

juniper:
  - vmx1
  - vmx2

nxos:
  - nxos1
  - nxos2

all:
  - arista1
  - arista2
  - arista3
  - arista4
  - cisco3
  - cisco4
  - vmx1
  - vmx2
  - nxos1
  - nxos2
```

### TB-321: `netmiko_course/class8/exercises/utilities.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `netmiko.ConnectHandler, yaml`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It defines reusable function(s): `load_devices, ssh_conn`.
5. It reads or writes files, which is how automation remembers inventory, commands, or reports.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
from netmiko import ConnectHandler
import yaml


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device_name, device_dict, cmd=None):
    with ConnectHandler(**device_dict) as net_connect:
        if cmd is None:
            return net_connect.find_prompt()
        else:
            output = net_connect.send_command(cmd)
            return (device_name, output)
```

### TB-322: `netmiko_course/class9/exercises/cfg_name_servers.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
no ip name-server 1.1.1.1
no ip name-server 1.0.0.1
ip name-server 8.8.8.8
ip name-server 8.8.4.4
ip domain name lasthop.io
```

### TB-323: `netmiko_course/class9/exercises/show_interfaces_ktb.txt`

**Lab type:** Python fundamentals lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
GigabitEthernet0/0/0 is up, line protocol is up 
  Hardware is C1111-2x1GE, address is a093.5141.b780 (bia a093.5141.b780)
  Internet address is 10.220.88.22/24
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  Full Duplex, 100Mbps, link type is auto, media type is RJ45
  output flow-control is off, input flow-control is off
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:02, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 4000 bits/sec, 5 packets/sec
  5 minute output rate 6000 bits/sec, 6 packets/sec
     12503976 packets input, 1549063563 bytes, 0 no buffer
     Received 77240 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 9931939 multicast, 0 pause input
     4837937 packets output, 1541010289 bytes, 0 underruns
     Output 68 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 1 interface resets
     35 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/0/1 is administratively down, line protocol is down 
  Hardware is C1111-2x1GE, address is a093.5141.b781 (bia a093.5141.b781)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  Full Duplex, 1000Mbps, link type is auto, media type is RJ45
  output flow-control is on, input flow-control is on
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 packets output, 0 bytes, 0 underruns
     Output 0 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1/0 is down, line protocol is down (notconnect) 
  Hardware is C1111-ES-4, address is a093.5141.b788 (bia a093.5141.b788)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  Auto-duplex, Auto-speed, link type is auto, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1/1 is down, line protocol is down (notconnect) 
  Hardware is C1111-ES-4, address is a093.5141.b789 (bia a093.5141.b789)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  Auto-duplex, Auto-speed, link type is auto, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1/2 is down, line protocol is down (notconnect) 
  Hardware is C1111-ES-4, address is a093.5141.b78a (bia a093.5141.b78a)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  Auto-duplex, Auto-speed, link type is auto, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     0 packets output, 0 bytes, 0 underruns
     Output 0 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1/3 is down, line protocol is down (notconnect) 
  Hardware is C1111-ES-4, address is a093.5141.b78b (bia a093.5141.b78b)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive not supported 
  Auto-duplex, Auto-speed, link type is auto, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
```

_Source excerpt shown: first 160 of 222 lines. Use the repository file for the full data/output sample._

### TB-324: `python_course_mar26/class4/exercises/concurrency_ex/concurrency_ex.md`

**Lab type:** Reading and design lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Concurrency Exercise

Connect using a thread pool and Netmiko to pods1-5. Your thread pool size should be set to 5.

Using threads execute "show interface eth0" and retreive the output. You should also record your hostname in the thread result (so you know which device the result came from). 

Use the "as_completed" pattern to print out the results as they are returned. However, only display the device hostname and the "ipv4-address" from the "show interface" output.

Record and print the total execution time for your script. 

Change the thread pool size to 2 and see how it changes your execution time.

Optional: Convert from threads over to processes. Use a process pool size of 5 and compare the execution time (threads to processes).
```

### TB-325: `python_course_mar26/class4/exercises/concurrency_ex/concurrency_ex.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `concurrent.futures.ThreadPoolExecutor, concurrent.futures.as_completed, datetime.datetime, netmiko.ConnectHandler, my_devices.device_list`.
2. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
3. After that, it sends a show command and saves the text that comes back from the device.
4. It defines reusable function(s): `ssh_conn`.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
# Pool size 5: 0:00:02.135320 (Threads)
# Pool size 2: 0:00:06.356690 (Threads)
#
# Pool size 5: 0:00:02.155889 (Processes)
from concurrent.futures import ThreadPoolExecutor, as_completed

# from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    host = net_connect.host
    cmd = "show interface eth0"
    data = net_connect.send_command(cmd)
    return (host, data)


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 5

    pool = ThreadPoolExecutor(max_threads)
    # pool = ProcessPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    # Process as completed
    print()
    for future in as_completed(future_list):
        (host, result) = future.result()
        print(f"\n{host}:")
        print("-" * 20)
        for line in result.splitlines():
            if "ipv4-address" in line:
                print(line)
        print()

    end_time = datetime.now()
    print()
    print(end_time - start_time)
    print()
```

### TB-326: `python_course_mar26/class4/exercises/concurrency_ex/my_devices.py`

**Lab type:** Python fundamentals lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. First, it brings in helper tools: `os, dotenv.load_dotenv`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from dotenv import load_dotenv


# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw1 = {
    "host": "chkpnt-pod1.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}
chkpt_fw2 = {
    "host": "chkpnt-pod2.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw3 = {
    "host": "chkpnt-pod3.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw4 = {
    "host": "chkpnt-pod4.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw5 = {
    "host": "chkpnt-pod5.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}


device_list = [chkpt_fw1, chkpt_fw2, chkpt_fw3, chkpt_fw4, chkpt_fw5]
```

### TB-327: `netmiko_course/class11/collateral/redispatch1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, netmiko.ConnectHandler, netmiko.redispatch, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. Then it sends configuration commands, which is the part that can change a real device.
6. Finally, it disconnects so the network session is not left hanging open.
7. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Rewrite the configuration section as a dry run that prints planned commands before sending anything.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
"""
Note: Students won't be able to run this code since the terminal server is not accessible.
"""
import os
import time
from netmiko import ConnectHandler, redispatch
from getpass import getpass

# Code so automated tests will run properly
password = (
    os.getenv("TERM_SERVER_PASSWORD")
    if os.getenv("TERM_SERVER_PASSWORD")
    else getpass()
)

# Code so automated tests will run properly
end_device_pwd = (
    os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
)

term_server = {
    "device_type": "generic_termserver_telnet",
    "host": "184.105.247.69",
    "username": "admin",
    "password": password,
    "session_log": "term_server.out",
}

net_connect = ConnectHandler(**term_server)
net_connect.std_login()
print(net_connect.find_prompt())

net_connect.write_channel("cisco3\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

net_connect.write_channel("\r")
time.sleep(0.5)
net_connect.write_channel("\r")
time.sleep(0.5)
output = net_connect.read_channel()
print(output)

# Now login to the end device
try:
    # If "sername" isn't present assume we are already logged in from a previous session
    if "sername" in output:
        net_connect.username = "pyclass"
        net_connect.password = end_device_pwd
        net_connect.std_login()

    net_connect.secret = end_device_pwd
    net_connect.set_base_prompt()
    print(net_connect.find_prompt())

    # We are fully logged into the end device; we now must switch the Netmiko class
    redispatch(net_connect, device_type="cisco_ios_telnet")

    print(net_connect)
    print(net_connect.send_command("show ip int brief"))
    net_connect.enable()
    print(net_connect.send_config_set("logging buffered 30000"))
    net_connect.write_channel("exit\r")
    time.sleep(0.5)
finally:
    net_connect.disconnect()
```

### TB-328: `netmiko_course/class11/collateral/term_server1.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, getpass.getpass, netmiko.ConnectHandler`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
Note: Students won't be able to run this code since the terminal server is not accessible.
"""
import os
from getpass import getpass
from netmiko import ConnectHandler

# Code so automated tests will run properly
password = (
    os.getenv("TERM_SERVER_PASSWORD")
    if os.getenv("TERM_SERVER_PASSWORD")
    else getpass()
)

term_server = {
    "device_type": "generic_termserver_telnet",
    "host": "184.105.247.69",
    "username": "admin",
    "password": password,
    "session_log": "term_server.out",
}

net_connect = ConnectHandler(**term_server)
net_connect.std_login()
print(net_connect.find_prompt())
net_connect.disconnect()
```

### TB-329: `netmiko_course/class11/collateral/term_server2.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
Note: Students won't be able to run this code since the terminal server is not accessible.
"""
import os
import time
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = (
    os.getenv("TERM_SERVER_PASSWORD")
    if os.getenv("TERM_SERVER_PASSWORD")
    else getpass()
)

term_server = {
    "device_type": "generic_termserver_telnet",
    "host": "184.105.247.69",
    "username": "admin",
    "password": password,
    "session_log": "term_server.out",
}

net_connect = ConnectHandler(**term_server)
net_connect.std_login()
print(net_connect.find_prompt())

net_connect.write_channel("cisco3\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

# Send an extra enter
net_connect.write_channel("\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

net_connect.disconnect()
```

### TB-330: `netmiko_course/class11/collateral/term_server3.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
Note: Students won't be able to run this code since the terminal server is not accessible.
"""
import os
import time
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = (
    os.getenv("TERM_SERVER_PASSWORD")
    if os.getenv("TERM_SERVER_PASSWORD")
    else getpass()
)

term_server = {
    "device_type": "generic_termserver_telnet",
    "host": "184.105.247.69",
    "username": "admin",
    "password": password,
    "session_log": "term_server.out",
}

net_connect = ConnectHandler(**term_server)
net_connect.std_login()
print(net_connect.find_prompt())

net_connect.write_channel("cisco3\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

# Send an extra enter
net_connect.write_channel("\r")
time.sleep(0.5)
net_connect.write_channel("\r")
time.sleep(0.5)
output = net_connect.read_channel()
print(output)

net_connect.disconnect()
```

### TB-331: `netmiko_course/class11/collateral/term_server4.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, time, netmiko.ConnectHandler, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. Finally, it disconnects so the network session is not left hanging open.
5. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.

**Source listing:**

```python
"""
Note: Students won't be able to run this code since the terminal server is not accessible.
"""
import os
import time
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
password = (
    os.getenv("TERM_SERVER_PASSWORD")
    if os.getenv("TERM_SERVER_PASSWORD")
    else getpass()
)

term_server = {
    "device_type": "generic_termserver_telnet",
    "host": "184.105.247.69",
    "username": "admin",
    "password": password,
    "session_log": "term_server.out",
}

net_connect = ConnectHandler(**term_server)
net_connect.std_login()
print(net_connect.find_prompt())

net_connect.write_channel("cisco3\r")
time.sleep(1)
output = net_connect.read_channel()
print(output)

# Try to find the
net_connect.write_channel("\r")
time.sleep(0.5)
net_connect.write_channel("\r")
time.sleep(0.5)
output = net_connect.read_channel()
print(output)

# Now login to the end device
if "sername" in output:

    # Code so automated tests will run properly
    end_device_pwd = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    net_connect.username = "pyclass"
    net_connect.password = end_device_pwd
    net_connect.std_login()
    print(net_connect.find_prompt())

net_connect.disconnect()
```

### TB-332: `netmiko_course/class8/collateral/cf_processes.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, yaml, concurrent.futures.ProcessPoolExecutor, concurrent.futures.wait, datetime.datetime, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `load_devices, ssh_conn`.
6. It reads or writes files, which is how automation remembers inventory, commands, or reports.
7. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
import os
import yaml
from concurrent.futures import ProcessPoolExecutor, wait
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device_name, device_dict, cmd=None):
    with ConnectHandler(**device_dict) as net_connect:
        if cmd is None:
            return net_connect.find_prompt()
        else:
            output = net_connect.send_command(cmd)
            return (device_name, output)


if __name__ == "__main__":

    start_time = datetime.now()

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    arista_list = my_devices["arista"]
    cisco_list = my_devices["cisco"]
    nxos_list = my_devices["nxos"]
    device_list = arista_list + cisco_list + nxos_list

    max_procs = 20

    pool = ProcessPoolExecutor(max_procs)

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        # future = pool.submit(ssh_conn, device_name, device_dict, "show ip arp")
        future = pool.submit(
            ssh_conn,
            device_name=device_name,
            device_dict=device_dict,
            cmd="show ip arp",
        )
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()

    # There is an odd concurrent futures exception if you don't cleanup the pool gracefully.
    del pool
    end_time = datetime.now()
    print(end_time - start_time)
```

### TB-333: `netmiko_course/class8/collateral/cf_threads.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, yaml, concurrent.futures.ThreadPoolExecutor, concurrent.futures.wait, datetime.datetime, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `load_devices, ssh_conn`.
6. It reads or writes files, which is how automation remembers inventory, commands, or reports.
7. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
import yaml
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device_name, device_dict, cmd=None):
    with ConnectHandler(**device_dict) as net_connect:
        if cmd is None:
            return net_connect.find_prompt()
        else:
            output = net_connect.send_command(cmd)
            return (device_name, output)


if __name__ == "__main__":

    start_time = datetime.now()

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    arista_list = my_devices["arista"]
    cisco_list = my_devices["cisco"]
    nxos_list = my_devices["nxos"]
    device_list = arista_list + cisco_list + nxos_list

    max_threads = 20

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        # future = pool.submit(ssh_conn, device_name, device_dict, "show ip arp")
        future = pool.submit(
            ssh_conn,
            device_name=device_name,
            device_dict=device_dict,
            cmd="show ip arp",
        )
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()

    end_time = datetime.now()
    print(end_time - start_time)
```

### TB-334: `netmiko_course/class8/collateral/cf_threads_asc.py`

**Lab type:** Device automation lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. First, it brings in helper tools: `os, yaml, concurrent.futures.ThreadPoolExecutor, concurrent.futures.as_completed, datetime.datetime, getpass.getpass`.
2. Then it gets secrets from the environment or a password prompt, instead of hard-coding them.
3. Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.
4. After that, it sends a show command and saves the text that comes back from the device.
5. It defines reusable function(s): `load_devices, ssh_conn`.
6. It reads or writes files, which is how automation remembers inventory, commands, or reports.
7. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- Mark the exact line where a real network connection begins and list the required safety checks before that line.
- Change the show command to a harmless command in your lab and explain what type of output you expect.

**Source listing:**

```python
import os
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device_name, device_dict, cmd=None):
    with ConnectHandler(**device_dict) as net_connect:
        if cmd is None:
            return net_connect.find_prompt()
        else:
            output = net_connect.send_command(cmd)
            return (device_name, output)


if __name__ == "__main__":

    start_time = datetime.now()

    # Code so automated tests will run properly
    password = (
        os.getenv("NETMIKO_PASSWORD") if os.getenv("NETMIKO_PASSWORD") else getpass()
    )

    my_devices = load_devices()
    arista_list = my_devices["arista"]
    cisco_list = my_devices["cisco"]
    nxos_list = my_devices["nxos"]
    device_list = arista_list + cisco_list + nxos_list

    max_threads = 20

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        # future = pool.submit(ssh_conn, device_name, device_dict, "show ip arp")
        future = pool.submit(
            ssh_conn,
            device_name=device_name,
            device_dict=device_dict,
            cmd="show ip arp",
        )
        future_list.append(future)

    for future in as_completed(future_list):
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()

    end_time = datetime.now()
    print(end_time - start_time)
```

### TB-335: `netmiko_course/class8/collateral/lab_devices.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass


# Any list is group of devices
cisco:
  - cisco3
  - cisco4

arista:
  - arista1
  - arista2
  - arista3
  - arista4

juniper:
  - vmx1
  - vmx2

nxos:
  - nxos1
  - nxos2
```

### TB-336: `netmiko_course/class9/collateral/test.txt`

**Lab type:** API automation lab

**Objective:** It runs the same network task across multiple devices without waiting for one device at a time.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.
- List every exception path and what the script does after the failure.

**Source listing:**

```text
# Script to detect memory leaks. It runs on the Polaris switch.
# $Id: memleak.tcl,v 1.63 2018/02/07 01:41:41 vpendyal Exp $
# Copyright (c) 2015-2019 by Cisco Systems, Inc.
# Author: Veeru Pendyala
#         2 Sep 2015
# Usage: 
#  Copy the tcl script to flash on switch
#  Execute 'tclsh' from IOS prompt
#  Prepare testbed for test (i.e. bringup your sessions etc.)
#  Execute 'memleak_baseline' to get a baseline of memory snapshot
#  Perform the tests like session leave/rejoin, roam etc.
#  Execute 'memleak_detect' to get summary of leak report
# Things to control:
#  What leak types to detect, by default all types enabled except ios_gd_leaks
#  and ios_gdchunk_leaks
#  Modify proc_list variables to add/remove processes from monitoring list
#  Change leak_threshold to whatever you need
#  Control standby flag whether need to monitor stdby procs or not

##########Global variables##########
#Base process list common to all platforms in polaris
set proc_list "ios fman_rp fman_fp repm dbm cli_agent smand plogd hman lman \
               nginx psd btman"
set leak_types "rss_leaks ios_gd_leaks ios_gdchunk_leaks ios_procmem_leaks \
                ios_allocpc_leaks ios_chunk_leaks ios_buffer_leaks bmalloc_leaks \
                bmchunk_leaks tdlmsg_leaks tdldb_leaks mmalloc_leaks smaps_leaks \
                qfp_leaks"
set leak_threshold 0.5
set standby 1
set top_leaks 5
set backtrace_depth 0
set script_version 1.68
set platform ""
set sw_str ""
set rp_str ""
set fp_str ""
set fed_str ""
set qfp_str ""
set sv_enabled 0
set image_version ""
array set mem_base {}
array set mem_latest {}
array set mem {}
set tcl_ios_cmd_max_len 253

##########Procedures##########
proc incr {varName {amount 1}} {
   upvar 1 $varName var
   set var [expr {$var+$amount}]
}

proc union {list1 list2} {
   foreach elem $list1 {
      set cache($elem) 1
   }
   foreach elem $list2 {
      if {![info exists cache($elem)]} {
         lappend list1 $elem
      }
   }
   return $list1
}

proc exec_potential_long_cmd {cmd} {
global tcl_ios_cmd_max_len debug
   if {[string length $cmd] > $tcl_ios_cmd_max_len} {
       set out [get_long_cmd_output $cmd $tcl_ios_cmd_max_len]
   } else {
       if {$debug} {puts "Executing $cmd"}
       set out [exec $cmd]
   }
   return $out
}

proc callsite_action {role action} {
   global proc_list sw_str rp_str fp_str fed_str qfp_str debug
   build_strings $role
   foreach proc $proc_list {
      switch $proc {
         fman_rp {set cmd "deb plat soft mem forwar $sw_str $rp_str alloc call $action"}
         fman_fp {set cmd "deb plat soft mem forwar $sw_str $fp_str alloc call $action"}
         repm {set cmd "deb plat soft mem repl $sw_str $rp_str alloc call $action"}
         cli_agent {set cmd "deb plat soft mem cli-agent $sw_str $rp_str alloc call $action"}
         smand {set cmd "deb plat soft mem shell $sw_str $rp_str alloc call $action"}
         plogd {set cmd "deb plat soft mem logger $sw_str $rp_str alloc call $action"}
         hman {set cmd "deb plat soft mem host-manager $sw_str $rp_str alloc call $action"}
         lman {set cmd "deb plat soft mem license-manager $sw_str $rp_str alloc call $action"}
         bt_logger {set cmd "deb plat soft mem bt-logger $sw_str $rp_str alloc call $action"}
         keyman {continue}
         psd {set cmd "deb plat soft mem pluggable $sw_str $rp_str alloc call $action"}
         tms {set cmd "deb plat soft mem table-manager $sw_str $rp_str alloc call $action"}
         fed {set cmd "deb plat soft mem fed $sw_str $fed_str alloc call $action"}
         platform {set cmd "deb plat soft mem platform $sw_str $rp_str alloc call $action"}
         sif_mgr {set cmd "deb plat soft mem sif $sw_str $rp_str alloc call $action"}
         stack_mgr {set cmd "deb plat soft mem stack $sw_str $rp_str alloc call $action"}
         sessmgrd {set cmd "deb plat soft mem smd $sw_str $rp_str alloc call $action"}
         wncmgrd {set cmd "deb plat soft mem wireless $sw_str $rp_str alloc call $action"}
         odm_proxy {set cmd "deb plat soft mem odm-proxy $sw_str $rp_str alloc call $action"}
         btman {set cmd "deb plat soft mem btrace-m $sw_str $rp_str alloc call $action"}
         pubd {set cmd "deb plat soft mem mdt-pubd $sw_str $rp_str alloc call $action"}
         ndbmand {set cmd "deb plat soft mem ndbman $sw_str $rp_str alloc call $action"}
         pttcd {continue}
         ncsshd {continue}
         confd {continue}
         cmand {set cmd "deb plat soft mem chassis-manager $sw_str $rp_str alloc call $action"}
         cman_fp {set cmd "deb plat soft mem chassis-manager $sw_str $fp_str alloc call $action"}
         cmcc {continue}
         iomd {continue}
         vman {set cmd "deb plat soft mem virt-manager $sw_str $rp_str alloc call $action"}
         rif_mgr {continue}
         cpp_cp_svr {set cmd "deb plat soft mem qfp-control $sw_str $qfp_str alloc callsite $action"}
         cpp_driver {set cmd "deb plat soft mem qfp-driver $sw_str $qfp_str alloc callsite $action"}
         cpp_ha {set cmd "deb plat soft mem qfp-ha $sw_str $qfp_str alloc callsite $action"}
         cpp_sp_svr {set cmd "deb plat soft mem qfp-service $sw_str $qfp_str alloc callsite $action"}
         default {set cmd "deb plat soft mem $proc $sw_str $rp_str alloc call $action"}
      }
      if {[regexp {(.*)_(\d+)$} $proc match myproc instance]} {
          switch $myproc {
              wncd {set cmd "deb plat soft mem wncd $instance $sw_str $rp_str alloc call $action"}
              hman {set cmd "deb plat soft mem host $sw_str $instance alloc call $action"}
              cmcc {set cmd "deb plat soft mem chassis $sw_str $instance alloc call $action"}
              iomd {set cmd "deb plat soft mem iomd $sw_str $instance/0 alloc call $action"}
          }
      }
      if {$debug} {puts "Executing $cmd"}
      set out [exec $cmd]
   }
}

proc callsite_backtrace_action {role proc action callsite_list} {
   global sw_str rp_str fp_str fed_str qfp_str backtrace_depth debug 
   build_strings $role
   switch $proc {
      fman_rp {set cmd "deb plat soft mem forwar $sw_str $rp_str alloc back $action"}
      fman_fp {set cmd "deb plat soft mem forwar $sw_str $fp_str alloc back $action"}
      repm {set cmd "deb plat soft mem repl $sw_str $rp_str alloc back $action"}
      cli_agent {set cmd "deb plat soft mem cli-agent $sw_str $rp_str alloc back $action"}
      smand {set cmd "deb plat soft mem shell $sw_str $rp_str alloc back $action"}
      plogd {set cmd "deb plat soft mem logger $sw_str $rp_str alloc back $action"}
      hman {set cmd "deb plat soft mem host-manager $sw_str $rp_str alloc back $action"}
      lman {set cmd "deb plat soft mem license-manager $sw_str $rp_str alloc back $action"}
      bt_logger {set cmd "deb plat soft mem bt-logger $sw_str $rp_str alloc back $action"}
      psd {set cmd "deb plat soft mem pluggable $sw_str $rp_str alloc back $action"}
      tms {set cmd "deb plat soft mem table-manager $sw_str $rp_str alloc back $action"}
      fed {set cmd "deb plat soft mem fed $sw_str $fed_str alloc back $action"}
      platform {set cmd "deb plat soft mem platform $sw_str $rp_str alloc back $action"}
      sif_mgr {set cmd "deb plat soft mem sif $sw_str $rp_str alloc back $action"}
      stack_mgr {set cmd "deb plat soft mem stack $sw_str $rp_str alloc back $action"}
      sessmgrd {set cmd "deb plat soft mem smd $sw_str $rp_str alloc back $action"}
      wncmgrd {set cmd "deb plat soft mem wireless $sw_str $rp_str alloc back $action"}
      odm_proxy {set cmd "deb plat soft mem odm-proxy $sw_str $rp_str alloc back $action"}
      btman {set cmd "deb plat soft mem btrace-m $sw_str $rp_str alloc back $action"}
      pubd {set cmd "deb plat soft mem mdt-pubd $sw_str $rp_str alloc back $action"}
      ndbmand {set cmd "deb plat soft mem ndbman $sw_str $rp_str alloc back $action"}
      pttcd {return}
      ncsshd {return}
      confd {return}
      cmand {set cmd "deb plat soft mem chassis-manager $sw_str $rp_str alloc back $action"}
      cman_fp {set cmd "deb plat soft mem chassis-manager $sw_str $fp_str alloc back $action"}
      vman {set cmd "deb plat soft mem virt-manager $sw_str $rp_str alloc back $action"}
```

_Source excerpt shown: first 160 of 3172 lines. Use the repository file for the full data/output sample._

### TB-337: `netmiko_course/class9/collateral/test2.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
no logging console
logging buffered 50000
```

### TB-338: `netmiko_course/class9/collateral/testx.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
Cisco IOS
```

### TB-339: `netmiko_course/.netmiko.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
# Dictionaries are devices
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass

# Any list is group of devices
cisco:
  - cisco3
  - cisco4

arista:
  - arista1
  - arista2
  - arista3
  - arista4

juniper:
  - vmx1
  - vmx2

nxos:
  - nxos1
  - nxos2
```

### TB-340: `netmiko_course/README.md`

**Lab type:** Reading and design lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
# netmiko_course
Netmiko Course / Python for Network Engineers
```

### TB-341: `netmiko_course/lab_devices.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
cisco3:
  device_type: cisco_xe
  host: cisco3.lasthop.io
  username: pyclass

cisco4:
  device_type: cisco_xe
  host: cisco4.lasthop.io
  username: pyclass

arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  username: pyclass

arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  username: pyclass

arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  username: pyclass

arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  username: pyclass

vmx1:
  device_type: juniper_junos
  host: vmx1.lasthop.io
  username: pyclass

vmx2:
  device_type: juniper_junos
  host: vmx2.lasthop.io
  username: pyclass

nxos1:
  device_type: cisco_nxos
  host: nxos1.lasthop.io
  username: pyclass

nxos2:
  device_type: cisco_nxos
  host: nxos2.lasthop.io
  username: pyclass


# Any list is group of devices
cisco:
  - cisco3
  - cisco4

arista:
  - arista1
  - arista2
  - arista3
  - arista4

juniper:
  - vmx1
  - vmx2

nxos:
  - nxos1
  - nxos2

all:
  - arista1
  - arista2
  - arista3
  - arista4
  - cisco3
  - cisco4
  - vmx1
  - vmx2
  - nxos1
  - nxos2
```

### TB-342: `netmiko_course/requirements.txt`

**Lab type:** Testing lab

**Objective:** It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
netmiko >= 3.3.0
pytest==6.0.2
pylama==7.7.1
black==20.8b1
ipdb>=0.13.3
ipython>=7.18.1
pyyaml
```

### TB-343: `netmiko_course/setup.cfg`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```ini
[metadata]
license_file = LICENSE

[pylama]
linters = mccabe,pep8,pyflakes
ignore = D203,C901
skip = .tox/*

[pylama:pep8]
max_line_length = 100
```

### TB-344: `python_course_mar26/class4/concurrency/my_devices.py`

**Lab type:** Python fundamentals lab

**Objective:** It repeats a network task over items such as devices, interfaces, commands, or retries.

**What to notice:**

1. First, it brings in helper tools: `os, dotenv.load_dotenv`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import os
from dotenv import load_dotenv


# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw1 = {
    "host": "chkpnt-pod1.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}
chkpt_fw2 = {
    "host": "chkpnt-pod2.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw3 = {
    "host": "chkpnt-pod3.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw4 = {
    "host": "chkpnt-pod4.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw5 = {
    "host": "chkpnt-pod5.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}


device_list = [chkpt_fw1, chkpt_fw2, chkpt_fw3, chkpt_fw4, chkpt_fw5]
```

### TB-345: `python_course_mar26/class1/exercises/func_ex/func_ex1.md`

**Lab type:** Reading and design lab

**Objective:** It explains an exercise or workflow that the code examples are meant to practice.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Function Exercise1

Create a simple function named 'my_func' that takes no arguments. This function should print "Hello world".

Call this function three times.

Executing your Python program should produce the following output:

'''bash
$ python func_ex1.py 
Hello world
Hello world
Hello world
'''
```

### TB-346: `python_course_mar26/class1/exercises/func_ex/func_ex1.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. It defines reusable function(s): `my_func`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python


def my_func():
    print("Hello world")


my_func()
my_func()
my_func()
```

### TB-347: `python_course_mar26/class1/exercises/func_ex/func_ex2.md`

**Lab type:** Reading and design lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
### Function Exercise2

Create a function named "fw_func" that has one parameter "fw_name". The function body should just use an f-string to print out the value of the "fw_name" variable:

'''python
print(f"{fw_name=}")
'''

Call fw_func using a positional argument. Call fw_func using a named argument.

Your output should look similar to the following:

'''bash
$ python func_ex2.py 
fw_name='fw1'
fw_name='chkpnt-fw1'
'''
```

### TB-348: `python_course_mar26/class1/exercises/func_ex/func_ex2.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. It defines reusable function(s): `fw_func`.
3. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python


def fw_func(fw_name):
    print(f"{fw_name=}")


fw_func("fw1")
fw_func(fw_name="chkpnt-fw1")
```

### TB-349: `python_course_mar26/class1/exercises/func_ex/func_ex3.py`

**Lab type:** Python fundamentals lab

**Objective:** It wraps repeated network work in functions, so the same idea can be reused safely.

**What to notice:**

1. The first line tells Unix-like systems which Python program should run this file.
2. First, it brings in helper tools: `rich.print`.
3. It defines reusable function(s): `fw_func`.
4. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
#!/usr/bin/env python
from rich import print


def fw_func(name, ipaddr, os_version="R82"):
    print(f"{name=}")
    print(f"{ipaddr=}")
    print(f"{os_version=}")
    return f"{name}-{ipaddr}-{os_version}"


# Positional arguments
print("\nFunction call with positional arguments")
print("-" * 30)
ret_val = fw_func("chkpnt-pod99", "3.77.44.109", "R81.20")
print(f"\n{ret_val=}\n")

# Named arguments
print("\nFunction call with named arguments")
print("-" * 30)
ret_val = fw_func(
    os_version="R82",
    ipaddr="3.77.44.100",
    name="chkpnt-pod1",
)
print(f"\n{ret_val=}\n")

# Named arguments use default value
print("\nFunction call with named arguments and a default value")
print("-" * 30)
ret_val = fw_func(
    name="chkpnt-pod1",
    ipaddr="3.77.44.100",
)
print(f"\n{ret_val=}\n")

# Both named and positional
print("\nFunction call with both positional and named arguments")
print("-" * 30)
ret_val = fw_func(
    "chkpnt-pod2",
    os_version="R82.10",
    ipaddr="3.77.44.9",
)
print(f"\n{ret_val=}\n")
```

### TB-350: `python_course_mar26/class1/exercises/list_ex/locations.yml`

**Lab type:** Data lab

**Objective:** It stores inventory or settings in a human-readable file that scripts can load and reuse.

**What to notice:**

1. This is data, not a program: it gives Python facts to work with.
2. Think of each key as a label on a box and each value as what is inside the box.
3. A script can load this file and use the values to decide which devices or commands to handle.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Find the top-level keys and explain what each section represents operationally.
- Add one safe fake device/object and update a script or pseudocode loop to consume it.

**Source listing:**

```yaml
---
- Berlin
- Munich
- Cologne
- Frankfurt
- Hamburg
- Stuttgart
```

### TB-351: `python_course_mar26/class3/exercises/fw_policy_ex1/chkpt_exceptions.py`

**Lab type:** Python fundamentals lab

**Objective:** It bundles network data and behavior into an object, like making a small model of a device or session.

**What to notice:**

1. It defines class blueprint(s): `ChkPntConfigError, ChkPntPolicyInstallError`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
class ChkPntConfigError(Exception):
    pass


class ChkPntPolicyInstallError(Exception):
    pass
```

### TB-352: `python_course_mar26/class3/exercises/fw_policy_ex2/chkpt_exceptions.py`

**Lab type:** Python fundamentals lab

**Objective:** It bundles network data and behavior into an object, like making a small model of a device or session.

**What to notice:**

1. It defines class blueprint(s): `ChkPntConfigError, ChkPntPolicyInstallError`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
class ChkPntConfigError(Exception):
    pass


class ChkPntPolicyInstallError(Exception):
    pass
```

### TB-353: `python_course_mar26/class3/exercises/fw_policy_ex2/fw_policy_delete_rule.md`

**Lab type:** Reading and design lab

**Objective:** It makes a decision from network data, such as whether to act, skip, retry, or report.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.
- List every exception path and what the script does after the failure.

**Source listing:**

```markdown
### Delete firewall rule exercise

Add an additional parameter to your 'cfg_fw_rule' function. This parameter should be named 'delete_rule' and should default to False.

If you call your cfg_fw_rule function and specify 'delete_rule=True', then the function will delete the specified firewall rule.

Recreate the code you used in the 'edit firewall rule' exercise except use your function to delete the specified firewall rule.

After the firewall rule has been deleted, publish your changes, and install your new firewall policy.
```

### TB-354: `python_course_mar26/README.md`

**Lab type:** Reading and design lab

**Objective:** It explains an exercise or workflow that the code examples are meant to practice.

**What to notice:**

1. This is an exercise or explanation file.
2. It tells the human what problem to solve before or after running the Python code.
3. In the book, this becomes the bridge between the idea and the hands-on network task.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Turn the instructions into a checklist you could follow during a maintenance window.
- Write the smallest script that would support one step in the exercise.

**Source listing:**

```markdown
# python_course_mar26
Python Course March 2026
```

### TB-355: `python_course_mar26/class1/libraries/lib_test1.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `re, ipdb`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
import re
import ipdb  # noqa

ipdb.set_trace()
print(re.__file__)
```

### TB-356: `python_course_mar26/class1/libraries/lib_test2.py`

**Lab type:** Python fundamentals lab

**Objective:** It is a small course example that supports the chapter's network automation idea.

**What to notice:**

1. First, it brings in helper tools: `rich.print, re.search, ipdb`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print
from re import search
import ipdb  # noqa

ipdb.set_trace()
```

### TB-357: `python_course_mar26/class1/libraries/sys_path_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `sys, rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
"""Can't use ipdb for this since it alters sys.path."""
import sys
from rich import print

print("\nsys.path:")
print("-" * 30)
print(sys.path)
print()
```

### TB-358: `python_course_mar26/class3/sets/set_ex.py`

**Lab type:** Python fundamentals lab

**Objective:** It proves the script can run by printing a visible message, which is the first feedback loop before automating devices.

**What to notice:**

1. First, it brings in helper tools: `rich.print`.
2. It prints something you can see, so you know the script actually ran.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.

**Source listing:**

```python
from rich import print

my_list = [1, 1, 3, 4, 7, 6, 7, 8, 3, 10]
my_list2 = [1, 1, 7, 6, 7, 8, 3, 10, 20, 45, 81, 99]

my_set1 = set(my_list)
print(type(my_set1))
print(my_set1)

my_set2 = set(my_list2)
print(my_set2)

union_sets = my_set1 | my_set2
print(union_sets)

intersect_sets = my_set1 & my_set2
print(intersect_sets)

set_diff1 = my_set1 - my_set2
print(f"{my_set1=}")
print(f"{my_set2=}")
print(set_diff1)

set_diff2 = my_set2 - my_set1
print(f"{my_set1=}")
print(f"{my_set2=}")
print(set_diff2)
```

### TB-359: `python_course_mar26/lib_class4/chkpt_exceptions.py`

**Lab type:** Python fundamentals lab

**Objective:** It bundles network data and behavior into an object, like making a small model of a device or session.

**What to notice:**

1. It defines class blueprint(s): `ChkPntConfigError, ChkPntPolicyInstallError`.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Run it in a safe lab or convert it to a dry run by replacing device calls with `print()` statements.
- Change exactly one value, predict the result, then run again.
- List every exception path and what the script does after the failure.

**Source listing:**

```python
class ChkPntConfigError(Exception):
    pass


class ChkPntPolicyInstallError(Exception):
    pass
```

### TB-360: `python_course_mar26/work/notes.txt`

**Lab type:** Python fundamentals lab

**Objective:** It provides command text, sample output, hosts, or notes that another script can consume.

**What to notice:**

1. This supporting file provides text, templates, commands, or sample output for the scripts.

**Mastery tasks:**

- Read the source once without running it. Write one sentence describing its purpose.
- Identify the Python concept from the chapter track that this lab reinforces.
- Explain whether this file is input data, command data, output data, or helper text.
- Write a tiny Python snippet that reads this file and prints the number of non-empty lines.

**Source listing:**

```text
show-arp
```

---

Part III includes 360 lab cards from the twin-bridges course repositories.


# References

- PacketSwitch, [Python For Network Engineers - Introduction](https://www.packetswitch.co.uk/python-for-network-engineers-introduction/)
- PacketSwitch, [Python - Netmiko](https://www.packetswitch.co.uk/python-netmiko/)
- PacketSwitch, [Python - Functions](https://www.packetswitch.co.uk/python-functions/)
- twin-bridges, [python_course_mar26](https://github.com/twin-bridges/python_course_mar26)
- twin-bridges, [netmiko_course](https://github.com/twin-bridges/netmiko_course)
- jagadnag, [labato_1010](https://github.com/jagadnag/labato_1010)
