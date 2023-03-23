
from PyPDF2 import PdfReader
import io
import streamlit as st

# Define a function to extract text from a PDF file
def extract_text_from_pdf(file):
    # Read PDF content
    pdf_reader = PdfReader(io.BytesIO(file.read()))
    num_pages = len(pdf_reader.pages)
    text = ''
    for page in range(num_pages):
        page_obj = pdf_reader.pages[page]
        text += page_obj.extract_text()
    return text

# Define the Streamlit app
def main():
    st.title("PDF Combiner")

    # Prompt user to upload up to 10 PDF files
    st.write("For uploading Real Text PDFs only")
    st.write(" ")
    st.write("For scanned images PDFs, need to convert PDF to Image & Image to text first to be readable PDFs")
    st.write("Upload up to 3 Real texts PDF files to combine:")
    
    files = []
    for i in range(3):
        file = st.file_uploader(f"PDF file {i+1}", type="pdf", key=f"pdf_upload{i}")
        if file:
            files.append(file)

    if not files:
        st.warning("Please upload one or more PDF files to continue.")
    else:
        # Extract text from each PDF file
        texts = [extract_text_from_pdf(file) for file in files]

        # Combine the text into a single string
        combined_text = '\n\n'.join(texts)

        # Display the combined text
        st.write("Combined text:")
        st.write(combined_text)

if __name__ == "__main__":
    main()
