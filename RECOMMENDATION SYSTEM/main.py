import pickle
import streamlit as st
import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)


movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

@app.route('/')

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("Movie Recommendation System")
selected_movie_name=st.selectbox(
                    "How would you like to be contacted?",
                    (movies['title'].values)
                    )
if st.button('recommend'):
    recommendations=recommend(selected_movie_name)

    for i in recommendations:
         st.write(i)
if __name__ == '__main__':
    app.run()   