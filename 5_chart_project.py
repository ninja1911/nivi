import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('LifeExpectancy (1).csv')
    return data

life_expectancy_data = load_data()

# Navigation bar
st.sidebar.title("Life Expectancy Data Visualizations")
options = st.sidebar.radio('Select a Chart:', 
                           ('Life Expectancy Trend', 
                            'Country Comparison',
                            'GDP vs Life Expectancy',
                            'Correlation Heatmap',
                            'Life Expectancy Distribution',
                            'Health Challenges by Country'))

# Visualization 1: Life Expectancy Trend
if options == 'Life Expectancy Trend':
    st.header("Global Average Adult Mortality Rate Over the Years")
    average_adult_mortality = life_expectancy_data.groupby('Year')['Adult Mortality'].mean()
    plt.figure(figsize=(12, 6))
    plt.plot(average_adult_mortality.index, average_adult_mortality.values)
    plt.title('Global Average Adult Mortality Rate Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Adult Mortality Rate')
    plt.grid(True)
    st.pyplot(plt)

# Visualization 2: Country Comparison
elif options == 'Country Comparison':
    st.header("Life Expectancy in Different Countries in a Selected Year")
    selected_year = st.selectbox("Select Year", life_expectancy_data['Year'].unique())
    life_expectancy_selected_year = life_expectancy_data[life_expectancy_data['Year'] == selected_year]
    countries = life_expectancy_selected_year['Country']
    life_expectancies = life_expectancy_selected_year['Life expectancy']
    plt.figure(figsize=(12, 6))
    plt.bar(countries, life_expectancies)
    plt.xticks(rotation=45)
    plt.title(f'Life Expectancy in Different Countries in {selected_year}')
    plt.xlabel('Country')
    plt.ylabel('Life Expectancy')
    plt.grid(True)
    st.pyplot(plt)

# Visualization 3: GDP vs Life Expectancy
elif options == 'GDP vs Life Expectancy':
    st.header("Relationship between GDP and Life Expectancy")
    selected_year = st.selectbox("Select Year", life_expectancy_data['Year'].unique(), key='scatter')
    scatter_data = life_expectancy_data[life_expectancy_data['Year'] == selected_year]
    plt.figure(figsize=(12, 6))
    plt.scatter(scatter_data['GDP'], scatter_data['Life expectancy'])
    plt.title(f'Relationship between GDP and Life Expectancy in {selected_year}')
    plt.xlabel('GDP in USD')
    plt.ylabel('Life Expectancy')
    plt.grid(True)
    st.pyplot(plt)

# Visualization 4: Correlation Heatmap
elif options == 'Correlation Heatmap':
    st.header("Correlation Heatmap of Various Health and Economic Indicators")
    numerical_columns = life_expectancy_data.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = life_expectancy_data[numerical_columns].corr()
    plt.figure(figsize=(12, 10))
    plt.imshow(correlation_matrix, cmap='coolwarm')
    plt.colorbar()
    plt.xticks(np.arange(len(numerical_columns)), numerical_columns, rotation=90)
    plt.yticks(np.arange(len(numerical_columns)), numerical_columns)
    plt.title('Correlation Heatmap')
    st.pyplot(plt)

# Visualization 5: Life Expectancy Distribution
elif options == 'Life Expectancy Distribution':
    st.header("Distribution of Life Expectancy Across the Dataset")
    plt.figure(figsize=(12, 6))
    plt.hist(life_expectancy_data['Life expectancy'], bins=30, edgecolor='black')
    plt.title('Distribution of Life Expectancy')
    plt.xlabel('Life Expectancy')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt)

# Visualization 6: Health Challenges by Country
elif options == 'Health Challenges by Country':
    st.header("Health Challenges by Country in a Selected Year")
    selected_year = st.selectbox("Select Year for Health Challenges", life_expectancy_data['Year'].unique(), key='health_challenges')
    health_data = life_expectancy_data[life_expectancy_data['Year'] == selected_year]
    countries = health_data['Country']
    adult_mortality = health_data['Adult Mortality']
    infant_deaths = health_data['infant deaths']
    plt.figure(figsize=(12, 6))
    p1 = plt.bar(countries, adult_mortality, color='blue')
    p2 = plt.bar(countries, infant_deaths, color='red', bottom=adult_mortality)
    plt.xticks(rotation=45)
    plt.ylabel('Counts')
    plt.title('Health Challenges in Different Countries in ' + str(selected_year))
    plt.legend((p1[0], p2[0]), ('Adult Mortality', 'Infant Deaths'))
    plt.grid(True)
    st.pyplot(plt)
