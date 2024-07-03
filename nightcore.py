# Author: Leroy Musa
#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
import logging
from pydub import AudioSegment
import yt_dlp as youtube_dl
import signal

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pid = os.getpid()
tmp_dir = f"tmp_{pid}"

def cleanup_temp_dir():
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)

def speedup_song(input_path, output_path):
    logging.info("Speeding up the song.")
    try:
        sound = AudioSegment.from_file(input_path)
        octaves = 4 / 12
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
        nightcore_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        nightcore_sound = nightcore_sound.set_frame_rate(44100)
        nightcore_sound.export(output_path, format="mp3", bitrate="192k")
    except Exception as e:
        logging.error(f"Error speeding up the song: {e}")
        cleanup_temp_dir()
        sys.exit(1)

def download_audio_from_youtube(search_terms, output_path):
    logging.info("Downloading audio from YouTube.")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_terms])
    except Exception as e:
        logging.error(f"Error downloading from YouTube: {e}")
        cleanup_temp_dir()
        sys.exit(1)

def signal_handler(sig, frame):
    logging.info("Interrupt received, cleaning up...")
    cleanup_temp_dir()
    sys.exit(0)

def main(args):
    signal.signal(signal.SIGINT, signal_handler)
    
    if os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    
    audio_path = ''
    if args.ytdl:
        download_audio_from_youtube(args.ytdl, f"{tmp_dir}/youtubedl.%(ext)s")
        audio_path = f"{tmp_dir}/youtubedl.mp3"
    elif args.search:
        download_audio_from_youtube(f'ytsearch:{args.search}', f"{tmp_dir}/youtubedl.%(ext)s")
        audio_path = f"{tmp_dir}/youtubedl.mp3"
    elif args.file:
        audio_path = args.file

    output_dir = args.output_dir if args.output_dir else '.'
    output_filename = args.output if args.output else f"nightcore_{pid}.mp3"
    output_path = os.path.join(output_dir, output_filename)

    speedup_song(audio_path, output_path)
    cleanup_temp_dir()
    logging.info(f"Nightcore audio successfully generated at {output_path}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A tool to automatically generate nightcore audio from an audio file.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-y", "--ytdl", help="Use yt-dlp to download a video from YouTube")
    group.add_argument("-s", "--search", help="Search for a specific song on YouTube to Nightcore-ify (same as --ytdl ytsearch:[search])")
    group.add_argument("-f", "--file", help="File path to the song to Nightcore-ify")
    parser.add_argument("-o", "--output", help="Name of the output file")
    parser.add_argument("-d", "--output_dir", help="Directory to save the output file")
    main(parser.parse_args())