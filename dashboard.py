import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('clean_data.csv')
a,b= st.columns(2)
with a:
    st.title('Indian Startup Analysis')
with b:
    st.image('image.jpeg')

st.sidebar.title('Startup Funding Analysis')
pages=['Overall Analysis','Startups Analyis','Invester Analysis']
btn1= st.sidebar.selectbox('Select Your Choice',pages)
total=str(round(df.Funding_Amount.sum(),2)) + " Cr"
if btn1==pages[0]:
    st.metric(label='Total Funding Raised',value=total)

if btn1==pages[1]:
    btn1= st.sidebar.selectbox('Choose your Startup',df['Invester_name'].unique())
    

if btn1==pages[2]:
    pass
