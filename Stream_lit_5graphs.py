import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
st.title("Selectbox")
graphs = ["Linechart","BarChart","Scatterplot","BoxPlot","PieChart"]
graph_selected=st.selectbox("Choose a graph to visualize",options=graphs)
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

if graph_selected=="Linechart":

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
    st.subheader("Line Chart:", divider='rainbow')
    st.pyplot(Line_chart)
    st.subheader('A few basic insights of the given graph:', divider='rainbow')
    st.write('''
\n•From the data we can infer that smelt is least weighed and Pike is the heaviest of all the fishes.
\n•Also for Pike and Perch the min and max values are spread out a lot more than the rest whereas for Smelt all 3 values are around a close range thus making the mean  of this species much more reliable.
\n•Also from the data we can see that the min value of roach is 0 making it an anomaly or out layer.''')
    
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
    st.subheader("Bar Chart:", divider='rainbow')
    st.pyplot(Bar_Chart)
    st.subheader('A few basic insights of the given graph:', divider='rainbow')
    st.write('''•There is significant difference in mean and max weights for Pike and Perch.
\n•While the max weight for Perch, Whitefish, Roach and Parkki is twice of its mean weight. 
\n•Whereas Smelt is the least heavy of all species.''')
elif graph_selected=="Scatterplot":
    colors = ['b', 'y', 'm', 'r']
    perch_data=df[df['Species']=='Perch']
    pike_data=df[df['Species']=='Pike']
    
    lo = plt.scatter(perch_data['Height'], perch_data['Weight'], marker='x', color=colors[0])
    ll = plt.scatter(pike_data['Height'], pike_data['Weight'], marker='o', color=colors[1])
    
    plt.title("Height and Weight Scatter plot of Perch vs Pike Species")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend((lo, ll),
               ('Perch', 'Pike'),
               scatterpoints=1,
               loc='upper left',
               ncol=3,
               fontsize=8)
    
    plt.show()
    Scatter_plot=plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #inserting the header for Scatter plot
    st.subheader("Scatter Plot:", divider='rainbow')
    st.pyplot(Scatter_plot)
    st.subheader('A few basic insights of the given graph:', divider='rainbow')
    st.write('''•Both Perch and Pike species show a strong positive correlation between height and weight, signifying that as height increases, weight also increases.
\n•Pike, in particular, displays a steeper slope, indicating that it tends to be heavier than Perch for a given height.
\n•Most specimens fall within the 5 to 7 height range and weigh under 250 pounds, highlighting common size and weight patterns for these species.''')
elif graph_selected=="BoxPlot":
    perch_data=df[df['Species']=='Perch']
    
    ax = df[['Height', 'Width']].plot(kind='box', title='boxplot')
    plt.title("Distribution of height and weight of fish species")
    plt.xlabel("Height/Width")
    plt.ylabel("Height/Width")
    # show plot
    plt.show()
    Box_Plot=plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #inserting the header for Box Plot
    st.subheader("Box Plot:", divider='rainbow')
    st.pyplot(Box_Plot)
    st.subheader('A few basic insights of the given graph:', divider='rainbow')
    st.write('''•Variability in Height and Width: The wider distribution of height compared to width suggests that there is more variability in the heights of the fish species than in their widths. 
\n•Absence of Outliers: The absence of outliers indicates that there are no extreme or unusual values in the dataset for either height or width.''')
elif graph_selected=="PieChart":
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%({:d})".format(pct, absolute)
    
    spec= data['Species'].tolist()
    plt.pie(mean_weight, labels = spec,autopct = lambda pct: func(pct, mean_weight))
    plt.title('Mean weight across species', fontsize=12,color='red')
    plt.show()
    Pie_Chart=plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #inserting the header for Pie Chart
    st.subheader("Pie Chart:")
    st.pyplot(Pie_Chart)
    st.subheader('A few basic insights of the given graph:', divider='rainbow')
    st.write('''•From the pie chart it can be inferred that Pike's are the heaviest of all the Fishes with mean weight of 718kgs constituting to 28% Bream are little lighter taking 24.1 % and mean weight of 617.
    \n•Whitefish and Parkki take up 20.7 and 14.9% while Parkki, Roach and Smelt are lightest with 6%, 5.9% and 0.4% of the total respectively.''')
st.write('The transformed data used to populate the chart: ')
# inserting headder and displaying the table in streamlit
data = data.reset_index(drop=True)
st.subheader("The aggregated value of each species:", divider='rainbow')
st.table(data)
