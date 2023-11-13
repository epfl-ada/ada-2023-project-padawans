import pandas as pd
import numpy as np


def processing():
    # Load the CSV files into pandas DataFrames
    rating = pd.read_csv('data/ratings.csv')
    links = pd.read_csv('data/links.csv')
    movies = pd.read_csv('data/movies_metadata.csv')

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


    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv('data/merged_file.csv', index=False)



def main():
    # Call your functions with appropriate file names
    processing()

if __name__ == "__main__":
    main()