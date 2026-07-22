import os
import tempfile
import ffmpeg


def extract_audio(video_file):
    """
    Extract audio from uploaded video and return path to WAV file.
    """

    temp_dir = tempfile.mkdtemp()

    video_path = os.path.join(temp_dir, "video.mp4")
    audio_path = os.path.join(temp_dir, "audio.wav")

    with open(video_path, "wb") as f:
        f.write(video_file.read())

    (
        ffmpeg
        .input(video_path)
        .output(
            audio_path,
            ac=1,
            ar=16000,
            format="wav"
        )
        .overwrite_output()
        .run(quiet=True)
    )

    return audio_path
