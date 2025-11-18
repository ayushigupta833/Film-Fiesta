# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2f39568353757806f274f9a0a35ade64&language=en-US'.format(movie_id))
#     data=response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500/" +  data['poster_path']
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies=[]
#     recommended_movies_posters=[]
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetching posters
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies,recommended_movies_posters
#
# movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# movies=pd.DataFrame(movies_dict)
# st.title('Movie Recommender System')
#
# similarity=pickle.load(open('similarity.pkl','rb'))
#
# selected_movie_name = st.selectbox(
# 'How would you like to be contacted?' ,
# movies['title'].values)
#
# if st.button('Recommend'):
#    names,posters = recommend(selected_movie_name)
#    col1, col2, col3, col4, col5 = st.columns(5)
#    with col1:
#        st.text(names[0])
#        st.image(posters[0])
#    with col2:
#        st.text(names[1])
#        st.image(posters[1])
#    with col3:
#        st.text(names[2])
#        st.image(posters[2])
#    with col4:
#        st.text(names[3])
#        st.image(posters[3])
#    with col5:
#        st.text(names[4])
#        st.image(posters[4])
#
#
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Sidebar Config
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# # 🎨 Theme Toggle
# theme = st.sidebar.radio("🎨 Choose Theme", ["Light", "Dark"])
#
# # 🔁 Inject Dynamic CSS Based on Theme
# if theme == "Dark":
#     bg_color = "#0e1117"
#     text_color = "#f5f5f5"
#     card_color = "#1c1c1c"
# else:
#     bg_color = "#ffffff"
#     text_color = "#111"
#     card_color = "#f9f9f9"
#
# st.markdown(f"""
#     <style>
#     body {{
#         background-color: {bg_color};
#         color: {text_color};
#     }}
#     .title {{
#         font-size: 48px;
#         font-weight: bold;
#         text-align: center;
#         color: #e50914;
#         margin-bottom: 30px;
#         font-family: 'Trebuchet MS', sans-serif;
#     }}
#     .movie-title {{
#         font-size: 16px;
#         text-align: center;
#         font-weight: 600;
#         margin-top: 10px;
#         color: {text_color};
#     }}
#     .stImage > img {{
#         border-radius: 12px;
#         box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
#         transition: transform 0.3s ease-in-out;
#     }}
#     .stImage:hover > img {{
#         transform: scale(1.03);
#     }}
#     .card-info {{
#         background-color: {card_color};
#         border-radius: 10px;
#         padding: 8px;
#         text-align: center;
#         font-size: 14px;
#         color: {text_color};
#     }}
#     </style>
# """, unsafe_allow_html=True)
#
# # 🎬 Title
# st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
#
# # 🖼️ Fetch Poster, IMDb, and Genres
# def fetch_movie_details(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2f39568353757806f274f9a0a35ade64&language=en-US'
#     data = requests.get(url).json()
#     poster_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#     rating = data.get('vote_average', 'N/A')
#     genres = ', '.join([g['name'] for g in data.get('genres', [])])
#     return poster_url, rating, genres
#
# # 🔁 Recommendation Logic
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_data = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         title = movies.iloc[i[0]].title
#         poster, rating, genres = fetch_movie_details(movie_id)
#         recommended_data.append((title, poster, rating, genres))
#     return recommended_data
#
# # 📦 Load Data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # 🧭 Sidebar Movie Selector
# selected_movie_name = st.sidebar.selectbox('🎥 Choose a Movie:', movies['title'].values)
#
# # 🔍 Main Action
# if st.sidebar.button('🔍 Recommend'):
#     recommended = recommend(selected_movie_name)
#     cols = st.columns(5)
#     for idx, col in enumerate(cols):
#         title, poster, rating, genres = recommended[idx]
#         with col:
#             st.image(poster, use_container_width=True)
#             st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
#             st.markdown(f"<div class='card-info'>⭐ {rating} <br> 🎭 {genres}</div>", unsafe_allow_html=True)


import streamlit as st
import pickle
import pandas as pd
import requests


# Function to fetch movie poster
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6f23933d4b80b317173a4362daa88e15&language=en-US',
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"


# Function to recommend movies by content similarity
def recommend(movie, movies, similarity):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# Function to recommend movies by actor
def recommend_by_actor(actor_name, movies):
    # Find movies where this actor appears (case insensitive)
    matched_movies = movies[movies['cast'].apply(lambda cast_list: actor_name in cast_list)]

    # Limit to 5 recommendations
    recommended_movies = []
    recommended_movies_poster = []

    for idx, row in matched_movies.head(5).iterrows():
        recommended_movies.append(row.title)
        recommended_movies_poster.append(fetch_poster(row.movie_id))

    return recommended_movies, recommended_movies_poster


# Page configuration
st.set_page_config(page_title="🎥 Movie Recommender", layout="wide")

# Inject custom dark theme CSS
dark_theme = """
<style>
body {
    background-color: #0E1117;
    color: #FAFAFA;
}
.stApp {
    background-color: #0E1117;
    color: #FAFAFA;
}
.css-1d391kg, .stTextInput, .stButton>button, .stSelectbox {
    background-color: #262730;
    color: #FAFAFA;
    border: 1px solid #FAFAFA;
}
.stButton>button {
    border-radius: 8px;
}
.stMarkdown {
    color: #FAFAFA;
}
</style>
"""
st.markdown(dark_theme, unsafe_allow_html=True)

# Main title
st.title("🍿 Movie Recommendation System")
st.markdown("Get personalized recommendations based on your favorite movie 🎥✨")

# Mode selection: Normal / Actor-based
mode = st.selectbox(
    "Recommendation Mode:",
    ["Standard (Content-based)", "Actor-enhanced (Cast-based Boost)"]
)

# Load selected data and similarity matrix based on mode
if mode == "Standard (Content-based)":
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
else:
    movies_dict = pickle.load(open('movie_dict_with_actors.pkl', 'rb'))
    similarity = pickle.load(open('similarity_with_actors.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

# Full-width search selectbox and button
col_search = st.columns([6, 1])

with col_search[0]:
    if mode == "Standard (Content-based)":
        selected_item = st.selectbox(
            "Select a movie to get recommendations:",
            movies['title'].values,
            label_visibility="collapsed"
        )
    else:
        # Extract unique actors from 'cast' column (list of lists)
        all_actors = set(actor for cast_list in movies['cast'] for actor in cast_list)
        selected_item = st.selectbox(
            "Select an actor to get recommendations:",
            sorted(all_actors),
            label_visibility="collapsed"
        )

with col_search[1]:
    recommend_clicked = st.button("🎲 Recommend")

# Display recommendations horizontally
if recommend_clicked:
    if mode == "Standard (Content-based)":
        names, posters = recommend(selected_item, movies, similarity)
        st.subheader(f"🎞 Recommended for *'{selected_item}'*")
    else:
        names, posters = recommend_by_actor(selected_item, movies)
        st.subheader(f"🎭 Movies featuring *{selected_item}*")

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if idx < len(names):
            with col:
                st.image(posters[idx], use_container_width=True)
                st.markdown(f"<h4 style='text-align: center; color: #FAFAFA'>{names[idx]}</h4>", unsafe_allow_html=True)
else:
    st.markdown("👉 Select an option and hit *Recommend* to get suggestions!")

# Footer
st.markdown("""
<hr style='border: 1px solid #333;'>
<small style='color: #888;'>💡 Built with Streamlit and TMDb API</small>
""", unsafe_allow_html=True)