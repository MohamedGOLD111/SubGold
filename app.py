import streamlit as st

st.set_page_config(page_title="SubGold", page_icon="🎬")

st.title("🎬 SubGold")
st.write("AI Subtitle Generator")

video = st.file_uploader(
    "Upload your video",
    type=["mp4", "mov", "avi", "mkv"]
)

if video:
    st.success("✅ Video uploaded successfully!")
    st.video(video)
