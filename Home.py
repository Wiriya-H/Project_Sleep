import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("Natthinan Khemthong DATA SCIENCE NPRU")


col1, col2 = st.columns(2)
with col1:
    st.image('./pic/2.jpg')
    lot3="https://lottie.host/347e3388-72e3-4b11-9fe8-49b2349c4a7a/GekjLnvyXb.json"
    lottie3 = load_lottieurl(lot3)
    st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()
