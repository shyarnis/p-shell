import sys
import shlex
from app.utils import ensure_directory_exists


def handle_echo_command(command):
    parts = shlex.split(command)
    message = " ".join(parts[1:])

    # Handle redirection
    stdout_file = None
    stderr_file = None
    append_stdout = False
    append_stderr = False

    # Extract redirection operators and message
    message_parts = []
    i = 1
    while i < len(parts):
        if parts[i] in [">", "1>", "2>", ">>", "1>>", "2>>"]:
            is_append = ">>" in parts[i]
            if parts[i].startswith("2"):
                stderr_file = parts[i + 1]
                append_stderr = is_append
            else:
                stdout_file = parts[i + 1]
                append_stdout = is_append
            i += 2
        else:
            message_parts.append(parts[i])
            i += 1
    message = " ".join(message_parts)

    try:
        if stderr_file:
            ensure_directory_exists(stderr_file)

            with open(stderr_file, "a" if append_stderr else "w") as f:
                pass

            # Echo always prints to stdout
            print(message)

        elif stdout_file:
            ensure_directory_exists(stdout_file)
            with open(stdout_file, "a" if append_stdout else "w") as f:
                f.write(message + "\n")

        else:
            print(message)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
