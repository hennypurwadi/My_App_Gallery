
import base64
import pandas as pd
import streamlit as st
from io import BytesIO

st.title("Excel to CSV Converter")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read Excel file into DataFrame
    df = pd.read_excel(uploaded_file)

    # Preview data
    #st.write("Here's a preview of your data:")
    #st.write(df.head())

    # Convert DataFrame to CSV
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Create download button
    st.download_button(
        label="Download CSV File",
        data=csv_buffer,
        file_name="converted_file.csv",
        mime="text/csv",
    )
