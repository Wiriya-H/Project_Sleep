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


html_2 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center>
<button onclick="predictOutcome()">ทำนายผล</button>

<div id="result"></div>
<button onclick="noPrediction()">ไม่ทำนายผล</button>

<script>
function predictOutcome() {
   // Assuming you have already defined the values of ptlen, ptwd, splen, and spwd
   var ptlen = /* populate ptlen */;
   var ptwd = /* populate ptwd */;
   var splen = /* populate splen */;
   var spwd = /* populate spwd */;

   // Assuming you have already loaded the DecisionTreeClassifier and df data
   var X = /* Populate your X data */;
   var y = /* Populate your y data */;

   var tree_model = new DecisionTreeClassifier();
   tree_model.fit(X, y);

   var x_input = [[ptlen, ptwd, splen, spwd]];
   var out = tree_model.predict(x_input);

   var resultDiv = document.getElementById("result");

   if (out[0] == "Normal") {
      resultDiv.innerHTML = "<h1>Normal</h1><p>AI: ผลการทำนายคือปกติ</p>";
   } else if (out[0] == "Sleep Apnea") {
      resultDiv.innerHTML = "<h1>Sleep Apnea</h1><p>AI: ผลการทำนายคือ Sleep Apnea</p>";
   } else {
      resultDiv.innerHTML = "<h1>Insomnia</h1><p>AI: ผลการทำนายคือ Insomnia</p>";
   }
}

function noPrediction() {
   // Implement the behavior when "ไม่ทำนายผล" button is clicked
}
</script>

</center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")
