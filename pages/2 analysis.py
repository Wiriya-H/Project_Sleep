import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')
st.table(df.head())

df1 = df['Sleep Duration'].sum()
df2 = df['Quality of Sleep'].sum()
df3 = df['Physical Activity Level'].sum()
df4 = df['Stress Level'].sum()
dx = [df1, df2, df3, df4]
dx2 = pd.DataFrame(dx, index=["Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level"])

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("Not show bar chart")
else :
    st.button("Not show bar chart") 
    
    
sd = st.number_input("กรุณาเลือกข้อมูล Sleep Duration",0,10)
qos = st.slider("กรุณาเลือกข้อมูล Quality of Sleep",0,10)

pal = st.number_input("กรุณาเลือกข้อมูล Physical Activity Level")
sl = st.slider("กรุณาเลือกข้อมูล Stress Level"0,10)

