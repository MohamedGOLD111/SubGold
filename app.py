import streamlit as st

st.set_page_config(
    page_title="SubGold",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 SubGold")
st.write("Welcome to SubGold!")

uploaded_video = st.file_uploader(
    "Upload your video",
    type=["mp4", "mov", "avi", "mkv"]
)

if uploaded_video:
    st.success("✅ Video uploaded successfully!")
    st.video(uploaded_video)
