"""Script takes a .mp4 file and extracts the audio and converts it to a .wav file."""

import ffmpeg
import sys

def extract_audio_from_mp4(input_file, output_file):
    """Extracts audio from .mp4 file and saves it as .wav file."""
    try:
        ffmpeg.input(input_file).output(output_file, ar="16000", ac=1, acodec="pcm_s16le", f="wav").run()
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_audio_from_mp4(input_file, output_file)
