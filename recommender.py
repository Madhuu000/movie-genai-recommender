import pandas as pd

# Load datasets
movies = pd.read_csv("data//movies.csv")
ratings = pd.read_csv("data//ratings.csv")

# Merge datasets using movieId
data = pd.merge(ratings, movies, on="movieId")

# Create user-movie rating matrix
user_movie_matrix = data.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

# Calculate similarity between movies
movie_similarity = user_movie_matrix.corr()

def recommend_movies(movie_name, n=5):

    if movie_name not in movie_similarity.columns:
        return ["Movie not found"]

    similar_movies = (
        movie_similarity[movie_name]
        .sort_values(ascending=False)
        .iloc[1:n+1]
    )

    return list(similar_movies.index)