import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c2679edc030d5b826a865e5cb9e37ae8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]


    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
      movie_id = i[0]
      
      recommended_movies.append(movies.iloc[i[0]].title)
       #fetch poster from API
      recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

 
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
 
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col3:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
