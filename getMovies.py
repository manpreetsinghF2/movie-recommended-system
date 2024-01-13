import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

tfidf = TfidfVectorizer(stop_words='english')

df1=pd.read_csv('datasets/tmdb_5000_credits.csv')
df2=pd.read_csv('datasets/tmdb_5000_movies.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')

df2.loc[:, 'genres'] = df2.genres.apply(lambda x: ",".join(i.get('name') for i in literal_eval(x)))

C= df2['vote_average'].mean()
m= df2['vote_count'].quantile(0.9)

def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return (v/(v+m) * R) + (m/(m+v) * C)

def getTrendingMovies(froms):
    if froms == 'all':
         df = df2
    if froms == 'action':
         df = df2[df2.genres.apply(lambda x: 'action' in x.lower())]
    q_movies = df.copy().loc[df2['vote_count'] >= m]

    # Define a new feature 'score' and calculate its value with `weighted_rating()`
    q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

    #Sort movies based on score calculated above
    q_movies = q_movies.sort_values('score', ascending=False)

    #Print the top 15 movies
    return q_movies[['title', 'vote_count', 'vote_average', 'score', 'tagline']].head(10)


def getPopularMovies():
    pop= df2.sort_values('popularity', ascending=False)
    return pop.head(10)

def getContentRecommend(movie):
     try:
          df = pd.DataFrame()
          if ((df2.original_title.str.lower() == movie.lower()).any()):
               df = pd.concat((df, df2[df2.original_title == movie][['title', 'tagline']]), axis = 0)
          df2['overview'] = df2['overview'].fillna('')

          #Construct the required TF-IDF matrix by fitting and transforming the data
          tfidf_matrix = tfidf.fit_transform(df2['overview'])

          cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
          indices = pd.Series(df2.index, index=df2['title'].str.lower()).drop_duplicates()
     # Get the index of the movie that matches the title
          idx = indices[movie]

          # Get the pairwsie similarity scores of all movies with that movie
          sim_scores = list(enumerate(cosine_sim[idx]))

          # Sort the movies based on the similarity scores
          sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

          # Get the scores of the 10 most similar movies
          sim_scores = sim_scores[1:11]

          # Get the movie indices
          movie_indices = [i[0] for i in sim_scores]

          # Return the top 10 most similar movies
          return pd.concat([df, df2.loc[movie_indices, ['title', 'tagline']]], axis = 0)
     except Exception as e:
          print(e)
          return False