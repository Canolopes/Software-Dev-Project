import streamlit as st
import pandas as pd
import plotly.express as px
cars = pd.read_csv('C:/Users/canol/Software-Dev-Project/vehicles_us.csv')
st.header("Data Analysis of Vehicle Sales Data", divider="blue")
cars['is_4wd'] = cars['is_4wd'].fillna(0)
cars = cars.dropna()
fig_scatter = px.scatter(cars, x='model_year', y='days_listed', title='Model Year vs. Days Listed')
fig_scatter.update_layout(xaxis_range=[1960, 2020])
st.plotly_chart(fig_scatter)
fig_hist = px.histogram(cars, x='price', title ='Distribution of Car Prices')
fig_hist.update_layout(xaxis_range =[0,80000])
st.plotly_chart(fig_hist)
show_modern_cars = st.checkbox('Show only cars from 2010 and up')
if show_modern_cars:
    cars = cars[cars['model_year'] > 2009]
else:
    cars = cars

st.write(cars)