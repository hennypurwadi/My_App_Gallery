
import streamlit as st
import pandas as pd

def convert_to_csv(file):
    # read the Excel file
    df = pd.read_excel(file)

    # convert the Excel file to CSV
    csv_file = df.to_csv(index=False)

    return csv_file

# set page title
st.set_page_config(page_title="Excel to CSV Converter")

# set page heading
st.title("Excel to CSV Converter")

# add file uploader
file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if file is not None:
    # convert the file to CSV
    csv_file = convert_to_csv(file)

    # add download link for the CSV file
    st.download_button(
        label="Download CSV",
        data=csv_file,
        file_name="converted_file.csv",
        mime="text/csv"
    )
else:
    st.warning("Please upload an Excel file.")
