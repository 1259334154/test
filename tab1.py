import streamlit as st
from st_clickable_images import clickable_images
import base64
from tab3 import page_3
def page_1():
    st.write('########')
    st.write('#' * 20)

def image():
    images = []
    for file in ['./text.jpg']:  # 添加照片位置，可以添加多张照片，返回地址
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")

    clicked = clickable_images(
        images,
        titles=[f"Image #{str(i)}" for i in range(len(images))],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )

    if clicked == 0:
        # page_2()
        page_3()
