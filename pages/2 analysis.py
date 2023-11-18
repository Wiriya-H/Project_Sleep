import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Assume 'df' is your DataFrame
df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')

# Feature selection
selected_features = ["Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level"]
X = df[selected_features]
y = df["Sleep Disorder"]

# Encoding categorical variables if any
le = LabelEncoder()

# Print column names
print("Column names in X:", X.columns)

# Check unique values in 'Gender' column
print("Unique values in 'Gender' column:", X['Gender'].unique())

# Encode 'Gender' column
X['Gender'] = le.fit_transform(X['Gender'])

for cat_column in X.select_dtypes('object').columns:
    X[cat_column] = le.fit_transform(X[cat_column])

# Create and fit the model
dt_model = DecisionTreeClassifier()
dt_model.fit(X, y)

# Streamlit UI
st.title("Sleep Disorder Prediction")

# User input for prediction
sd = st.number_input("Sleep Duration", 0, 10)
qos = st.slider("Quality of Sleep", 0, 10)
pal = st.number_input("Physical Activity Level")
sl = st.slider("Stress Level", 0, 10)

if st.button("Predict"):
    # Prepare the input data for prediction
    x_input = np.array([[sd, qos, pal, sl]])

    # Make prediction
    prediction = dt_model.predict(x_input)

    # Display the prediction result
    if prediction[0] == "Normal":
        st.header("Normal")
    elif prediction[0] == "Sleep Apnea":
        st.header("Sleep Apnea")
    else:
        st.header("Other Sleep Disorder")

# Button for not making a prediction
st.button("Do Not Predict")
