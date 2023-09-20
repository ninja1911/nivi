import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
df=pd.read_csv(r"Fish.csv")
data=df.groupby('Species').agg({"Weight": ["mean","min","max"]})
# rename columns
data.columns = ['weight_mean', 'weight_min', 'weight_max']
# reset index to get grouped columns back
data = data.reset_index()
data=data.sort_values(by=['weight_mean'], ascending=True)
print(data)
plt.plot(data['Species'], data['weight_mean'], label ='weight_mean', marker='o')
plt.plot(data['Species'], data['weight_min'], label ='weight_min', marker='o')
plt.plot(data['Species'], data['weight_max'], label ='weight_max', marker='o')

plt.title('Max/Mean/Min weight across species in increasing order', fontsize=14)
plt.xlabel('Species', fontsize=14)
plt.ylabel('Weight', fontsize=14)
# plt.grid(True)
plt.legend()
Line_chart=plt.show()
st.pyplot(Line_chart)
