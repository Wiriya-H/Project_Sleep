import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

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
    
    
sd = st.number_input("กรุณาเลือกข้อมูล Sleep Duration")
qos = st.slider("กรุณาเลือกข้อมูล Quality of Sleep",0,10)
pal = st.number_input("กรุณาเลือกข้อมูล Physical Activity Level")
sl = st.slider("กรุณาเลือกข้อมูล Stress Level",0,10)

if st.button("ทำนายผล"):
    le = LabelEncoder()
    x = df.drop("Sleep Disorder", axis=1)
    x['Gender'] = le.fit_transform(x['Gender'])

    for cat_columns in x.select_dtypes('object').columns.to_list():
        one_hot_encoded = pd.get_dummies(x[cat_columns], prefix=f'is_{cat_columns}')
        x = pd.concat([x, one_hot_encoded], axis=1)
        x = x.drop(cat_columns, axis=1)

    # Create a DataFrame for prediction with the same structure as the training data
    x_input = pd.DataFrame([[sd, qos, pal]])  # Adjust one-hot-encoded columns

    y = df["Sleep Disorder"]

    Knn_model = KNeighborsClassifier(n_neighbors=3)
    Knn_model.fit(X, y)

    #ข้อมูล input สำหรับทดลองจำแนกข้อมูล
   x_input = np.array([[sd, qos, pal, sl]])
    # เอา input ไปทดสอบ
   st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)

    if out[0] == "Normal":
        st.header("0")
    elif out[0] == "Sleep Apnea":
        st.header("1")
    else:
        st.header("2")

st.button("ไม่ทำนายผล")



