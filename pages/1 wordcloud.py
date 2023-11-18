import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from termcolor import colored


# Add header row while reading a CSV file
df = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')


st.header("Positive ")
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named df
# Example:
# df = pd.DataFrame({'Sleep Disorder': ['A', 'A', 'B', 'B', 'C', 'C'],
#                    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']})

# Group by 'Sleep Disorder' and 'Gender' and get value counts
grouped_data = df.groupby('Sleep Disorder')['Gender'].value_counts()

# Reshape the data for plotting
reshaped_data = grouped_data.unstack()

# Plotting pie charts
fig, axes = plt.subplots(nrows=1, ncols=len(reshaped_data), figsize=(15, 5))

for i, (sleep_disorder, counts) in enumerate(reshaped_data.iterrows()):
    ax = axes[i]
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
    ax.set_title(f'Sleep Disorder {sleep_disorder}')

plt.show()


st.header("Negative ")
#df.pivot_table(index='BMI Category',columns='Sleep Disorder',aggfunc={'Sleep Disorder':'count'}).plot.pie()

plt.axis('equal')
plt.show()