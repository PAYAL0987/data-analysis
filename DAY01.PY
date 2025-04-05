# Import libraries

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns



# Load dataset

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/Telecom_customer_churn.csv"

df = pd.read_csv(url)



# Show first 5 rows

print("First 5 rows:")

print(df.head())



# Drop 'customerID' column

df.drop(['customerID'], axis=1, inplace=True)



# Check for missing values

print("\nMissing values:")

print(df.isnull().sum())



# Simple Visualization: Churn distribution

plt.figure(figsize=(6, 4))

sns.countplot(x='Churn', data=df, palette='Set2')

plt.title('Customer Churn Count')

plt.show()



# Churn by InternetService type

plt.figure(figsize=(8, 5))

sns.countplot(x='InternetService', hue='Churn', data=df)

plt.title('Churn by Internet Service Type')

plt.show()