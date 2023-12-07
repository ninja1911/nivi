import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
                            'GDP, Life Expectancy, and Population Bubble Chart'))

# Visualization 1: Life Expectancy Trend
if options == 'Life Expectancy Trend':
    st.header("Global Average Adult Mortality Rate Over the Years")
    average_adult_mortality = life_expectancy_data.groupby('Year')['Adult Mortality'].mean()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=average_adult_mortality.index, y=average_adult_mortality.values)
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
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Country', y='Life expectancy', data=life_expectancy_selected_year)
    plt.xticks(rotation=45)
    plt.title(f'Life Expectancy in Different Countries in {selected_year}')
    plt.xlabel('Country')
    plt.ylabel('Life Expectancy')
    plt.grid(True)
    st.pyplot(plt)

# Visualization 3: GDP vs Life Expectancy
elif options == 'GDP vs Life Expectancy':
    st.header("Relationship between GDP and Life Expectancy")
    selected_year = st.selectbox("Select Year", life_expectancy_data['Year'].unique())
    scatter_data = life_expectancy_data[life_expectancy_data['Year'] == selected_year]
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='GDP', y='Life expectancy', data=scatter_data)
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
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    st.pyplot(plt)

# Visualization 5: Life Expectancy Distribution
elif options == 'Life Expectancy Distribution':
    st.header("Distribution of Life Expectancy Across the Dataset")
    plt.figure(figsize=(12, 6))
    sns.histplot(life_expectancy_data['Life expectancy'], kde=True)
    plt.title('Distribution of Life Expectancy')
    plt.xlabel('Life Expectancy')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot(plt)

# Visualization 6: GDP, Life Expectancy, and Population Bubble Chart
elif options == 'GDP, Life Expectancy, and Population Bubble Chart':
    st.header("Bubble Chart: GDP, Life Expectancy, and Population")
    selected_year = st.selectbox("Select Year for Bubble Chart", life_expectancy_data['Year'].unique(), key='bubble_chart_year')
    bubble_data = life_expectancy_data[life_expectancy_data['Year'] == selected_year]
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=bubble_data, x="GDP", y="Life expectancy", size="Population", legend='full', sizes=(20, 1000))
    plt.title(f'Bubble Chart for {selected_year}: GDP, Life Expectancy, and Population')
    plt.xlabel('GDP in USD')
    plt.ylabel('Life Expectancy')
    plt.grid(True)
    st.pyplot(plt)
