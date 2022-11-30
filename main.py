import init_streamlit
import streamlit as st

from tab3 import page_3
from tab1 import page_1
from tab2 import page_2
from tab4 import page_4
from image import images


st.set_page_config(page_icon="🌴", page_title="An online platform for exploring single cell adrenal glands atlas", layout="wide")

st.title("An online platform for exploring single cell adrenal glands atlas")


tab1,tab3, tab4 = st.tabs(["page_1","page_3","pag_4"])
with tab1:
    images()
    page_1()
with tab3:
    page_3()
with tab4:
    page_4()
