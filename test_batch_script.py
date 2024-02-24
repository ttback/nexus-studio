import subprocess
import os

def run_batch_script(batch_script_path, argument, wait=True, capture_output=False):
    """Runs a batch script in a subprocess, passes an argument, and handles output writing and capturing.

    Args:
        batch_script_path (str): Path to the batch script.
        argument (str): Argument to pass to the batch script.
        wait (bool, optional): Whether to wait for the subprocess to finish before returning. Defaults to True.
        capture_output (bool, optional): Whether to capture the subprocess's output. Defaults to False.

    Returns:
        str or None: If capture_output is True, returns the captured output. Otherwise, returns None.

    Raises:
        subprocess.CalledProcessError: If the subprocess exits with a non-zero status.
    """

    try:
        # Ensure the output file path exists to avoid errors
        # os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Execute the batch script using subprocess.Popen with appropriate shell arguments
        process = subprocess.Popen(
            [batch_script_path, argument, r"/World/audio2face/PlayerStreaming"],  # Pass the argument as a list element
            stdout=subprocess.PIPE if capture_output else subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,  # Required for proper handling of spaces and special characters in batch commands
            universal_newlines=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

        # Optionally wait for the subprocess to finish
        if wait:
            process.wait()

        # Capture output if requested
        if capture_output:
            output = process.stdout.read()
            return output

    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError(f"Batch script exited with non-zero status: {e.returncode}")

# Example usage:
batch_script_path = r"C:\Users\llmdev\Desktop\autogen-studio\skills\send_wav_a2f.bat"
argument = "hello world"  # Replace with your actual argument

# Run the batch script with argument and capture output
output = run_batch_script(batch_script_path, argument, capture_output=True)
print(output)  # Print the captured output

# Run the batch script with argument without capturing output
run_batch_script(batch_script_path, argument, wait=False)  # Don't wait for the script to finish
