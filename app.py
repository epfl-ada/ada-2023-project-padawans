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
    intro_markdown = read_markdown_file("figures/intro1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('giphy.gif', width=480, use_column_width=True)
    intro_markdown = read_markdown_file("figures/intro2.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    st.map(data)

def correlation_analysis():
    st.header('Part 2: Data Exploration')

    text = read_markdown_file("figures/MAX_1 - Copie.md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/Crelease_year_histo_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (2).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/Dtop10_release_histo.json', 'r') as json_file:
        fig_json = json.load(json_file)
        fig = go.Figure(fig_json)
        st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (3).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/MAX_Genres_5y_barplot_withothernondisplayed.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (4).md")
    st.markdown(text, unsafe_allow_html=True)
    

    with open('figures/boxoffice_percentage_max.json', 'r') as json_file:
        fig_json = json.load(json_file)

    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (5).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/MAX_Fboxofficeshare_genre_total_max.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (6).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/MAx_scatter_boxoffice_vs_ratingbruh.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (7).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/Max_boxoffice_vs_year.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (8).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/Max_reg.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/Max_r2_reg.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (9).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/Max_reg_rating.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    with open('figures/Max_r2_reg_rating.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (10).md")
    st.markdown(text, unsafe_allow_html=True)

    with open('figures/Gcorrelplot_max.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    text = read_markdown_file("figures/MAX_1 - Copie (11).md")
    st.markdown(text, unsafe_allow_html=True)

    text = read_markdown_file("figures/MAX_1 - Copie (12).md")
    st.markdown(text, unsafe_allow_html=True)

    text = read_markdown_file("figures/MAX_1 - Copie (13).md")
    st.markdown(text, unsafe_allow_html=True)
    


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

    with open('figures/ethnicity-representation0.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard2.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation1.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard3.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation_significance.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)
    
    intro_markdown = read_markdown_file("figures/richard4.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation_AlliesEnemies.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard5.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation_reaction_speed.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard6.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)


def ratings_socio_political():

    st.header('Part 5:  Ratings analysis of socio-political themed movies')    

    intro_markdown = read_markdown_file("figures/koami1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    with open('figures/bar_chart_figure.json', 'r') as json_file:
        fig_json = json.load(json_file)
    
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/koami3.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    with open('figures/bar_emotions_figure.json', 'r') as json_file2:
        fig2_json = json.load(json_file2)
    
    fig2 = go.Figure(fig2_json)
    st.plotly_chart(fig2)
    
    intro_markdown = read_markdown_file("figures/koami4.md")
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
    intro_markdown = read_markdown_file("figures/conclusion1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('movies_collage.png', width=480, use_column_width=True)

    intro_markdown = read_markdown_file("figures/conclusion2.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

def main():
    st.title('My Streamlit App')

    #Options Menu
    with st.sidebar:
        selected = option_menu('Topics', ['Overview','Data Exploration', "Analysis of Socio-Political Themes", "Social and Demographic Groups", 'Sentiment', 'Ratings analysis of socio-political themed movies', 'Conclusions'], 
            icons=['0-square-fill','1-square-fill','2-square-fill', '3-square-fill','4-square-fill','5-square-fill'],menu_icon='intersect', default_index=0)

    if selected == "Overview":
        overview()
        correlation_analysis()
        socio_political()
        social_and_demographic_groups()
        sentiment()
        ratings_socio_political()
    elif selected == "Data Exploration":
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
