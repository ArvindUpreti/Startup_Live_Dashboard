import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


st.set_page_config(layout="wide", page_title="Start-up Analysis Dashboard")


df = pd.read_csv("clean_data.csv")


a, b = st.columns(2)
with a:
    st.title("Indian Startup Analysis")
with b:
    st.image("image.jpeg")

# Adding a Sidebar to webpage 
st.sidebar.title("Startup Funding Analysis")
pages = ["Overall Analysis", "Startups Analysis", "Investor Analysis"]
btn1 = st.sidebar.selectbox("Select Your Choice", pages)

# Key statistics
total = f"{round(df['Funding_Amount_in_cr'].sum(), 2)} Cr"
max_ = f"{round(df['Funding_Amount_in_cr'].max(), 2)} Cr"

# Top industries based on funding
top = (
    df.groupby("Industry_Vertical")["Funding_Amount_in_cr"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
df_top_industries = pd.DataFrame(top).reset_index()  # Prepare DataFrame for plotting

# Top 10 funded startups
df_sorted = df.sort_values(by="Funding_Amount_in_cr", ascending=False).head(10)

# Conditional rendering based on selected page
if btn1 == pages[0]:  # Overall Analysis
    x, y = st.columns(2)
    with x:
        st.metric(label="Total Funding Raised", value=total)
    with y:
        st.metric(label="Maximum Funding Raised", value=max_)

    st.subheader("Top Funding Companies")
    st.dataframe(df_sorted)

    # Display a bar chart for top industries by funding
    st.subheader("Top Industries by Funding")
    bar_chart = alt.Chart(df_top_industries).mark_bar().encode(
        x=alt.X("Funding_Amount_in_cr:Q", title="Total Funding (Cr)"),
        y=alt.Y("Industry_Vertical:N", sort="-x", title="Industry Vertical"),
        color=alt.Color("Industry_Vertical:N", legend=None),
    )
    st.altair_chart(bar_chart, use_container_width=True)

elif btn1 == pages[1]:  # Startups Analysis
    st.subheader("Startups Analysis")
    # Add content here for startups analysis if needed

elif btn1 == pages[2]:  # Investor Analysis
    # Sidebar input to choose an investor
    btn2 = st.sidebar.selectbox("Choose your Investor", df["Invester_name"].unique())

    # Display total investment by selected investor
    total_investment = df.groupby("Invester_name")["Funding_Amount_in_cr"].sum().loc[btn2]
    h,i,j=st.columns(3)
    with h:
        st.metric(label="Total Investment", value=f"{total_investment} Cr")
    with i:
        st.metric(label="Total Investment", value=f"{total_investment} Cr")
    with j:
        st.metric(label="Total Investment", value=f"{total_investment} Cr")
    # Show a line chart for funding by industry for the selected investor
    investor_funding = df[df["Invester_name"] == btn2].groupby("Industry_Vertical")[
        "Funding_Amount_in_cr"
    ].sum().reset_index()
    
    # Ensure there is data to display

    x,y=st.columns(2)
    with x:
        if not investor_funding.empty:
            st.write(f"Funding by Industry for {btn2}")
            line_chart = alt.Chart(investor_funding).mark_line().encode(
                x=alt.X("Industry_Vertical:N", title="Industry Vertical"),
                y=alt.Y("Funding_Amount_in_cr:Q", title="Funding Amount (Cr)"),
                color=alt.value("#FF5733"),
            )
            st.altair_chart(line_chart, use_container_width=True)
        else:
            st.write("No data available for the selected investor.")
    with y:
        if not investor_funding.empty:
            st.write(f"Funding by Industry for {btn2}")
            # Create a bar chart for the funding data
            bar_chart = alt.Chart(investor_funding).mark_bar().encode(
                x=alt.X("Industry_Vertical:N", title="Industry Vertical", sort="-y"),
                y=alt.Y("Funding_Amount_in_cr:Q", title="Funding Amount (Cr)"),
                color=alt.value("#FF5733"),
            )
            st.altair_chart(bar_chart, use_container_width=True)
        else:
            st.subheader(f"No data available for the selected investor: {btn2}")
