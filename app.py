import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=4ecc8dca976766083c68aae9e3e98ee6".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies [ movies [ 'title' ] == movie ].index [ 0 ]
    distances = similarity [ movie_index ]
    movie_list = sorted(list(enumerate(distances)) , reverse = True , key = lambda x: x [ 1 ]) [ 1:6 ]

    recommend_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc [ i [ 0 ] ].movie_id
        recommend_movies.append(movies.iloc [ i [ 0 ] ].title)
        #fetching movie poster form API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies , recommended_movies_poster


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    recommended_movie_names , recommended_movie_posters = recommend(selected_movie_name)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names [ 0 ])
        st.image(recommended_movie_posters [ 0 ])
    with col2:
        st.text(recommended_movie_names [ 1 ])
        st.image(recommended_movie_posters [ 1 ])

    with col3:
        st.text(recommended_movie_names [ 2 ])
        st.image(recommended_movie_posters [ 2 ])
    with col4:
        st.text(recommended_movie_names [ 3 ])
        st.image(recommended_movie_posters [ 3 ])
    with col5:
        st.text(recommended_movie_names [ 4 ])
        st.image(recommended_movie_posters [ 4 ])

    # run by using >  E:\Jupyter\Projects\Movie Recommender System\Movie-Recommender-System> streamlit run app.p |command