
import streamlit as st
import pandas as pd
from io import BytesIO
import os

# Set page configuration
st.set_page_config(page_title="Excel to CSV Converter", page_icon=":pencil:")

# Create title
st.title("Excel to CSV Converter")

# Create file uploader
uploaded_file = st.file_uploader("Upload an Excel file (.xlsx)", type=["xlsx", "xls"])

# If file is uploaded
if uploaded_file is not None:
    # Read in Excel file
    try:
        df = pd.read_excel(uploaded_file)
    except:
        # Display error message if file cannot be read
        st.error("Failed to read file. Please make sure it is a valid Excel file.")
        st.stop()

    # Convert to CSV
    csv = df.to_csv(index=False).encode()

    # Create download link
    with BytesIO() as b:
        b.write(csv)
        href = f'<a href="data:file/csv;base64,{b.getvalue().decode()}" download="converted.csv">Download CSV File</a>'

    # Display success message and download link
    st.success("File conversion successful!")
    st.markdown(href, unsafe_allow_html=True)
