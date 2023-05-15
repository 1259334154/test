import init_streamlit
import streamlit as st
import pandas as pd

from tab3 import page_3
from tab1 import page_1
# from tab2 import page_2
from tab4 import page_4
from image import images


st.set_page_config(page_icon="🌴", page_title="An online platform for exploring single cell adrenal glands atlas", layout="wide")

st.title("An online platform for exploring single cell adrenal glands atlas")

st.markdown("""
    <style>
        .st-cg {
            font-size: 30px;
        }
    </style>
""", unsafe_allow_html=True)
tab1,tab2,tab3 = st.tabs(["introduction","Cluster","Markers"])
with tab1:
#     images()
    page_1()
with tab2:
#     page_3()
    df = pd.read_csv('./cluster.csv', encoding='gbk')
    st.table(df)
with tab3:
    page_4()
