# Python Crash Course Appendices A-C Coverage Index

Source PDF: `C:\Users\jag\Downloads\Python Crash Course - 3rd Edition - Eric Matthes.pdf`
Official script source: `https://github.com/ehmatthes/pcc_3e`

This index lists every captured source block.

## Appendix A: Installation and Troubleshooting

Source: PDF pages 741-748
PDF pages for outline/context: 741-748

Captured blocks: 10

- A.1 | PDF | page 744 | Installing the Latest Version of Python | $ sudo apt install python3-dev python3-pip python3-venv
- A.2 | PDF | page 745 | Installing the Latest Version of Python | $ sudo add-apt-repository ppa:deadsnakes/ppa $ sudo apt update $ sudo apt install python3.11
- A.3 | PDF | page 745 | Installing the Latest Version of Python | $ python3.11 >>>
- A.4 | PDF | page 745 | Installing the Latest Version of Python | python3.11
- A.5 | PDF | page 745 | Installing the Latest Version of Python | $ sudo apt install python3.11-dev python3.11-venv
- A.6 | PDF | page 745 | Installing the Latest Version of Python | python3.11
- A.7 | PDF | page 746 | Python Keywords | $ python --version Python 3.11.0
- A.8 | PDF | page 747 | Python Built-in Functions | False await else import pass None break except in raise True class finally is return and continue for lambda try as d...
- A.9 | PDF | page 747 | Python Built-in Functions | abs() hash() slice() aiter() help() sorted() all() hex() staticmethod() any() id() str() anext() input() sum() ascii(...
- A.10 | PDF | page 748 | Python Built-in Functions | globals() set() hasattr() setattr()

## Appendix B: Text Editors and IDEs

Source: PDF pages 749-760
PDF pages for outline/context: 749-760

Captured blocks: 5

- B.1 | PDF | page 753 | Configuring VS Code | editor.rulers
- B.2 | PDF | page 753 | Configuring VS Code | "editor.rulers": [ 80, ]
- B.3 | PDF | page 754 | Configuring VS Code | { --snip-- "configurations": [ { --snip-- "console": "internalConsole", "justMyCode": true } ] }
- B.4 | PDF | page 755 | VS Code Shortcuts | input()
- B.5 | PDF | page 756 | VS Code Shortcuts | #

## Appendix C: Getting Help

Source: PDF pages 761-853
PDF pages for outline/context: 761-853

Captured blocks: 158

- C.1 | PDF | page 764 | Stack Overflow | > python hello _world.py Python was not found; run without arguments to install from t he Microsoft Store...
- C.2 | PDF | page 770 | Ignoring Files | $ git config --global user.name " $ git config --global user.email "
- C.3 | PDF | page 770 | Ignoring Files | $ git config --global init.defaultBranch main
- C.4 | PDF | page 770 | Ignoring Files | print("Hello Git world!")
- C.5 | PDF | page 771 | Initializing a Repository | .DS_Store
- C.6 | PDF | page 771 | Initializing a Repository | git_practice$ git init Initialized empty Git repository in git_practice/.git/ git_practice$
- C.7 | PDF | page 772 | Adding Files to the Repository | git_practice$ git status On branch main No commits yet
- C.8 | PDF | page 772 | Adding Files to the Repository | Untracked files: (use "git add <file>..." to include in what will be committ ed) .gitignore hello_git.py
- C.9 | PDF | page 772 | Adding Files to the Repository | nothing added to commit but untracked files present (use "gi t add" to track) git_practice$
- C.10 | PDF | page 773 | Making a Commit | git_practice$ git add . git_practice$ git status On branch main No commits yet
- C.11 | PDF | page 773 | Making a Commit | Changes to be committed: (use "git rm --cached <file>..." to unstage) new file: .gitignore new file: hello_git.py
- C.12 | PDF | page 773 | Making a Commit | git_practice$
- C.13 | PDF | page 773 | Making a Commit | git_practice$ git commit -m "Started project." [main (root-commit) cea13dd] Started project. 2 files changed, 5 inser...
- C.14 | PDF | page 774 | Checking the Log | git_practice$ git log commit cea13ddc51b885d05a410201a54faf20e0d2e246 (HEAD -> mai n) Author: eric <eric@example.com>...
- C.15 | PDF | page 774 | Checking the Log | Started project. git_practice$
- C.16 | PDF | page 774 | Checking the Log | git_practice$ git log --pretty=oneline cea13ddc51b885d05a410201a54faf20e0d2e246 (HEAD -> main) Start ed project. git_...
- C.17 | PDF | page 775 | The Second Commit | --pretty=oneline
- C.18 | PDF | page 775 | The Second Commit | print("Hello Git world!") print("Hello everyone.")
- C.19 | PDF | page 775 | The Second Commit | git_practice$ git status On branch main Changes not staged for commit: (use "git add <file>..." to update what will b...
- C.20 | PDF | page 775 | The Second Commit | modified: hello_git.py
- C.21 | PDF | page 775 | The Second Commit | no changes added to commit (use "git add" and/or "git commit -a") git_practice$
- C.22 | PDF | page 775 | The Second Commit | git_practice$ git commit -am "Extended greeting." [main 945fa13] Extended greeting. 1 file changed, 1 insertion(+), 1...
- C.23 | PDF | page 776 | Abandoning Changes | git_practice$ git status On branch main nothing to commit, working tree clean git_practice$ git log --pretty=oneline ...
- C.24 | PDF | page 776 | Abandoning Changes | print("Hello Git world!") print("Hello everyone.")
- C.25 | PDF | page 776 | Abandoning Changes | print("Oh no, I broke the project!")
- C.26 | PDF | page 776 | Abandoning Changes | git_practice$ git status On branch main Changes not staged for commit:
- C.27 | PDF | page 777 | Abandoning Changes | (use "git add <file>..." to update what will be committed) (use "git restore <file>..." to discard changes in working...
- C.28 | PDF | page 777 | Abandoning Changes | modified: hello_git.py
- C.29 | PDF | page 777 | Abandoning Changes | no changes added to commit (use "git add" and/or "git commit -a") git_practice$
- C.30 | PDF | page 777 | Abandoning Changes | git_practice$ git restore . git_practice$ git status On branch main nothing to commit, working tree clean git_practice$
- C.31 | PDF | page 777 | Abandoning Changes | git restore .
- C.32 | PDF | page 777 | Abandoning Changes | print("Hello Git world!") print("Hello everyone.")
- C.33 | PDF | page 778 | Checking Out Previous Commits | git_practice$ git log --pretty=oneline 945fa13af128a266d0114eebb7a3276f7d58ecd2 (HEAD -> main) Exten ded greeting. ce...
- C.34 | PDF | page 778 | Checking Out Previous Commits | You are in 'detached HEAD' state. You can look around, make experimental changes and commit them, and you can discard...
- C.35 | PDF | page 778 | Checking Out Previous Commits | If you want to create a new branch to retain commits you crea te, you may do so (now or later) by using -c with the s...
- C.36 | PDF | page 779 | Checking Out Previous Commits | Or undo this operation with:
- C.37 | PDF | page 779 | Checking Out Previous Commits | Turn off this advice by setting config variable advice.detach edHead to false
- C.38 | PDF | page 779 | Checking Out Previous Commits | HEAD is now at cea13d Started project. git_practice$
- C.39 | PDF | page 779 | Checking Out Previous Commits | git_practice$ git switch - Previous HEAD position was cea13d Started project. Switched to branch 'main' git_practice$
- C.40 | PDF | page 779 | Checking Out Previous Commits | git_practice$ git status On branch main nothing to commit, working directory clean git_practice$ git log --pretty=one...
- C.41 | PDF | page 780 | Deleting the Repository | 945fa13af128a266d0114eebb7a3276f7d58ecd2 (HEAD -> main) Exten ded greeting. cea13ddc51b885d05a410201a54faf20e0d2e246 ...
- C.42 | PDF | page 781 | Deleting the Repository | git_practice$ git status On branch main nothing to commit, working directory clean git_practice$ rm -rf .git/ git_pra...
- C.43 | PDF | page 781 | Deleting the Repository | Untracked files: (use "git add <file>..." to include in what will be committ ed) .gitignore hello_git.py
- C.44 | PDF | page 781 | Deleting the Repository | nothing added to commit but untracked files present (use "git add" to track) git_practice$ git add . git_practice$ gi...
- C.45 | PDF | page 786 | Follow Onscreen Suggestions | $ platform push Enter a number to choose a project: [0] ll_project (votohz445ljyg) > 0
- C.46 | PDF | page 786 | Follow Onscreen Suggestions | [RootNotFoundException] Project root not found. This can only be run from inside a project directory.
- C.47 | PDF | page 786 | Follow Onscreen Suggestions | To set the project for this Git repository, run: platform project:set-remote [id]
- C.48 | PDF | page 786 | Follow Onscreen Suggestions | 0 RootNotFoundException
- C.49 | PDF | page 786 | Follow Onscreen Suggestions | project:set-remote
- C.50 | PDF | page 786 | Follow Onscreen Suggestions | $ platform project:set-remote votohz445ljyg Setting the remote project for this repository to: ll_project (votohz445l...
- C.51 | PDF | page 786 | Follow Onscreen Suggestions | The remote project for this repository is now set to: ll_project (votohz445ljyg)
- C.52 | PDF | page 787 | Read the Log Output | $ platform push Are you sure you want to push to the main (production) branc h? [Y/n] y Pushing HEAD to the existing ...
- C.53 | PDF | page 788 | Read the Log Output | --snip-- Collecting soupsieve==2.3.2.post1 Using cached soupsieve-2.3.2.post1-py3-none-any.whl (37 kB) Collecting sql...
- C.54 | PDF | page 788 | Read the Log Output | 130 static files copied to '/app/static'.
- C.55 | PDF | page 788 | Read the Log Output | Executing pre-flight checks... --snip--
- C.56 | PDF | page 789 | OS-Specific Troubleshooting | $ curl -fsS https://platform.sh/cli/installer | php
- C.57 | PDF | page 792 | Deploying from Windows | > curl -fsS https://platform.sh/cli/installer | php
- C.58 | PDF | page 792 | Deploying from Windows | ls dir
- C.59 | PDF | page 793 | Deploying from Linux | $ brew install php
- C.60 | PDF | page 794 | Other Deployment Approaches | $ curl -fsS https://platform.sh/cli/installer | php Command 'curl' not found, but can be installed with: sudo apt ins...
- C.61 | PDF | page 794 | Other Deployment Approaches | $ sudo apt install curl php-cli
- C.62 | PDF | page 797 | Index | +=
- C.63 | PDF | page 797 | Index | {}
- C.64 | PDF | page 797 | Index | ==
- C.65 | PDF | page 798 | Index | >=
- C.66 | PDF | page 798 | Index | #
- C.67 | PDF | page 798 | Index | !=
- C.68 | PDF | page 798 | Index | <=
- C.69 | PDF | page 798 | Index | []
- C.70 | PDF | page 798 | Index | +=
- C.71 | PDF | page 798 | Index | >>>
- C.72 | PDF | page 802 | Index | append()
- C.73 | PDF | page 803 | Index | {}
- C.74 | PDF | page 805 | Index | __init__()
- C.75 | PDF | page 805 | Index | super()
- C.76 | PDF | page 805 | Index | __init()__
- C.77 | PDF | page 806 | Index | csv.reader()
- C.78 | PDF | page 807 | Index | def
- C.79 | PDF | page 808 | Index | get()
- C.80 | PDF | page 808 | Index | items()
- C.81 | PDF | page 808 | Index | keys()
- C.82 | PDF | page 808 | Index | values()
- C.83 | PDF | page 813 | Index | save()
- C.84 | PDF | page 815 | Index | __str__()
- C.85 | PDF | page 815 | Index | redirect()
- C.86 | PDF | page 818 | Index | enumerate()
- C.87 | PDF | page 819 | Index | exists()
- C.88 | PDF | page 819 | Index | read_text()
- C.89 | PDF | page 819 | Index | splitlines()
- C.90 | PDF | page 819 | Index | write_text()
- C.91 | PDF | page 823 | Index | #
- C.92 | PDF | page 824 | Index | ==
- C.93 | PDF | page 825 | Index | import *
- C.94 | PDF | page 825 | Index | import this
- C.95 | PDF | page 825 | Index | input()
- C.96 | PDF | page 825 | Index | insert()
- C.97 | PDF | page 825 | Index | itemgetter()
- C.98 | PDF | page 825 | Index | items()
- C.99 | PDF | page 826 | Index | json.dumps()
- C.100 | PDF | page 826 | Index | json.loads()
- C.101 | PDF | page 826 | Index | keys()
- C.102 | PDF | page 829 | Index | len()
- C.103 | PDF | page 830 | Index | enumerate()
- C.104 | PDF | page 831 | Index | len()
- C.105 | PDF | page 831 | Index | max()
- C.106 | PDF | page 831 | Index | min()
- C.107 | PDF | page 831 | Index | range()
- C.108 | PDF | page 831 | Index | sum()
- C.109 | PDF | page 831 | Index | reverse()
- C.110 | PDF | page 831 | Index | sorted()
- C.111 | PDF | page 831 | Index | sort()
- C.112 | PDF | page 832 | Index | lstrip()
- C.113 | PDF | page 833 | Index | set_aspect()
- C.114 | PDF | page 834 | Index | plot()
- C.115 | PDF | page 834 | Index | savefig()
- C.116 | PDF | page 834 | Index | scatter()
- C.117 | PDF | page 834 | Index | subplots()
- C.118 | PDF | page 835 | Index | next()
- C.119 | PDF | page 836 | Index | round()
- C.120 | PDF | page 838 | Index | fig.show()
- C.121 | PDF | page 838 | Index | fig.write_html()
- C.122 | PDF | page 839 | Index | update_layout()
- C.123 | PDF | page 839 | Index | update_traces()
- C.124 | PDF | page 839 | Index | plotly.express
- C.125 | PDF | page 839 | Index | px.bar()
- C.126 | PDF | page 839 | Index | scatter_geo()
- C.127 | PDF | page 839 | Index | pop()
- C.128 | PDF | page 840 | Index | clock.tick()
- C.129 | PDF | page 841 | Index | print()
- C.130 | PDF | page 841 | Index | get_rect()
- C.131 | PDF | page 842 | Index | >>>
- C.132 | PDF | page 843 | Index | choice()
- C.133 | PDF | page 843 | Index | fill_walk()
- C.134 | PDF | page 844 | Index | range()
- C.135 | PDF | page 844 | Index | read_text()
- C.136 | PDF | page 844 | Index | removeprefix()
- C.137 | PDF | page 844 | Index | removesuffix()
- C.138 | PDF | page 844 | Index | randint()
- C.139 | PDF | page 844 | Index | rstrip()
- C.140 | PDF | page 845 | Index | sleep()
- C.141 | PDF | page 845 | Index | sorted()
- C.142 | PDF | page 845 | Index | sort()
- C.143 | PDF | page 845 | Index | splitlines()
- C.144 | PDF | page 845 | Index | split()
- C.145 | PDF | page 846 | Index | lower()
- C.146 | PDF | page 846 | Index | lstrip()
- C.147 | PDF | page 846 | Index | removeprefix()
- C.148 | PDF | page 846 | Index | removesuffix()
- C.149 | PDF | page 846 | Index | rstrip()
- C.150 | PDF | page 846 | Index | split()
- C.151 | PDF | page 846 | Index | splitlines()
- C.152 | PDF | page 846 | Index | strip()
- C.153 | PDF | page 846 | Index | title()
- C.154 | PDF | page 846 | Index | upper()
- C.155 | PDF | page 847 | Index | strip()
- C.156 | PDF | page 847 | Index | strptime()
- C.157 | PDF | page 850 | Index | values()
- C.158 | PDF | page 853 | Index | write_text()
