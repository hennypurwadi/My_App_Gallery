
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

    # Create download link
    b64 = base64.b64encode(csv_buffer.read()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="converted_file.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
