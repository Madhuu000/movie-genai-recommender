import streamlit as st
from recommender import recommend_movies
from genai_helper import generate_explanation

st.title("🎬 GenAI Movie Recommendation Assistant")

st.write("Get movie recommendations with AI explanations!")

movie_name = st.text_input("Enter a movie you like:")

if st.button("Recommend"):

    if movie_name:

        recommendations = recommend_movies(movie_name)

        st.subheader("🎥 Recommended Movies")
        for movie in recommendations:
            st.write("✅", movie)

        if "Movie not found" not in recommendations:
            explanation = generate_explanation(movie_name, recommendations)

            st.subheader("🤖 AI Explanation")
            st.write(explanation)