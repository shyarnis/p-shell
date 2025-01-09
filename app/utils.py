import os


def find_executable(command):
    paths = os.getenv("PATH", "").split(os.pathsep)
    for path in paths:
        executablePath = os.path.join(path, command)
        if os.path.isfile(executablePath):
            return executablePath
    return None


def ensure_directory_exists(filepath):
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)


def parse_redirection(parts):
    stdout_file = None
    stderr_file = None
    append_stdout = False
    append_stderr = False
    command_parts = []

    i = 0
    while i < len(parts):
        if parts[i] in [">", "1>", ">>", "1>>"]:
            stdout_file = parts[i + 1]
            append_stdout = ">>" in parts[i]
            i += 2
        elif parts[i] in ["2>", "2>>"]:
            stderr_file = parts[i + 1]
            append_stderr = ">>" in parts[i]
            i += 2
        else:
            command_parts.append(parts[i])
            i += 1

    return command_parts, stdout_file, stderr_file, append_stdout, append_stderr
