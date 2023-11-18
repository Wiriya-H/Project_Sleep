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

# Checkbox to show/hide the bar chart
show_chart = st.checkbox("Show bar chart")

# Display the bar chart if the checkbox is checked
if show_chart:
    st.bar_chart(dx2)