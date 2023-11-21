import streamlit as st


col1, col2, col3 = st.columns([1.5, 6, 1])

with col1:
    st.write("") 

with col2:
    st.image("./pic/dataset-cover.jpg")

with col3:
    st.write("")


html_1 = """
<div style="background-color:#0E1117;margin-top:40px;padding:5px;border-radius:5px;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h4 style ="filter: drop-shadow(0px 0px 5px #89c5fb);">ระบบวิเคราะห์สุขภาพการนอนหลับและไลฟ์สไตล์โดยใช้เทคนิคเหมืองข้อมูล</h4><h5  style ="filter: drop-shadow(0px 0px 5px #89c5fb);">The system analyzes health, sleep and lifestyle using data mining techniques</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

html_2 = """
<div style="background-color:#0E1117;padding:15px;">
<center></center><left><h6 style="text-indent: 30px;line-height: 1.5;">สุขภาพการนอนเป็นส่วนสำคัญของสุขภาพทั่วๆ ไป และมีผลมากต่อความเป็นอยู่ของบุคคลในทุกวัย การนอนไม่เพียงแต่เติมพลังให้ร่างกายและสมอง แต่ยังมีผลต่อการทำงานของระบบฮอร์โมน การฟื้นตัวของร่างกาย และส่งเสริมสุขภาพจิตใจด้วย ดังนั้นการนอนไม่เพียงพออาจส่งผลต่อสุขภาพทั้งกายและจิตในระยะยาว นอนน้อยสามารถทำให้ความต้านทานต่ำลง, ปัญหาการคิด และการเรียนรู้มีผลกระทบ, และเสี่ยงต่อโรคต่างๆ เช่น เช่น โรคอ้วน, โรคหัวใจ, วิตกกังวล, หรือโรคจิตเร้าอารมณ์,และภาวะซึมเศร้า ผู้วิจัยได้เห็นถึงความสำคัญของการนอนจึงได้นำข้อมูลการนอนมาวิเคราะห์เพื่อให้ผู้ที่เข้ามาทดสอบได้รู้ถึงปัญหาของตนเอง โดยที่ใช้ 3 เทคนิคในการวิเคราะห์ ได้แก่ เพื่อนบ้านใกล้สุด (K-nearest Neighbors) ต้นไม้ตัดสินใจ (Decision Tree) และ นาอีฟเบย์ (Naive Bayes) โดยผลลัพธ์ที่ได้คือ เทคนิค  ต้นไม้ตัดสินใจ (Decision Tree) ดีที่สุดมีค่าความแม่นยำอยู่ดี  0.89 รองลงมาคือเทคนิคนาอีฟเบย์ (Naive Bayes)มีค่าความแม่นยำอยู่ดี  0.88 และ เทคนิคเพื่อนบ้านใกล้สุด (K-nearest Neighbors)มีค่าความแม่นยำอยู่ดี  0.87 
</h6></left>
<center></center><left><h6 style="text-indent: 30px;line-height: 1.5;">Sleep health is a critical aspect of overall well-being, significantly influencing individuals of all ages. Sleep not only replenishes the body and mind but also plays a crucial role in hormonal regulation, physical recovery, and mental health promotion. Consequently, inadequate sleep can have long-term effects on both physical and mental health. Insufficient sleep may lead to decreased immune function, cognitive problems, learning impairments, and an increased risk of various conditions such as obesity, heart disease, anxiety disorders, or mood disorders like depression.
Recognizing the importance of sleep, researchers have analyzed sleep data to provide individuals with insights into their sleep patterns. Employing three analytical techniques – K-nearest Neighbors, Decision Tree, and Naive Bayes – the results indicate that the Decision Tree technique performs the best, achieving an accuracy of 0.89. Following closely is the Naive Bayes technique with an accuracy of 0.88, and the K-nearest Neighbors technique trails slightly with an accuracy of 0.87.</h6></left>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

html_3 = """
<div style="background-color:#0E1117;border-top: 3px solid #ffffff;">
<center><h4 style="text-indent: 50%;">Wiriya Hemmala 64/44 007</h4></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

st.snow()