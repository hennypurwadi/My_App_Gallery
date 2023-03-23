
import os
import pandas as pd
import streamlit as st
import openpyxl
from io import BytesIO

# Title of the app
st.title("Excel to CSV Converter")

# Upload the file
uploaded_file = st.file_uploader("Choose an Excel file (.xlsx)", type="xlsx")

# Check if the file is uploaded
if uploaded_file is not None:
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)

        # Preview of the data
        st.write("Here's a preview of your data:")
        st.write(df.head())

        # Convert the DataFrame to CSV and make it downloadable
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Create a download link
        b64 = base64.b64encode(csv_buffer.read()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="converted_file.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
