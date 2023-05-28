import subprocess
import time

# time.sleep(5)

# subprocess.call("cmd.exe")
# def push_to_git():

# commit_message = input("commit message")
# commands = ["git add .", f'git commit -m {commit_message}', "git push"]
commands = ["git add .", f'git commit -m "Automated commit message"', "git push"]
for i in range(len(commands)):
    subprocess.run(commands[i], shell=True)

    # push_to_git()
