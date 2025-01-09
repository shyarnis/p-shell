import os
from app.utils import find_executable


def handle_pwd():
    print(os.getcwd())


def handle_cd(args):
    if len(args) > 1:
        paths = args[1].strip()
    else:
        paths = os.path.expanduser("~")

    if paths.startswith("~"):
        paths = os.path.expanduser(paths)

    try:
        os.chdir(paths)
    except Exception:
        print(f"cd: {paths}: No such file or directory")


def handle_type(command_parts):
    builtin_command = command_parts[1]

    if builtin_command in ("echo", "exit", "type", "pwd", "cd"):
        print(f"{builtin_command} is a shell builtin")

    else:
        executable_path = find_executable(builtin_command)
        if executable_path:
            print(f"{builtin_command} is {executable_path}")
        else:
            print(f"{builtin_command}: not found")
