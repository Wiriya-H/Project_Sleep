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



html_1 = """
<div style="background-color:#0E1117;padding:5px;border-radius:5px;border-bottom: 5px solid #ffffff;border-top: 5px solid #ffffff;">
<center><h4>ระบบวิเคราะห์สุขภาพการนอนหลับและไลฟ์สไตล์โดยใช้เทคนิคเหมืองข้อมูล</h4><h5>The system analyzes health, sleep and lifestyle using data mining techniques</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

html_0 = """
<div style="border-top: 5px solid #ffffff;">
<center><image('./pic/1.jpg')></center>
</div>
"""
st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")


html_2 = """
<div style="background-color:#0E1117;">
<center><h4>บทคัดย่อ</h4></center><left><h6 style="text-indent: 30px;">การนอนมีความสำคัญมากสำหรับสุขภาพและความรู้สึกที่ดีของมนุษย์ โดยมีความสำคัญในหลายๆด้าน ดังนี้
    สุขภาพร่างกาย : การนอนหลับเพียงพอช่วยให้ร่างกายฟื้นตัวและซ่อมแซมเนื้อเยื่อ ทำให้ร่างกายสามารถดำเนินกิจกรรมประจำวันได้ดีขึ้น.
การนอนหลับเพียงพอช่วยรักษาน้ำหนักและสุขภาพในระดับที่เหมาะสม ลดความเสี่ยงของโรคอ้วนและโรคเบาหวาน.
</h6></left>
<center><h4>Abstract</h4></center><left><h5 style="text-indent: 30px;">Hello Monday</h5></left>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")







































col1, col2 = st.columns(2)
with col1:
    st.image('./pic/1.jpg')
    lot3="https://lottie.host/347e3388-72e3-4b11-9fe8-49b2349c4a7a/GekjLnvyXb.json"
    lottie3 = load_lottieurl(lot3)
    st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()
