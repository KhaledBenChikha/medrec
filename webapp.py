import streamlit as st
import cv2
from PIL import Image

import numpy as np
import easyocr
import pandas as pd

def recognize_with_easyocr(image):
    
    reader = easyocr.Reader(['en']) 
    result = reader.readtext(image,detail=0)
    return result



def main():
    
   
    st.title("Pfe")

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Image Recognition WebApp</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.image(our_image)

    if st.button("Recognise with easyocr"):
        text= recognize_with_easyocr(our_image)
        st.text(text)
    



if __name__ == '__main__':
    main()
