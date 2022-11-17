import streamlit as st
import pandas as pd
import numpy as np

## creating a header for this dashboard
st.header('Chipotle in America')

## creating some text about the dashboard 
st.text('If you are craving Chipotle look for a location here!')

## importing the dataset used for this dashboard
df = pd.read_csv('chipotle_stores.csv')
df.columns

## sorting the dataset by Eastern and Western Americas at the longitude of -97.5
df_sorted = df.sort_values(by='longitude', ascending=False)
chipotle_east = df_sorted.head(1844)
chipotle_west = df_sorted.tail(785)

#### Toggle ####
if st.checkbox('Show Chipotle East Dataset'):
    st.dataframe(chipotle_east)
if st.checkbox('Show Chipotle West Dataset'):
    st.dataframe(chipotle_west)

df = pd.DataFrame(columns=['latitude', 'longitude'])
st.map(df)