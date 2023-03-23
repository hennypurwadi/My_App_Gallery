
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel to CSV Converter", page_icon=":pencil:")

st.title("Excel to CSV Converter")

# Create file uploader
uploaded_file = st.file_uploader("Upload an Excel file (.xlsx or .xls)", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read in Excel file
    try:
        df = pd.read_excel(uploaded_file)
    except:
        st.error("Failed to read file. Please make sure it is a valid Excel file.")
        st.stop()

    # Convert to CSV
    csv = df.to_csv(index=False)

    # Create download link
    href = f'<a href="data:file/csv;base64,{b64encode(csv.encode()).decode()}" download="converted.csv">Download CSV File</a>'

    # Display download link
    st.markdown(href, unsafe_allow_html=True)
