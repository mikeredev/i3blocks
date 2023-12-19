# import required functions/modules
import subprocess


# function to run a shell command
def run_shell_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}, Output: {e.output.strip()}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
