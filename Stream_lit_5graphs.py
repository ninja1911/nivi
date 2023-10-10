import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
st.title("Selectbox")
graphs = ["Linechart","BarChart","Scatterplot","BoxPlot","PieChart"]
graph_selected=st.selectbox("Choose a graph to visualize",options=graphs)
if graph_selected=="Linechart":
    df=pd.read_csv(r"Fish.csv")
    data=df.groupby('Species').agg({"Weight": ["mean","min","max"]})
    # rename columns
    data.columns = ['weight_mean', 'weight_min', 'weight_max']
    # reset index to get grouped columns back
    data = data.reset_index()
    data=data.sort_values(by=['weight_mean'], ascending=True)
    plt.plot(data['Species'], data['weight_mean'], label ='weight_mean', marker='o')
    plt.plot(data['Species'], data['weight_min'], label ='weight_min', marker='o')
    plt.plot(data['Species'], data['weight_max'], label ='weight_max', marker='o')
    
    plt.title('Max/Mean/Min weight across species in increasing order', fontsize=14)
    plt.xlabel('Species', fontsize=14)
    plt.ylabel('Weight', fontsize=14)
    # plt.grid(True)
    plt.legend()
    Line_chart=plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #inserting the header for line chart
    st.subheader("Line Chart:")
    st.pyplot(Line_chart)
elif graph_selected=="BarChart":
    df=pd.read_csv(r"Fish.csv")
    data=df.groupby('Species').agg({"Weight": ["mean","min","max"]})
    # rename columns
    data.columns = ['weight_mean', 'weight_min', 'weight_max']
    # reset index to get grouped columns back
    data = data.reset_index()
    data=data.sort_values(by=['weight_mean'], ascending=True)
    #data
    #x-axis
    #rounding off data so that text is not clumpsy
    data['weight_mean']=data['weight_mean'].round(0)
    data['weight_max']=data['weight_max'].round(0)
    
    species = data['Species'].to_list()
    #y-axis
    mean_weight = data['weight_mean'].to_list()
    max_weight = data['weight_max'].to_list()
    
    #bar chart properties
    x = np.arange(len(species))
    width = 0.3
    
    #draw grouped bar chart
    fig, ax = plt.subplots()
    bar1 = ax.bar(x - width/2, max_weight, width, label='weight_max')
    bar2 = ax.bar(x + width/2, mean_weight, width, label='weight_mean')
    
    ax.set_xlabel('Species')
    ax.set_ylabel('Weight')
    ax.set_title('Mean and max weight of species')
    ax.set_xticks(x, species)
    ax.legend()
    
    #setting bar labels
    ax.bar_label(bar1)
    ax.bar_label(bar2)
    
    fig.tight_layout()
    
    plt.show()
    Bar_Chart=plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #inserting the header for line chart
    st.subheader("Bar Chart:")
    st.pyplot(Bar_Chart)
