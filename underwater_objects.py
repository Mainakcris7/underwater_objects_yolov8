import streamlit as st
import os
import shutil
from ultralytics import YOLO
from PIL import Image
import moviepy.editor as mpe

st.write("## Underwater object detection 🦈🐟🐧🪼")
selected_type = st.radio("Choose file type", options=["Image", "Video"])
file = st.file_uploader("Choose a file")

if selected_type == "Image":
    if file:
        img = Image.open(file)
        st.image(img, width=500)
        with open("saved_img.jpg", "wb") as f:
            f.write(file.getvalue())
else:
    if file:
        st.video("saved_video.mp4")
        with open("saved_video.mp4", "wb") as f:
            f.write(file.getvalue())


@st.cache_resource
def load_model():
    model = YOLO("best.pt")
    return model


def get_prediction(file_path):
    try:
        shutil.rmtree("runs")   # Clean-up before new prediction
    except:
        pass
    st.write("### Detected objects ")
    # Using command to get the prediction
    os.system(f"yolo predict model='best.pt' source='{file_path}' conf=0.3")


if st.button("Detect"):
    model = load_model()
    with st.spinner("Detecting"):
        if selected_type == 'Image':
            get_prediction("saved_img.jpg")
            st.image("runs/detect/predict/saved_img.jpg")
        else:
            get_prediction("saved_video.mp4")
            clip = mpe.VideoFileClip("runs/detect/predict/saved_video.avi")
            clip.write_videofile("runs/detect/predict/saved_video.mp4")
            st.video("runs/detect/predict/saved_video.mp4")
