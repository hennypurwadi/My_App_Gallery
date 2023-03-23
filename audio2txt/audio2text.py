
import tempfile
import pytube
import streamlit as st
from streamlit import caching

caching.clear_cache()

st.set_page_config(
    page_title="YouTube Video to Audio",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("YouTube Video to Audio")
st.sidebar.title("Settings")

@st.cache(suppress_st_warning=True, show_spinner=False)
def download_audio(video_url):
    data = pytube.YouTube(video_url)
    audio = data.streams.get_audio_only()
    audio_filename = f"{data.title}_audio_only.mp4"
    audio.download(filename=audio_filename)
    return audio_filename

def main():
    video_url = st.sidebar.text_input("Enter YouTube video URL:")

    if video_url:
        try:
            st.sidebar.write("Downloading audio, please wait...")
            audio_filename = download_audio(video_url)
            st.sidebar.write("Audio download complete!")

            with open(audio_filename, "rb") as f:
                st.download_button("Download Audio", data=f, file_name=audio_filename, mime="video/mp4")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
