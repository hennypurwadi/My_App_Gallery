
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Apps Gallery", page_icon=":guardsman:", layout="wide")
st.title("Apps Gallery")
st.write("Here are some of the apps:")

col1, col2, col3, col4, col5 = st.columns(5)

# URLs of the images in the GitHub repository
img1_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img1.jpg?raw=true"
img2_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img2.jpg?raw=true"
img3_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img3.jpg?raw=true"
img4_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img4.jpg?raw=true"
img5_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img5.jpg?raw=true"

# Display the images and create clickable links
with col1:
    st.markdown(f'[![PDF to Image converter]({img1_url})](https://hennypurwadi-pdf-to-img-converter-pdf2img-gctxe8.streamlit.app/)')
    st.write("PDF to Image converter")
    st.markdown('[Go to App →](https://hennypurwadi-pdf-to-img-converter-pdf2img-gctxe8.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/pdf_to_img_converter)')
    
with col2:
    st.markdown(f'[![Image to Text converter]({img2_url})](https://hennypurwadi-collection-apps-img2text-m5cjli.streamlit.app/)')
    st.write("Image to text converter")
    st.markdown('[Go to App →](https://hennypurwadi-collection-apps-img2text-m5cjli.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/Image_to_Text_Converter)')

with col3:    
    st.markdown(f'[![PDF Summarizer]({img3_url})](https://hennypurwadi-pdf-summary-pdf-summary-xlstst.streamlit.app/)')
    st.write("PDF Summarizer")
    st.markdown('[Go to App →](https://hennypurwadi-pdf-summary-pdf-summary-xlstst.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/pdf_summary)')    
    
with col4:    
    st.markdown(f'[![Question Answering App]({img4_url})](https://hennypurwadi-qna-app-qa-gpt-l0vila.streamlit.app/)')
    st.write("Question Answering App")
    st.markdown('[Go to App →](https://hennypurwadi-qna-app-qa-gpt-l0vila.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/QnA_App)')            

with col5:
    st.markdown(f'[![PDF Combiners]({img5_url})](https://projectgroupinfo-apps-gallery-combine-pdfscombine-pdf-xtq139.streamlit.app/)')
    st.write("PDF combiners")
    st.markdown('[Go to App →](https://projectgroupinfo-apps-gallery-combine-pdfscombine-pdf-xtq139.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/ProjectGroupInfo/apps_gallery/tree/main/combine_pdfs)')
    
# #FOR FUTURE APPS    
    
# col6, col7, col8, col9, col10 = st.columns(5)

# # URLs of the images in the GitHub repository
# img6_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img6.jpg?raw=true"
# img7_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img7.jpg?raw=true"
# img8_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img8.jpg?raw=true"
# img9_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img9.jpg?raw=true"
# img10_url = "https://github.com/hennypurwadi/app_gallery/blob/main/img/img10.jpg?raw=true"

# # Display the images and create clickable links
# with col6:
#     st.write("Speech to text converter")
    
# with col7:
#     st.write("Extract Data from PDF")

# with col8:    
#     st.write("Settlement Predictor App")
    
# with col9:    
#     st.write("Future App")

# with col10:
#     st.write("Other App")
