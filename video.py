from base64 import b64encode
from pathlib import Path
import streamlit as st
from streamlit_player import st_player, _SUPPORTED_EVENTS

st.title("Display Current Playback Time in Real-Time")

# Set player options
options = {
    "events": ["onPlay", "onProgress", "onError", "onPause"],
    "progress_interval": 500,  # Update every 500 milliseconds
    "volume": .2,
    "playing": False,
    "loop": True,
    "controls": True,
    "muted": False,
    "light": False,
}
def local_video(path, mime="video/mp4"):
    data = b64encode(Path(path).read_bytes()).decode()
    return [{"type": mime, "src": f"data:{mime};base64,{data}"}]

# Input the media URL
# url = "https://youtu.be/c9k8K1eII4g"
# url = "http://127.0.0.1:5000/rand.mp4"
url="https://youtu.be/qUNOPOJJKC8"

# Create a placeholder for the timestamp
time_placeholder = st.empty()

# Embed the player and get events
event = st_player(url, **options, key="asdasmedia_player")

# Display the event data
st.write(event)

# Extract and display the current playback time
# if event and event[0] == "onProgress":
#     current_time = event[1]["playedSeconds"]
#     time_placeholder.write(f"Current playback time: {current_time:.2f} seconds")
if event.name:
    st.write(f"Event: {event.name}, Data: {event.data}")