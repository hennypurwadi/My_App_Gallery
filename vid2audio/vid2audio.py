
import streamlit as st
from pytube import YouTube
from io import BytesIO

st.title("YouTube to Audio Converter")

# Get YouTube video URL from user input
video_url = st.text_input("Enter YouTube video URL:")

# Check if the input is a valid YouTube URL
if video_url.startswith("https://www.youtube.com/") or video_url.startswith("https://youtu.be/"):

    try:
        # Load the YouTube video
        youtube_video = YouTube(video_url)
        st.write(f"Video title: {youtube_video.title}")

        # Filter to get only audio streams and select the first one
        streams = youtube_video.streams.filter(only_audio=True)
        stream = streams.first()

        # Download the audio stream to memory
        audio_data = BytesIO()
        stream.stream_to_buffer(audio_data)
        audio_data.seek(0)

        # Create a download button for the audio file
        st.download_button(
            label="Download Audio",
            data=audio_data,
            file_name=f"{youtube_video.title}.mp4",
            mime="audio/mp4",
        )
    except Exception as e:
        st.error(f"Error: {e}")
else:
    if video_url:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
