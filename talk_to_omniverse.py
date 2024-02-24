
## This is a python script to talk to omniverse
import subprocess
import os
from autogenstudio.env import set_env_variables
set_env_variables()
def talk_to_omniverse(text:str):
    """
    Python function to say or speak text to ominiverse

    :param text: str, the text to speak
    Returns:
      str: The text content of the spoken text
    """
    def run_batch_script(batch_script_path, argument, wait=True, capture_output=False):
        try:
            process = subprocess.Popen(
                ["python", batch_script_path, argument, os.environ['AUDIO2FACE_INSTANCE_ID']],  # Pass the argument as a list element
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
        
    run_batch_script(os.environ['TTS_SCRIPT_ABS_PATH'], text, wait=False)
    return f"spoke {text}"

# Example usage of the function:
# talk_to_omniverse("A cute baby sea otter")