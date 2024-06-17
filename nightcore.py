#Author: Leroy Musa
#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
import logging
from pydub import AudioSegment
import yt_dlp as youtube_dl

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pid = os.getpid()
tmp_dir = f"tmp_{pid}"

def speedup_song(input_path, output_path):
    """
    Function to speed up the song by increasing the sample rate.
    
    Args:
        input_path (str): Path to the input audio file.
        output_path (str): Path to the output audio file.
    
    Returns:
        None
    """
    # Log the information about the task
    logging.info("Speeding up the song.")
    
    try:
        # Load the audio file
        sound = AudioSegment.from_file(input_path)
        
        # Calculate the number of octaves to increase the speed
        # Here we are increasing the speed by 25% (x1.25)
        octaves = 4 / 12 
        
        # Calculate the new sample rate
        # The new sample rate is calculated by multiplying the original sample rate
        # with the exponential value of octaves
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
        
        # Create a new audio segment with the increased sample rate
        # The `overrides` parameter is used to override the frame rate of the audio segment
        nightcore_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        
        # Set the frame rate of the audio segment to 44100
        # This is the standard sample rate for CD quality audio
        nightcore_sound = nightcore_sound.set_frame_rate(44100)
        
        # Export the audio segment to the output file in MP3 format
        # The bitrate is set to 192k
        nightcore_sound.export(output_path, format="mp3", bitrate="192k")
    except Exception as e:
        # If there is an error, log the error and exit the program
        logging.error(f"Error speeding up the song: {e}")
        sys.exit(1)

def download_audio_from_youtube(search_terms, output_path):
    """
    Function to download audio from YouTube using yt-dlp.
    
    Args:
        search_terms (str): The search terms to use for downloading the audio.
        output_path (str): The path to save the downloaded audio file.
    
    Returns:
        None
    """
    # Log the information about the task
    logging.info("Downloading audio from YouTube.")
    
    # Set up the options for yt-dlp
    ydl_opts = {
        # Specify the format of the audio to be downloaded
        'format': 'bestaudio/best',
        # Specify the post-processing options for the downloaded audio
        'postprocessors': [{
            # Use FFmpeg to extract the audio from the downloaded file
            'key': 'FFmpegExtractAudio',
            # Specify the preferred codec for the extracted audio
            'preferredcodec': 'mp3',
            # Specify the preferred quality for the extracted audio
            'preferredquality': '192',
        }],
        # Specify the template for the output file name
        'outtmpl': output_path
    }
    
    try:
        # Use yt-dlp to download the audio from YouTube
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_terms])
    except Exception as e:
        # If there is an error, log the error and exit the program
        logging.error(f"Error downloading from YouTube: {e}")
        sys.exit(1)

def main(args):
    """
    Function to run the main program logic

    Args:
        args (argparse.Namespace): The arguments parsed by argparse

    Returns:
        None
    """
    if os.path.isdir(tmp_dir):
        # If the temporary directory already exists, remove it
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    # Create the temporary directory
    
    audio_path = ''
    if args.ytdl:
        # If the user wants to download from YouTube using yt-dlp, do the following:
        download_audio_from_youtube(args.ytdl, f"{tmp_dir}/youtubedl.%(ext)s")
        # Download the audio file from YouTube using yt-dlp and save it in the temporary directory
        audio_path = f"{tmp_dir}/youtubedl.mp3"
        # Set the audio path to the location of the downloaded audio file

    elif args.search:
        # If the user wants to search for a specific song on YouTube to Nightcore-ify, do the following:
        download_audio_from_youtube(f'ytsearch:{args.search}', f"{tmp_dir}/youtubedl.%(ext)s")
        # Search for the specified song on YouTube using yt-dlp and save the first result in the temporary directory
        audio_path = f"{tmp_dir}/youtubedl.mp3"
        # Set the audio path to the location of the downloaded audio file

    elif args.file:
        # If the user wants to use an existing audio file, set the audio path to that file
        audio_path = args.file

    # Set the output file path to the specified output file name, or generate a default name
    output = args.output if args.output else f"nightcore_{pid}.mp3"
    
    # Speed up the audio file
    speedup_song(audio_path, output)

    # Remove the temporary directory
    shutil.rmtree(tmp_dir)
    logging.info("Nightcore audio successfully generated!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A tool to automatically generate nightcore audio from an audio file.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-y", "--ytdl", help="Use yt-dlp to download a video from YouTube")
    group.add_argument("-s", "--search", help="Search for a specific song on YouTube to Nightcore-ify (same as --ytdl ytsearch:[search])")
    group.add_argument("-f", "--file", help="File path to the song to Nightcore-ify")
    parser.add_argument("-o", "--output", help="Name of the output file")
    main(parser.parse_args())