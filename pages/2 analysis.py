import streamlit as st

html_1 = """
<div style="background-color:#0E2954;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้เบื้องต้น</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
df=pd.read_csv('./data/Sleep_predic.csv')
st.write(df.head(10))

dt1 = df['Sleep Duration'].sum()
dt2 = df['Quality of Sleep'].sum()
dt3 = df['Physical Activity Level'].sum()
dt4 = df['Stress Level'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 

html_2 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายคลาสดอกไม้</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")   


ptlen = st.slider("กรุณาเลือกข้อมูล petal.length",0,10)
ptwd = st.slider("กรุณาเลือกข้อมูล petal.width",0,10)

splen = st.number_input("กรุณาเลือกข้อมูล sepal.length")
spwd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
   # ทำนาย

   X = df.drop('Sleep Disorder', axis=1)
   y = df["Sleep Disorder"]  

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)

    #ข้อมูล input สำหรับทดลองจำแนกข้อมูล
   x_input = np.array([[ptlen, ptwd, splen, spwd]])
    # เอา input ไปทดสอบ
   st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)

   if out[0]=="Normal":
      st.header("Normal")
   elif out[0]=="Sleep Apnea":
      st.header("Sleep Apnea")
   else:
      st.header("Insomnia")
   st.button("ไม่ทำนายผล")
else :
    st.button("ไม่ทำนายผล")