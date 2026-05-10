import streamlit as st
import requests
import pickle
import pandas as pd

with pickle.load("similarity.pkl","rb") as file:
   sim=open("similarity.pkl")

st.title("Movie Recommender System")

with pickle.load("movie_data.pkl","rb") as file:
   d1=open("movie_data.pkl")
movie_data=pd.DataFrame(d1)

options=st.selectbox(
   movie_data["title"].value_counts()
)

def fetch_poster(movie_id):
    dapi_key = "YOUR_API_KEY"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    data = requests.get(url)
    data = data.json()


def recommend(film):
   mov_idx=movie_data[movie_data['title']==film].index[0]
   distance=sim(mov_idx)
   l=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
   
   for i in l:
      st.write(movie_data.iloc[i[0]].title)

