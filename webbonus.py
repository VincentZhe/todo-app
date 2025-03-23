import streamlit as st
from PIL import Image

st.title('Color to Grayscale Converter')

uploaded_image = st.file_uploader("UploadImage")

with st.expander("Start the camera"):
    #Start the camera
    camera_img = st.camera_input("Camera")

if camera_img:
    #create a pillow image instance
    img = Image.open(camera_img)


    #convert the pillow image to grayscale
    gray_img = img.convert('L')


    #Render the grayscale image on the webpage
    st.image(gray_img)


if uploaded_image:
    # create a pillow image instance
    img = Image.open(uploaded_image)

    # convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Render the grayscale image on the webpage
    st.image(gray_img)