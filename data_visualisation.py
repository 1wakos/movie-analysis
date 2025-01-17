from movies_data import Movies
import pandas as pd
import matplotlib.pyplot as plt

def create_movie_table(data):
    movies = data['results']
    movie_list = []
    
    for movie in movies:
        movie_list.append({
            'Title': movie['title'],
            'Rating': round(movie.get('vote_average', 0),2),
            'Release Date': movie['release_date'],
        })
    
    df = pd.DataFrame(movie_list)
    return df

def top3_reviews_table(data):
    df = pd.DataFrame(data)
    return df

def plot_movie_ratings(df):
    plt.figure(figsize=(10, 6))
    plt.barh(df['Title'], df['Rating'], color='maroon')
    plt.xlabel('Rating')
    plt.title('Popular Movies Ratings')
    plt.show()