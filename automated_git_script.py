import subprocess
from pathlib import Path
# import time

# time.sleep(5)

# subprocess.call("cmd.exe")
# def push_to_git():

# commit_message = input("commit message")
# commands = ["git add .", f'git commit -m {commit_message}', "git push"]
# commands = ["git add .", f'git commit -m "Automated commit message"', "git push"]
# subprocess.Popen(commands[0], shell=True)
# for i in range(len(commands)):
#     subprocess.Popen(commands[i], shell=True)

# push_to_git()
# commands = ["cd ..", "git status", "git add ."]
#
# for i in range(len(commands)):
#     subprocess.Popen(commands[i], shell=True)
path = Path.cwd().absolute()
print(path)
commands = [
    ["git", "-C", path, "add", "."],
    ["git", "-C", path, "commit", "-m", "Automated commit message"],
    ["git", "-C", path, "push"]
]

for command in commands:
    subprocess.run(command, check=True)
