import sys
import subprocess
from app.utils import ensure_directory_exists


def execute_command_with_redirection(
    args, stdout_file=None, stderr_file=None, append_stdout=False, append_stderr=False
):
    try:
        if stdout_file:
            ensure_directory_exists(stdout_file)
        if stderr_file:
            ensure_directory_exists(stderr_file)

        stdout_mode = "a" if append_stdout else "w"
        stderr_mode = "a" if append_stderr else "w"

        stdout_handle = open(stdout_file, stdout_mode) if stdout_file else sys.stdout
        stderr_handle = (
            open(stderr_file, stderr_mode) if stderr_file else subprocess.PIPE
        )

        # Run the command with appropriate redirection
        result = subprocess.run(
            args, stdout=stdout_handle, stderr=stderr_handle, text=True
        )

        if stdout_file and stdout_handle != sys.stdout:
            stdout_handle.close()
        if stderr_file and stderr_handle != subprocess.PIPE:
            stderr_handle.close()

        if not stderr_file and result.stderr:
            sys.stderr.write(result.stderr)

        if not stdout_file and result.stdout:
            sys.stdout.write(result.stdout)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
