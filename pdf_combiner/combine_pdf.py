
from PyPDF2 import PdfReader, PdfWriter
import io
import streamlit as st

# extract text from a PDF
def extract_text_from_pdf(file):
    # Read PDF content
    pdf_reader = PdfReader(io.BytesIO(file.read()))
    num_pages = len(pdf_reader.pages)
    text = ''
    for page in range(num_pages):
        page_obj = pdf_reader.pages[page]
        text += page_obj.extract_text()
    return text

# Define Streamlit app
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

        # Create new PDF file with the combined text
        pdf_writer = PdfWriter()
        pdf_writer.add_page(PdfReader(io.BytesIO(combined_text.encode())).getPage(0))
        pdf_bytes = io.BytesIO()
        pdf_writer.write(pdf_bytes)

        # Display the combined PDF file
        st.write("Combined PDF:")
        st.write(pdf_bytes, unsafe_allow_html=True)

        # Download button
        st.download_button(
            label="Download combined PDF",
            data=pdf_bytes.getvalue(),
            file_name="combined.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    main()
