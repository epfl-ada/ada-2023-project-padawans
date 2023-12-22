# Unveiling socio-political reflections in twentieth century movies

[Data Story](https://ada-2023-project-padawans-8bq993byh5h9xcgsyrauxz.streamlit.app/)

## Abstract

We want to investigate the extent to which movies serve as mirrors to the social and political climate of the twentieth century. Through a multidimensional analysis of the combined dataset of [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) and IMDB, encompassing genre trends and thematic content, we discern nuanced patterns of socio-political reflection within movies narratives. Employing advanced natural language processing techniques, we dissect plot summaries to uncover implicit and explicit references to key societal issues. Our findings illuminate the intricate interplay between movies and the evolving socio-political landscape, shedding light on the enduring impact of movies as a medium of reflection, commentary, and influence. This research not only advances our comprehension of film as a cultural artifact but also underscores its potential as a historical and sociological archive of the twentieth century.


## Research Questions:
1. How do movie genres change over time, and how do they relate to major social or political movements in the 20th and beginning of the 21st century?
2. What socio-political themes are prominent in movies across different decades, and how do they connect with historical events and cultural shifts?
3. How are different social and demographic groups represented in films, and how does this representation evolve over time?
4. Are there patterns in movie plot summaries that correlate with significant social or political events of their respective time periods?
5. How does the critical reception and recognition of movies with explicit socio-political content compare to those focused on entertainment or aesthetics?



## Methods:
- **Data Preparation and Datasets:**
  - Evaluate the extent of missing data in relevant movie information (genres, release date, box office revenue, rating, etc.).
  - Address the high proportion of missing box office data by incorporating additional datasets from the TMDb API.
  - Clean and insert socio-political key events into the movie information dataframe.
  - Datasets: CMU datset + IMDB dataset + Movie Lense 25M
- **Time Period Selection:**
  - Focus on the years 1900 to 2010 within the 20th and beginning of the 21st century.

- **For Q1 - Correlation Analysis of Genres and Socio-Political Events:**
(To be able to vizualize this section you need plotly)
  - Plot the number and percentage of movies per genre and per year.
  - Visualize the evolution of genres over time (e.g., using bar plots, line plots) to identify trends.
  - Visualize the box office shares of movie genres over time.
  - Perform correlation analysis to explore connections between genres.
  - Perform regression analysis to identify which genres can explain the boxoffice or ratings of a movie and see the evolution of genre coefficients through time.

- **For Q2 - Analysis of Socio-Political Themes:**
  - Analyze movie plots using NLP or similarity search to identify occurrences of defined socio-political themes.
  - Apply topic modeling techniques (LDA, NMF) to identify key themes within plot summaries.
  - Group data by decades and count the frequency of each socio-political theme within each decade.
  - Create comparison visualizations of socio-political themes across decades and historical key events.

- **For Q3 - Representation of Social and Demographic Groups:**
(To be able to vizualize this section you need plotly)
  - Analyze how the representation of various social groups changes over time.
  - Visualize changes in representation for each social group.
  - Explore correlations between representation changes and key socio-political events.

- **For Q4 - Sentiment Analysis:**
  - Preprocess plot summaries (cleaning and tokenization).
  - Analyze sentiment in plot summaries (positive, negative, or neutral) using libraries like TextBlob, NLTK, or VADER.
  - Apply topic modeling techniques (e.g., LDA, NMF) to identify key themes within plot summaries.
  - Analyze sentiment trends over time.
  - Investigate correlations between identified themes and sentiment.
- **For Q5 - Ratings analysis of socio-political themed movies**:
  - Define keywords associated with socio-political themes
  - Check if any of the socio-political keywords appear in the plot summary and genres.
  - Compare the average ratings of movies in both categories.
  - Analyze how the critical reception of movies in these categories has changed over time
  - Conduct statistical tests (like t-tests or ANOVA) to see if there are significant differences in ratings between the two categories.

## Proposed Timeline
  1. Step 1 - Answer to the five questions and give enough proofs (eg. plots, stats, etc...) One question per person
  2. Step 2 - Merge all findings and create a story out of them, and go deeper if an interesting thing is found
  3. Step 3 - Create the website and add the story

* Step 1 - 17.11 to 24.11
* Step 2 - 24.11 to 01.12
* Step 3 - 01.11 to 08.12

## Organisation within the team

Although we organised the work so that each person works on one research question, the work in general was done in group
- Maxime Chanson : Correlation Analysis of Genres and Socio-Political Events
- Igor Jomaron : Analysis of Socio-Political Themes
- Richard Gabriel Chiu : Representation of Social and Demographic Groups
- Abdherramane Ould Bay : Sentiment Analysis
- Koami Gafan : Ratings analysis of socio-political themed movies
