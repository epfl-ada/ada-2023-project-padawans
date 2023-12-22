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
    st.write("""Imagine a world where cinema does more than entertain; it shapes the course of history. In 1982, the release of "Gandhi," directed by Richard Attenborough, became not just a cinematic event but a cultural phenomenon. As the movie brought to life the struggles and philosophies of Mahatma Gandhi, it reignited a conversation about non-violence and civil rights across the globe. In South Africa, it reportedly influenced movements against apartheid, demonstrating the profound effect a movie can have on the socio-political landscape.

This is not an isolated instance. Throughout the twentieth century, numerous movies have echoed the sentiments of their times, influenced public opinion, and even swayed the course of political events. From the bold anti-fascist statement in Charlie Chaplin’s "The Great Dictator" to the nuanced portrayal of the Vietnam War in "Apocalypse Now," movies have been a powerful medium for socio-political commentary and change.""")
    col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('giphy.gif', width=480, use_column_width=True)
    st.write("""In this project, we delve into the rich interplay between movies and the socio-political fabric of the twentieth century. We aim to uncover how movies have reflected, influenced, and sometimes even transformed the socio-political climate of their times. Our exploration begins with an analysis of socio-political themes, identifying and understanding the prevalent motifs in movies. We then examine the correlation between movies genres and major socio-political events, exploring how cinematic expressions respond to and influence historical contexts. The study also investigates the representation of diverse social and demographic groups in movies, reflecting the evolving societal narratives. Additionally, we assess public perception and emotional responses to socio-political themes in movies through sentiment analysis. Finally, we evaluate how audiences and critics have received films with socio-political themes, providing insight into their impact and reception.

Our journey will conclude with a synthesis of these findings, revealing the powerful role movies have played as both a reflector and an influencer of socio-political narratives. Join us as we unravel the stories behind the screen, uncovering the hidden dialogues between movies and society.""")
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
    st.write("""As the final reel of our cinematic journey winds to a close, we find ourselves not at an end, but at a profound moment of synthesis and realization. Our exploration through the lens of twentieth-century movies has unveiled a landscape rich in diversity, challenge, and change. We have seen how movies are not mere reflections of the times but also powerful catalysts that can shape and redefine the socio-political narrative.

The synthesis of our results paints a vivid tapestry. In analyzing socio-political themes, we observed the evolution of cinematic storytelling, mirroring the changing contours of societal and political concerns. From the daring satire of "The Great Dictator" to the introspective depth of "Gandhi," movies have served as barometers of public sentiment, capturing the zeitgeist of their eras.

Our correlation analysis of genres and socio-political events further highlighted how movies adapt and respond to the world's heartbeat. The flux of genres, from the rise of war dramas during global conflicts to the emergence of dystopian movies in times of political uncertainty, underscores movies's responsiveness to the human condition.

In examining the representation of social and demographic groups, we uncovered a narrative of progress and ongoing challenges. While there has been a gradual increase in diversity and representation, the journey towards a truly inclusive cinematic world remains a work in progress, reflecting wider societal struggles.

Sentiment analysis brought to light the emotional impact of socio-political themes in movies. Movies with powerful messages resonated deeply with audiences, influencing perceptions and, in many cases, spurring dialogue and action.

Finally, our ratings analysis provided insight into how socio-political themes are received and valued by audiences and critics alike. This metric offered a unique window into the public's engagement with and reaction to movies that dared to address significant socio-political issues.

In conclusion, our exploration has revealed that movies, in their most impactful moments, transcends entertainment. It becomes a conduit for change, a voice for the voiceless, and a mirror reflecting our collective hopes, fears, and aspirations. The stories told on the silver screen are more than just tales; they are fragments of our shared history and indicators of our societal trajectory.""")

    col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('movies_collage.png', width=480, use_column_width=True)

    st.write("""As we step out from this cinematic exploration, we are left with a profound appreciation for the medium's power and responsibility. Movies do not just belong to the realm of art; they are integral threads in the fabric of socio-political discourse. They challenge us, inspire us, and most importantly, remind us of the unending dialogue between art and life, movies and society.

In the flickering light of the projector, we have witnessed a world in motion, a narrative of humanity unfolding. And as the screen fades to black, we are left not only in awe but also with a newfound understanding of the indelible imprint cinema leaves on the pages of our collective history.""")

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
