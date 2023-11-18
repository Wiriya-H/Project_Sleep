pip install termcolor


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored


# Add header row while reading a CSV file
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')


st.header("Positive ")
grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()
reshaped_data = grouped_data.unstack()
fig, axes = plt.subplots(nrows=1, ncols=len(reshaped_data), figsize=(15, 5))
custom_colors = ['#C39BD3', '#D2B4DE', '#EBDEF0', '#F4ECF7']
for i, (sleep_disorder, counts) in enumerate(reshaped_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.set_title(f'Sleep Disorder {sleep_disorder}')

plt.show()


st.header("Negative ")
df.pivot_table(index='BMI Category',columns='Sleep Disorder',aggfunc={'Sleep Disorder':'count'}).plot.pie(autopct ='%1.1f%%',subplots=True,figsize=(20,10),colors=['#C39BD3','#D2B4DE','#EBDEF0','#F4ECF7'])

plt.axis('equal')
plt.show()