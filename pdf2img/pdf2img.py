
import io
import os
import tempfile
import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def pdf_to_jpg(pdf_bytes):
    images = convert_from_bytes(pdf_bytes)

    # Convert all pages of the PDF to JPEG images
    jpg_images = []
    for image in images:
        with io.BytesIO() as output:
            image.save(output, format='JPEG')
            jpg_images.append(output.getvalue())

    return jpg_images


def main():
    st.title("PDF to JPEG converter")

    # Allow user to upload a PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

    if pdf_file:
        # Convert PDF to JPEG images
        jpg_images = pdf_to_jpg(pdf_file.read())

        # Offer JPEG images for download
        for i, jpg_image in enumerate(jpg_images):
            # Create a temporary file in memory
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                tmp_file.write(jpg_image)

            # Offer the temporary file for download as an attachment
            st.download_button(
                label=f"Download Page {i+1}",
                data=jpg_image,
                file_name=f"page_{i+1}.jpg",
                mime='image/jpeg'
            )

if __name__ == "__main__":
    main()
