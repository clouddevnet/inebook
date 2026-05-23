# Python Network Automation Crash Course Part II: Chapters 12-20 Coverage Index

Twin-bridges Python course: `https://github.com/twin-bridges/python_course_mar26` at `8d23646`
Twin-bridges Netmiko course: `https://github.com/twin-bridges/netmiko_course` at `8c31f4e`

This index maps each chapter to authored network-automation bridge examples and assigned twin-bridges course examples.

## Chapter 12: Starting a Netmiko Project

PCC Chapter 12 begins the first larger project by combining classes, loops, and an external library.

Concept flow: `device dict -> ConnectHandler -> prompt/show command -> disconnect`

Authored bridge examples:
- Netmiko connection shape
- Lab-safe connection checklist

Assigned twin-bridges source maps:
- 12.1 | netmiko_course | `class1/collateral/simple_conn.py` | score 35
- 12.2 | netmiko_course | `class1/collateral/simple_conn_cm.py` | score 35
- 12.3 | netmiko_course | `class1/collateral/simple_conn_dict.py` | score 35
- 12.4 | netmiko_course | `class1/exercises/exercise1.py` | score 27
- 12.5 | netmiko_course | `class1/exercises/exercise2.py` | score 27
- 12.6 | netmiko_course | `class1/exercises/exercise3.py` | score 27
- 12.7 | netmiko_course | `class1/collateral/simple_conn_slog.py` | score 26

## Chapter 13: Collecting Show Commands Across a Fleet

PCC Chapter 13 grows the project by adding repeated objects and state changes.

Concept flow: `device fleet -> command loop -> per-device output -> result dictionary`

Authored bridge examples:
- Collect simulated show output
- Track command success

Assigned twin-bridges source maps:
- 13.1 | netmiko_course | `class2/collateral/read_timeout/traceroute_long.py` | score 39
- 13.2 | netmiko_course | `class2/collateral/read_timeout/traceroute_timeout.py` | score 38
- 13.3 | netmiko_course | `class2/collateral/read_timeout/traceroute_working.py` | score 38
- 13.4 | netmiko_course | `class2/collateral/conn_mult_devices.py` | score 35
- 13.5 | netmiko_course | `class2/exercises/exercise2.py` | score 29
- 13.6 | netmiko_course | `class2/exercises/exercise1.py` | score 28
- 13.7 | netmiko_course | `class2/exercises/exercise3.py` | score 28
- 13.8 | netmiko_course | `class2/exercises/exercise4.py` | score 28
- 13.9 | netmiko_course | `class2/collateral/expect_str.py` | score 27
- 13.10 | netmiko_course | `class2/collateral/show_command.py` | score 27
- 13.11 | netmiko_course | `class2/collateral/netmiko_log.py` | score 26

## Chapter 14: Configuration, Validation, and Rollback Thinking

PCC Chapter 14 adds user experience, scoring, levels, and reset behavior to a project.

Concept flow: `intended state -> config commands -> verification command -> rollback notes`

Authored bridge examples:
- Build VLAN config
- Verification plan

Assigned twin-bridges source maps:
- 14.1 | netmiko_course | `class12/collateral/commit.py` | score 36
- 14.2 | netmiko_course | `class4/collateral/send_multiline/file_delete_pattern.py` | score 36
- 14.3 | netmiko_course | `class4/collateral/send_multiline/mline_pattern.py` | score 36
- 14.4 | netmiko_course | `class4/collateral/send_multiline_timing/file_delete_timing.py` | score 36
- 14.5 | netmiko_course | `class4/collateral/send_multiline_timing/mline_time.py` | score 36
- 14.6 | netmiko_course | `class5/collateral/config_file.py` | score 36
- 14.7 | netmiko_course | `class5/collateral/config_vlans.py` | score 36
- 14.8 | netmiko_course | `class5/exercises/exercise3.py` | score 29
- 14.9 | netmiko_course | `class12/exercises/exercise3.py` | score 28
- 14.10 | netmiko_course | `class4/exercises/exercise3.py` | score 28
- 14.11 | netmiko_course | `class4/exercises/exercise4.py` | score 28
- 14.12 | netmiko_course | `class5/exercises/exercise1.py` | score 28
- 14.13 | netmiko_course | `class5/exercises/exercise2.py` | score 28
- 14.14 | netmiko_course | `class12/exercises/exercise1.py` | score 27
- 14.15 | netmiko_course | `class12/exercises/exercise2.py` | score 27
- 14.16 | netmiko_course | `class4/exercises/exercise1.py` | score 27
- 14.17 | netmiko_course | `class4/exercises/exercise2.py` | score 27
- 14.18 | netmiko_course | `class5/collateral/disable_cmd_verify.py` | score 27
- 14.19 | netmiko_course | `class5/exercises/vlans.txt` | score 27
- 14.20 | netmiko_course | `class12/collateral/config_mode.py` | score 26
- 14.21 | netmiko_course | `class12/collateral/enable.py` | score 26
- 14.22 | netmiko_course | `class12/collateral/fast_cli.py` | score 26
- 14.23 | netmiko_course | `class4/collateral/send_command_prompting.py` | score 26
- 14.24 | netmiko_course | `class4/collateral/send_command_timing_prompting.py` | score 26
- 14.25 | netmiko_course | `class5/collateral/config_rm_user.py` | score 26
- 14.26 | netmiko_course | `class5/collateral/lab_devices.yml` | score 26
- 14.27 | netmiko_course | `class5/collateral/vlans.txt` | score 26

## Chapter 15: Generating Network Reports

PCC Chapter 15 turns generated data into visual insight.

Concept flow: `raw command output -> parsed records -> aggregate -> report`

Authored bridge examples:
- Summarize interface states
- Compliance score

Assigned twin-bridges source maps:
- 15.1 | netmiko_course | `class3/exercises/show_vlan.ttp` | score 36
- 15.2 | netmiko_course | `class3/collateral/show_genie.py` | score 35
- 15.3 | netmiko_course | `class3/collateral/show_ttp.py` | score 35
- 15.4 | netmiko_course | `class3/exercises/exercise5.py` | score 28
- 15.5 | netmiko_course | `class3/exercises/exercise1.py` | score 27
- 15.6 | netmiko_course | `class3/exercises/exercise2.py` | score 27
- 15.7 | netmiko_course | `class3/exercises/exercise3.py` | score 27
- 15.8 | netmiko_course | `class3/exercises/exercise4.py` | score 27
- 15.9 | netmiko_course | `class3/collateral/read_timeout_timing/traceroute_timeout.py` | score 26
- 15.10 | netmiko_course | `class3/collateral/read_timeout_timing/traceroute_working.py` | score 26
- 15.11 | netmiko_course | `class3/collateral/show_genie_nxos.py` | score 26
- 15.12 | netmiko_course | `class3/collateral/show_run_intf.ttp` | score 26
- 15.13 | netmiko_course | `class3/collateral/show_textfsm.py` | score 26
- 15.14 | netmiko_course | `class3/collateral/show_timing.py` | score 26
- 15.15 | python_course_mar26 | `class3/list_comprehenson/list_comp_ex.py` | score 9

## Chapter 16: Inventories, YAML, JSON, and Real-World Data

PCC Chapter 16 pulls data from files and online sources.

Concept flow: `YAML/JSON/source of truth -> parse -> clean -> command plan`

Authored bridge examples:
- Use structured inventory data
- Generate commands from data

Assigned twin-bridges source maps:
- 16.1 | netmiko_course | `class10/exercises/devices.yaml` | score 45
- 16.2 | netmiko_course | `class10/exercises/exercise2.py` | score 34
- 16.3 | netmiko_course | `class10/exercises/exercise1.py` | score 27
- 16.4 | netmiko_course | `class10/exercises/exercise3.py` | score 27
- 16.5 | netmiko_course | `class10/exercises/my_hosts.txt` | score 27
- 16.6 | netmiko_course | `class10/collateral/detect_platform.py` | score 26
- 16.7 | netmiko_course | `class10/collateral/snmp_detect.py` | score 26
- 16.8 | netmiko_course | `class10/collateral/telnet_example.py` | score 26
- 16.9 | netmiko_course | `class10/collateral/write_read.py` | score 26
- 16.10 | python_course_mar26 | `class1/exercises/dict_ex/net_object_net128.json` | score 11
- 16.11 | python_course_mar26 | `class1/exercises/file_ex/network_objects.json` | score 11
- 16.12 | python_course_mar26 | `class2/exercises/complex_ds_ex/show_tasks.json` | score 11
- 16.13 | python_course_mar26 | `class2/exercises/complex_ds_ex/complex_ds_ex2.py` | score 7
- 16.14 | python_course_mar26 | `class1/exercises/list_ex/list_ex1.py` | score 5
- 16.15 | python_course_mar26 | `class2/exercises/complex_ds_ex/complex_ds_ex1.py` | score 5
- 16.16 | python_course_mar26 | `class1/exercises/list_ex/list_ex1.md` | score 4
- 16.17 | python_course_mar26 | `class2/exercises/complex_ds_ex/complex_ds_ex1.md` | score 4

## Chapter 17: Network APIs

PCC Chapter 17 uses web APIs and response dictionaries.

Concept flow: `API endpoint -> request/session -> JSON dicts -> object/config action`

Authored bridge examples:
- API response dictionary
- Pagination pattern

Assigned twin-bridges source maps:
- 17.1 | python_course_mar26 | `class4/sdk_api_query/sdk_api_query.py` | score 71
- 17.2 | python_course_mar26 | `class4/exercises/api_pages_ex/api_pages_ex.py` | score 67
- 17.3 | python_course_mar26 | `class4/exercises/main_project/03_mgmt_api_cfg.py` | score 66
- 17.4 | python_course_mar26 | `class4/exercises/api_pages_ex/api_query_ex.py` | score 64
- 17.5 | python_course_mar26 | `class4/sdk_api_query/sdk_gen_api_query.py` | score 62
- 17.6 | python_course_mar26 | `class2/exercises/gaia_api_ex/gaia_auth_ex.md` | score 56
- 17.7 | python_course_mar26 | `class3/exercises/chkpnt_sdk_ex/group_net_objects_ex.py` | score 54
- 17.8 | python_course_mar26 | `class3/exercises/chkpnt_sdk_ex/mgmt_cfg_hostobj_ex.py` | score 54
- 17.9 | python_course_mar26 | `class3/exercises/chkpnt_sdk_ex/mgmt_cfg_netobj_ex.py` | score 54
- 17.10 | python_course_mar26 | `class2/exercises/gaia_api_ex/gaia_auth_ex.py` | score 52
- 17.11 | python_course_mar26 | `class3/chkpnt_sdk/api_notes.txt` | score 52
- 17.12 | python_course_mar26 | `class3/exercises/mgmt_api_ex/mgmt_api_ex1.md` | score 52
- 17.13 | python_course_mar26 | `class3/exercises/mgmt_api_ex/mgmt_api_ex1.py` | score 52
- 17.14 | python_course_mar26 | `class3/exercises/mgmt_api_ex/mgmt_funcs.py` | score 50
- 17.15 | python_course_mar26 | `class4/exercises/api_pages_ex/api_pagination.md` | score 50
- 17.16 | python_course_mar26 | `class3/chkpnt_sdk/gaia_intf.py` | score 48
- 17.17 | python_course_mar26 | `class3/chkpnt_sdk/gaia_intf_fingerprint.py` | score 48
- 17.18 | python_course_mar26 | `class3/chkpnt_sdk/mgmt_cfg_netobj.py` | score 48
- 17.19 | python_course_mar26 | `class2/api/gaia_auth.py` | score 47
- 17.20 | python_course_mar26 | `class3/exercises/class_api_ex/chkpt_api_ex.md` | score 47
- 17.21 | python_course_mar26 | `work/clear_sessions.py` | score 47
- 17.22 | python_course_mar26 | `class3/chkpnt_sdk/gaia_cfg_dns.py` | score 46
- 17.23 | python_course_mar26 | `class3/chkpnt_sdk/mgmt_show_networks.py` | score 45
- 17.24 | python_course_mar26 | `class2/api/awx_auth.py` | score 44
- 17.25 | python_course_mar26 | `class2/exercises/gaia_api_ex/gaia_proc.py` | score 42
- 17.26 | python_course_mar26 | `class2/exercises/gaia_api_ex/gaia_proc.md` | score 36
- 17.27 | python_course_mar26 | `class2/gaia_ssh/api_status.py` | score 35
- 17.28 | python_course_mar26 | `class3/exercises/fw_policy_ex2/fw_policy_funcs.py` | score 33
- 17.29 | python_course_mar26 | `class3/exercises/chkpnt_sdk_ex/mgmt_cfg_hostobj_ex.md` | score 32
- 17.30 | python_course_mar26 | `class3/fw_policy/fw_policy.py` | score 31
- 17.31 | python_course_mar26 | `class3/exercises/chkpnt_sdk_ex/group_net_objects_ex.md` | score 30
- 17.32 | python_course_mar26 | `class3/exercises/chkpnt_sdk_ex/mgmt_cfg_netobj_ex.md` | score 30
- 17.33 | python_course_mar26 | `class3/exercises/fw_policy_ex1/fw_policy_funcs.py` | score 30
- 17.34 | python_course_mar26 | `class4/exercises/main_project/tests/conftest.py` | score 30
- 17.35 | python_course_mar26 | `lib_class4/chkpt_policy_funcs.py` | score 28
- 17.36 | python_course_mar26 | `class3/chkpnt_sdk/fingerprints.txt` | score 25
- 17.37 | python_course_mar26 | `lib_class4/chkpt_object_funcs.py` | score 25
- 17.38 | python_course_mar26 | `class3/exercises/object_func_ex/object_funcs.py` | score 21
- 17.39 | python_course_mar26 | `work/gaia_intf_work.py` | score 20
- 17.40 | python_course_mar26 | `class3/exercises/fw_policy_ex1/fw_policy_ex1.py` | score 19
- 17.41 | python_course_mar26 | `class3/exercises/fw_policy_ex2/fw_policy_edit_rule.py` | score 19
- 17.42 | python_course_mar26 | `class3/exercises/fw_policy_ex2/fw_policy_delete_rule.py` | score 18
- 17.43 | python_course_mar26 | `class4/exercises/show_changes_ex/show_changes.py` | score 18
- 17.44 | python_course_mar26 | `class3/exercises/object_func_ex/conftest.py` | score 17
- 17.45 | python_course_mar26 | `class3/exercises/fw_policy_ex1/object_funcs.py` | score 14
- 17.46 | python_course_mar26 | `class3/exercises/fw_policy_ex2/object_funcs.py` | score 14
- 17.47 | python_course_mar26 | `class3/exercises/fw_policy_ex1/fw_policy_ex1.md` | score 13
- 17.48 | python_course_mar26 | `class3/exercises/object_func_ex/common_object_function.md` | score 10
- 17.49 | python_course_mar26 | `class3/exercises/object_func_ex/object_function_tests.md` | score 8

## Chapter 18: Building a Network Automation Tool

PCC Chapter 18 starts a web app by organizing models, views, and templates.

Concept flow: `operator request -> validation -> automation function -> rendered report`

Authored bridge examples:
- Tool pipeline
- Render a tiny report

Assigned twin-bridges source maps:
- 18.1 | python_course_mar26 | `class4/exercises/main_project/blocked_ip_funcs.py` | score 45
- 18.2 | python_course_mar26 | `class4/exercises/main_project/run_scripts.sh` | score 45
- 18.3 | python_course_mar26 | `class4/exercises/main_project/main_project.md` | score 37
- 18.4 | python_course_mar26 | `class4/exercises/main_project/01_gaia_cfg_settings.py` | score 36
- 18.5 | python_course_mar26 | `class4/exercises/main_project/02_gaia_ssh_cfg.py` | score 36
- 18.6 | python_course_mar26 | `class4/exercises/main_project/blocked_ips.txt` | score 36
- 18.7 | python_course_mar26 | `class4/exercises/main_project/gaia_check_password_policy.py` | score 36
- 18.8 | python_course_mar26 | `class4/exercises/main_project/gen_fw_rules.py` | score 36
- 18.9 | python_course_mar26 | `class4/exercises/main_project/host_objects.py` | score 36
- 18.10 | python_course_mar26 | `class4/run_script/run_script_gaia.py` | score 35
- 18.11 | python_course_mar26 | `class4/run_script/run_script_mgmt.py` | score 35

## Chapter 19: Credentials, Ownership, and Guardrails

PCC Chapter 19 adds user accounts, protected data, forms, and ownership.

Concept flow: `operator identity -> permissions -> owned device set -> protected action`

Authored bridge examples:
- Permission guard
- Secrets stay out of code

Assigned twin-bridges source maps:
- 19.1 | netmiko_course | `class6/collateral/ssh_keys.py` | score 35
- 19.2 | netmiko_course | `class6/collateral/ssh_keys_agent.py` | score 35
- 19.3 | netmiko_course | `class6/collateral/ssh_keys_encr.py` | score 35
- 19.4 | netmiko_course | `class7/collateral/auth_fail.py` | score 35
- 19.5 | netmiko_course | `class7/collateral/auth_fail_keys.py` | score 35
- 19.6 | netmiko_course | `class7/collateral/auth_retry.py` | score 35
- 19.7 | netmiko_course | `class7/collateral/auth_retry_func.py` | score 35
- 19.8 | python_course_mar26 | `class4/ssh_session/mgmt_cli_session.md` | score 35
- 19.9 | python_course_mar26 | `class2/gaia_ssh/mgmt_cli_sessions.py` | score 34
- 19.10 | python_course_mar26 | `class4/ssh_session/conftest.py` | score 34
- 19.11 | python_course_mar26 | `class4/ssh_session/mgmt_cli_session.py` | score 34
- 19.12 | netmiko_course | `class6/exercises/exercise1.py` | score 27
- 19.13 | netmiko_course | `class6/exercises/exercise2.py` | score 27
- 19.14 | netmiko_course | `class6/exercises/exercise3.py` | score 27
- 19.15 | netmiko_course | `class6/exercises/my_ssh_config` | score 27
- 19.16 | netmiko_course | `class7/exercises/exercise1.py` | score 27
- 19.17 | netmiko_course | `class7/exercises/exercise2.py` | score 27
- 19.18 | netmiko_course | `class7/exercises/exercise3.py` | score 27
- 19.19 | netmiko_course | `class7/exercises/exercise4.py` | score 27
- 19.20 | python_course_mar26 | `class2/exercises/gaia_ssh_ex/gaia_ssh_ex1.md` | score 27
- 19.21 | python_course_mar26 | `class2/exercises/gaia_ssh_ex/gaia_ssh_ex1.py` | score 27
- 19.22 | python_course_mar26 | `class2/exercises/gaia_ssh_ex/mgmt_cli_ex1.md` | score 27
- 19.23 | python_course_mar26 | `class2/exercises/gaia_ssh_ex/mgmt_cli_ex1.py` | score 27
- 19.24 | netmiko_course | `class6/collateral/lab_devices.yml` | score 26
- 19.25 | netmiko_course | `class6/collateral/ssh_config_file.py` | score 26
- 19.26 | netmiko_course | `class6/collateral/ssh_notes.txt` | score 26
- 19.27 | netmiko_course | `class6/collateral/ssh_proxy_jump.py` | score 26
- 19.28 | netmiko_course | `class7/collateral/banner_fail.py` | score 26
- 19.29 | netmiko_course | `class7/collateral/conn_log.py` | score 26
- 19.30 | netmiko_course | `class7/collateral/devices.py` | score 26
- 19.31 | netmiko_course | `class7/collateral/dns_fail.py` | score 26
- 19.32 | netmiko_course | `class7/collateral/handle_failures.py` | score 26
- 19.33 | netmiko_course | `class7/collateral/lab_devices.yml` | score 26
- 19.34 | netmiko_course | `class7/collateral/tcp_conn_fail.py` | score 26
- 19.35 | python_course_mar26 | `class2/gaia_ssh/cfg_domain_name.py` | score 25
- 19.36 | python_course_mar26 | `class2/gaia_ssh/retrieve_fingerprint.py` | score 25
- 19.37 | python_course_mar26 | `class2/gaia_ssh/show_version.py` | score 25
- 19.38 | python_course_mar26 | `class4/concurrency/ssh_procs_ascompleted.py` | score 25
- 19.39 | python_course_mar26 | `class4/concurrency/ssh_procs_ascompleted_cm.py` | score 25
- 19.40 | python_course_mar26 | `class4/concurrency/ssh_threads_ascompleted.py` | score 25
- 19.41 | python_course_mar26 | `class4/concurrency/ssh_threads_ascompleted_cm.py` | score 25
- 19.42 | python_course_mar26 | `class4/concurrency/ssh_threads_wait.py` | score 25
- 19.43 | python_course_mar26 | `work/ssh_conn_ex.py` | score 25

## Chapter 20: Operating and Deploying Automation

PCC Chapter 20 finishes a project by styling, configuring, deploying, and operating it.

Concept flow: `local script -> config/logging/tests -> scheduled run -> operational report`

Authored bridge examples:
- Operational run summary
- Release checklist

Assigned twin-bridges source maps:
- 20.1 | netmiko_course | `class9/collateral/get_file.py` | score 37
- 20.2 | netmiko_course | `class9/collateral/put_file.py` | score 37
- 20.3 | netmiko_course | `deploy.sh` | score 34
- 20.4 | netmiko_course | `tests.sh` | score 34
- 20.5 | netmiko_course | `class9/exercises/exercise1.py` | score 29
- 20.6 | netmiko_course | `class9/exercises/exercise2.py` | score 29
- 20.7 | netmiko_course | `class9/collateral/get_progress_bar.py` | score 28
- 20.8 | netmiko_course | `class9/collateral/put_progress_bar.py` | score 28
- 20.9 | netmiko_course | `class11/exercises/exercise1_final.py` | score 27
- 20.10 | netmiko_course | `class11/exercises/exercise1a.py` | score 27
- 20.11 | netmiko_course | `class11/exercises/exercise1b.py` | score 27
- 20.12 | netmiko_course | `class11/exercises/exercise1c.py` | score 27
- 20.13 | netmiko_course | `class8/exercises/exercise1.py` | score 27
- 20.14 | netmiko_course | `class8/exercises/exercise2.py` | score 27
- 20.15 | netmiko_course | `class8/exercises/lab_devices.yml` | score 27
- 20.16 | netmiko_course | `class8/exercises/utilities.py` | score 27
- 20.17 | netmiko_course | `class9/exercises/cfg_name_servers.txt` | score 27
- 20.18 | netmiko_course | `class9/exercises/show_interfaces_ktb.txt` | score 27
- 20.19 | python_course_mar26 | `class4/exercises/concurrency_ex/concurrency_ex.md` | score 27
- 20.20 | python_course_mar26 | `class4/exercises/concurrency_ex/concurrency_ex.py` | score 27
- 20.21 | python_course_mar26 | `class4/exercises/concurrency_ex/my_devices.py` | score 27
- 20.22 | netmiko_course | `class11/collateral/redispatch1.py` | score 26
- 20.23 | netmiko_course | `class11/collateral/term_server1.py` | score 26
- 20.24 | netmiko_course | `class11/collateral/term_server2.py` | score 26
- 20.25 | netmiko_course | `class11/collateral/term_server3.py` | score 26
- 20.26 | netmiko_course | `class11/collateral/term_server4.py` | score 26
- 20.27 | netmiko_course | `class8/collateral/cf_processes.py` | score 26
- 20.28 | netmiko_course | `class8/collateral/cf_threads.py` | score 26
- 20.29 | netmiko_course | `class8/collateral/cf_threads_asc.py` | score 26
- 20.30 | netmiko_course | `class8/collateral/lab_devices.yml` | score 26
- 20.31 | netmiko_course | `class9/collateral/test.txt` | score 26
- 20.32 | netmiko_course | `class9/collateral/test2.txt` | score 26
- 20.33 | netmiko_course | `class9/collateral/testx.txt` | score 26
- 20.34 | netmiko_course | `.netmiko.yml` | score 25
- 20.35 | netmiko_course | `README.md` | score 25
- 20.36 | netmiko_course | `lab_devices.yml` | score 25
- 20.37 | netmiko_course | `requirements.txt` | score 25
- 20.38 | netmiko_course | `setup.cfg` | score 25
- 20.39 | python_course_mar26 | `class4/concurrency/my_devices.py` | score 25
- 20.40 | python_course_mar26 | `class1/exercises/func_ex/func_ex1.md` | score 2
- 20.41 | python_course_mar26 | `class1/exercises/func_ex/func_ex1.py` | score 2
- 20.42 | python_course_mar26 | `class1/exercises/func_ex/func_ex2.md` | score 2
- 20.43 | python_course_mar26 | `class1/exercises/func_ex/func_ex2.py` | score 2
- 20.44 | python_course_mar26 | `class1/exercises/func_ex/func_ex3.py` | score 2
- 20.45 | python_course_mar26 | `class1/exercises/list_ex/locations.yml` | score 2
- 20.46 | python_course_mar26 | `class3/exercises/fw_policy_ex1/chkpt_exceptions.py` | score 2
- 20.47 | python_course_mar26 | `class3/exercises/fw_policy_ex2/chkpt_exceptions.py` | score 2
- 20.48 | python_course_mar26 | `class3/exercises/fw_policy_ex2/fw_policy_delete_rule.md` | score 2
- 20.49 | python_course_mar26 | `README.md` | score 1
- 20.50 | python_course_mar26 | `class1/libraries/lib_test1.py` | score 1
- 20.51 | python_course_mar26 | `class1/libraries/lib_test2.py` | score 1
- 20.52 | python_course_mar26 | `class1/libraries/sys_path_ex.py` | score 1
- 20.53 | python_course_mar26 | `class3/sets/set_ex.py` | score 1
- 20.54 | python_course_mar26 | `lib_class4/chkpt_exceptions.py` | score 1
- 20.55 | python_course_mar26 | `work/notes.txt` | score 1
