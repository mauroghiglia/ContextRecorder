# ContextRecorder

ContextRecorder is an open-source Python application designed to capture audio from any available source on a computer, including microphones and system audio (loopback devices).

The project started as the recording component of a larger context-aware assistant system and is being developed as a standalone tool that can later serve as the foundation for transcription, meeting analysis, AI assistants, and real-time monitoring solutions.

## Features

### Current Features

* Audio device discovery
* Microphone recording
* Windows loopback (system audio) recording
* WAV file generation
* Keyboard-controlled recording
* Timestamped output files
* Modular architecture

### Planned Features

* Device selection from command line
* Simultaneous recording from multiple devices
* Multi-track recording
* MP3 and FLAC export
* Real-time audio monitoring
* Voice activity detection (VAD)
* Live transcription
* Speaker identification
* Plugin architecture

## Project Structure

```text
ContextRecorder/
│
├── src/
│   ├── main.py
│   ├── recorder.py
│   ├── commands.py
│   ├── devices.py
│   └── interpreter.py
│
├── recordings/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

* Python 3.10+
* Windows 10/11

### Python Packages

```bash
pip install sounddevice
pip install soundcard
pip install soundfile
pip install keyboard
pip install numpy
```

Or:

```bash
pip install -r requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-user>/ContextRecorder.git
cd ContextRecorder
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the application:

```bash
python src/main.py
```

Default keyboard commands:

| Key | Action                  |
| --- | ----------------------- |
| s   | Start recording         |
| x   | Stop recording and save |
| q   | Quit application        |

Recorded audio files are stored in the `recordings` directory.

## Design Goals

ContextRecorder is designed to be:

* Simple
* Lightweight
* Extensible
* Open source
* Independent of any cloud service

The project aims to provide a reliable audio capture layer that can later be integrated with speech recognition, AI assistants, monitoring systems, and meeting analysis tools.

## Contributing

Contributions, bug reports, feature requests, and pull requests are welcome.

## License

MIT License
