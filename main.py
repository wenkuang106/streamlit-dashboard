import streamlit as st
import pandas as pd
import numpy as np

## creating a header for this dashboard
st.header('Chipotle in America')

## creating some text about the dashboard 
st.text('If you are craving Chipotle look for a location here!')

## importing the dataset used for this dashboard
df = pd.read_csv('chipotle_stores.csv')

## sorting the dataset by Eastern and Western Americas at the longitude of -97.5
df_sorted = df.sort_values(by='longitude', ascending=False)
chipotle_east = df_sorted.head(1844)
chipotle_west = df_sorted.tail(785)

#### Toggle ####
if st.checkbox('Show Chipotle East Dataset'):
    st.dataframe(chipotle_east)
if st.checkbox('Show Chipotle West Dataset'):
    st.dataframe(chipotle_west)

if st.checkbox('Chipotle in Western America'):
    st.subheader('This is shows the Chipotle areas in Western America')
    st.map(chipotle_west)
if st.checkbox('Chipotle in Eastern America'):
    st.subheader('This is shows the Chipotle areas in Eastern America')
    st.map(chipotle_east)

## creating a bar and line graph of # of chipotle per state
Chart = df[["state"]]
if st.checkbox('Line/Bar Graph of Chipotle Dataset'):
    st.subheader('This is a Line and Bar Graph of Amount of Chipotle per State')
    st.bar_chart(Chart)
    st.line_chart(Chart)

## code-block
if st.checkbox('Press if you wish to see a snippet of code used'):
    code = '''## sorting the dataset by Eastern and Western Americas at the longitude of -97.5
    df_sorted = df.sort_values(by='longitude', ascending=False)
    chipotle_east = df_sorted.head(1844)
    chipotle_west = df_sorted.tail(785)'''
    st.code(code, language='python')