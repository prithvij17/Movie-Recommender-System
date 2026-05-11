import streamlit as st
import requests
import pickle
import pandas as pd

st.title("Movie Recommender System") 

with open("similarity.pkl", "rb") as file:
   sim = pickle.load(file)

with open("movie_data.pkl", "rb") as file:
   d1 = pickle.load(file)
movie_data=pd.DataFrame(d1)

options=st.selectbox("Select a Movie",
   movie_data["title"].values
)


def fetch_poster(movie_id):
    api_key = "c3545b887fef5c0d0a3bc52cabdb2f0e"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(film):
   mov_idx=movie_data[movie_data['title']==film].index[0]
   distance=sim[mov_idx]
   l=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
   recommended_movies = []
   recommended_posters = []

   for i in l:

      movie_id = movie_data.iloc[i[0]].id

      recommended_movies.append(movie_data.iloc[i[0]].title)

      # Fetch poster
      recommended_posters.append(fetch_poster(movie_id))

   return recommended_movies, recommended_posters

  

if st.button('RECOMMEND'):

    names, posters = recommend(options)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

