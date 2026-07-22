import streamlit as st
import os

from utils import extract_audio
from transcriber import GroqTranscriber

st.set_page_config(page_title="SubGold", page_icon="🎬")

st.title("🎬 SubGold")
st.write("AI Subtitle Generator")

uploaded_file = st.file_uploader(
    "Upload Video or Audio",
    type=["mp4", "mov", "avi", "mkv", "mp3", "wav", "m4a"]
)

if uploaded_file:

    st.info("Extracting audio...")

    audio_path = extract_audio(uploaded_file)

    st.info("Transcribing...")

    api_key = st.secrets["GROQ_API_KEY"]

    transcriber = GroqTranscriber(api_key)

    result = transcriber.transcribe(audio_path)

    st.success("Done!")

    st.write(result.text)
