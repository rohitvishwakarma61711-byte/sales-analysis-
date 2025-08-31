import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import streamlit as st
st.markdown(f"# :orange[Sales Data Visualization]")

data=pd.read_csv(r"C:\Users\hp\OneDrive\Documents\sales_data_sample.csv",encoding="latin")
data.drop(columns=['ADDRESSLINE2','ADDRESSLINE1','STATE',"TERRITORY","POSTALCODE"],inplace=True)
#st.dataframe(data)
#st.write(data.shape)
st.write("      ")
st.write("")

col1,col2,col3=st.columns(3)
with col2:
   total_country=data["COUNTRY"].nunique()
   st.subheader("TOTAL COUNTRY")
   st.header(total_country)
with col1:
   total_order=data["ORDERNUMBER"].nunique()
   st.subheader("TOTAL ORDER")
   st.header(total_order)
with col3:
   suma=data["SALES"].sum()
   st.subheader("TOTAL SALE")
   st.header(int(suma))


    
st.markdown(f" # :orange[------------------------------------------------]")
      
st.header("Top 5 Countries by Number of Orders")
plt.figure(figsize=(4,4))
ax=data["COUNTRY"].value_counts()[:5].plot(kind="bar",)
ax.bar_label(ax.containers[0])
plt.show()
st.pyplot(ax.figure)

st.markdown(f" # :orange[------------------------------------------------]")

st.header("Top 5 Cities by Number of Orders")
plt.figure(figsize=(6,6))
ax=data["CITY"].value_counts()[:5].plot(kind="bar",color="orange")
ax.bar_label(ax.containers[0])
plt.show()
st.pyplot(ax.figure)

st.markdown(f" # :orange[------------------------------------------------]")
 
st.header("ORDER STATUS")
plt.figure(figsize=(6,6))
a=sn.countplot(x="STATUS",data=data)
a.bar_label(a.containers[0])
plt.show()
st.pyplot(a.figure)

st.markdown(f" # :orange[------------------------------------------------]")
st.header("ORDER SIZE")
plt.figure(figsize=(6,6))
a=sn.countplot(x="DEALSIZE",data=data)
a.bar_label(a.containers[0])
plt.show()
st.pyplot(a.figure)