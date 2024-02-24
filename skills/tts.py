import pyttsx3
import wave

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties for the speech output (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Set the output file name
output_file = 'output.wav'

# Convert text to speech
text = "Hello, I am an AI agent"
engine.save_to_file(text, output_file)

# Run the speech synthesis
engine.runAndWait()

# Optional: Get the audio data in the form of a wave file object
with wave.open(output_file, 'rb') as wav_file:
    # You can now manipulate the wave file object as needed
    # For example, you can get information about the audio file:
    frames = wav_file.getnframes()
    channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()
    frame_rate = wav_file.getframerate()
    duration = frames / float(frame_rate)

    print("Audio information:")
    print(f"Number of frames: {frames}")
    print(f"Number of channels: {channels}")
    print(f"Sample width: {sample_width}")
    print(f"Frame rate: {frame_rate}")
    print(f"Duration: {duration} seconds")