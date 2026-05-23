import ast
import json
import re
import subprocess
import tempfile
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
CACHE_ROOT = Path(tempfile.gettempdir()) / "twin_bridges_courses"
PYTHON_REPO_URL = "https://github.com/twin-bridges/python_course_mar26"
NETMIKO_REPO_URL = "https://github.com/twin-bridges/netmiko_course"
PYTHON_REPO = CACHE_ROOT / "python_course_mar26"
NETMIKO_REPO = CACHE_ROOT / "netmiko_course"

PARTS = [
    {
        "title": "Python Network Automation Crash Course Part I: Chapters 1-11",
        "start": 1,
        "end": 11,
        "out": ROOT / "python_network_automation_part1_ch1_11_source_map_context_practice.ipynb",
        "coverage": ROOT / "python_network_automation_part1_ch1_11_coverage_index.md",
    },
    {
        "title": "Python Network Automation Crash Course Part II: Chapters 12-20",
        "start": 12,
        "end": 20,
        "out": ROOT / "python_network_automation_part2_ch12_20_source_map_context_practice.ipynb",
        "coverage": ROOT / "python_network_automation_part2_ch12_20_coverage_index.md",
    },
]

CHAPTERS = {
    1: {
        "title": "Chapter 1: Getting Started in a Network Lab",
        "pcc": "PCC Chapter 1 teaches how to run a tiny program and trust the feedback loop.",
        "topic": "run Python, print device context, and build the first lab-safe habit",
        "flow": "editor -> Python file -> simulated device fact -> printed result",
        "keywords": ["python_script", "simple_conn.py", "simple_conn_cm.py", "simple_conn_dict.py"],
        "examples": [
            (
                "Hello, network world",
                """
                device_name = "edge-sw1"
                mgmt_ip = "192.0.2.10"

                print(f"Hello, {device_name} at {mgmt_ip}.")
                print("Python can describe network intent before it touches a device.")
                """,
            ),
            (
                "First device prompt, simulated",
                """
                prompt = "edge-sw1#"
                command = "show version"

                print(f"{prompt} {command}")
                print("Cisco IOS XE Software, Version 17.09")
                """,
            ),
        ],
    },
    2: {
        "title": "Chapter 2: Variables, Strings, and Device Facts",
        "pcc": "PCC Chapter 2 turns names, strings, numbers, and comments into readable programs.",
        "topic": "store hostnames, interfaces, versions, and command text",
        "flow": "raw fact -> variable name -> string method/f-string -> readable report",
        "keywords": ["strings", "f_strings.py", "show_command.py", "netmiko_log.py"],
        "examples": [
            (
                "Normalize hostnames",
                """
                hostname = " Core-Rtr1 "
                platform = "cisco_ios"
                os_version = "17.09"

                normalized = hostname.strip().lower()
                print(f"{normalized} runs {platform} {os_version}.")
                """,
            ),
            (
                "Build command text",
                """
                interface = "GigabitEthernet1/0/1"
                command = f"show running-config interface {interface}"

                print(command)
                """,
            ),
        ],
    },
    3: {
        "title": "Chapter 3: Introducing Device Lists",
        "pcc": "PCC Chapter 3 introduces lists as a way to keep related values together.",
        "topic": "track device groups, command queues, and change windows",
        "flow": "device list -> index/slice/method -> selected maintenance target",
        "keywords": ["lists", "list_ex.py", "list_methods.py", "lab_devices.yml", "conn_mult_devices.py"],
        "examples": [
            (
                "Device list basics",
                """
                devices = ["edge-sw1", "edge-sw2", "core-rtr1"]

                print(devices[0])
                print(devices[-1])

                devices.append("wan-rtr1")
                print(devices)
                """,
            ),
            (
                "Command queue",
                """
                commands = ["show version", "show ip int brief", "show vlan brief"]
                next_command = commands.pop(0)

                print(f"Run first: {next_command}")
                print(f"Still queued: {commands}")
                """,
            ),
        ],
    },
    4: {
        "title": "Chapter 4: Working Through Networks with Loops",
        "pcc": "PCC Chapter 4 makes repeated work explicit with loops, ranges, slices, and comprehensions.",
        "topic": "iterate over inventories and produce repeatable checks",
        "flow": "inventory -> for loop/comprehension -> repeated command plan",
        "keywords": ["loops", "loop_ex", "while_ex", "cf_threads.py", "cf_threads_asc.py"],
        "examples": [
            (
                "Loop through devices",
                """
                devices = ["edge-sw1", "edge-sw2", "core-rtr1"]

                for device in devices:
                    print(f"Collect show ip int brief from {device}")
                """,
            ),
            (
                "Build interface names",
                """
                access_ports = [f"GigabitEthernet1/0/{number}" for number in range(1, 5)]

                for port in access_ports:
                    print(f"default interface {port}")
                """,
            ),
        ],
    },
    5: {
        "title": "Chapter 5: If Statements for Network Decisions",
        "pcc": "PCC Chapter 5 teaches programs to choose a path based on data.",
        "topic": "decide whether an interface, device, or API version needs action",
        "flow": "network fact -> condition -> allow/deny/remediate branch -> action",
        "keywords": ["cond", "booleans", "api_support_versions.yml", "handle_failures.py"],
        "examples": [
            (
                "Interface state decision",
                """
                interface = {"name": "Gi1/0/10", "status": "notconnect", "vlan": 20}

                if interface["status"] == "connected":
                    print(f"{interface['name']} is active.")
                elif interface["status"] == "notconnect":
                    print(f"{interface['name']} is unused; safe candidate for cleanup review.")
                else:
                    print(f"{interface['name']} needs manual inspection.")
                """,
            ),
            (
                "Change-window guard",
                """
                change_window_open = False
                has_approval = True

                if change_window_open and has_approval:
                    print("Proceed with configuration.")
                else:
                    print("Do not configure. Record the skipped action.")
                """,
            ),
        ],
    },
    6: {
        "title": "Chapter 6: Dictionaries for Device Inventory",
        "pcc": "PCC Chapter 6 adds meaningful keys so records are easier to model.",
        "topic": "model devices, interfaces, services, and firewall objects",
        "flow": "real network object -> dict keys/values -> lookup/update/report",
        "keywords": ["dict", "complex_dstruct", "network_objects.json", "tcp_services.json", "devices.yaml"],
        "examples": [
            (
                "Single device dictionary",
                """
                device = {
                    "hostname": "edge-sw1",
                    "mgmt_ip": "192.0.2.10",
                    "platform": "cisco_ios",
                    "site": "dal",
                }

                print(f"{device['hostname']} at {device['site']} uses {device['platform']}.")
                """,
            ),
            (
                "Nested inventory",
                """
                inventory = {
                    "edge-sw1": {"role": "access", "site": "dal", "vlans": [10, 20, 30]},
                    "core-rtr1": {"role": "core", "site": "dal", "vlans": [99]},
                }

                for hostname, facts in inventory.items():
                    print(f"{hostname}: {facts['role']} device, VLANs {facts['vlans']}")
                """,
            ),
        ],
    },
    7: {
        "title": "Chapter 7: Operator Input and While Loops",
        "pcc": "PCC Chapter 7 connects prompts, validation, and loops to interactive programs.",
        "topic": "collect operator intent safely and retry bounded workflows",
        "flow": "operator input -> validate -> while loop -> planned network action",
        "keywords": ["while_ex", "try_except", "auth_retry.py", "auth_retry_func.py"],
        "examples": [
            (
                "Bounded retry loop",
                """
                pending_devices = ["edge-sw1", "edge-sw2", "core-rtr1"]
                attempts = 0

                while pending_devices and attempts < 2:
                    device = pending_devices.pop(0)
                    print(f"Attempt {attempts + 1}: connect to {device}")
                    attempts += 1
                """,
            ),
            (
                "Validate requested VLAN",
                """
                requested_vlan = "20"

                if requested_vlan.isdigit():
                    vlan_id = int(requested_vlan)
                    if 1 <= vlan_id <= 4094:
                        print(f"VLAN {vlan_id} is valid.")
                """,
            ),
        ],
    },
    8: {
        "title": "Chapter 8: Functions for Reusable Automation",
        "pcc": "PCC Chapter 8 packages behavior into named, reusable functions.",
        "topic": "turn repeated checks, command builders, and parsers into functions",
        "flow": "arguments -> function body -> return/report -> reuse across devices",
        "keywords": ["functions", "gaia_func", "mgmt_func", "utilities.py"],
        "examples": [
            (
                "Build a show command",
                """
                def show_interface_command(interface):
                    return f"show running-config interface {interface}"


                print(show_interface_command("GigabitEthernet1/0/1"))
                print(show_interface_command("Vlan20"))
                """,
            ),
            (
                "Summarize device health",
                """
                def summarize_device(hostname, reachable, config_saved):
                    status = "ready" if reachable and config_saved else "needs attention"
                    return {"hostname": hostname, "status": status}


                report = summarize_device("edge-sw1", reachable=True, config_saved=False)
                print(report)
                """,
            ),
        ],
    },
    9: {
        "title": "Chapter 9: Classes for Devices and Sessions",
        "pcc": "PCC Chapter 9 groups data and behavior into objects.",
        "topic": "model devices, API clients, and SSH sessions",
        "flow": "class blueprint -> device/session instance -> methods -> automation behavior",
        "keywords": ["gaia_class", "mgmt_class", "chkpt_api_ex.py", "config_mode.py"],
        "examples": [
            (
                "Device object",
                """
                class NetworkDevice:
                    def __init__(self, hostname, mgmt_ip, platform):
                        self.hostname = hostname
                        self.mgmt_ip = mgmt_ip
                        self.platform = platform

                    def connection_summary(self):
                        return f"{self.hostname} ({self.platform}) at {self.mgmt_ip}"


                device = NetworkDevice("edge-sw1", "192.0.2.10", "cisco_ios")
                print(device.connection_summary())
                """,
            ),
            (
                "Session-like object for dry runs",
                """
                class DryRunSession:
                    def __init__(self, hostname):
                        self.hostname = hostname
                        self.commands = []

                    def send_config_set(self, commands):
                        self.commands.extend(commands)
                        return f"{self.hostname}: queued {len(commands)} command(s)"


                session = DryRunSession("edge-sw1")
                print(session.send_config_set(["vlan 20", "name USERS"]))
                """,
            ),
        ],
    },
    10: {
        "title": "Chapter 10: Files, Exceptions, and Network Data",
        "pcc": "PCC Chapter 10 connects Python to files, errors, and saved data.",
        "topic": "load inventories, handle bad data, and write audit artifacts",
        "flow": "file/API data -> read/parse -> handle errors -> save report",
        "keywords": ["files", "read_json.py", "read_yaml.py", "write_json.py", "dns_fail.py", "tcp_conn_fail.py"],
        "examples": [
            (
                "Parse inventory JSON safely",
                """
                import json

                raw_inventory = '[{"hostname": "edge-sw1", "mgmt_ip": "192.0.2.10"}]'

                try:
                    devices = json.loads(raw_inventory)
                except json.JSONDecodeError as exc:
                    print(f"Inventory is invalid: {exc}")
                else:
                    print(f"Loaded {len(devices)} device(s).")
                """,
            ),
            (
                "Write an audit line",
                """
                from pathlib import Path
                import tempfile

                audit_path = Path(tempfile.gettempdir()) / "network_audit_demo.txt"
                audit_path.write_text("edge-sw1: show version collected\\n", encoding="utf-8")

                print(audit_path.read_text(encoding="utf-8").strip())
                """,
            ),
        ],
    },
    11: {
        "title": "Chapter 11: Testing Network Automation",
        "pcc": "PCC Chapter 11 builds confidence by checking expected behavior automatically.",
        "topic": "test parsers, command builders, inventory validation, and policy logic",
        "flow": "expected network behavior -> test case -> run test -> fix automation",
        "keywords": ["test_", "pytest", "test_mgmt", "test_gaia", "test_class"],
        "examples": [
            (
                "Test a command builder",
                """
                def build_vlan_commands(vlan_id, name):
                    return [f"vlan {vlan_id}", f"name {name}"]


                assert build_vlan_commands(20, "USERS") == ["vlan 20", "name USERS"]
                print("Command builder test passed.")
                """,
            ),
            (
                "Test inventory validation",
                """
                def has_required_device_keys(device):
                    required = {"hostname", "mgmt_ip", "platform"}
                    return required.issubset(device)


                assert has_required_device_keys({"hostname": "r1", "mgmt_ip": "192.0.2.1", "platform": "cisco_ios"})
                assert not has_required_device_keys({"hostname": "r2"})
                print("Inventory validation tests passed.")
                """,
            ),
        ],
    },
    12: {
        "title": "Chapter 12: Starting a Netmiko Project",
        "pcc": "PCC Chapter 12 begins the first larger project by combining classes, loops, and an external library.",
        "topic": "connect to a lab device, find a prompt, and disconnect cleanly",
        "flow": "device dict -> ConnectHandler -> prompt/show command -> disconnect",
        "keywords": ["simple_conn.py", "simple_conn_cm.py", "simple_conn_dict.py", "show_command.py"],
        "examples": [
            (
                "Netmiko connection shape",
                """
                device = {
                    "device_type": "cisco_ios",
                    "host": "cisco3.lasthop.io",
                    "username": "pyclass",
                    "password": "use-an-environment-variable",
                }

                print("ConnectHandler(**device)")
                print(f"Target host: {device['host']}")
                """,
            ),
            (
                "Lab-safe connection checklist",
                """
                checks = ["credentials loaded", "device reachable", "prompt found", "disconnect called"]

                for check in checks:
                    print(f"[ ] {check}")
                """,
            ),
        ],
    },
    13: {
        "title": "Chapter 13: Collecting Show Commands Across a Fleet",
        "pcc": "PCC Chapter 13 grows the project by adding repeated objects and state changes.",
        "topic": "run operational commands against many devices and track results",
        "flow": "device fleet -> command loop -> per-device output -> result dictionary",
        "keywords": ["conn_mult_devices.py", "send_command", "traceroute", "show_timing.py", "show_textfsm.py"],
        "examples": [
            (
                "Collect simulated show output",
                """
                devices = ["edge-sw1", "edge-sw2", "core-rtr1"]
                command = "show ip int brief"
                results = {}

                for device in devices:
                    results[device] = f"{device}: simulated output for {command}"

                for device, output in results.items():
                    print(device, "->", output)
                """,
            ),
            (
                "Track command success",
                """
                results = {"edge-sw1": True, "edge-sw2": True, "core-rtr1": False}
                failed = [device for device, ok in results.items() if not ok]

                print(f"Successful devices: {len(results) - len(failed)}")
                print(f"Failed devices: {failed}")
                """,
            ),
        ],
    },
    14: {
        "title": "Chapter 14: Configuration, Validation, and Rollback Thinking",
        "pcc": "PCC Chapter 14 adds user experience, scoring, levels, and reset behavior to a project.",
        "topic": "prepare config sets, apply changes, verify state, and plan rollback",
        "flow": "intended state -> config commands -> verification command -> rollback notes",
        "keywords": ["send_config", "config_file.py", "config_vlans.py", "send_multiline", "commit.py"],
        "examples": [
            (
                "Build VLAN config",
                """
                vlan = {"id": 20, "name": "USERS"}
                commands = [f"vlan {vlan['id']}", f"name {vlan['name']}"]

                print("Config plan:")
                for command in commands:
                    print(command)
                """,
            ),
            (
                "Verification plan",
                """
                change = {"device": "edge-sw1", "vlan": 20, "expected_name": "USERS"}
                verify_command = f"show vlan id {change['vlan']}"
                rollback_commands = [f"no vlan {change['vlan']}"]

                print(verify_command)
                print(rollback_commands)
                """,
            ),
        ],
    },
    15: {
        "title": "Chapter 15: Generating Network Reports",
        "pcc": "PCC Chapter 15 turns generated data into visual insight.",
        "topic": "summarize interface status, VLAN counts, latency, and compliance",
        "flow": "raw command output -> parsed records -> aggregate -> report",
        "keywords": ["show_genie.py", "show_ttp.py", "show_vlan.ttp", "list_comp_ex.py"],
        "examples": [
            (
                "Summarize interface states",
                """
                interfaces = [
                    {"name": "Gi1/0/1", "status": "connected"},
                    {"name": "Gi1/0/2", "status": "notconnect"},
                    {"name": "Gi1/0/3", "status": "connected"},
                ]

                connected = [intf for intf in interfaces if intf["status"] == "connected"]
                print(f"Connected interfaces: {len(connected)} / {len(interfaces)}")
                """,
            ),
            (
                "Compliance score",
                """
                checks = {"ntp": True, "syslog": True, "aaa": False, "snmp": True}
                score = sum(checks.values()) / len(checks) * 100

                print(f"Baseline compliance: {score:.0f}%")
                """,
            ),
        ],
    },
    16: {
        "title": "Chapter 16: Inventories, YAML, JSON, and Real-World Data",
        "pcc": "PCC Chapter 16 pulls data from files and online sources.",
        "topic": "load inventories and transform external data into device actions",
        "flow": "YAML/JSON/source of truth -> parse -> clean -> command plan",
        "keywords": ["yaml", "json", "devices.yaml", "lab_devices.yml", "pathlib_ex.py"],
        "examples": [
            (
                "Use structured inventory data",
                """
                inventory = [
                    {"hostname": "edge-sw1", "site": "dal", "role": "access"},
                    {"hostname": "core-rtr1", "site": "dal", "role": "core"},
                ]

                access_switches = [device for device in inventory if device["role"] == "access"]
                print(access_switches)
                """,
            ),
            (
                "Generate commands from data",
                """
                desired_vlans = [
                    {"id": 10, "name": "VOICE"},
                    {"id": 20, "name": "USERS"},
                ]

                commands = []
                for vlan in desired_vlans:
                    commands.extend([f"vlan {vlan['id']}", f"name {vlan['name']}"])

                print(commands)
                """,
            ),
        ],
    },
    17: {
        "title": "Chapter 17: Network APIs",
        "pcc": "PCC Chapter 17 uses web APIs and response dictionaries.",
        "topic": "authenticate, request network data, paginate, and process API responses",
        "flow": "API endpoint -> request/session -> JSON dicts -> object/config action",
        "keywords": ["api", "gaia_auth", "awx_auth", "mgmt_api", "api_pages", "sdk_api_query"],
        "examples": [
            (
                "API response dictionary",
                """
                response = {
                    "status_code": 200,
                    "objects": [
                        {"name": "web-01", "ipv4-address": "198.51.100.10"},
                        {"name": "db-01", "ipv4-address": "198.51.100.20"},
                    ],
                }

                if response["status_code"] == 200:
                    for obj in response["objects"]:
                        print(f"{obj['name']} -> {obj['ipv4-address']}")
                """,
            ),
            (
                "Pagination pattern",
                """
                total = 250
                limit = 100
                offsets = list(range(0, total, limit))

                for offset in offsets:
                    print(f"GET objects?limit={limit}&offset={offset}")
                """,
            ),
        ],
    },
    18: {
        "title": "Chapter 18: Building a Network Automation Tool",
        "pcc": "PCC Chapter 18 starts a web app by organizing models, views, and templates.",
        "topic": "shape scripts into a small tool with clear inputs, outputs, and modules",
        "flow": "operator request -> validation -> automation function -> rendered report",
        "keywords": ["main_project", "run_script", "blocked_ip_funcs.py", "utilities.py"],
        "examples": [
            (
                "Tool pipeline",
                """
                def validate_request(request):
                    return {"vlan", "devices"}.issubset(request)


                def build_plan(request):
                    return [f"Configure VLAN {request['vlan']} on {device}" for device in request["devices"]]


                request = {"vlan": 20, "devices": ["edge-sw1", "edge-sw2"]}
                if validate_request(request):
                    print(build_plan(request))
                """,
            ),
            (
                "Render a tiny report",
                """
                results = [{"device": "edge-sw1", "changed": True}, {"device": "edge-sw2", "changed": False}]

                for result in results:
                    marker = "changed" if result["changed"] else "skipped"
                    print(f"{result['device']}: {marker}")
                """,
            ),
        ],
    },
    19: {
        "title": "Chapter 19: Credentials, Ownership, and Guardrails",
        "pcc": "PCC Chapter 19 adds user accounts, protected data, forms, and ownership.",
        "topic": "separate secrets, authorization, device ownership, and approval checks",
        "flow": "operator identity -> permissions -> owned device set -> protected action",
        "keywords": ["ssh_keys", "auth_fail", "auth_retry", "mgmt_cli_session", "conftest.py"],
        "examples": [
            (
                "Permission guard",
                """
                user = {"name": "alex", "roles": {"read-only", "change-requester"}}
                requested_action = "configure_vlan"

                if requested_action == "configure_vlan" and "network-admin" not in user["roles"]:
                    print("Denied: configuration requires network-admin.")
                else:
                    print("Approved.")
                """,
            ),
            (
                "Secrets stay out of code",
                """
                import os

                username = os.getenv("NETOPS_USERNAME", "demo-user")
                password_loaded = bool(os.getenv("NETOPS_PASSWORD"))

                print(f"Username source is environment/default: {username}")
                print(f"Password loaded from environment: {password_loaded}")
                """,
            ),
        ],
    },
    20: {
        "title": "Chapter 20: Operating and Deploying Automation",
        "pcc": "PCC Chapter 20 finishes a project by styling, configuring, deploying, and operating it.",
        "topic": "package scripts, run checks, log sessions, and prepare production workflows",
        "flow": "local script -> config/logging/tests -> scheduled run -> operational report",
        "keywords": ["deploy.sh", "tests.sh", "conn_log.py", "fast_cli.py", "file_transfer", "get_file.py", "put_file.py"],
        "examples": [
            (
                "Operational run summary",
                """
                run = {
                    "job": "nightly-show-version",
                    "devices": 12,
                    "success": 11,
                    "failed": ["edge-sw9"],
                }

                print(f"{run['job']}: {run['success']} of {run['devices']} succeeded")
                if run["failed"]:
                    print(f"Review failures: {', '.join(run['failed'])}")
                """,
            ),
            (
                "Release checklist",
                """
                checklist = [
                    "unit tests pass",
                    "dry-run reviewed",
                    "rollback documented",
                    "session logging enabled",
                    "credentials loaded from environment",
                ]

                for item in checklist:
                    print(f"[ ] {item}")
                """,
            ),
        ],
    },
}


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": dedent(text).strip().splitlines(True)}


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(text).strip("\n").splitlines(True),
    }


def sync_repo(path, url):
    if path.exists():
        subprocess.run(["git", "-C", str(path), "remote", "set-head", "origin", "-a"], check=True)
        default_ref = subprocess.check_output(
            ["git", "-C", str(path), "symbolic-ref", "refs/remotes/origin/HEAD"],
            text=True,
        ).strip()
        default_branch = default_ref.rsplit("/", 1)[-1]
        subprocess.run(["git", "-C", str(path), "fetch", "--depth=1", "origin", default_branch], check=True)
        subprocess.run(["git", "-C", str(path), "checkout", "-q", "FETCH_HEAD"], check=True)
    else:
        subprocess.run(["git", "clone", "--depth=1", url + ".git", str(path)], check=True)
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "--short", "HEAD"], text=True).strip()


def language_for(path):
    return {
        ".py": "python",
        ".json": "json",
        ".yml": "yaml",
        ".yaml": "yaml",
        ".md": "markdown",
        ".txt": "text",
        ".ttp": "text",
        ".sh": "bash",
        ".cfg": "ini",
    }.get(path.suffix.lower(), "text")


def iter_source_files():
    for repo_name, repo_path in [("python_course_mar26", PYTHON_REPO), ("netmiko_course", NETMIKO_REPO)]:
        for path in repo_path.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".py", ".json", ".yml", ".yaml", ".md", ".txt", ".ttp", ".sh", ".cfg"} and path.name not in {"my_ssh_config"}:
                continue
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            rel = path.relative_to(repo_path).as_posix()
            yield repo_name, path, rel


def read_source(path):
    try:
        return path.read_text(encoding="utf-8").strip("\n")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig").strip("\n")


def chapter_hint_for_path(repo_name, rel):
    lower = rel.lower()
    if repo_name == "netmiko_course":
        match = re.search(r"class(\d+)", lower)
        if match:
            class_number = int(match.group(1))
            return {
                1: 12,
                2: 13,
                3: 15,
                4: 14,
                5: 14,
                6: 19,
                7: 19,
                8: 20,
                9: 20,
                10: 16,
                11: 20,
                12: 14,
            }.get(class_number)
        if lower.startswith("tests/"):
            return 11
        return 20

    if lower.startswith("class1/strings"):
        return 2
    if lower.startswith("class1/lists"):
        return 3
    if lower.startswith("class1/loops"):
        return 4
    if lower.startswith("class1/cond") or lower.startswith("class1/booleans"):
        return 5
    if lower.startswith("class1/dict") or "complex_dstruct" in lower:
        return 6
    if "while" in lower or "try_except" in lower:
        return 7
    if lower.startswith("class1/functions"):
        return 8
    if "gaia_class" in lower or "mgmt_class" in lower or "class_api" in lower:
        return 9
    if lower.startswith("class1/files") or "linux_python" in lower:
        return 10
    if "test_" in lower or "/tests/" in lower or "pytest" in lower:
        return 11
    if "api" in lower or "sdk" in lower:
        return 17
    if "main_project" in lower or "run_script" in lower:
        return 18
    if "ssh" in lower or "session" in lower:
        return 19
    if "concurrency" in lower:
        return 20
    if lower.startswith("class1/python_script"):
        return 1
    return None


def score_file(rel, text, keywords, repo_name=None, chapter_number=None):
    haystack = f"{rel}\n{text[:3000]}".lower()
    score = 0
    for keyword in keywords:
        key = keyword.lower()
        if key in rel.lower():
            score += 8
        score += haystack.count(key)
    if "/exercises/" in rel:
        score += 2
    if "/collateral/" in rel:
        score += 1
    if repo_name and chapter_number and chapter_hint_for_path(repo_name, rel) == chapter_number:
        score += 25
    return score


def collect_all_sources():
    sources = []
    for repo_name, path, rel in iter_source_files():
        text = read_source(path)
        if not text:
            continue
        sources.append(
            {
                "repo": repo_name,
                "path": rel,
                "language": language_for(path),
                "source": text,
            }
        )
    return sources


def assign_sources_to_chapters(sources):
    assigned = {number: [] for number in CHAPTERS}
    for source in sources:
        scored = []
        for number, chapter in CHAPTERS.items():
            score = score_file(
                source["path"],
                source["source"],
                chapter["keywords"],
                source["repo"],
                number,
            )
            scored.append((score, number))
        score, number = max(scored)
        if score <= 0:
            number = chapter_hint_for_path(source["repo"], source["path"]) or 20
            score = 1
        assigned[number].append({**source, "score": score})

    for number in assigned:
        assigned[number].sort(key=lambda item: (-item["score"], item["repo"], item["path"]))
    return assigned


def collect_related_sources(chapter, limit=None):
    matches = []
    for repo_name, path, rel in iter_source_files():
        text = read_source(path)
        score = score_file(rel, text, chapter["keywords"])
        if score <= 0:
            continue
        matches.append(
            {
                "repo": repo_name,
                "path": rel,
                "language": language_for(path),
                "source": text.strip("\n"),
                "score": score,
            }
        )
    matches.sort(key=lambda item: (-item["score"], item["repo"], item["path"]))
    return matches if limit is None else matches[:limit]


def code_preview(text, max_lines=24):
    lines = text.strip("\n").splitlines()
    preview = "\n".join(lines[:max_lines])
    if len(lines) > max_lines:
        preview += f"\n# ... {len(lines) - max_lines} more line(s) in source file"
    return preview.replace("```", "'''")


def network_context(chapter, source=None):
    lines = [
        f"This chapter teaches {chapter['topic']} in the language of network automation.",
        chapter["pcc"],
        "Start with a small safe example, observe the output, change one thing, then connect the pattern to a real network task.",
        "Real device operations are shown as source-map study blocks; runnable cells use simulated data unless the cell clearly says otherwise.",
        "When you move this into a lab, replace fake inventory and outputs first, then add credentials, connectivity, and configuration writes last.",
    ]
    if source:
        lines[0] = f"This source is a close twin-bridges use case for {chapter['topic']}."
    return lines


def python_code_facts(source):
    facts = {
        "imports": [],
        "functions": [],
        "classes": [],
        "calls": set(),
        "has_main_guard": "__main__" in source,
        "has_assert": "assert " in source,
    }
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return facts

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            facts["imports"].extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            facts["imports"].extend(f"{module}.{alias.name}" if module else alias.name for alias in node.names)
        elif isinstance(node, ast.FunctionDef):
            facts["functions"].append(node.name)
        elif isinstance(node, ast.ClassDef):
            facts["classes"].append(node.name)
        elif isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                facts["calls"].add(func.id)
            elif isinstance(func, ast.Attribute):
                facts["calls"].add(func.attr)
    facts["calls"] = sorted(facts["calls"])
    return facts


def plain_english_goal(source):
    rel = source["path"].lower()
    text = source["source"].lower()
    if "netmiko" in text or "connecthandler" in text:
        return "It shows how Python opens an SSH-style network session, sends commands, and then cleans up the connection."
    if "pytest" in text or source["path"].split("/")[-1].startswith("test_") or "assert " in text:
        return "It checks automation logic with tests, so mistakes are caught before a script touches real infrastructure."
    if "json" in text or rel.endswith(".json"):
        return "It treats network facts as structured data, so code can look up exact fields instead of reading text by eye."
    if "yaml" in text or rel.endswith((".yml", ".yaml")):
        return "It stores inventory or settings in a human-readable file that scripts can load and reuse."
    if "thread" in text or "process" in text or "concurrent" in text:
        return "It runs the same network task across multiple devices without waiting for one device at a time."
    if "api" in text or "requests" in text or "session" in text:
        return "It talks to a network API, which means Python asks a controller or firewall manager for data or changes."
    if "class " in text:
        return "It bundles network data and behavior into an object, like making a small model of a device or session."
    if "def " in text:
        return "It wraps repeated network work in functions, so the same idea can be reused safely."
    if "print(" in text:
        return "It proves the script can run by printing a visible message, which is the first feedback loop before automating devices."
    if "for " in text or "while " in text:
        return "It repeats a network task over items such as devices, interfaces, commands, or retries."
    if "if " in text or "elif " in text or "else:" in text:
        return "It makes a decision from network data, such as whether to act, skip, retry, or report."
    if rel.endswith(".md"):
        return "It explains an exercise or workflow that the code examples are meant to practice."
    if rel.endswith(".txt"):
        return "It provides command text, sample output, hosts, or notes that another script can consume."
    return "It is a small course example that supports the chapter's network automation idea."


def kid_level_steps(source):
    text = source["source"]
    lower = text.lower()
    steps = []
    if source["language"] == "python":
        facts = python_code_facts(text)
        if text.startswith("#!"):
            steps.append("The first line tells Unix-like systems which Python program should run this file.")
        if facts["imports"]:
            steps.append(f"First, it brings in helper tools: `{', '.join(facts['imports'][:6])}`.")
        if "getpass" in lower or "os.getenv" in lower:
            steps.append("Then it gets secrets from the environment or a password prompt, instead of hard-coding them.")
        if "connecthandler" in lower:
            steps.append("Next, it builds a device connection dictionary and hands it to Netmiko's `ConnectHandler`.")
        if "send_command" in lower:
            steps.append("After that, it sends a show command and saves the text that comes back from the device.")
        if "send_config" in lower or "send_config_set" in lower or "send_config_from_file" in lower:
            steps.append("Then it sends configuration commands, which is the part that can change a real device.")
        if "disconnect" in lower:
            steps.append("Finally, it disconnects so the network session is not left hanging open.")
        if facts["classes"]:
            steps.append(f"It defines class blueprint(s): `{', '.join(facts['classes'][:5])}`.")
        if facts["functions"]:
            steps.append(f"It defines reusable function(s): `{', '.join(facts['functions'][:8])}`.")
        if facts["has_assert"]:
            steps.append("It uses assertions/tests to say, `this result must be true`.")
        if "open(" in lower or "path(" in lower or ".read_text" in lower or ".write_text" in lower:
            steps.append("It reads or writes files, which is how automation remembers inventory, commands, or reports.")
        if "print(" in lower:
            steps.append("It prints something you can see, so you know the script actually ran.")
        if not steps:
            steps.append("It runs from top to bottom: create values, transform them, and print or return a result.")
    elif source["language"] in {"json", "yaml"}:
        steps.extend(
            [
                "This is data, not a program: it gives Python facts to work with.",
                "Think of each key as a label on a box and each value as what is inside the box.",
                "A script can load this file and use the values to decide which devices or commands to handle.",
            ]
        )
    elif source["language"] == "markdown":
        steps.extend(
            [
                "This is an exercise or explanation file.",
                "It tells the human what problem to solve before or after running the Python code.",
                "In the book, this becomes the bridge between the idea and the hands-on network task.",
            ]
        )
    elif source["language"] == "bash":
        steps.extend(
            [
                "This is a shell helper script.",
                "It strings together command-line steps so the same setup or test can be repeated.",
            ]
        )
    else:
        steps.append("This supporting file provides text, templates, commands, or sample output for the scripts.")
    return steps[:7]


def foundational_lessons(source, chapter):
    lower = source["source"].lower()
    lessons = [
        f"The Python idea here is `{chapter['topic']}`.",
        "Networking code is just normal Python with more serious inputs and outputs.",
    ]
    if "connecthandler" in lower:
        lessons.append("A device dictionary is a contract: device type, host, username, and password must be correct.")
    if "send_command" in lower:
        lessons.append("Show commands are read-only, so they are the safest first step in real network automation.")
    if "send_config" in lower:
        lessons.append("Configuration commands need guardrails: dry run, approval, verification, and rollback.")
    if "json" in lower or source["language"] in {"json", "yaml"}:
        lessons.append("Structured data is easier for Python to trust than copied terminal text.")
    if "pytest" in lower or "assert " in lower:
        lessons.append("Tests let you practice failure in a harmless place before a network change window.")
    if "exception" in lower or "try:" in lower:
        lessons.append("Network scripts must expect failure: DNS, TCP, authentication, prompts, and timeouts can all break.")
    if "thread" in lower or "process" in lower or "concurrent" in lower:
        lessons.append("Concurrency saves time, but every result needs a clear success or failure record.")
    return lessons[:6]


def try_this_next(source):
    lower = source["source"].lower()
    if "connecthandler" in lower:
        return "Replace the host with a lab-only device, load the password from an environment variable, and run a read-only command first."
    if "send_config" in lower:
        return "Convert the config commands into a dry-run list, print them, and write the verification command before sending anything."
    if source["language"] in {"json", "yaml"}:
        return "Add one fake device or object, then write a tiny loop that prints the fields you need."
    if "assert " in lower or "test_" in source["path"].lower():
        return "Add one failing test first, then change the function until the test passes."
    if "def " in lower:
        return "Call the function with two different fake devices and compare the return values."
    if "for " in lower:
        return "Add one more device or interface to the list and predict how many lines print."
    return "Change one value, predict the output, then run the cell or script and compare."


def source_breakdown(source, chapter):
    steps = "\n".join(f"{idx}. {step}" for idx, step in enumerate(kid_level_steps(source), start=1))
    lessons = "\n".join(f"- {lesson}" for lesson in foundational_lessons(source, chapter))
    return {
        "goal": plain_english_goal(source),
        "steps": steps,
        "lessons": lessons,
        "try_next": try_this_next(source),
    }


def markdown_for_source(chapter_number, source_index, chapter, source):
    breakdown = source_breakdown(source, chapter)
    return "\n".join(
        [
            f"#### Twin-bridges source map {chapter_number}.{source_index}",
            "",
            f"Source: `{source['repo']}/{source['path']}`",
            "",
            "**What This Example Is For**",
            "",
            breakdown["goal"],
            "",
            "**Explain It Like You Are New**",
            "",
            breakdown["steps"],
            "",
            "**Foundational Ideas**",
            "",
            breakdown["lessons"],
            "",
            "**How It Connects to This Chapter**",
            "",
            f"`{chapter['flow']}`",
            "",
            "**Try This Next**",
            "",
            breakdown["try_next"],
            "",
            "**Source Preview**",
            "",
            f"```{source['language']}",
            code_preview(source["source"]),
            "```",
        ]
    )


def chapter_intro(number, chapter, related_sources):
    lines = network_context(chapter)
    related = "\n".join(f"- `{src['repo']}/{src['path']}`" for src in related_sources)
    return f"""
    ## {chapter['title']}

    **Bridge from Python Crash Course**

    {chapter['pcc']}

    **Network Automation Translation**

    1. {lines[0]}
    2. {lines[2]}
    3. {lines[3]}
    4. {lines[4]}

    **Concept Flow**

    ```text
    {chapter['flow']}
    ```

    **Assigned twin-bridges examples**

    {related if related else "- No close source file found; this chapter uses authored bridge examples."}
    """


def practice_checkpoint(number, chapter):
    return f"""
    ### {chapter['title']} Practice Checkpoint

    1. Pick one safe example from this chapter and rename the devices to match your lab.
    2. Write the command or API action you would run in a dry-run variable before connecting to anything.
    3. Add one validation check that would stop the script from making a bad change.
    4. Compare the authored bridge example with the assigned twin-bridges source files and note what becomes real-device-specific.
    """


def build_notebook(part, revisions):
    selected = [(number, CHAPTERS[number]) for number in range(part["start"], part["end"] + 1)]
    all_sources = collect_all_sources()
    assigned_sources = assign_sources_to_chapters(all_sources)
    related_by_chapter = {number: assigned_sources[number] for number, _ in selected}

    cells = [
        md(
            f"""
            # {part['title']}

            Sources:
            - Python teaching pattern and chapter bridge: local Python Crash Course notebooks generated in this workspace.
            - Twin-bridges Python course: `{PYTHON_REPO_URL}` at `{revisions['python']}`
            - Twin-bridges Netmiko course: `{NETMIKO_REPO_URL}` at `{revisions['netmiko']}`

            Goal: bridge a reader who has finished Python Crash Course into network automation.
            Each chapter preserves the PCC teaching logic, then translates the same idea into
            network inventory, command collection, Netmiko, APIs, testing, and operational safety.

            Safety note: runnable cells use simulated data by default. Real Netmiko/API examples
            are included as source-map study blocks so readers can adapt them intentionally in a lab.
            """
        ),
        code(
            """
            import json
            import os
            import random
            import tempfile
            from pathlib import Path
            from pprint import pprint

            print("Network automation study setup complete.")
            """
        ),
        md("## Coverage Summary\n\n" + "\n".join(
            f"- {CHAPTERS[number]['title']}: {len(related_by_chapter[number])} twin-bridges source map(s), {len(CHAPTERS[number]['examples'])} authored bridge example(s)"
            for number, _ in selected
        )),
    ]

    for number, chapter in selected:
        related_sources = related_by_chapter[number]
        cells.append(md(chapter_intro(number, chapter, related_sources)))
        for title, source in chapter["examples"]:
            cells.append(md(f"#### Bridge Example: {title}"))
            cells.append(code(source))
        for source_index, source in enumerate(related_sources, start=1):
            cells.append(md(markdown_for_source(number, source_index, chapter, source)))
            cells.append(
                code(
                    f"""
                    # Practice rewrite for twin-bridges source map {number}.{source_index}
                    # Source: {source['repo']}/{source['path']}
                    # Rewrite one idea from the source with simulated data before using a real device.
                    simulated_device = {{"hostname": "edge-sw1", "platform": "cisco_ios", "reachable": True}}
                    print(f"Plan for {{simulated_device['hostname']}}: inspect the source pattern, then dry-run it.")
                    """
                )
            )
        cells.append(md(practice_checkpoint(number, chapter)))

    cells.append(
        md(
            """
            ## Final Study Routine

            1. Name the Python concept from PCC.
            2. Identify the matching network object: device, interface, command, API response, config, or test.
            3. Run the safe simulated cell.
            4. Read the assigned twin-bridges source map.
            5. Rewrite the example against fake data.
            6. Only then adapt it to a lab device with environment-based credentials and logging.
            """
        )
    )

    return {
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


def write_coverage(part, notebook, revisions):
    all_sources = collect_all_sources()
    assigned_sources = assign_sources_to_chapters(all_sources)
    lines = [
        f"# {part['title']} Coverage Index",
        "",
        f"Twin-bridges Python course: `{PYTHON_REPO_URL}` at `{revisions['python']}`",
        f"Twin-bridges Netmiko course: `{NETMIKO_REPO_URL}` at `{revisions['netmiko']}`",
        "",
        "This index maps each chapter to authored network-automation bridge examples and assigned twin-bridges course examples.",
        "",
    ]
    for number in range(part["start"], part["end"] + 1):
        chapter = CHAPTERS[number]
        lines.extend([f"## {chapter['title']}", "", chapter["pcc"], "", f"Concept flow: `{chapter['flow']}`", ""])
        lines.append("Authored bridge examples:")
        for title, _ in chapter["examples"]:
            lines.append(f"- {title}")
        lines.append("")
        lines.append("Assigned twin-bridges source maps:")
        sources = assigned_sources[number]
        for idx, source in enumerate(sources, start=1):
            lines.append(f"- {number}.{idx} | {source['repo']} | `{source['path']}` | score {source['score']}")
        lines.append("")
    part["coverage"].write_text("\n".join(lines), encoding="utf-8")


def validate_notebook(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    failures = []
    code_cells = 0
    source_maps = 0
    for index, cell in enumerate(notebook["cells"], start=1):
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            source_maps += source.count("Twin-bridges source map")
        if cell["cell_type"] == "code":
            code_cells += 1
            try:
                ast.parse(source)
            except SyntaxError as exc:
                failures.append((index, exc.msg))
    return {"cells": len(notebook["cells"]), "code_cells": code_cells, "source_maps": source_maps, "failures": failures}


def main():
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    revisions = {
        "python": sync_repo(PYTHON_REPO, PYTHON_REPO_URL),
        "netmiko": sync_repo(NETMIKO_REPO, NETMIKO_REPO_URL),
    }
    print(f"Using {PYTHON_REPO_URL} at {revisions['python']}")
    print(f"Using {NETMIKO_REPO_URL} at {revisions['netmiko']}")

    for part in PARTS:
        notebook = build_notebook(part, revisions)
        part["out"].write_text(json.dumps(notebook, indent=2), encoding="utf-8")
        write_coverage(part, notebook, revisions)
        stats = validate_notebook(part["out"])
        print(part["out"])
        print(part["coverage"])
        print(stats)


if __name__ == "__main__":
    main()
