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


tripadvisor_restos = pd.read_csv(r"tripadvisor_restos.csv", sep=";")
def rating(note):
    return "⭐️" if 0 < note <= 2 else "⭐️⭐️" if 2 < note <= 3 else "⭐️⭐️⭐️" if 3 < note <= 4 else "⭐️⭐️⭐️⭐️" if 4 < note <= 5 else "⭐️⭐️⭐️⭐️⭐️"


#------------------------------------------------------------------------------------
#                               Style
#------------------------------------------------------------------------------------

st.markdown(
    """
    <style>
        .st-emotion-cache-vk3wp9 {
            visibility: hidden;
            min-width: 0; 
            max-width: 0;
            
        }
        p{
            list-style-type: none; 
            padding: 0;
            text-align: center;
        }
        .st-emotion-cache-vk3wp9 eczjsme11 {
            width: 0;
            
        }
        .st-emotion-cache-10trblm {
            text-align: center;
        }
        .st-emotion-cache-1r4qj8v {
            text-align: center;
        }


    </style>
    """,
    unsafe_allow_html=True
)



# Chemin vers le répertoire des images
image_dir = "picture"

# Fonction pour convertir une image en base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Fonction pour créer un bouton avec une image en base64
def button_with_image_base64(image_base64, picture_texte,width=100,height=100, href_page=None):
    return f"""
    <a href="{href_page}" class="button-with-image" target="_self">
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    </a>
    """
def image(image_base64, picture_texte,width=100,height=100):
    return f"""
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    """

# HTML et CSS pour le bouton avec une image
button_style = """
<style>
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
}
.button-with-image {
    display: inline-block;
    border: none;
    padding: 10px;
    text-align: center;
    text-decoration: none;
    background-color: transparent;
    cursor: pointer;
    flex: 1 1 100px;  /* Flex-grow, flex-shrink, flex-basis */
    max-width: 100px;
}
.button-with-image img {
}


</style>
"""

image_path = os.path.join(image_dir, "logo.png")
image_base64 = load_image_as_base64(image_path)
st.markdown(image(image_base64,"logo","auto",250), unsafe_allow_html=True)

recherche_resto = st.selectbox(
    "",
    index=None,
    placeholder="Recherche de Restaurents ...",
    options=["Mcdo","KFC","Quick"],
    key="recherche_resto_box"
)

st.markdown(button_style, unsafe_allow_html=True)

burger, chicken, pizza, salad, sandwich, sushi = st.columns(6)

# Ajouter les boutons avec des images dans chaque colonne
with burger:
    image_path = os.path.join(image_dir, "burger.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64,"burger",href_page="liste_resto"), unsafe_allow_html=True)
    st.write("burger")

with chicken:
    image_path = os.path.join(image_dir, "indien.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64,"indien",href_page="liste_resto"), unsafe_allow_html=True)
    st.write("indien")

with pizza:
    image_path = os.path.join(image_dir, "pizza.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64,"pizza",href_page="liste_resto"), unsafe_allow_html=True)
    st.write("pizza")

with salad:
    image_path = os.path.join(image_dir, "salad.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64,"salad",href_page="liste_resto"), unsafe_allow_html=True)
    st.write("salad")

with sandwich:
    image_path = os.path.join(image_dir, "sandwich.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64,"sandwich",href_page="liste_resto"), unsafe_allow_html=True)
    st.write("sandwich")

with sushi:
    image_path = os.path.join(image_dir, "sushi.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64,"sushi",href_page="liste_resto"), unsafe_allow_html=True)
    st.write("sushi")


def csv(number1,number2):
    tripadvisor_restos.sort_values('avg_rating',ascending=False).iloc[number1 : number2].to_csv("hdquoh.csv", index=False)

resto1, resto2, resto3  = st.columns(3)

with resto1:
    image_path = os.path.join(image_dir, "fast_food_picture.png")
    image_base64 = load_image_as_base64(image_path)
    if st.markdown(button_with_image_base64(image_base64, "fast_food_picture",200,200,href_page="resto"), unsafe_allow_html=True):
        csv(0,2)   
        print("condition1")

    vide ,no_sound, disabled, hide, vide  = st.columns([1,1,1,1,1.4])

    with no_sound:
        image_path = os.path.join(image_dir, "no-sound.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "no-sound",50,50), unsafe_allow_html=True)
    with disabled:
        image_path = os.path.join(image_dir, "disabled.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "disabled",50,50), unsafe_allow_html=True)
    with hide:
        image_path = os.path.join(image_dir, "hide.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "hide",50,50), unsafe_allow_html=True)
    
    st.markdown(f"<u>**{tripadvisor_restos.sort_values('avg_rating',ascending=False)['restaurant_name'].iloc[0]}**</u>", unsafe_allow_html=True)
    st.write(f"{rating(tripadvisor_restos.sort_values('avg_rating',ascending=False)['avg_rating'].iloc[0])}")
    st.write(f"{tripadvisor_restos.sort_values('avg_rating',ascending=False)['address'].iloc[0]}") 

with resto2:
    image_path = os.path.join(image_dir, "healthy_picture.png")
    image_base64 = load_image_as_base64(image_path)
    if st.markdown(button_with_image_base64(image_base64, "healthy_picture",200,200,href_page="resto"), unsafe_allow_html=True):
        tripadvisor_restos.sort_values('avg_rating',ascending=False).iloc[1:3].to_csv('hdquoh.csv')   
        print("condition2")    


    vide ,no_sound, disabled, hide, vide  = st.columns([1,1,1,1,1.4])

    with no_sound:
        image_path = os.path.join(image_dir, "no-sound.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "no-sound",50,50), unsafe_allow_html=True)
    with disabled:
        image_path = os.path.join(image_dir, "disabled.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "disabled",50,50), unsafe_allow_html=True)
    with hide:
        image_path = os.path.join(image_dir, "hide.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "hide",50,50), unsafe_allow_html=True)

    st.markdown(f"<u>**{tripadvisor_restos.sort_values('avg_rating',ascending=False)['restaurant_name'].iloc[1]}**</u>", unsafe_allow_html=True)
    st.write(f"{rating(tripadvisor_restos.sort_values('avg_rating',ascending=False)['avg_rating'].iloc[1])}")
    st.write(f"{tripadvisor_restos.sort_values('avg_rating',ascending=False)['address'].iloc[1]}") 

with resto3:
    image_path = os.path.join(image_dir, "salad_resto.png")
    image_base64 = load_image_as_base64(image_path)
    if st.markdown(button_with_image_base64(image_base64, "salad_resto",200,200,href_page="resto"), unsafe_allow_html=True):
        testo = tripadvisor_restos.sort_values('avg_rating',ascending=False).iloc[2:4]
        testo.to_csv('hdquoh.csv')
        print("condition3")

    vide ,no_sound, disabled, hide, vide  = st.columns([1,1,1,1,1.4])

    with no_sound:
        image_path = os.path.join(image_dir, "no-sound.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "no-sound",50,50), unsafe_allow_html=True)
    with disabled:
        image_path = os.path.join(image_dir, "disabled.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "disabled",50,50), unsafe_allow_html=True)
    with hide:
        image_path = os.path.join(image_dir, "hide.png")
        image_base64 = load_image_as_base64(image_path)
        st.markdown(image(image_base64, "hide",50,50), unsafe_allow_html=True)

    st.markdown(f"<u>**{tripadvisor_restos.sort_values('avg_rating',ascending=False)['restaurant_name'].iloc[2]}**</u>", unsafe_allow_html=True)
    st.write(f"{rating(tripadvisor_restos.sort_values('avg_rating',ascending=False)['avg_rating'].iloc[2])}")
    st.write(f"{tripadvisor_restos.sort_values('avg_rating',ascending=False)['address'].iloc[2]}") 


#------------------------------------------------------------------------------------
#                               Trajet de la flamme
#------------------------------------------------------------------------------------


# Remplacez par votre propre clé API OpenRouteService

api_key = '5b3ce3597851110001cf6248302d9fcb8b44439aa282335994a41406'
client = openrouteservice.Client(key=api_key)

# Points de départ et d'arrivée

# Point d'avant Paris
start_coords = (2.454307999480008,48.83374390337135)


middle_coords = (2.362897133418489,48.85706328709478)


# Point d'après Paris
end_coords = (2.2533449626886175,48.84546466556765)



# Obtenir un itinéraire
route2 = client.directions( coordinates=[middle_coords, end_coords],
    profile='foot-walking',
    format='geojson'
)

route1 = client.directions( coordinates=[start_coords, middle_coords],
    profile='foot-walking',
    format='geojson'
)



# Afficher la réponse brute pour vérification (facultatif)
#print(route)

# Extraire les coordonnées de l'itinéraire
route_coords = route1['features'][0]['geometry']['coordinates']
route_coords = [(coord[1], coord[0]) for coord in route_coords]  # Inverser latitude et longitude


# Extraire les coordonnées de l'itinéraire
route_coords2 = route2['features'][0]['geometry']['coordinates']
route_coords2 = [(coord[1], coord[0]) for coord in route_coords2]  # Inverser latitude et longitude


# Créer une carte centrée sur le point de départ
m4 = folium.Map(location=[middle_coords[1], middle_coords[0]], zoom_start=12, tiles ="Cartodb Positron")

# Ajouter un marqueur pour le point des lacs de la forêt d'Orient
folium.Marker(
    location=[start_coords[1], start_coords[0]],
    popup='INSEP',
    icon=folium.Icon(color='green')
).add_to(m4)


# Ajouter un marqueur pour le deuxième point
folium.Marker(
    location=[middle_coords[1], middle_coords[0]],
    popup='Musée Carnavalet',
    icon=folium.Icon(color='bleu')
).add_to(m4)


# Ajouter un marqueur pour le point d'arrivée
folium.Marker(
    location=[end_coords[1], end_coords[0]],
    popup='Court Simonne-Mathieu',
    icon=folium.CustomIcon('https://storage.googleapis.com/endurance-apps-liip/media/cache/olympics-games_asset_card_grid_fs/622093e093e86c66c21cfc9b',
                           icon_size=(50, 50))
).add_to(m4)

# Ajouter l'itinéraire à la carte
folium.PolyLine(
    route_coords,
    color='yellow',
    weight=5,
    opacity=0.7
).add_to(m4)

folium.PolyLine(
    route_coords2,
    color='yellow',
    weight=5,
    opacity=0.7
).add_to(m4)


st.title(" ")
st_folium(m4, width=700, height=500)