import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    """Returns the best 5 recommendations"""
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    distances = list(enumerate(distances))
    movies_list = sorted(distances, reverse=True, key=(lambda x:x[1]))[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommendation = movies.iloc[i[0]].title
        recommended_movies.append(recommendation)
    return recommended_movies

# importing the preprocessed data and the model
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")
st.subheader("I want to see a movie like:")
selected_movie_name = st.selectbox(
    "",
    movies['title'].values,
    label_visibility = "collapsed"
)

if st.button("Recommend"):
    st.subheader("Then you should watch:")
    recommendations = recommend(selected_movie_name)
    for title in recommendations:
        st.write("\t-",title)



