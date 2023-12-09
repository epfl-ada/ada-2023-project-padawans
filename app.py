import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pydeck as pdk

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


def introduction():
    st.markdown("""
    # Introduction
    Welcome to this Streamlit app. This is a basic demonstration of a multi-section interactive app.
    """)

def overview():
    st.header('Part 1: Overview')
    st.write("""The "Great Dictator" directed by and starring Charlie Chaplin in 1940 is a famous movie made 
             during World War II which vehiculates critique of facism and dictatorship, an anti-war message and an iconic message for humanity. 
             This movie is a great example amongst many which show clearly how movies can be used as a medium for social and political commentary, 
             influencing public opinion and bringing attention to critical global issues. In this project, we want to investigate the extent to 
             which movies serve as mirrors to the social and political climate of the twentieth century.""")
    col1, col2, col3 = st.columns(3)
    # Three columns with different widths
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('giphy.gif', width=480, use_column_width=True)
    #st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
    st.map(data)


def data_exploration():
    st.header('Part 2: Data Exploration')
    st.write('In this section, you would typically include widgets for data exploration.')

def visualizations():
    st.header('Part 3: Visualizations')
    st.write('Here you can display different data visualizations.')

def sentiment():
    st.header('Sentiment')
    st.write('This part might include more in-depth analysis or statistical tests.')

def conclusions():
    st.header('Part 5: Conclusions')
    st.write('The final section where you summarize the findings and conclusions of the app.')

def main():
    st.title('My Streamlit App')

    #Options Menu
    with st.sidebar:
        selected = option_menu('Nav', ['Overview','Data Exploration', 'Sentiment', 'Conclusions'], 
            icons=['0-square-fill','1-square-fill','2-square-fill', '3-square-fill','4-square-fill','5-square-fill'],menu_icon='intersect', default_index=0)

    if selected == "Overview":
        overview()
    elif selected == "Data Exploration":
        data_exploration()
    elif selected == "Visualizations":
        visualizations()
    elif selected == "Sentiment":
        sentiment()
    elif selected == "Conclusions":
        conclusions()

if __name__ == "__main__":
    main()
