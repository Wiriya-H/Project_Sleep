import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')

st.table(df.head())

st.header("The relationship between (sex) and (Sleep Disorder)")

grouped_data = df.groupby(['Sleep Disorder', 'Gender']).size().reset_index(name='count')
pivot_table = pd.pivot_table(grouped_data, values='count', index='Sleep Disorder', columns='Gender', fill_value=0)
fig, ax = plt.subplots(figsize=(15, 7))
colors = ['#57b199', '#7fc15a', '#ffa53b']
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=colors)
plt.axis('equal')
st.pyplot(fig)

st.header("The relationship between (Age) and (Sleep Disorder)")

grouped_data = df.groupby(['Sleep Disorder', 'Age']).size().reset_index(name='count')
st.bar_chart(grouped_data.set_index('Age'))

st.header("The relationship between (BMI) and (Sleep Disorder)")
pivot_table = df.pivot_table(index='BMI Category', columns='Sleep Disorder', aggfunc={'Sleep Disorder': 'count'})

# Create a vertical bar chart using Matplotlib
fig, ax = plt.subplots(figsize=(20, 10))
pivot_table.plot.bar(ax=ax, color=['#57b199', '#7fc15a', '#ffa53b', '#e33d25'], stacked=True)

# Set chart title and labels
plt.title('Sleep Disorder distribution across BMI Categories')
plt.xlabel('BMI Category')
plt.ylabel('Count')

# Set legend
plt.legend(title='Sleep Disorder')

# Display the plot in Streamlit
st.pyplot(fig)
