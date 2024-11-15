import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    layout="wide",  # Sets the layout to wide mode
      # Expands the sidebar by default
)
df=pd.read_csv('clean_data.csv')
a,b= st.columns(2)
with a:
    st.title('Indian Startup Analysis')
with b:
    st.image('image.jpeg')

st.sidebar.title('Startup Funding Analysis')
pages=['Overall Analysis','Startups Analyis','Invester Analysis']
btn1= st.sidebar.selectbox('Select Your Choice',pages)
total=str(round(df.Funding_Amount_in_cr.sum(),2)) + " Cr"
max_=str(round(df['Funding_Amount_in_cr'].max(),2)) +' Cr'
df_sorted = df.sort_values(by='Funding_Amount_in_cr', ascending=False).head(10)
# selected_columns = df_sorted  
if btn1==pages[0]:
    x,y=st.columns(2)
    with x:
        st.metric(label='Total Funding Raised',value=total)
    with y:
        st.metric(label='Maximum Funding Raised',value=max_)
    st.write('          Top Funding getting Company')
    st.dataframe(df_sorted)
if btn1==pages[1]:
    pass
if btn1==pages[2]:
    btn2= st.sidebar.selectbox('Choose your Startup',df['Invester_name'].unique())
    st.metric(label='Total Investment',value=str((df.groupby('Invester_name')['Funding_Amount_in_cr'].sum().loc[btn2])) +' Crs ')
    top = df.groupby('Industry_Vertical')['Funding_Amount_in_cr'].sum().sort_values(ascending =False).head(3)
    
    st.bar_chart(top)
