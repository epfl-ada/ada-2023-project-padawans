import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pydeck as pdk
import html
import plotly.graph_objs as go
import json
from pathlib import Path


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

    with open('figures/MAX_Genres_5y_barplot_withothernondisplayednew.json', 'r') as json_file:
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

    with open('figures/socio-political-themes-frequency-evolution', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)
    intro_markdown = read_markdown_file("figures/igor.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

def social_and_demographic_groups():
    st.header('Part 3:  Representation of Social and Demographic Groups')
    st.write('Here you can display different data visualizations.')
    def read_markdown_file(markdown_file):
        return Path(markdown_file).read_text()
    
    intro_markdown = read_markdown_file("figures/richard1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation0.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    #intro_markdown = read_markdown_file("figures/richard2.md")
    #st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation1.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard3.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/ethnicity-representation_significance.json', 'r') as json_file:
        fig_json = json.load(json_file)
    #fig = go.Figure(fig_json)
    #st.plotly_chart(fig)
    
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

    with open('figures/ethnicity-representation_us_bias.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    st.plotly_chart(fig)

    intro_markdown = read_markdown_file("figures/richard7.md")
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

    st.header('Part 4:  Sentiment Analysis on plot summaries')

    intro_markdown = read_markdown_file("figures/abderrahmane1.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    intro_markdown = read_markdown_file("figures/abderrahmane2.5.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

    with open('figures/boxoffice-ratings.json', 'r') as json_file:
        fig_json = json.load(json_file)
    fig = go.Figure(fig_json)
    fig.update_layout(
                    height=900,  # Increase figure height
                    width=1000,   # Increase figure width
                    )

    st.plotly_chart(fig)
    intro_markdown = read_markdown_file("figures/abderrahmane2.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    intro_markdown = read_markdown_file("figures/abderrahmane3.5.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # Create two columns
    cols = st.columns(2)

    # Load and display the first chart in the first column
    with cols[0]:
        with open('figures/genre-emotion.json', 'r') as json_file:
            fig_json = json.load(json_file)
        fig = go.Figure(fig_json)
        st.plotly_chart(fig, use_container_width=True)

    # Load and display the second chart in the second column
    with cols[1]:
        with open('figures/genre-sentiment.json', 'r') as json_file:
            fig_json = json.load(json_file)
        fig = go.Figure(fig_json)
        st.plotly_chart(fig, use_container_width=True)

    intro_markdown = read_markdown_file("figures/abderrahmane3.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)


    intro_markdown = read_markdown_file("figures/abderrahmane4.5.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    # Create two columns
    cols = st.columns(2)

    # Load and display the first chart in the first column
    with cols[0]:
        with open('figures/time-emotion.json', 'r') as json_file:
            fig_json = json.load(json_file)
        fig = go.Figure(fig_json)
        fig.update_layout(
                    height=400,  # Increase figure height
                    width=1000,   # Increase figure width
                    )
        st.plotly_chart(fig, use_container_width=True)

    # Load and display the second chart in the second column
    with cols[1]:
        with open('figures/time-sentiment.json', 'r') as json_file:
            fig_json = json.load(json_file)
        fig = go.Figure(fig_json)
        fig.update_layout(
                height=400,  # Increase figure height
                width=1000,   # Increase figure width
            )
        st.plotly_chart(fig, use_container_width=True)

    intro_markdown = read_markdown_file("figures/abderrahmane4.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    
    intro_markdown = read_markdown_file("figures/abderrahmane5.5.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)
    json_filenames = [
    'figures/genre-emotion_war_Afghanistan.json',
    'figures/genre-emotion_war_Cold War.json',
    'figures/genre-emotion_war_Iraq.json',
    'figures/genre-emotion_war_Nazi.json',
    'figures/genre-emotion_war_Vietnam.json',
    'figures/genre-emotion_war_World War 2.json'
    ]

    for i in range(0, len(json_filenames), 2):
        cols = st.columns(2)  # Create two columns

        for j in range(2):
            if i + j < len(json_filenames):
                with cols[j]:
                    with open(json_filenames[i + j], 'r') as json_file:
                        fig_json = json.load(json_file)
                    fig = go.Figure(fig_json)

                    # Modify the figure layout
                    fig.update_layout(
                        height=900,  # Increase figure height
                        width=1500,   # Increase figure width
                        legend=dict(
                            font=dict(size=10),  # Decrease legend font size
                            yanchor="top",
                            y=0.99,
                            xanchor="left",
                            x=0.01
                        ),
                        title=dict(
                            font=dict(size=14)  # Increase title font size
                        ),
                        xaxis=dict(
                            title_font=dict(size=10)  # Increase x-axis title font size
                        ),
                        yaxis=dict(
                            title_font=dict(size=10)  # Increase y-axis title font size
                        )
                    )

                    # Increase the font size of the subplot titles (annotations)
                    for annotation in fig.layout.annotations:
                        annotation.font.size = 8  # Update this number to your preferred font size

                    # Render the plot in Streamlit
                    st.plotly_chart(fig, use_container_width=True)
    intro_markdown = read_markdown_file("figures/abderrahmane5.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)

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
    st.set_page_config(layout="wide")

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
