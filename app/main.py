import os
import sys
import shlex

from app.commands import handle_pwd, handle_cd, handle_type
from app.echo import handle_echo_command
from app.utils import find_executable, parse_redirection
from app.executor import execute_command_with_redirection


def main():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()

            if command == "exit 0":
                sys.exit(0)

            elif command == "pwd":
                handle_pwd()

            elif command.startswith("cd"):
                handle_cd(command.split())

            elif command.startswith("echo"):
                handle_echo_command(command)

            elif command.startswith("type"):
                handle_type(command.split())

            elif command.startswith("clear"):
                os.system("clear")

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
            print("exit")
            sys.exit(0)


if __name__ == "__main__":
    main()
