import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from termcolor import colored


# Add header row while reading a CSV file
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')


st.header("Positive ")
grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()
reshaped_data = grouped_data.unstack()
fig, axes = plt.subplots(nrows=1, ncols=len(reshaped_data), figsize=(15, 5))
for i, (sleep_disorder, counts) in enumerate(reshaped_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Sleep Disorder {sleep_disorder}')

plt.show()


st.header("Negative ")
df.pivot_table(index='BMI Category',columns='Sleep Disorder',aggfunc={'Sleep Disorder':'count'}).plot.pie()

plt.axis('equal')
plt.show()