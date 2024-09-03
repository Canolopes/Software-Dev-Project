import streamlit as st
import pandas as pd
import plotly.express as px
cars = pd.read_csv('C:/Users/canol/Software-Dev-Project/vehicles_us.csv')
st.header("Data Analysis of Vehicle Sales Data", divider="blue")
