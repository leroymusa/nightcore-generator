# Nightcore Generator

A Python tool to automatically generate nightcore audio from an input audio file. It supports downloading audio from YouTube, searching for songs on YouTube, or using a local audio file.

## Features

- Speed up and pitch shift audio files to create nightcore tracks.
- Download audio from YouTube using `yt-dlp`.
- Search for specific songs on YouTube and create nightcore versions.

## Requirements

- Python 3.x
- `pydub`
- `yt-dlp`
- `ffmpeg` (required by `pydub` and `yt-dlp` for audio processing)

## Installation

### Ubuntu Linux

1. Clone the repository:
    ```bash
    git clone https://github.com/leroymusa/nightcore-generator
    cd nightcore-generator
    ```

2. Install Python 3.8 (if not already installed):
    ```bash
    sudo apt update
    sudo apt install python3.8 python3.8-venv python3.8-dev
    ```

3. Create and activate a virtual environment:
    ```bash
    python3.8 -m venv venv
    source venv/bin/activate
    ```

4. Install the required Python packages:
    ```bash
    pip install pydub yt-dlp
    ```

5. Ensure `ffmpeg` is installed on your system:
    ```bash
    sudo apt install ffmpeg
    ```

### Other Operating Systems

1. Clone the repository:
    ```bash
    git clone https://github.com/leroymusa/nightcore-generator
    cd nightcore-generator
    ```

2. Install Python 3.8 (ensure Python 3.8 or higher is installed). Refer to the official Python website for installation instructions: https://www.python.org/downloads/

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required Python packages:
    ```bash
    pip install pydub yt-dlp
    ```

5. Ensure `ffmpeg` is installed on your system:
    - **Windows**: Download from https://ffmpeg.org/download.html and follow the installation instructions.
    - **macOS**: Install using Homebrew:
        ```bash
        brew install ffmpeg
        ```

## Usage

Run the script with one of the following options:

- Download a video from YouTube and create a nightcore version:
    ```bash
    python nightcore.py -y <YouTube URL>
    ```

- Search for a specific song on YouTube and create a nightcore version:
    ```bash
    python nightcore.py -s "<Search Query>"
    ```

- Use a local audio file to create a nightcore version:
    ```bash
    python nightcore.py -f <Path to Audio File>
    ```

- Optionally specify the output file name:
    ```bash
    python nightcore.py -f <Path to Audio File> -o <Output File Name>
    ```

## Examples

- Create a nightcore version from a YouTube video:
    ```bash
    python nightcore.py -y https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```

- Search for a song on YouTube and create a nightcore version:
    ```bash
    python nightcore.py -s "Never Gonna Give You Up"
    ```

- Use a local audio file to create a nightcore version:
    ```bash
    python nightcore.py -f song.mp3
    ```

## Note

Ensure that the virtual environment is activated each time you work with the project:
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`