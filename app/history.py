import os

HISTORY_FILE = os.path.expanduser("~/.shell_history")


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "w+") as file:
        return [line.strip() for line in file.readlines()]


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        file.writelines(f"{command}\n" for command in history)


def print_history(history):
    for index, command in enumerate(history, start=1):
        print(f"{index} {command}")
