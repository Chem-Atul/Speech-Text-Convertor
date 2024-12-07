import os
import json
import sounddevice as sd
import vosk
import numpy as np

# Define model path (make sure the model files are downloaded and extracted)
model_path = r"C:\Users\ASUS\Documents\EEPL Python\path_to_vosk_model"

# Load the model
if not os.path.exists(model_path):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model_path' in the current folder.")
    exit(1)

model = vosk.Model(model_path)

# Function to record audio and transcribe it
def transcribe_audio():
    # Sample rate should match the sample rate of the model
    sample_rate = 16000

    # Open a stream with sounddevice
    with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening... (Press Ctrl+C to stop)")
        rec = vosk.KaldiRecognizer(model, sample_rate)

        while True:
            data, overflowed = stream.read(4000)
            # Convert data to numpy array
            np_data = np.frombuffer(data, dtype=np.int16)
            # Convert numpy array to bytes
            if rec.AcceptWaveform(np_data.tobytes()):
                result = rec.Result()
                print(json.loads(result)["text"])
            else:
                print(json.loads(rec.PartialResult())["partial"])

if __name__ == "__main__":
    try:
        transcribe_audio()
    except KeyboardInterrupt:
        print("\nTranscription stopped.")
