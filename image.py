# import streamlit as st
# from st_clickable_images import clickable_images
#
# clicked = clickable_images(
#     [
#         "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
#         "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
#         "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
#         "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
#         # "./text.jpg",
#     ],
#     titles=[f"Image #{str(i)}" for i in range(5)],
#     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
#     img_style={"margin": "5px", "height": "200px"},
# )
#
# st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

import base64
import streamlit as st
from st_clickable_images import clickable_images
from tab2 import page_2
from tab3 import page_3


def images():
    images = []
    for file in ['./text.jpg', './th.jpg', './OIP-C.jpg']:  # 添加照片位置，可以添加多张照片，返回地址
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
        st.download_button(label='Download',
                           data='./test.csv',
                           file_name='test.csv')
