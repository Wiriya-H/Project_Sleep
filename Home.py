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


col1, col2, col3 = st.columns([1.5, 6, 1])

with col1:
    st.write("") 

with col2:
    st.image("./pic/dataset-cover.jpg")

with col3:
    st.write("")


html_1 = """
<div style="background-color:#0E1117;margin-top:40px;padding:5px;border-radius:5px;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h4>ระบบวิเคราะห์สุขภาพการนอนหลับและไลฟ์สไตล์โดยใช้เทคนิคเหมืองข้อมูล</h4><h5>The system analyzes health, sleep and lifestyle using data mining techniques</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

html_2 = """
<div style="background-color:#0E1117;">
<center><h4>บทคัดย่อ</h4></center><left><h6 style="text-indent: 30px;line-height: 1.5;">สุขภาพการนอนเป็นส่วนสำคัญของสุขภาพทั่วๆ ไป และมีผลมากต่อความเป็นอยู่ของบุคคลในทุกวัย การนอนไม่เพียงแต่เติมพลังให้ร่างกายและสมอง แต่ยังมีผลต่อการทำงานของระบบฮอร์โมน การฟื้นตัวของร่างกาย และส่งเสริมสุขภาพจิตใจด้วย ผู้วิจัยได้เห็นถึงความสำคัญของการนอนจึงได้นำข้อมูลการนอนมาวิเคราะห์เพื่อให้ผู้ที่เข้ามาทดสอบได้รู้ถึงปัญหาของตนเอง โดยที่ใช้ 3 เทคนิคในการวิเคราะห์ ได้แก่ เพื่อนบ้านใกล้สุด (K-nearest Neighbors) ต้นไม้ตัดสินใจ (Decision Tree) และ นาอีฟเบย์ (Naive Bayes) โดยผลลัพธ์ที่ได้คือ เทคนิค  ต้นไม้ตัดสินใจ (Decision Tree) ดีที่สุดมีค่าความแม่นยำอยู่ดี  0.89 รองลงมาคือเทคนิคนาอีฟเบย์ (Naive Bayes)มีค่าความแม่นยำอยู่ดี  0.88 และ เทคนิคเพื่อนบ้านใกล้สุด (K-nearest Neighbors)มีค่าความแม่นยำอยู่ดี  0.87 
</h6></left>
<center><h4>Abstract</h4></center><left><h5 style="text-indent: 30px;line-height: 1.5;">Sleep health is crucial for overall well-being, significantly impacting individuals of all ages. Sleep not only rejuvenates the body and mind but also plays a vital role in hormonal regulation, bodily restoration, and mental health promotion. Recognizing the importance of sleep, researchers have analyzed sleep data to provide individuals with insights into their sleep patterns. This analysis employs three techniques: K-nearest Neighbors, Decision Tree, and Naive Bayes.
The results reveal that the Decision Tree technique outperforms the others, achieving an accuracy of 0.89. Following closely is the Naive Bayes technique with an accuracy of 0.88, and the K-nearest Neighbors technique trails slightly with an accuracy of 0.87.</h5></left>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

html_3 = """
<div style="background-color:#0E1117;border-top: 3px solid #ffffff;">
<center><h4 style="text-indent: 60%;">Wiriya Hemmala 64/44 007</h4></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")






































st.balloons()
