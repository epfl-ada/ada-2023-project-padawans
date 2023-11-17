import pandas as pd
import numpy as np
import spacy



def processing():
    df_plot_summaries = pd.read_csv('data/MovieSummaries/plot_summaries.txt', sep='\t', names = ['WikipediaMovieID', 'PlotSummaries'], index_col = ['WikipediaMovieID'])
    """    df_character = pd.read_csv("MovieSummaries/character.metadata.tsv", sep='\t', names = ['WikipediaMovieID', 'FreebaseMovieID', 'MovieReleaseDate', 'CharacterName', 
                                                                        'ActorDateOfBirth', 'ActorGender', 'ActorHeight', 'ActorEthnicity', 
                                                                        'ActorName', 'ActorAgeAtMovieRelease','FreebaseCharacter', 
                                                                        'FreebaseCharacterID', 'FreebaseActorID'], index_col = ['WikipediaMovieID'])"""
    df_movies = pd.read_csv("data/MovieSummaries/movie.metadata.tsv", sep='\t', header = None, names = ['WikipediaMovieID', 'FreebaseMovieID', 'MovieName', 
                                                                                        'MovieReleaseDate', 'MovieBoxOfficeRevenue',
                                                                                        'MovieRuntime', 'MovieLanguages', 'MovieCountries',
                                                                                        'MovieGenres'], index_col = ['WikipediaMovieID'])


    df_movies['MovieReleaseDate'] = df_movies['MovieReleaseDate'].str.extract(r'^(.{4})')
    df_movies = df_movies.dropna(subset='MovieReleaseDate')
    df_movies['MovieReleaseDate'] = df_movies['MovieReleaseDate'].astype("Int64")
    df_movies = df_movies[df_movies.MovieReleaseDate >= 1800]
    df_movies = pd.merge(df_movies, df_plot_summaries, how='left', on ='WikipediaMovieID')


    # Load the CSV files into pandas DataFrames
    rating = pd.read_csv('data/KaggleMovies/ratings.csv')
    links = pd.read_csv('data/KaggleMovies/links.csv')
    movies = pd.read_csv('data/KaggleMovies/movies_metadata.csv', low_memory=False)


    # Load spaCy model with disabled components for efficiency
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

    # Pre-compile the list of stop words for faster checking
    stop_words = nlp.Defaults.stop_words

    # Function to check if token should be included
    def is_token_allowed(token):
        return not token.is_punct and token.pos_ in ["ADJ", "PROPN", "NOUN"] and token.text.lower() not in stop_words

    # Function to preprocess token
    def preprocess_token(token):
        return token.lemma_.strip().lower()

    def process_text(summary):
        # Ensure the text is treated as a writable string
        doc = nlp(summary)
        # Convert the processed tokens to strings to avoid any complex types
        return [preprocess_token(token) for token in doc if is_token_allowed(token)]

    # Group by 'id' and calculate the average rating for each group
    average_ratings = rating.groupby('movieId')['rating'].agg(np.nanmean).reset_index()

    def strip(text):
        return str(text).replace('tt', '')

    # Merge DataFrames on the "id" column
    merged_df = pd.merge(average_ratings, links, on='movieId', how='outer')
    merged_df.rename(columns={'imdbId': 'imdb_id'}, inplace=True)
    merged_df.imdb_id = merged_df['imdb_id']
    # Change types

    merged_df['imdb_id'] = merged_df['imdb_id'].astype(str)
    movies['imdb_id'] = movies['imdb_id'].apply(strip).astype(str)
    movies = movies.astype(str)

    merged_df = pd.merge(merged_df, movies, on='imdb_id', how='inner')

    #df_plot_summaries['tokens']= df_plot_summaries['Summary'].apply(process_text)

    #pd.merge(merged_df, df_plot_summaries, on='Wikipedia_ID', how='left')

    merged_df.release_date = pd.to_datetime(merged_df.release_date, errors='coerce')

    # Now extract the year
    merged_df.release_date = merged_df.release_date.dt.year.astype("Int64")
    merged_df.release_date


    columns = ['FreebaseMovieID', 'original_title', 'release_date',
        'MovieBoxOfficeRevenue', 'MovieRuntime', 'MovieLanguages',
        'MovieCountries', 'MovieGenres', 'PlotSummaries']
    df_movies.columns = columns


    merged_df = pd.merge(merged_df, df_movies, how= 'outer', on =['original_title', 'release_date'])
    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv('data/merged_file.csv',index=None)


def main():
    # Call your functions with appropriate file names
    processing()

if __name__ == "__main__":
    main()
