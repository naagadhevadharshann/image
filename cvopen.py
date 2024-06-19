import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title of the app
st.title("Image Processing App")

# Provide options to the user
option = st.radio("Choose an option", ("Upload from Gallery", "Take a Picture"))

# Placeholder for image
image = None

# Function to convert image to grayscale
def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
4
# Function to flip the image
def flip_image(img):
    return cv2.flip(img, 1)

# Upload or capture image based on user selection
if option == "Upload from Gallery":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        image = np.array(Image.open(uploaded_file))
elif option == "Take a Picture":
    picture = st.camera_input("Take a picture")
    if picture is not None:
        # Convert the file to an opencv image.
        image = np.array(Image.open(picture))

# If an image is available, display options for image processing
if image is not None:
    st.image(image, caption='Original Image', use_column_width=True)
    st.write("")

    # Choose operation
    operation = st.selectbox("Choose an operation", ["Convert to Grayscale", "Flip Image"])

    # Perform operation
    processed_image = None
    if operation == "Convert to Grayscale":
        processed_image = convert_to_grayscale(image)
    elif operation == "Flip Image":
        processed_image = flip_image(image)

    # Display processed image
    if processed_image is not None:
        st.image(processed_image, caption='Processed Image', use_column_width=True)
