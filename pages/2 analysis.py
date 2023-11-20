import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd


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

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 

html_1 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Class Prediction</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


ptlen = st.number_input("ระยะเวลาการนอนหลับ (ชั่วโมง)")
ptwd = st.slider("คุณภาพการนอนหลับ (มาตราส่วน: 1-10)",0,10)
splen = st.number_input("ระดับการออกกําลังกาย (นาที / วัน)")
spwd = st.slider("ระดับความเครียด (มาตราส่วน: 1-10)",0,10)



col1, col2, col3 = st.columns([4, 6, 1])

with col1:
    st.write("") 

with col2:
    if st.button("ทำนายผล"):
    
      X = df.drop('Sleep Disorder', axis=1)
      y = df["Sleep Disorder"]  

      tree_model = DecisionTreeClassifier()
      tree_model.fit(X, y)


      x_input = np.array([[ptlen, ptwd, splen, spwd]])

      out = tree_model.predict(x_input)

      if out[0]=="Normal":
         st.header("Normal")
         st.write("AI: ผลการทำนายคือปกติ")
      elif out[0]=="Sleep Apnea":
         st.header("Sleep Apnea")
         st.write("AI: ผลการทำนายคือ Sleep Apnea")
      else:
         st.header("Insomnia")
         st.write("AI: ผลการทำนายคือ Insomnia")
      st.button("ไม่ทำนายผล")

with col3:
    st.write("")







