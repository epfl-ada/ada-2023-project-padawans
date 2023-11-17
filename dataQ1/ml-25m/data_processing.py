import pandas as pd
import numpy as np


def processing():
    #download link: https://files.grouplens.org/datasets/movielens/ml-25m.zip
    # Load the CSV files into pandas DataFrames
    rating = pd.read_csv("ratings.csv")
    links = pd.read_csv('links.csv')
    movies = pd.read_csv('movies.csv')

    # Group by 'id' and calculate the average rating for each group
    average_ratings = rating.groupby('movieId')['rating'].agg(np.nanmean).reset_index()

    def strip(text):
        return str(text).replace('tt', '')

    # Merge DataFrames on the "id" column
    merged_df = pd.merge(average_ratings, links, on='movieId', how='outer')
    #merged_df.rename(columns={'movieId': 'movieId'}, inplace=True)
    merged_df.movieId = merged_df['movieId']
    # Change types
    merged_df['movieId'] = merged_df['movieId'].astype(str)
    movies['movieId'] = movies['movieId'].apply(strip).astype(str)
    movies = movies.astype(str)

    merged_df = pd.merge(merged_df, movies, on='movieId', how='inner')


    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv('merged_file_ml_25m.csv', index=False)



def main():
    # Call your functions with appropriate file names
    processing()

if __name__ == "__main__":
    main()