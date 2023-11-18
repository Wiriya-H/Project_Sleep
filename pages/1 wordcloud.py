import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')


st.header("Positive ")
grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()

# Reshape the data for plotting
reshaped_data = grouped_data.unstack()

# Specify the colors
custom_colors = ['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7']

# Create a Streamlit figure
fig, axes = plt.subplots(nrows=len(reshaped_data), ncols=1, figsize=(5, 10))

# วนลูปทุกคอลัมน์ (Gender)
for i, gender in enumerate(reshaped_data.columns):
    ax = axes[i]
    ax.pie(reshaped_data[gender], labels=reshaped_data.index, autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.set_title(f'Gender {gender}')

# แสดงภาพใน Streamlit โดยใช้ st.pyplot()
st.pyplot(fig)

# Optionally, you can add some space between the pie charts
st.text("")  # Add an empty line

st.header("Negative ")
pivot_table = df.pivot_table(index='BMI Category', columns='Sleep Disorder', aggfunc={'Sleep Disorder': 'count'})
fig1, ax = plt.subplots(figsize=(20, 10))
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7'])
plt.axis('equal') 

# Display the figure using st.pyplot()
st.pyplot(fig1)