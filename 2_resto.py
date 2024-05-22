import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import folium
import openrouteservice
import base64
import os
import requests
import pandas as pd
import numpy as np
import time
from pprint import pprint
from tqdm import tqdm
from streamlit_folium import st_folium

restoclick = pd.read_csv(r"hdquoh.csv",sep=",")



#------------------------------------------------------------------------------------
#                               Style
#------------------------------------------------------------------------------------



st.markdown(
    """
    <style>
        .st-emotion-cache-vk3wp9 {
            min-width: 0; 
            max-width: 0;
            visibility: hidden;
            
        }
        p{
            list-style-type: none; 
            padding: 0;
            text-align: center;
        }
        .st-emotion-cache-vk3wp9 eczjsme11 {
            width: 0;
            
        }
        .st-emotion-cache-1r4qj8v {
            text-align: center;
        }
        .st-emotion-cache-10trblm {
            text-align: center;
        }

    </style>
    """,
    unsafe_allow_html=True
)

def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def image(image_base64, picture_texte,width=100,height=100):
    return f"""
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    """
    
image_dir = "picture"

st.title(f"{restoclick['restaurant_name'].iloc[0]}")

image_path = os.path.join(image_dir, "salad_resto.png")
image_base64 = load_image_as_base64(image_path)
st.markdown(image(image_base64,"salad_resto", width=400 , height=400), unsafe_allow_html=True)
st.title(" ")

st.subheader("Ouverture ")
st.write("Lun - Mar- Mer - Jeu - Ven - Sa - Dim")
st.write("12h - 15 h / 18h - 21h")
st.title(" ")


acces, infos = st.columns(2)

with acces:
    st.subheader("Accécibilité")
    vide ,no_sound, disabled, hide, vide  = st.columns(5)

    with no_sound:
        image_path = os.path.join(image_dir, "no-sound.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "no-sound",30,30), unsafe_allow_html=True)
    with disabled:
        image_path = os.path.join(image_dir, "disabled.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "disabled",30,30), unsafe_allow_html=True)
    with hide:
        image_path = os.path.join(image_dir, "hide.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "hide",30,30), unsafe_allow_html=True)

with infos:
    st.subheader("Infos pratiques")
    vide ,wifi, card, terasse, vide  = st.columns(5)
    with wifi:
        image_path = os.path.join(image_dir, "wifi.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "wifi",30,30), unsafe_allow_html=True)
    with card:
        image_path = os.path.join(image_dir, "card.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "card",30,30), unsafe_allow_html=True)
    with terasse:
        image_path = os.path.join(image_dir, "terasse.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "terasse",30,30), unsafe_allow_html=True)

st.title(" ")
st.subheader("Spécial Diet")

vide ,halal, kosher, vegan, gluten, vide  = st.columns(6)
with halal:
    image_path = os.path.join(image_dir, "halal.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(image(image_base64, "halal",30,30), unsafe_allow_html=True)
with kosher:
    image_path = os.path.join(image_dir, "kosher.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(image(image_base64, "kosher",30,30), unsafe_allow_html=True)
with vegan:
    image_path = os.path.join(image_dir, "vegan.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(image(image_base64, "vegan",30,30), unsafe_allow_html=True)
with gluten:
    image_path = os.path.join(image_dir, "gluten.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(image(image_base64, "gluten",30,30), unsafe_allow_html=True)
st.title(" ")

#------------------------------------------------------------------------------------
#                               Emplacement du resto
#------------------------------------------------------------------------------------

# Créer un client OpenRouteService en spécifiant votre clé API
api_key = '5b3ce3597851110001cf6248302d9fcb8b44439aa282335994a41406'
client = openrouteservice.Client(key=api_key)

# Adresse à géolocaliser // donné par le client
adresse = "44 Rue Alphonse Penaud, 75020 Paris"          # Ce format est obligatoire (risque de ne pas trouver le point)

# Géolocalisation de l'adresse
response = client.pelias_search(adresse)

# Extrait des coordonnées géographiques si une réponse est disponible
if response['features']:
    location = response['features'][0]['geometry']['coordinates']
    latitude_client, longitude_client = location[1], location[0]
    print("Latitude:", latitude_client)
    print("Longitude:", longitude_client)
else:
    print("Adresse introuvable.")


# Points de départ et d'arrivée
start_coords = (longitude_client,latitude_client)  # Coordonnées du point de départ (longitude, latitude)

#Mettre les coordonnées de l'adresse du restaurant
end_coords = (float(restoclick['longitude'].iloc[0]), float(restoclick['latitude'].iloc[0]))  # Coordonnées du point d'arrivée (longitude, latitude)

# Obtenir un itinéraire
route = client.directions(  coordinates=[start_coords, end_coords],
    profile='foot-walking',
    format='geojson'
)

adresse_client = (latitude_client, longitude_client)

# Afficher la réponse brute pour vérification (facultatif)
#print(route)

# Extraire les coordonnées de l'itinéraire
route_coords = route['features'][0]['geometry']['coordinates']
route_coords = [(coord[1], coord[0]) for coord in route_coords]  # Inverser latitude et longitude

# Créer une carte centrée sur le point de départ
m_trajet = folium.Map(location=[start_coords[1], start_coords[0]], zoom_start=13, tiles ="Cartodb Positron")

# Ajouter un marqueur pour le point de départ
folium.Marker(
    location= adresse_client,
    popup= folium.Popup('Vous'),
    icon=folium.CustomIcon('https://cdn-icons-png.flaticon.com/512/3537/3537838.png',
                           icon_size=(30, 30))
).add_to(m_trajet)

# Ajouter un marqueur pour le point d'arrivée
folium.Marker(
    location=[end_coords[1], end_coords[0]],
    popup=folium.Popup(restoclick["restaurant_name"]),
    icon=folium.CustomIcon('https://cdn-icons-png.flaticon.com/512/3448/3448609.png', # Remplacer le lien par celui de l'icone (fonctionne avec les fichiers locaux)
                           icon_size=(30, 30))
).add_to(m_trajet)

# Ajouter l'itinéraire à la carte
folium.PolyLine(
    route_coords,
    color='blue',
    weight=5,
    opacity=0.7
).add_to(m_trajet)


# Afficher un aperçu de la carte (uniquement si vous êtes dans un environnement Jupyter)
st_folium(m_trajet, width=700, height=500)
