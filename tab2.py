import streamlit as st
import pandas as pd
import numpy as np

def page_2():
    file = st.file_uploader("Choose a CSV file", type=["csv"])#文件上传的
    if file is not None:
        df = pd.read_csv(file,encoding='gbk')
        # st.dataframe(data=df)
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])
    
        st.area_chart(chart_data)

