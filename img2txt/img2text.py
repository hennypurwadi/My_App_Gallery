
import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Config
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def convert_image_to_text(image):
    img = np.array(image.convert('RGB'))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    text = pytesseract.image_to_string(img, lang='eng')
    return text

# layout
st.title("Image to Text Converter")
st.write("Upload an image (.jpg or .png) to extract the text.")

uploaded_image = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")

    if st.button("Convert to Text"):
        st.write("Converting...")
        extracted_text = convert_image_to_text(image)
        st.write("Extracted Text:")
        st.write(extracted_text)
