# -*- coding: utf-8 -*-
"""patient survival prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rbCLkQIfxyukCBhoJkxeUzzVaA0aLPUF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/content/dataset.csv')

df.head()

df.shape

df.describe()

df.info()

df.isnull().sum()

df.eq(0).sum()

df = df.drop(['Unnamed: 83'], axis = 1)

sns.heatmap(df.corr())

df.columns

df.drop(['encounter_id','patient_id', 'icu_admit_source',
             'icu_id', 'icu_stay_type', 'icu_type'], axis = 1, inplace = True)

df.head()

df.nunique()

df.duplicated().sum()

df = df[df[['bmi', 'weight', 'height']].isna().sum(axis=1) == 0]

import plotly.express as px

fig = px.histogram(df[['age', 'gender', 'hospital_death', 'bmi']].dropna(), x= "age", y = "hospital_death", color = 'gender',
                  marginal = 'box', hover_data = df[['age', 'gender', 'hospital_death', 'bmi']].columns)
fig.show()

#female death rate is higher

sns.countplot(df, x='gender')

sns.histplot(df, x='age', bins=20, kde= True)
plt.title('Age Distribution')
plt.show()

sns.histplot(df, x='age', bins=20, kde= True, hue= 'gender')
plt.title('Age Distribution')
plt.show()

sns.histplot(df, x='bmi', bins=20, kde= True)
plt.title('BMI Distribution')
plt.show()

sns.histplot(df, x='bmi', bins=20, kde= True, hue= 'gender')
plt.title('BMI Distribution')
plt.show()

