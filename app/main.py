import os
import sys
import shlex

from app.commands import handle_pwd, handle_cd, handle_type
from app.echo import handle_echo_command
from app.utils import find_executable, parse_redirection
from app.executor import execute_command_with_redirection
from app.history import load_history, save_history, print_history


def main():
    history = load_history()

    while True:
        try:
            sys.stdout.write("$ ")
            command = input()

            if not command.strip():
                continue

            if command == "exit 0":
                save_history(history)
                sys.exit(0)

            history.append(command)

            if command == "history":
                print_history(history)
                continue

            if command == "pwd":
                handle_pwd()

            elif command.startswith("cd"):
                handle_cd(command.split())

            elif command.startswith("echo"):
                handle_echo_command(command)

            elif command.startswith("type"):
                handle_type(command.split())

            elif command == "clear":
                os.system("clear" if os.name == "posix" else "cls")

            else:
                # Parse command and handle redirection
                parts = shlex.split(command)
                args, stdout_file, stderr_file, append_stdout, append_stderr = (
                    parse_redirection(parts)
                )

                if not args:
                    continue

                executablePath = find_executable(args[0])

                if executablePath:
                    execute_command_with_redirection(
                        args, stdout_file, stderr_file, append_stdout, append_stderr
                    )

                else:
                    print(f"{args[0]}: command not found")

        except EOFError:
            save_history(history)
            print("exit")
            sys.exit(0)


if __name__ == "__main__":
    main()
