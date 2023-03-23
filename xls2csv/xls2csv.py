
import pandas as pd
import streamlit as st

# set page title
st.set_page_config(page_title='XLS to CSV Converter', layout='wide')

# add page title and description
st.title('XLS to CSV Converter')
st.write('This app allows you to convert an XLS file to CSV.')

# add file upload widget
xls_file = st.file_uploader('Choose an XLS file', type=['xls', 'xlsx'])

# if file uploaded
if xls_file is not None:
    # read the XLS file
    xls_df = pd.read_excel(xls_file)

    # convert to CSV and get as string
    csv_str = xls_df.to_csv(index=False)

    # create download link
    b64 = base64.b64encode(csv_str.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="converted.csv">Download CSV file</a>'

    # display download link
    st.markdown(href, unsafe_allow_html=True)
