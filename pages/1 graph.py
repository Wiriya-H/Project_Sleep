import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')

st.table(df.head())

st.header("---")

grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()
reshaped_data = grouped_data.unstack()
custom_colors = ['#ff20b6', '#6eedf2']
fig, axes = plt.subplots(nrows=1, ncols=len(reshaped_data), figsize=(12, 4))
for i, (sleep_disorder, counts) in enumerate(reshaped_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.set_title(f'Sleep Disorder {sleep_disorder}')
st.pyplot(fig)

st.header("---")

pivot_table = df.pivot_table(index='BMI Category', columns='Sleep Disorder', aggfunc={'Sleep Disorder': 'count'})
fig, ax = plt.subplots(figsize=(20, 10))
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=['#57b199', '#7fc15a', '#ffa53b', '#e33d25'])
plt.axis('equal') 
st.pyplot(fig)

st.header("---")
grouped_data = sleep_data.groupby(['Sleep Disorder', 'Gender']).size().reset_index(name='count')

# Create a new DataFrame with Sleep Disorder and Gender as index, and count as values
pivot_table = pd.pivot_table(grouped_data, values='count', index='Sleep Disorder', columns='Gender', fill_value=0)

# Plot the pie chart
fig, ax = plt.subplots(figsize=(15, 7))
colors = ['#4A235A', 'pink', '#4A235A', 'pink', '#4A235A', 'pink']
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=colors)
plt.title('The relationship between (sex) and (Sleep Disorder)')
plt.axis('equal')

# Display the plot in Streamlit
st.pyplot(fig)