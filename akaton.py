import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import folium
import openrouteservice
import base64
import os
import webbrowser


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
        .st-emotion-cache-7ym5gk {
            text-align: center;        
        }

    </style>
    """,
    unsafe_allow_html=True
)

image_dir = "picture"

def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def image(image_base64, picture_texte,width=100,height=100):
    return f"""
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    """
def button_with_image_base64(image_base64, picture_texte,width=100,height=100, href_page="resto"):
    return f"""
    <a href="{href_page}" class="button-with-image" target="_self">
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    </a>
    """

image_path = os.path.join(image_dir, "logo.png")
image_base64 = load_image_as_base64(image_path)
st.markdown(image(image_base64,"logo","auto",250), unsafe_allow_html=True)

st.title("BIENVENUE")

address = st.text_input("", placeholder="Veuillez indiquer votre adresse ...")
# Chemin vers le répertoire des images

st.title(" ")
image_path = os.path.join(image_dir, "location.png")
image_base64 = load_image_as_base64(image_path)
st.markdown(image(image_base64,"location",300,300), unsafe_allow_html=True)

st.title(" ")

if st.button("Lancer la recherche"):
    # Vérifier si l'adresse est saisie
    if address:
        with open("pages\informations.txt", "w") as fichier:
            fichier.write(address)
            
        webbrowser.open("http://localhost:8501/acceuil", new=0, autoraise=False)
            
    else:
        st.error("Veuillez indiquer votre adresse !")