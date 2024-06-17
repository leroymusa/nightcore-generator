# Nightcore Generator

A Python tool to automatically generate nightcore audio from an input audio file. It supports downloading audio from YouTube, searching for songs on YouTube, or using a local audio file.

## Features

- Speed up and pitch shift audio files to create nightcore tracks.
- Download audio from YouTube using yt-dlp.
- Search for specific songs on YouTube and create nightcore versions.

## Requirements

- Python 3.x
- `pydub`
- `yt-dlp`
- `ffmpeg` (required by `pydub` and `yt-dlp` for audio processing)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/leroymusa/nightcore-generator
    cd nightcore-generator
    ```

2. Install the required Python packages:
    ```bash
    pip install pydub yt-dlp
    ```

3. Ensure `ffmpeg` is installed on your system.

## Usage

Run the script with one of the following options:

- Download a video from YouTube and create a nightcore version:
    ```bash
    python nightcore_generator.py -y <YouTube URL>
    ```

- Search for a specific song on YouTube and create a nightcore version:
    ```bash
    python nightcore_generator.py -s "<Search Query>"
    ```

- Use a local audio file to create a nightcore version:
    ```bash
    python nightcore_generator.py -f <Path to Audio File>
    ```

- Optionally specify the output file name:
    ```bash
    python nightcore_generator.py -f <Path to Audio File> -o <Output File Name>
    ```

## Examples

- Create a nightcore version from a YouTube video:
    ```bash
    python nightcore_generator.py -y https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```

- Search for a song on YouTube and create a nightcore version:
    ```bash
    python nightcore_generator.py -s "Never Gonna Give You Up"
    ```

- Use a local audio file to create a nightcore version:
    ```bash
    python nightcore_generator.py -f song.mp3
    ```