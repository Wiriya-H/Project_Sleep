import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('./data/Sleep_predic.csv')
dt = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')



html_0 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Example data table</h3></center>
</div>
"""
st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")
st.write(dt.head(10))


dt1 = df['Sleep Duration'].sum()
dt2 = df['Quality of Sleep'].sum()
dt3 = df['Physical Activity Level'].sum()
dt4 = df['Stress Level'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level"])

show_chart = st.checkbox("Show bar chart")

if show_chart:
    fig, ax = plt.subplots()
    bars = ax.bar(dx2.index, dx2[0], color='#FF4B4B')  # Set the color to #FF4B4B

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
   
    plt.xticks(fontsize=8)
    st.pyplot(fig)


html_1 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Class Prediction</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


s1 = st.number_input("ระยะเวลาการนอนหลับ (ชั่วโมง)")
s2 = st.slider("คุณภาพการนอนหลับ (มาตราส่วน: 1-10)",0,10)
s3 = st.number_input("ระดับการออกกําลังกาย (นาที / วัน)")
s4 = st.slider("ระดับความเครียด (มาตราส่วน: 1-10)",0,10)

if st.button("ทำนายผล"):

   X = df.drop('Sleep Disorder', axis=1)
   y = df["Sleep Disorder"]  

   tree_model = DecisionTreeClassifier()
   tree_model.fit(X, y)


   x_input = np.array([[s1, s2, s3, s4]])

   out = tree_model.predict(x_input)

   if out[0]=="Normal":
      st.header("Normal")
      st.subheader("AI: ผลการทำนายคือปกติ")
   elif out[0]=="Sleep Apnea":
      html_4 = """
      <div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
      <center><h3 style="border-bottom: 3px solid #ffffff;">Sleep Apnea</h3></center>
      <left><h6 style="text-indent: 30px;line-height: 1.5;">สร้างรูปแบบการนอน: พยายามนอนและตื่นในเวลาเดียวกันทุกวัน, รวมทั้งในวันหยุด, เพื่อช่วยสร้างระบบนอนที่มีความเสถียร.
      ลดการบริโภคสารกระตุ้น: ลดหรือหลีกเลี่ยงการบริโภคสารกระตุ้นต่อประสาท เช่นคาเฟอีนและนิโคตีนในช่วงหลังเที่ยงคืน.
      สร้างสภาพแวดล้อมที่เหมาะสมสำหรับการนอน: มีที่นอนที่สะดวกสบาย, ควบคุมแสง, และอุณหภูมิห้องให้เหมาะสม.
      ออกกำลังกายอย่างสม่ำเสมอ: การออกกำลังกายสามารถช่วยลดความเครียดและเพิ่มคุณภาพการนอน.
      ลดการใช้อุปกรณ์อิเล็กทรอนิกส์ก่อนนอน: หลีกเลี่ยงการใช้สมาร์ทโฟน, แท็บเล็ต, หรือคอมพิวเตอร์ที่มีหน้าจอสองชั่วโมงก่อนนอน.
      หลีกเลี่ยงการทานอาหารหนักในช่วงเย็น: ลดการทานอาหารหนักและเครื่องดื่มที่มีคาเฟอีนหรือแอลกอฮอล์ในช่วงเย็น.
      ใช้เตียงเพื่อการนอน: หลีกเลี่ยงใช้เตียงเพื่อทำงานหรือดูทีวี เพื่อให้ร่างกายเข้าใจว่าที่นอนคือสถานที่สำหรับการนอน.
      พักผ่อนก่อนนอน: ให้ตัวเองเวลาสักพักผ่อนก่อนการนอน เช่น การอ่านหนังสือ, การฟังเพลงผ่อนคลาย, หรือการทำโยคะ.
      หากปัญหาการนอนไม่หลับยังคงต่อเนื่องหลังจากลองมีการปรับปรุงดังกล่าว, คุณควรพบแพทย์หรือผู้เชี่ยวชาญด้านการนอนเพื่อการปรึกษาและการวินิจฉัยที่ถูกต้อง</h6></left>
      </div>
      """
      st.markdown(html_4, unsafe_allow_html=True)
      st.markdown("")

      
   elif out[0]=="Insomnia":
      st.header("Insomnia")
      
      
      st.subheader("การที่คุณไม่สามารถหลับหลับหรือมีปัญหาการนอนเป็นสถานะที่พบได้บ่อยและสามารถเกิดขึ้นจากหลายสาเหตุ. นอนไม่หลับหรือมีปัญหาการนอนมีชื่อทางการแพทย์ว่า นอนไม่หลับ หรือ Insomnia นอนไม่หลับอาจจะเกิดจากปัจจัยที่เป็นปัจจัยทางจิตและทางร่างกาย. นี่คือบางแนวทางที่อาจช่วยให้คุณนอนหลับมีคุณภาพมากขึ้น:")
      st.subheader("1.สร้างรูปแบบการนอน: พยายามนอนและตื่นในเวลาเดียวกันทุกวัน, รวมทั้งในวันหยุด, เพื่อช่วยสร้างระบบนอนที่มีความเสถียร.")   
      st.button("ไม่ทำนายผล")


