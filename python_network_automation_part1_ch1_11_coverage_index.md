# Python Network Automation Crash Course Part I: Chapters 1-11 Coverage Index

Twin-bridges Python course: `https://github.com/twin-bridges/python_course_mar26` at `8d23646`
Twin-bridges Netmiko course: `https://github.com/twin-bridges/netmiko_course` at `8c31f4e`

This index maps each chapter to authored network-automation bridge examples and assigned twin-bridges course examples.

## Chapter 1: Getting Started in a Network Lab

PCC Chapter 1 teaches how to run a tiny program and trust the feedback loop.

Concept flow: `editor -> Python file -> simulated device fact -> printed result`

Authored bridge examples:
- Hello, network world
- First device prompt, simulated

Assigned twin-bridges source maps:
- 1.1 | python_course_mar26 | `class1/python_script/my_script.py` | score 34

## Chapter 2: Variables, Strings, and Device Facts

PCC Chapter 2 turns names, strings, numbers, and comments into readable programs.

Concept flow: `raw fact -> variable name -> string method/f-string -> readable report`

Authored bridge examples:
- Normalize hostnames
- Build command text

Assigned twin-bridges source maps:
- 2.1 | python_course_mar26 | `class1/strings/f_strings.py` | score 44
- 2.2 | python_course_mar26 | `class1/strings/unicode_chars.py` | score 34
- 2.3 | python_course_mar26 | `class1/exercises/string_ex/strings_ex1.md` | score 15
- 2.4 | python_course_mar26 | `class1/exercises/string_ex/strings_ex1.py` | score 11
- 2.5 | python_course_mar26 | `class1/exercises/func_ex/func_ex3.md` | score 3

## Chapter 3: Introducing Device Lists

PCC Chapter 3 introduces lists as a way to keep related values together.

Concept flow: `device list -> index/slice/method -> selected maintenance target`

Authored bridge examples:
- Device list basics
- Command queue

Assigned twin-bridges source maps:
- 3.1 | python_course_mar26 | `class1/lists/list_ex.py` | score 43
- 3.2 | python_course_mar26 | `class1/lists/list_methods.py` | score 43

## Chapter 4: Working Through Networks with Loops

PCC Chapter 4 makes repeated work explicit with loops, ranges, slices, and comprehensions.

Concept flow: `inventory -> for loop/comprehension -> repeated command plan`

Authored bridge examples:
- Loop through devices
- Build interface names

Assigned twin-bridges source maps:
- 4.1 | python_course_mar26 | `class1/loops/loop_ex1.py` | score 43
- 4.2 | python_course_mar26 | `class1/loops/loop_ex2.py` | score 43
- 4.3 | python_course_mar26 | `class1/loops/loop_ex3.py` | score 43
- 4.4 | python_course_mar26 | `class1/loops/loop_ex4.py` | score 43
- 4.5 | python_course_mar26 | `class1/loops/loop_ex5.py` | score 43
- 4.6 | python_course_mar26 | `class1/loops/loop_ex6.py` | score 43
- 4.7 | python_course_mar26 | `class1/loops/loop_ex7.py` | score 43
- 4.8 | python_course_mar26 | `class1/loops/while_ex1.py` | score 43
- 4.9 | python_course_mar26 | `class1/loops/while_ex2.py` | score 43
- 4.10 | python_course_mar26 | `class1/loops/while_ex3.py` | score 43
- 4.11 | python_course_mar26 | `class1/exercises/loops_ex/loops_ex1.md` | score 13
- 4.12 | python_course_mar26 | `class1/exercises/loops_ex/loops_ex2.md` | score 13
- 4.13 | python_course_mar26 | `class1/exercises/loops_ex/loops_ex3.md` | score 13
- 4.14 | python_course_mar26 | `class1/exercises/loops_ex/loops_ex1.py` | score 12
- 4.15 | python_course_mar26 | `class1/exercises/loops_ex/loops_ex2.py` | score 12
- 4.16 | python_course_mar26 | `class1/exercises/loops_ex/loops_ex3.py` | score 12

## Chapter 5: If Statements for Network Decisions

PCC Chapter 5 teaches programs to choose a path based on data.

Concept flow: `network fact -> condition -> allow/deny/remediate branch -> action`

Authored bridge examples:
- Interface state decision
- Change-window guard

Assigned twin-bridges source maps:
- 5.1 | python_course_mar26 | `class1/cond/api_support_versions.yml` | score 43
- 5.2 | python_course_mar26 | `class1/booleans/show_circuit.py` | score 38
- 5.3 | python_course_mar26 | `class1/cond/cond_ex4.py` | score 36
- 5.4 | python_course_mar26 | `class1/cond/cond_ex5.py` | score 36
- 5.5 | python_course_mar26 | `class1/cond/cond_ex1.py` | score 35
- 5.6 | python_course_mar26 | `class1/cond/cond_ex2.py` | score 35
- 5.7 | python_course_mar26 | `class1/cond/cond_ex3.py` | score 35
- 5.8 | python_course_mar26 | `class1/booleans/truish.py` | score 34
- 5.9 | python_course_mar26 | `class1/cond/tcp_services.json` | score 34
- 5.10 | python_course_mar26 | `class1/exercises/cond_ex/cond_ex1.md` | score 15
- 5.11 | python_course_mar26 | `class1/exercises/cond_ex/cond_ex1.py` | score 12

## Chapter 6: Dictionaries for Device Inventory

PCC Chapter 6 adds meaningful keys so records are easier to model.

Concept flow: `real network object -> dict keys/values -> lookup/update/report`

Authored bridge examples:
- Single device dictionary
- Nested inventory

Assigned twin-bridges source maps:
- 6.1 | python_course_mar26 | `class1/dict/tcp_services.json` | score 43
- 6.2 | python_course_mar26 | `class2/complex_dstruct/network_objects.json` | score 43
- 6.3 | python_course_mar26 | `class2/complex_dstruct/tcp_services.json` | score 43
- 6.4 | python_course_mar26 | `class1/dict/dict_ex.py` | score 35
- 6.5 | python_course_mar26 | `class2/complex_dstruct/complex_ds2.py` | score 35
- 6.6 | python_course_mar26 | `class2/complex_dstruct/complex_ds3.py` | score 35
- 6.7 | python_course_mar26 | `class2/complex_dstruct/complex_ds.py` | score 34
- 6.8 | python_course_mar26 | `class2/complex_dstruct/sessions.json` | score 34
- 6.9 | python_course_mar26 | `class1/exercises/dict_ex/dict_ex1.md` | score 18
- 6.10 | python_course_mar26 | `class1/exercises/dict_ex/dict_ex1.py` | score 16
- 6.11 | python_course_mar26 | `class2/exercises/complex_ds_ex/complex_ds_ex2.md` | score 6

## Chapter 7: Operator Input and While Loops

PCC Chapter 7 connects prompts, validation, and loops to interactive programs.

Concept flow: `operator input -> validate -> while loop -> planned network action`

Authored bridge examples:
- Bounded retry loop
- Validate requested VLAN

Assigned twin-bridges source maps:
- 7.1 | python_course_mar26 | `class1/exercises/loops_ex/while_ex1.md` | score 37
- 7.2 | python_course_mar26 | `class1/exercises/loops_ex/while_ex1.py` | score 36
- 7.3 | python_course_mar26 | `class1/try_except/try_except_ex1.py` | score 35
- 7.4 | python_course_mar26 | `class1/try_except/try_except_ex2.py` | score 35
- 7.5 | python_course_mar26 | `class1/try_except/try_except_ex3.py` | score 35
- 7.6 | python_course_mar26 | `class1/try_except/try_except_ex4.py` | score 35
- 7.7 | python_course_mar26 | `class1/try_except/try_except_ex5.py` | score 35
- 7.8 | python_course_mar26 | `class1/try_except/try_except_ex6.py` | score 35
- 7.9 | python_course_mar26 | `class1/try_except/try_except_ex7.py` | score 35
- 7.10 | python_course_mar26 | `class1/try_except/try_except_ex8.py` | score 35

## Chapter 8: Functions for Reusable Automation

PCC Chapter 8 packages behavior into named, reusable functions.

Concept flow: `arguments -> function body -> return/report -> reuse across devices`

Authored bridge examples:
- Build a show command
- Summarize device health

Assigned twin-bridges source maps:
- 8.1 | python_course_mar26 | `class1/functions/func_ex1.py` | score 34
- 8.2 | python_course_mar26 | `class1/functions/func_ex2.py` | score 34
- 8.3 | python_course_mar26 | `class1/functions/func_ex3.py` | score 34
- 8.4 | python_course_mar26 | `class1/functions/func_ex4.py` | score 34
- 8.5 | python_course_mar26 | `class1/functions/func_ex5.py` | score 34
- 8.6 | python_course_mar26 | `class2/gaia_func/gaia_funcs.py` | score 10
- 8.7 | python_course_mar26 | `class3/mgmt_func/mgmt_funcs.py` | score 10
- 8.8 | python_course_mar26 | `work/gaia_funcs.py` | score 9
- 8.9 | python_course_mar26 | `work/mgmt_funcs.py` | score 9
- 8.10 | python_course_mar26 | `class3/exercises/fw_policy_ex2/fw_policy_edit_rule.md` | score 5

## Chapter 9: Classes for Devices and Sessions

PCC Chapter 9 groups data and behavior into objects.

Concept flow: `class blueprint -> device/session instance -> methods -> automation behavior`

Authored bridge examples:
- Device object
- Session-like object for dry runs

Assigned twin-bridges source maps:
- 9.1 | python_course_mar26 | `class3/exercises/class_api_ex/chkpt_api_ex.py` | score 36
- 9.2 | python_course_mar26 | `class3/gaia_class/gaia_class.py` | score 35
- 9.3 | python_course_mar26 | `class3/gaia_class/gaia_class_cfg.py` | score 35
- 9.4 | python_course_mar26 | `class3/mgmt_class/mgmt_class.py` | score 35
- 9.5 | python_course_mar26 | `class3/mgmt_class/mgmt_class_cfg.py` | score 35
- 9.6 | python_course_mar26 | `class3/exercises/class_api_ex/chkpt_api_ex_old.py` | score 27
- 9.7 | python_course_mar26 | `class3/exercises/class_api_ex/test_chkpt_class.py` | score 27

## Chapter 10: Files, Exceptions, and Network Data

PCC Chapter 10 connects Python to files, errors, and saved data.

Concept flow: `file/API data -> read/parse -> handle errors -> save report`

Authored bridge examples:
- Parse inventory JSON safely
- Write an audit line

Assigned twin-bridges source maps:
- 10.1 | python_course_mar26 | `class1/files/read_json.py` | score 43
- 10.2 | python_course_mar26 | `class1/files/read_yaml.py` | score 43
- 10.3 | python_course_mar26 | `class1/files/write_json.py` | score 43
- 10.4 | python_course_mar26 | `class1/files/my_file.txt` | score 35
- 10.5 | python_course_mar26 | `class1/files/file_cm.py` | score 34
- 10.6 | python_course_mar26 | `class1/files/gaia_api.json` | score 34
- 10.7 | python_course_mar26 | `class1/files/gaia_api.yaml` | score 34
- 10.8 | python_course_mar26 | `class1/files/new_file.txt` | score 34
- 10.9 | python_course_mar26 | `class1/files/read_file.py` | score 34
- 10.10 | python_course_mar26 | `class1/files/write_file.py` | score 34
- 10.11 | python_course_mar26 | `class1/files/write_file_cm.py` | score 34
- 10.12 | python_course_mar26 | `class1/files/write_yaml.py` | score 34
- 10.13 | python_course_mar26 | `class2/exercises/linux_python_ex/firewalls.yml` | score 27
- 10.14 | python_course_mar26 | `class2/exercises/linux_python_ex/pathlib_ex1.md` | score 27
- 10.15 | python_course_mar26 | `class2/exercises/linux_python_ex/pathlib_ex1.py` | score 27
- 10.16 | python_course_mar26 | `class2/linux_python/os_system_ex.py` | score 25
- 10.17 | python_course_mar26 | `class2/linux_python/pathlib_ex.py` | score 25
- 10.18 | python_course_mar26 | `class2/linux_python/subprocess_ping.py` | score 25
- 10.19 | python_course_mar26 | `class2/linux_python/subprocess_popen.py` | score 25
- 10.20 | python_course_mar26 | `class1/exercises/file_ex/files_ex1.md` | score 13
- 10.21 | python_course_mar26 | `class1/exercises/file_ex/files_ex1.py` | score 11

## Chapter 11: Testing Network Automation

PCC Chapter 11 builds confidence by checking expected behavior automatically.

Concept flow: `expected network behavior -> test case -> run test -> fix automation`

Authored bridge examples:
- Test a command builder
- Test inventory validation

Assigned twin-bridges source maps:
- 11.1 | python_course_mar26 | `class3/exercises/pytest_ex/test_funcs_ex.md` | score 73
- 11.2 | python_course_mar26 | `class3/test_pytest_ex/test_mgmt_api.py` | score 57
- 11.3 | python_course_mar26 | `class3/test_pytest_ex/test_some_funcs.py` | score 56
- 11.4 | python_course_mar26 | `class3/exercises/pytest_ex/test_funcs_ex.py` | score 54
- 11.5 | python_course_mar26 | `class3/test_pytest_ex/test_simple_exc.py` | score 48
- 11.6 | python_course_mar26 | `class4/exercises/main_project/tests/test_mgmt_cfg.py` | score 48
- 11.7 | python_course_mar26 | `class3/test_pytest_ex/test_simple.py` | score 47
- 11.8 | python_course_mar26 | `class4/exercises/main_project/tests/test_gaia_cfg.py` | score 47
- 11.9 | python_course_mar26 | `class4/ssh_session/test_mgmt_cli_auth.py` | score 47
- 11.10 | python_course_mar26 | `class3/test_pytest_ex/conftest.py` | score 46
- 11.11 | python_course_mar26 | `class3/exercises/object_func_ex/test_object_funcs.py` | score 45
- 11.12 | python_course_mar26 | `class3/exercises/pytest_ex/simple_funcs.py` | score 45
- 11.13 | python_course_mar26 | `class3/test_pytest_ex/some_funcs.py` | score 44
- 11.14 | netmiko_course | `tests/test_class2.py` | score 43
- 11.15 | netmiko_course | `tests/test_class3.py` | score 43
- 11.16 | python_course_mar26 | `class2/gaia_func/test_gaia_funcs.py` | score 43
- 11.17 | python_course_mar26 | `class3/mgmt_func/test_mgmt_funcs.py` | score 43
- 11.18 | python_course_mar26 | `work/test_gaia_funcs.py` | score 43
- 11.19 | python_course_mar26 | `work/test_mgmt_funcs.py` | score 43
- 11.20 | netmiko_course | `tests/test_class7.py` | score 41
- 11.21 | python_course_mar26 | `class4/exercises/main_project/tests/test_users_and_password_pol.py` | score 38
- 11.22 | netmiko_course | `tests/test_class4.py` | score 34
- 11.23 | netmiko_course | `tests/test_class1.py` | score 32
- 11.24 | netmiko_course | `tests/test_class10.py` | score 32
- 11.25 | netmiko_course | `tests/test_class12.py` | score 32
- 11.26 | netmiko_course | `tests/test_class5.py` | score 32
- 11.27 | netmiko_course | `tests/test_class6.py` | score 31
- 11.28 | netmiko_course | `tests/test_class8.py` | score 30
- 11.29 | netmiko_course | `tests/test_class9.py` | score 30
- 11.30 | netmiko_course | `tests/test_class11.py` | score 28
- 11.31 | netmiko_course | `tests/utilities.py` | score 25
