
# Real-Time Noise Cancellation System

## Objective
The goal of this project is to develop a real-time noise cancellation system that processes audio in two distinct scenarios: single speaker and multiple speakers.

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

2. Navigate to the project directory:
   
```bash
cd noise-cancellation-system
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
To run the noise cancellation system, execute the following command:

```bash
python src/main.py
```

## Features

- **Real-time processing:** The system should process audio streams in real-time, with a latency of less than `100 milliseconds` for each `200 ms` audio chunk.  

- **Input and Output:** The system will take live audio input from a microphone and output a clean, noise-reduced audio stream.  

- **File Output:** The processed (cleaned) audio will be saved as a `.wav` file.

## License
This project is licensed under the MIT License.
