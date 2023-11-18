import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
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
    
    
# Label encode the 'Gender' column
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# One-hot encode categorical columns
for cat_column in df.select_dtypes('object').columns.to_list():
    df = pd.get_dummies(df, columns=[cat_column], prefix=[f'is_{cat_column}'])

# Select features (X) and target variable (y)
X = df.drop("SleepDisorder", axis=1)
y = df[["SleepDisorder"]]

# Decision Tree Classifier
dt_model = DecisionTreeClassifier()
dt_model.fit(X, y)

# Input for prediction
sd = st.number_input("กรุณาเลือกข้อมูล Sleep Duration")
qos = st.slider("กรุณาเลือกข้อมูล Quality of Sleep", 0, 10)
pal = st.number_input("กรุณาเลือกข้อมูล Physical Activity Level")
sl = st.slider("กรุณาเลือกข้อมูล Stress Level", 0, 10)

if st.button("ทำนายผล"):
    # Input data for prediction
    x_input = np.array([[sd, qos, pal, sl]])

    # Prediction
    st.write(dt_model.predict(x_input))
    out = dt_model.predict(x_input)

    if out[0] == "Normal":
        st.image("./pic/iris.jpg")
        st.header("0")
    elif out[0] == "Sleep Apnea":
        st.image("./pic/iris2.jpg")
        st.header("1")
    else:
        st.image("./pic/iris1.jpg")  
        st.header("2")

    st.button("ไม่ทำนายผล")
else:
    st.button("ไม่ทำนายผล")