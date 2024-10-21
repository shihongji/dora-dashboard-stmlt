from datetime import datetime
import streamlit as st
import time
import os
import time
from pad_content import get_content
from feed_content import get_dummy_data
from styles import get_feed_styles, get_pad_styles
import cv2
# video_file = open("/Users/hongji/code/dora/video/tianjin/ot.mp4", "rb")
# video_bytes = video_file.read()
# Load the video file using OpenCV
video_path = "/Users/hongji/code/dora/video/tianjin/ot.mp4"
cap = cv2.VideoCapture(video_path)

# Get total number of frames and frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Initialize Streamlit video element
video_file = open(video_path, "rb")
video_bytes = video_file.read()


st.set_page_config(layout="wide")
st.title("篮球AI教练 - 数据智能分析师")
# Apply custom CSS for columns and up-container directly using class selectors

upContainer = st.container(border=True, height=500)
with upContainer:
    col1, col2 = st.columns([1, 1])
    with col2:
        st.video(video_bytes)
        timestamp_display = st.empty()
        # video_list = tuple(os.listdir('/Users/hongji/code/dora/video/tianjin'))
        # video_list = [video for video in video_list if video.endswith('.mp4')]
        # option = st.selectbox(
        #     "Video",
        #     video_list,
        #     index=None,
        #     placeholder="请选择比赛视频",
        #     label_visibility="hidden",
        # )
        # if isinstance(option, str) and option.endswith(".mp4"):
        #     st.video(f"/Users/hongji/code/dora/video/tianjin/{option}", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)
    with col1:
        col1.subheader("Pad")
        pad_screen = st.empty()
        # End of up-container

# Custom CSS to fix the container height and make it scrollable
st.markdown(
    """
    <style>
    .fixed-height-container {
        height: 300px;  /* Set your desired fixed height */
        overflow-y: auto;  /* Enable vertical scrolling if content overflows */
        border: 1px solid #ddd;  /* Optional: add a border for visibility */
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
below = st.container(border=True, height=300)
with below:
    # Create a placeholder for waterfall display
    placeholder = st.empty()

# Use st.empty() to create a placeholder for the block

title, body_text, reason_text = get_content()
title_style, body_style = get_pad_styles()
# Create some custom CSS to center the block
st.markdown(
    """
    <style>
    .pad-text-area {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 30vh;  /* Adjust this as needed for the block size */
        text-align: center;
    }
    .custom-title {
        """ + title_style + """
    }
    .custom-body {
        """ + body_style + """
    }
    .custom-reason {
        """ + body_style + """
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Place your text block inside a div with the "centered-block" class
with pad_screen.container():
    st.markdown(f'''
                <div class="pad-text-area">
                    <div>
                        <div class="custom-title">{title}</div>
                        <div class="custom-body">{body_text}</div>      
                        <div class="custom-reason">{reason_text}</div>
                    </div>
                ''', unsafe_allow_html=True)

# Get content from content.py
feed_data = get_dummy_data()

# Get styles from styles.py
category_style, time_style, text_style = get_feed_styles()

# Function to display text in waterfall format

def display_waterfall(feed_data):
    displayed_entries = []

    for entry in feed_data:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if entry["time"] <= current_time:
            # Add new entry to the top
            displayed_entries.insert(0, entry)

            # Display the entries (newest on top)
            with placeholder.container():
                for e in displayed_entries:
                    st.markdown(
                        f'<div style="{category_style}">{e["category"]}</div>'
                        f'<div style="{time_style}">第{e["time"].split()[1]} ； {e["time"]}</div>'
                        f'<div style="{text_style}">{e["text"]}</div><hr>',
                        unsafe_allow_html=True
                    )

        time.sleep(1)

def display_waterfall_dummy(feed_data):
    displayed_entries = []

    for entry in feed_data:
        # Add new entry to the top
        displayed_entries.insert(0, entry)

        # Display the entries (newest on top)
        with placeholder.container():
            for e in displayed_entries:
                st.markdown(
                    f'<span style="{category_style}">{e["category"]}  </span>'
                    f'<span style="{time_style}">第{e["time"].split()[1]} ； {e["time"]} </span>'
                    f'<span style="{text_style}">{e["text"]}</span><hr>',
                    unsafe_allow_html=True
                )

        time.sleep(2)

# Call the function to start displaying entries
display_waterfall_dummy(feed_data)
# Start displaying the waterfall content in a separate thread-like function
st.session_state['waterfall_running'] = True  # Use this to avoid double execution in Streamlit reruns
if 'waterfall_started' not in st.session_state:
    st.session_state['waterfall_started'] = False

if not st.session_state['waterfall_started']:
    st.session_state['waterfall_started'] = True
    display_waterfall_dummy(feed_data)


# Track and display the video timestamp
def track_video_timestamp(cap, fps):
    current_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # No more frames

        # Calculate the current time in seconds
        current_time = current_frame / fps
        current_frame += 1

        # Display the current timestamp
        timestamp_display.text(f"Current Timestamp: {current_time:.2f} seconds")

        # Simulate real-time playback speed
        time.sleep(1 / fps)

# Run the video timestamp tracking
track_video_timestamp(cap, fps)
# Release the video capture object
cap.release()
st.write("Video playback completed!")