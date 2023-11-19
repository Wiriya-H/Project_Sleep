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

html_3 = """
<div style="background-color:#0E1117;">
<center><h4 style="text-indent: 100%;">Wiriya Hemmala</h4></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")






































st.balloons()
