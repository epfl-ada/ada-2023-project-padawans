import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pydeck as pdk
import html
import plotly.graph_objs as go
import json
from pathlib import Path

# DataFrame with latitude, longitude, and some additional data
data = pd.DataFrame({
    'lat': [46.2044, 47.3769],
    'lon': [6.1432, 8.5417],
    'label': ['Geneva', 'Zurich']
})

# Create a pydeck Layer
layer = pdk.Layer(
    'ScatterplotLayer',
    data,
    get_position='[lon, lat]',
    get_radius=20000,  # Radius in meters
    get_color=[0, 0, 255],  # RGB color value
)

# Set the viewport location
view_state = pdk.ViewState(
    latitude=47.0,
    longitude=8.3,
    zoom=7,
    pitch=0
)

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def overview():
    st.header('Part 1: Overview')
    st.write("""Imagine a world where cinema does more than entertain; it shapes the course of history. In 1982, the release of "Gandhi," directed by Richard Attenborough, became not just a cinematic event but a cultural phenomenon. As the film brought to life the struggles and philosophies of Mahatma Gandhi, it reignited a conversation about non-violence and civil rights across the globe. In South Africa, it reportedly influenced movements against apartheid, demonstrating the profound effect a film can have on the socio-political landscape.

This is not an isolated instance. Throughout the twentieth century, numerous films have echoed the sentiments of their times, influenced public opinion, and even swayed the course of political events. From the bold anti-fascist statement in Charlie Chaplin’s "The Great Dictator" to the nuanced portrayal of the Vietnam War in "Apocalypse Now," cinema has been a powerful medium for socio-political commentary and change.""")
    col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('giphy.gif', width=480, use_column_width=True)
    st.write("""In this project, we delve into the rich interplay between cinema and the socio-political fabric of the twentieth century. We aim to uncover how films have reflected, influenced, and sometimes even transformed the socio-political climate of their times. Through a blend of analytical rigor and narrative exploration, we will journey through the following facets:

Analysis of Socio-Political Themes: Identifying and understanding the prevalent socio-political themes in cinema.

Correlation Analysis of Genres and Socio-Political Events: Exploring the relationship between film genres and major socio-political events.

Representation of Social and Demographic Groups: Examining the portrayal of diverse groups in films against the backdrop of socio-political change.

Sentiment Analysis: Assessing public perception and emotional responses to socio-political themes in movies.

Ratings Analysis of Socio-Political Themed Movies: Evaluating audience and critic reception of films with socio-political themes.

Our journey will conclude with a synthesis of these findings, revealing the powerful role cinema has played as both a reflector and an influencer of socio-political narratives. Join us as we unravel the stories behind the screen, uncovering the hidden dialogues between cinema and society.""")
    st.map(data)


def correlation_analysis():
    st.header('Part 2: Data Exploration')

    with open('figures/release_year_histo_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/boxoffice_percentage_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/top10_release_histo.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/barplot_genres_fix_wo_other.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/genre_evolution_linechart_dynamic_with_other_max.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/genre_evolution_barplot_dynamic_with_other_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/boxofficeshare_genre_total_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig, width=1500)

    with open('figures/boxofficeshare_genre_top10fix_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig, width=1500)
    st.write('In this section, you would typically include widgets for data exploration.')

def socio_political():
    st.header('Part 2:  Analysis of Socio-Political Theme')
    st.write('Here you can display different data visualizations.')
    st.image('figures/igor-1.png', width=700, use_column_width=True)
    st.image('figures/igor-2.png', width=700, use_column_width=True)
    st.image('figures/igor-3.png', width=700, use_column_width=True)

    def read_markdown_file(markdown_file):
        return Path(markdown_file).read_text()

    intro_markdown = read_markdown_file("figures/igor.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

def social_and_demographic_groups():
    st.header('Part 3:  Representation of Social and Demographic Groups')
    st.write('Here you can display different data visualizations.')

    intro_markdown = read_markdown_file("figures/richard1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation1.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)


    with open('figures/ethnicity-representation2.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard2.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation3.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)
    
    intro_markdown = read_markdown_file("figures/richard3.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation4.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard4.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation5.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    def read_markdown_file(markdown_file):
        return Path(markdown_file).read_text()

    intro_markdown = read_markdown_file("figures/richard.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

def ratings_socio_political():

    st.header('Part 5:  Ratings analysis of socio-political themed movies')    

    intro_markdown = read_markdown_file("figures/koami1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    with open('figures/bar_chart_figure.json', 'r') as json_file:
        fig_json = json.load(json_file)
    
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/koami2.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

def sentiment():
    st.header('Sentiment')
    with open('figures/boxoffice-ratings.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/genre-emotion.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/genre-sentiment.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/time-emotion.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/time-sentiment.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    st.write('This part might include more in-depth analysis or statistical tests.')

def conclusions():
    st.header('Part 5: Conclusions')
    st.write('The final section where you summarize the findings and conclusions of the app.')

def main():
    st.title('My Streamlit App')

    #Options Menu
    with st.sidebar:
        selected = option_menu('Topics', ['Overview','Correlation Analysis of Genres and Socio-Political Events', "Analysis of Socio-Political Themes", "Social and Demographic Groups", 'Sentiment', 'Ratings analysis of socio-political themed movies', 'Conclusions'], 
            icons=['0-square-fill','1-square-fill','2-square-fill', '3-square-fill','4-square-fill','5-square-fill'],menu_icon='intersect', default_index=0)

    if selected == "Overview":
        overview()
        correlation_analysis()
        socio_political()
        social_and_demographic_groups()
        sentiment()
        ratings_socio_political()
    elif selected == "Correlation Analysis of Genres and Socio-Political Events":
        correlation_analysis()
    elif selected == "Analysis of Socio-Political Themes":
        socio_political()
    elif selected == "Social and Demographic Groups":
        social_and_demographic_groups()
    elif selected == "Sentiment":
        sentiment()
    elif selected == "Ratings analysis of socio-political themed movies":
        ratings_socio_political()
    elif selected == "Conclusions":
        conclusions()

if __name__ == "__main__":
    main()
