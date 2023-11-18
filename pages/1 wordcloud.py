import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')

st.table(df.head())

st.header("---")

grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()
reshaped_data = grouped_data.unstack()
custom_colors = ['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7']
fig, axes = plt.subplots(nrows=1, ncols=len(reshaped_data), figsize=(12, 4))
for i, (sleep_disorder, counts) in enumerate(reshaped_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.set_title(f'Sleep Disorder {sleep_disorder}')
st.pyplot(fig)

st.header("---")

pivot_table = df.pivot_table(index='BMI Category', columns='Sleep Disorder', aggfunc={'Sleep Disorder': 'count'})
fig, ax = plt.subplots(figsize=(20, 10))
pivot_table.plot.pie(subplots=True, autopct='%1.1f%%', ax=ax, colors=['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7'])
plt.axis('equal') 
st.pyplot(fig)

st.header("---")

fig = px.histogram(sleep_data, x='Sleep Disorder',
                   color='Sleep Disorder',
                   facet_col='Stress Level',
                   barmode='group',
                   color_discrete_sequence=['white', '#4A235A', '#C39BD3'],
                   opacity=0.8)

fig.update_layout(title='<b>The effect of Stress Level on Sleep Disorder</b> ..', title_font={'size': 30},
                  paper_bgcolor='#EBDEF0',
                  plot_bgcolor='#EBDEF0')

fig.update_yaxes(showgrid=False)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)