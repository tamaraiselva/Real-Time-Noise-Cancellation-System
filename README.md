# Real-Time Noise Cancellation System

## Objective
The goal of this project is to develop a real-time noise cancellation system that processes audio in two distinct scenarios: single speaker and multiple speakers.

1. **Single Speaker Scenario:**
The system isolates and enhances the audio of one primary speaker while suppressing background noise and other voices.

2. **Multiple Speaker Scenario:**
The system preserves multiple speaker voices and simultaneously filters out environmental noise (e.g., white noise, workplace background noise, or vehicle noise).

## **Requirements**

Python 3.7+

Dependencies:
- numpy
- pyaudio

## Project Structure
```
noise-cancellation-system
├── src
│   ├── main.py                # Entry point for the application
│   ├── audio_processor.py      # Handles audio input/output and filtering
│   ├── filters
│   │   ├── __init__.py        # Initializes the filters package
│   │   ├── single_speaker.py   # Isolates and enhances primary speaker audio
│   │   └── multi_speaker.py    # Preserves multiple speaker voices
│   └── utils
│       ├── __init__.py        # Initializes the utils package
│       └── audio_utils.py      # Utility functions for audio processing
├── tests
│   ├── __init__.py            # Initializes the tests package
│   └── test_audio_processor.py  # Unit tests for the AudioProcessor class
├── output                      # Directory for processed audio files
├── requirements.txt            # Lists project dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions
1. Clone the repository:

```bash
https://github.com/tamaraiselva/Real-Time-Noise-Cancellation-System.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## **Usage**

1. **Run the Application**

To run the noise cancellation system, execute the following command:

```bash
python src/main.py
```

2. **Select the Scenario**

When prompted, select either:

- `single` for Single Speaker Mode
- `multi` for Multi-Speaker Mode

3. **Process Audio**

The application will start processing audio from your microphone in real time. Processed audio will play back through your speakers or headphones.

4. **Stop the Application**

Press `Ctrl+C` to stop processing. The processed audio will be saved to a `.wav` file in the output/ directory.

**Example Output:**

- `output/processed_single_audio.wav` (Single Speaker Scenario)
- `output/processed_multi_audio.wav`(Multi-Speaker Scenario)

## Features

- **Real-time processing:** The system should process audio streams in real-time, with a latency of less than `100 milliseconds` for each `200 ms` audio chunk.  

- **Input and Output:** The system will take live audio input from a microphone and output a clean, noise-reduced audio stream.  

- **File Output:** The processed (cleaned) audio will be saved as a `.wav` file.

## License
This project is licensed under the MIT License.
