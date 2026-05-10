import streamlit as st
import requests
import pickle
import pandas as pd


st.title("Movie Recommender System")

with pickle.load("movie_data","wb"):
   d1=open("movie_data")
d2=pd.DataFrame(d1)

options=st.selectbox(
   d2["title"].value_counts()
)
