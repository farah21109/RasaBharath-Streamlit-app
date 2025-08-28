import streamlit as st
import os

# App title
st.markdown(
    "<h1 style='text-align: center; color: white;'>✨ తెలంగాణ ప్రసిద్ధ వంటకాలు ✨</h1>",
    unsafe_allow_html=True
)

# Add gradient background
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Folder where images are stored
img_folder = "images"

# Get all images in the folder
images = [img for img in os.listdir(img_folder) if img.endswith(("png", "jpg", "jpeg"))]

# Show recipes in grid
cols = st.columns(3)
for i, img in enumerate(images):
    with cols[i % 3]:
        st.image(os.path.join(img_folder, img), caption=img.split(".")[0], width=250, use_container_width=False)
