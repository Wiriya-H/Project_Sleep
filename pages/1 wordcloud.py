import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')

st.table(df.head())

st.header("Positive ")

grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()

# Reshape the data for plotting
reshaped_data = grouped_data.unstack()

# Specify the colors
custom_colors = ['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7']

# Create a Streamlit figure
fig, axes = plt.subplots(nrows=1, ncols=len(reshaped_data), figsize=(15, 5))

for i, (sleep_disorder, counts) in enumerate(reshaped_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.set_title(f'Sleep Disorder {sleep_disorder}')

st.pyplot(fig)

st.header("Negative ")
pivot_table = df.pivot_table(index='BMI Category', columns='Sleep Disorder', aggfunc={'Sleep Disorder': 'count'})

# พล็อต pie chart
fig, ax = plt.subplots()
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7'])
plt.axis('equal')  # รักษาอัตราส่วนเท่ากัน

# แสดงภาพใน Streamlit โดยใช้ st.pyplot()
st.pyplot()