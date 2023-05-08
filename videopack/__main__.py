import os
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor
from moviepy.editor import *


def unpack(video_path, output_folder, output_audio_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load video
    video = VideoFileClip(video_path)
    fps = video.iter_frames() / video.duration
    print(f"FPS: {fps}")

    # Extract and save audio
    print("Extracting audio...")
    audio = video.audio
    audio.write_audiofile(output_audio_path)
    print("Audio extracted.")

    # Extract and save frames
    print("Extracting frames...")

    def save_frame(i, frame):
        frame_path = os.path.join(output_folder, f"frame_{i:04d}.png")
        ImageClip(frame).save_frame(frame_path)

    with ThreadPoolExecutor() as executor:
        list(executor.map(save_frame, range(len(list(video.iter_frames()))), video.iter_frames()))

    print("Frames extracted.")


def pack(input_folder, input_audio_path, output_video_path, fps):
    # Get frame file paths and sort them
    frame_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]
    frame_files.sort()

    # Load frames as clips
    frame_duration = 1/fps
    frame_clips = [ImageClip(os.path.join(input_folder, f)).set_duration(frame_duration) for f in frame_files]

    # Concatenate frames and set duration for each frame
    video = concatenate_videoclips(frame_clips, method="compose")
    video = video.set_duration(len(frame_clips) / fps)

    # Load audio
    audio = AudioFileClip(input_audio_path)

    # Combine video and audio
    final_video = video.set_audio(audio)

    # Write final video to file
    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac", fps=fps)


def main():
    parser = argparse.ArgumentParser(description="Video packer/unpacker CLI.")
    subparsers = parser.add_subparsers(dest="command")

    unpack_parser = subparsers.add_parser("unpack", help="Unpack a video into frames and audio.")
    unpack_parser.add_argument("input", help="Input video file path.")
    unpack_parser.add_argument("--output", default="frames", help="Output folder for frames.")
    unpack_parser.add_argument("--audio_output", default="audio.mp3", help="Output path for audio.")

    pack_parser = subparsers.add_parser("pack", help="Pack frames and audio into a video.")
    pack_parser.add_argument("input", help="Input folder containing frames.")
    pack_parser.add_argument("--fps", type=int, default=60, help="Frames per second.")
    pack_parser.add_argument("--output", default="output.mp4", help="Output video file path.")
    pack_parser.add_argument("--audio_input", default="audio.mp3", help="Input path for audio.")

    args = parser.parse_args()

    if args.command == "unpack":
        unpack(args.input, args.output, args.audio_output)
    elif args.command == "pack":
        pack(args.input, args.audio_input, args.output, args.fps)
    else:
        print("Invalid command. Use 'videopack --help' for more information.")


if __name__ == "__main__":
    main()