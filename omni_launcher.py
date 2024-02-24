import subprocess
import os

def launch_omniverse():
    """Launches the NVIDIA Omniverse Launcher using the path specified in the OMNI_LAUNCHER environment variable.
    """

    launcher_path = os.environ.get('OMNI_LAUNCHER')
    if not launcher_path:
        return "OMNI_LAUNCHER environment variable is not set."

    try:
        subprocess.run([launcher_path], check=True)
    except subprocess.CalledProcessError as e:
        return  f"Failed to launch Omniverse Launcher: {e}"