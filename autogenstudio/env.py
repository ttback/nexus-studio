import os
#SET ENVIORNMENT VARIABLES WITH ABS PATH
def set_env_variables():
    os.environ['NVIDIA_API_KEY']=""
    os.environ['OPENAI_API_KEY']=""
    os.environ['TTS_SCRIPT_ABS_PATH']=r"C:\Users\llmdev\Desktop\autogen-studio\skills\streaming_server\tts_audio2face.py"
    os.environ['AUDIO2FACE_INSTANCE_ID']=r"/World/audio2face/PlayerStreaming"
    os.environ['OMNI_LAUNCHER']=r"C:\Users\llmdev\AppData\Local\Programs\omniverse-launcher\NVIDIA Omniverse Launcher.exe"
set_env_variables()