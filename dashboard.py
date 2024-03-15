import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

# Data URLs 
url = 'https://raw.githubusercontent.com/luthfiahafiz/Proyek-Analisis-Data/main/hour.csv'
url1 = 'https://raw.githubusercontent.com/luthfiahafiz/Proyek-Analisis-Data/main/day.csv'

# Read data
hour_data = pd.read_csv(url)
weather_data = pd.read_csv(url1)

# Merge data
merged_data = pd.merge(hour_data, weather_data, on='dteday', suffixes=('_hour', '_weather'))

# Data Exploration 
merged_data.info()
merged_data.describe()
merged_data.dropna(inplace=True)
merged_data.drop_duplicates(inplace=True)

st.title('Bike Sharing Dataset Visualization Dashboard')

# Correlation Matrices 
corr_matrix = merged_data[['temp_hour', 'atemp_hour', 'hum_hour', 'windspeed_hour', 'cnt_hour']].corr()
corr_matrix_weather = merged_data[['temp_weather', 'atemp_weather', 'hum_weather', 'windspeed_weather', 'cnt_weather']].corr()

# Various visualizations

# Correlation Matrix for Hourly Data
st.header('Correlation Matrix for Hourly Data')
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
plt.title('Correlation Matrix for Hourly Data')
st.pyplot(fig)

# Correlation Matrix for Weather Data
st.header('Correlation Matrix for Weather Data')
fig, ax = plt.subplots()
sns.heatmap(corr_matrix_weather, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
plt.title('Correlation Matrix for Weather Data')
st.pyplot(fig)

# Relationship between variables

# Temperature vs Number of Borrowings (Hourly)
st.header('Temperature, Humidity, Wind Speed, Weather Conditions vs Number of Borrowings (Hourly)')
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
sns.scatterplot(x='temp_hour', y='cnt_hour', data=merged_data, ax=axes[0, 0])
plt.title('Temperature vs Number of Borrowings (Hourly)')
plt.xlabel('Temperature')
plt.ylabel('Total')
plt.grid()

sns.scatterplot(x='hum_hour', y='cnt_hour', data=merged_data, ax=axes[0, 1])
plt.title('Humidity vs Number of Borrowings (Hourly)')
plt.xlabel('Humidity')
plt.ylabel('Total')
plt.grid()

sns.scatterplot(x='windspeed_hour', y='cnt_hour', data=merged_data, ax=axes[1, 0])
plt.title('Wind Speed vs Number of Borrowings (Hourly)')
plt.xlabel('Wind Speed')
plt.ylabel('Total')
plt.grid()

sns.boxplot(x='weathersit_hour', y='cnt_hour', data=merged_data, ax=axes[1, 1])
plt.title('Weather Conditions vs Number of Borrowings (Hourly)')
plt.xlabel('Weather Conditions')
plt.ylabel('Total')
plt.tight_layout()
plt.grid()
st.pyplot(fig)

# Visualization of hourly bike borrowings
st.header('Bike Loan per Hour')
fig, ax = plt.subplots()
sns.lineplot(data=merged_data, x='hr', y='cnt_hour', hue='workingday_hour', ax=ax)
plt.title('Bike Loan per Hour')
plt.xlabel('Hour')
plt.ylabel('Total')
plt.grid()
st.pyplot(fig)

# Bike borrowings distribution
st.header('Bike Borrowings Distribution')
fig, ax = plt.subplots()
sns.histplot(data=merged_data, x='cnt_hour', bins=30, kde=True, ax=ax)
plt.title('Bike Borrowings Distribution')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.grid()
st.pyplot(fig)