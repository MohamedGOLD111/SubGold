import os
from groq import Groq


class GroqTranscriber:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def transcribe(self, audio_path):
        with open(audio_path, "rb") as audio_file:
            response = self.client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3-turbo",
                response_format="verbose_json",
                language="en",
                temperature=0
            )

        return response
