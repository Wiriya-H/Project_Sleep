import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('./data/Sleep_predic.csv')
dt = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')



html_0 = """
<div style="background-color:#ffffff;border-bottom: 3px solid #0E1117;border-top: 3px solid #0E1117;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")
st.write(dt.head(10))

html_1 = """
<div style="background-color:#ffffff;border-bottom: 3px solid #0E1117;border-top: 3px solid #0E1117;margin-top:20px;">
<center><h3>Class Prediction</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

s1 = st.selectbox("เพศ (1 คือ ชาย | 0 คือ หญิง)",[0,1])
s2 = st.selectbox("ช่วงอายุ (1 คือ 20-27 | 2 คือ 28-35 | 3 คือ 36-43 | 4 คือ 44-51 | 5 คือ 52-59)",[1,2,3,4,5])
s3 = st.number_input("ระยะเวลาการนอนหลับ (ชั่วโมง)")
s4 = st.selectbox("คุณภาพการนอนหลับ (มาตราส่วน: 1-10)",[1,2,3,4,5,6,7,8,9,10])
s5 = st.number_input("ระดับการออกกําลังกาย (นาที/วัน)")
s6 = st.selectbox("ระดับความเครียด (มาตราส่วน: 1-10)",[1,2,3,4,5,6,7,8,9,10])
s7 = st.selectbox("หมวด BMI (1 คิอ Normal 2 คือ Overweight 3 คือ Obese)",[1,2,3])
s8 = st.number_input("ความดันโลหิตซิสโตลิก (Systolic Blood Pressure)")
s9 = st.number_input("ความดันโลหิตช่วงล่าง (Diastolic Blood Pressure)")
s10 = st.number_input("อัตราการเต้นของหัวใจ (Heart Rate)")
s11 = st.number_input("จํานวนก้าวรายวัน (Steps per day)")

if st.button("ทำนายผล"):

   X = df.drop('Sleep Disorder', axis=1)
   y = df["Sleep Disorder"]  

   tree_model = DecisionTreeClassifier(criterion='entropy')
   tree_model.fit(X, y)


   x_input = np.array([[s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]])

   out = tree_model.predict(x_input)

   if out[0]=="Normal":
      col1, col2, col3 = st.columns([1.5, 6, 1])
          
      with col1:
         st.write("") 

      with col2:
         st.image("./pic/nm.png")

      with col3:
         st.write("")
          
          
      html_4 = """
      <div style="background-color:#ffffff;padding:20px;border: 3px solid #0E1117;">
      <center><h3 style="border-bottom: 3px solid #0E1117;">นอนหลับปกติ (Normal)</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">สุขภาพการนอนเป็นส่วนสำคัญของสุขภาพทั่วๆ ไป และมีผลมากต่อความเป็นอยู่ของบุคคลในทุกวัย การนอนไม่เพียงแต่เติมพลังให้ร่างกายและสมอง แต่ยังมีผลต่อการทำงานของระบบฮอร์โมน การฟื้นตัวของร่างกาย และการนอนที่ดีเป็นสิ่งสำคัญที่มีผลดีต่อสุขภาพทั้งร่างกายและจิตใจ นี่คือบางแนวทางที่ช่วยให้คุณมีการนอนที่ดี</h6></left>
      <ul>
         <li>ตั้งเวลานอนและตื่น: พยายามที่จะนอนและตื่นขึ้นในเวลาเดียวกันทุกวัน, แม้วันหยุด การทำเช่นนี้ช่วยปรับลำดับการนอนของร่างกาย.</li>
         <li>สร้างสภาพแวดล้อมที่เหมาะสม: ให้ห้องนอนมีแสงสว่างที่น้อยลงในช่วงเวลาที่เตรียมตัวนอน และให้ห้องมีอุณหภูมิและความชื้นที่สบาย.</li>
         <li>หลีกเลี่ยงสิ่งกระตุ้น: หลีกเลี่ยงการดื่มกาแฟหรือเครื่องดื่มที่มีคาเฟอีนหลังบ่าย, และหลีกเลี่ยงการใช้สมาร์ทโฟนหรืออุปกรณ์อิเล็กทรอนิกส์ที่มีแสงสว่างสีฟ้าในช่วงเวลาที่ใกล้เข้าสู่การนอน.</li>
         <li>ทำกิจกรรมผ่อนคลายก่อนนอน: ทำกิจกรรมที่ช่วยผ่อนคลายเช่น อ่านหนังสือ, ฟังเพลงสบาย ๆ, หรือการทำโยคะ.</li>
         <li>ปฏิบัติการนอนที่สบาย: ใช้ที่นอนที่มีความสูงพอดี และใช้หมอนที่รองรับคอ.</li>
         <li>หลีกเลี่ยงการนอนกลางวัน: หากเป็นไปได้, หลีกเลี่ยงการนอนในช่วงเวลากลางวันหรือที่มีแสงแวดล้อม.</li>
         <li>การออกกำลังกาย: การออกกำลังกายสม่ำเสมอมีผลในการปรับปรุงคุณภาพการนอน แต่ควรหลีกเลี่ยงการออกกำลังกายในช่วงเวลาเย็นหรือก่อนนอน.</li>
         <li>รักษาน้ำหนัก: การรักษาน้ำหนักที่เหมาะสมสามารถช่วยลดโอกาสการเกิดปัญหาทางการนอน.</li>
         <li>หลีกเลี่ยงการรับประทานอาหารหนักในช่วงเย็น: การรับประทานอาหารหนักในช่วงเย็นอาจทำให้มีการย่อยอาหารที่ยากลำบากและมีผลต่อการนอน.</li>
         <li>หลีกเลี่ยงสารระงับการนอน: การลดหรือหยุดดื่มแอลกอฮอล์หรือสารที่ทำให้ร่างกายเครียด.</li>
      </ul>
      </div>
      """
      st.markdown(html_4, unsafe_allow_html=True)
      st.markdown("")

   elif out[0]=="Sleep Apnea":
      col1, col2, col3 = st.columns([1.5, 6, 1])
          
      with col1:
         st.write("") 

      with col2:
         st.image("./pic/sa.jpeg")

      with col3:
         st.write("")
          
          
      html_4 = """
      <div style="background-color:#ffffff;padding:20px;border: 3px solid #0E1117;">
      <center><h3 style="border-bottom: 3px solid #0E1117;">การหยุดหายใจขณะหลับ (Sleep Apnea)</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การหยุดหายใจขณะหลับอาจเกิดจากสาเหตุหลายประการ ซึ่งบางครั้งอาจเป็นเรื่องที่ร้ายแรงและต้องได้รับการตรวจวินิจฉัยและรักษาโดยทันที นอกจากนี้ก็มีสาเหตุที่ไม่ร้ายแรงหรือเป็นเรื่องที่เกิดขึ้นได้บ้าง ต่อไปนี้คือบางสาเหตุที่อาจทำให้เกิดการหยุดหายใจขณะหลับ นี่คือบางแนวทางที่อาจช่วยให้คุณนอนหลับมีคุณภาพมากขึ้น</h6></left>
      <ul>
         <li>การปรับเปลี่ยนท่านอน: การนอนที่ทำให้หัวและคออยู่ในตำแหน่งที่ดีสำหรับการหายใจ เช่น ท่านอนที่หลังหรือการใช้หมอนที่รองรับคอสามารถช่วยลดการอุดตันในท่อลมประสาท.</li>
         <li>การลดน้ำหนัก: หากการหยุดหายใจขณะหลับเกิดจากปัญหาน้ำหนักเกิน การลดน้ำหนักอาจช่วยลดความรุนแรงของอาการนี้.</li>
         <li>การเปลี่ยนพฤติกรรมการนอน: การลดหรือหลีกเลี่ยงสิ่งที่ทำให้การหยุดหายใจแย่ลง เช่น การลดหรือหยุดดื่มแอลกอฮอล์, การหลีกเลี่ยงยานอนหลับที่อาจทำให้การหยุดหายใจแย่ลง.</li>
         <li>การใช้เครื่องช่วยการหายใจ: สำหรับผู้ที่มี Sleep Apnea, การใช้ Continuous Positive Airway Pressure (CPAP) เป็นวิธีที่พบมีประสิทธิภาพมาก โดยเครื่อง CPAP จะส่งอากาศบริสุทธิ์เข้าสู่ท่อลมประสาทเพื่อป้องกันการอุดตัน.</li>
         <li>การทำกิจกรรมกลางวัน: การออกกำลังกายที่สม่ำเสมออาจช่วยในการลดอาการหยุดหายใจขณะหลับ.</li>
         <li>การรักษาโรคร่วมที่อาจเป็นสาเหตุ: การรักษาโรคอื่น ๆ ที่อาจมีผลกระทบต่อการหยุดหายใจขณะหลับ เช่น โรคเบาหวานหรือโรคหัวใจ.</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">คำแนะนำเหล่านี้เป็นเพียงแนวทางทั่วไป ควรปรึกษาแพทย์เพื่อการวินิจฉัยที่แม่นยำและรับคำแนะนำเพิ่มเติมเพื่อการรักษาที่เหมาะสมต่อสถานะสุขภาพของแต่ละบุคคล</h6></left>
      </div>
      """
      st.markdown(html_4, unsafe_allow_html=True)
      st.markdown("")

      
   elif out[0]=="Insomnia":
      col1, col2, col3 = st.columns([1.5, 6, 1])
          
      with col1:
         st.write("") 

      with col2:
         st.image("./pic/ln.jpg")

      with col3:
         st.write("")
          
          
      html_5 = """
      <div style="background-color:#ffffff;padding:20px;border: 3px solid #0E1117;">
      <center><h3 style="border-bottom: 3px solid #0E1117;">นอนไม่หลับ (Insomnia)</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">การที่คุณไม่สามารถหลับหลับหรือมีปัญหาการนอนเป็นสถานะที่พบได้บ่อยและสามารถเกิดขึ้นจากหลายสาเหตุ. นอนไม่หลับหรือมีปัญหาการนอนมีชื่อทางการแพทย์ว่า "นอนไม่หลับ" หรือ"Insomnia." นอนไม่หลับอาจจะเกิดจากปัจจัยที่เป็นปัจจัยทางจิตและทางร่างกาย. นี่คือบางแนวทางที่อาจช่วยให้คุณนอนหลับมีคุณภาพมากขึ้น</h6></left>
      <ul>
         <li>พยายามนอนและตื่นในเวลาเดียวกันทุกวัน, รวมทั้งในวันหยุด, เพื่อช่วยสร้างระบบนอนที่มีความเสถียร.</li>
         <li>ลดการบริโภคสารกระตุ้น: ลดหรือหลีกเลี่ยงการบริโภคสารกระตุ้นต่อประสาท เช่นคาเฟอีนและนิโคตีนในช่วงหลังเที่ยงคืน.</li>
         <li>สร้างสภาพแวดล้อมที่เหมาะสมสำหรับการนอน: มีที่นอนที่สะดวกสบาย, ควบคุมแสง, และอุณหภูมิห้องให้เหมาะสม.</li>
         <li>ออกกำลังกายอย่างสม่ำเสมอ: การออกกำลังกายสามารถช่วยลดความเครียดและเพิ่มคุณภาพการนอน.</li>
         <li>ลดการใช้อุปกรณ์อิเล็กทรอนิกส์ก่อนนอน: หลีกเลี่ยงการใช้สมาร์ทโฟน, แท็บเล็ต, หรือคอมพิวเตอร์ที่มีหน้าจอสองชั่วโมงก่อนนอน.</li>
         <li>หลีกเลี่ยงการทานอาหารหนักในช่วงเย็น: ลดการทานอาหารหนักและเครื่องดื่มที่มีคาเฟอีนหรือแอลกอฮอล์ในช่วงเย็น.</li>
         <li>ใช้เตียงเพื่อการนอน: หลีกเลี่ยงใช้เตียงเพื่อทำงานหรือดูทีวี เพื่อให้ร่างกายเข้าใจว่าที่นอนคือสถานที่สำหรับการนอน.</li>
         <li>พักผ่อนก่อนนอน: ให้ตัวเองเวลาสักพักผ่อนก่อนการนอน เช่น การอ่านหนังสือ, การฟังเพลงผ่อนคลาย, หรือการทำโยคะ.</li>
      </ul>
      <left><h6 style="text-indent: 30px;line-height: 1.5;padding-top:15px;">หากปัญหาการนอนไม่หลับยังคงต่อเนื่องหลังจากลองมีการปรับปรุงดังกล่าว, คุณควรพบแพทย์หรือผู้เชี่ยวชาญด้านการนอนเพื่อการปรึกษาและการวินิจฉัยที่ถูกต้อง</h6></left>
      </div>
      """
      st.markdown(html_5, unsafe_allow_html=True)
      st.markdown("")


