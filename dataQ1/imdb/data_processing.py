import pandas as pd
import numpy as np


def processing():
    #downloasd links: https://datasets.imdbws.com/title.akas.tsv.gz and https://datasets.imdbws.com/title.ratings.tsv.gz
    # Load the CSV files into pandas DataFrames
    rating = pd.read_csv("imdbratings.tsv", sep='\t')
   
    titles = pd.read_csv('titleimdb.tsv', sep='\t')

    # Group by 'id' and calculate the average rating for each group
    #average_ratings = rating.groupby('movieId')['rating'].agg(np.nanmean).reset_index()

    def strip(text):
        return str(text).replace('tt', '')

    # Merge DataFrames on the "id" column
    titles.rename(columns={'titleId': 'tconst'}, inplace=True)
    merged_df = pd.merge(rating, titles, on='tconst', how='outer')
    #merged_df.rename(columns={'movieId': 'movieId'}, inplace=True)
    #merged_df.movieId = merged_df['movieId']
    # Change types
    #merged_df['movieId'] = merged_df['movieId'].astype(str)
    #titles['movieId'] = titles['movieId'].apply(strip).astype(str)
    #titles = titles.astype(str)

    #merged_df = pd.merge(merged_df, titles, on='movieId', how='inner')


    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv('merged_file_imdb.csv', index=False)



def main():
    # Call your functions with appropriate file names
    processing()

if __name__ == "__main__":
    main()