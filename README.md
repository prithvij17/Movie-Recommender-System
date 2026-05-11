# 🎬 Movie Recommender System

A content-based movie recommendation web app built with **Streamlit** that suggests 5 similar movies based on your selection, complete with posters fetched live from the TMDB API.

---

## 📌 Overview

This project uses **content-based filtering** to recommend movies. Each movie is represented by a `tags` field (built from genres, keywords, cast, crew, and overview), and similarity between movies is computed using **cosine similarity** on vectorized tags. When a user selects a movie, the system finds the 5 closest matches from a dataset of **4,806 movies**.

---

## 🗂️ Project Structure

```
Movie-Recommender-System/
│
├── tmdb_5000_movies.csv        # Raw TMDB movies dataset
├── tmdb_5000_credits.csv       # Raw TMDB credits dataset
├── Preprocess_And_Model.ipynb  # Data preprocessing & similarity model building
├── movie_data.pkl              # Preprocessed movie DataFrame (title, id, tags)
├── similarity.pkl              # Precomputed cosine similarity matrix
├── ui.py                       # Streamlit frontend app
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

### 1. Preprocessing (`Preprocess_And_Model.ipynb`)
- Merges `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
- Extracts and cleans: genres, keywords, top 3 cast, director, and overview
- Combines them into a single `tags` column per movie
- Applies **Porter Stemming** to normalize words
- Vectorizes tags using **CountVectorizer**
- Computes a **cosine similarity matrix** across all 4,806 movies
- Saves the processed DataFrame as `movie_data.pkl` and the matrix as `similarity.pkl`

### 2. Recommendation (`ui.py`)
- Loads `movie_data.pkl` and `similarity.pkl`
- User selects a movie from the dropdown
- On clicking **RECOMMEND**, fetches the top 5 most similar movies
- Retrieves each movie's poster from the **TMDB API**
- Displays movie names and posters in a 5-column layout

---

## 🚀 Getting Started

## 🖥️ Demo

| Select a Movie | Get 5 Recommendations with Posters |
|---|---|
| Pick any of 4,806 movies from the dropdown | Click **RECOMMEND** to see results instantly |

---

## 🛠️ Tech Stack

| Tool | Purpose |

| Python | Core language |
| Pandas | Data manipulation |
| Scikit-learn | CountVectorizer & cosine similarity |
| NLTK | Porter Stemmer for tag normalization |
| Streamlit | Web UI |
| TMDB API | Fetching movie posters |
| Pickle | Saving/loading model artifacts |

---

## 📦 Dataset

- Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) on Kaggle
- Size: 4,806 movies after cleaning
- Columns used: `title`, `id`, `tags`

---

## 🙏 Acknowledgements

- [The Movie Database (TMDB)](https://www.themoviedb.org/) for the API and dataset
- [Kaggle](https://www.kaggle.com/) for hosting the dataset
