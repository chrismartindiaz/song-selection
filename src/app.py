import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo de predicción de 'mood'
lr_model = joblib.load('modelo_lr_mood.pkl')

# Cargar el modelo de predicción de 'motivation'
LinearSVC_model = joblib.load('modelo_linearSVC_motivation.pkl')

# Cargar el DataFrame de canciones procesadas
processed_songs = pd.read_csv('processed_songs_full.csv')

# Interfaz de usuario con Streamlit
st.title("¡Sorpréndeme con una canción!")

# Selección de ánimo (mood)
mood_options = {'Tristeza': 0, 'Felicidad': 1}
selected_mood = st.radio("¿Qué ánimo te representa más hoy?", list(mood_options.keys()))

# Selección de motivación (motivation)
motivation_options = {'Relax': 0, 'Energía': 1}
selected_motivation = st.radio("¿Prefieres motivarte o estar más tranquilo?", list(motivation_options.keys()))

# Selección de década (release_decade)
decade_options = ['1980s', '1990s', '2000s', '2010s', '2020s']
selected_decade = st.selectbox("¿Con qué década te encuentras más familiarizado?", decade_options)

# Botón para sorprender
if st.button("¡Sorpréndeme!"):
    # Filtrar el DataFrame con las selecciones del usuario
    filtered_songs = processed_songs[
        (processed_songs['mood'] == mood_options[selected_mood]) &
        (processed_songs['motivation'] == motivation_options[selected_motivation]) &
        (processed_songs['release_decade'] == selected_decade)
    ]

    # Mostrar 3 canciones que cumplen con las características
    if len(filtered_songs) >= 3:
        selected_songs = filtered_songs.sample(3)
        st.write("¡Aquí tienes tres canciones que podrían sorprenderte!")
        st.write(selected_songs[['id']])
    else:
        st.write("Lo siento, no hay suficientes canciones que cumplan con esas características.")

# Nota: Asegúrate de adaptar los nombres de las columnas y modelos según tus archivos y datos.
