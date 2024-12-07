# Speech-Text-Convertor

## Overview
The Speech-to-Text Converter is a Python-based application designed to convert spoken language into text using advanced speech recognition techniques. This project leverages the Vosk library, along with other Python libraries such as numpy, sounddevice, and os.

## Features
Real-time speech recognition.
Lightweight and easy to set up.
Uses the Vosk API for accurate transcription.
Portable across various systems supporting Python.

## Requirements
  Python 3.7 or later
  Required libraries:
    vosk
    sounddevice
    numpy
    
## Code Overview
Here’s a high-level overview of the main components:

vosk: Handles the speech recognition model.
sounddevice: Captures audio from the microphone.
numpy: Processes audio data.
os: Manages file and path-related operations.

## Troubleshooting
Error: "Model not found"
Ensure the downloaded Vosk model is correctly unpacked into the model_path directory in the current folder.

Microphone not detected
Verify that your microphone is connected and accessible by the system. Check its permissions if necessary.

## Contributing
Contributions are welcome! If you have suggestions for improvements or find a bug, feel free to open an issue or submit a pull request.
