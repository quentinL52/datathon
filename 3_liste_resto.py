import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import folium
import openrouteservice
import base64
import os


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



recherche_resto = st.selectbox(
    "",
    index=None,
    placeholder="Recherche de Restaurents ...",
    options=["Mcdo","KFC","Quick"],
    key="recherche_resto_box"
)


image_dir = "picture"

# Fonction pour convertir une image en base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Fonction pour créer un bouton avec une image en base64
def button_with_image_base64(image_base64, picture_texte,width=100,height=100, href_page="resto"):
    return f"""
    <a href="{href_page}" class="button-with-image" target="_self">
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    </a>
    """
def image(image_base64, picture_texte,width=100,height=100):
    return f"""
        <img src="data:image/png;base64,{image_base64}" alt={picture_texte} width={width} height={height}>
    """

st.title("Top Restaurant autour de vous")

st.subheader("Italien")
st.title(" ")

resto1, resto2 = st.columns(2)

with resto1:
    image_path = os.path.join(image_dir, "salad_resto.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64, "salad_resto",200,200,href_page="resto"), unsafe_allow_html=True)

    st.title(" ")

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
        
    st.title(" ")
    st.markdown("<u>**Le café de Paris**</u>", unsafe_allow_html=True)
    st.write("⭐️⭐️⭐️⭐️")
    st.write("44 Rue Alphonse Penaud, Paris") 

with resto2:
    image_path = os.path.join(image_dir, "salad_resto.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64, "salad_resto",200,200,href_page="resto"), unsafe_allow_html=True)

    st.title(" ")

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

    st.title(" ")
    st.markdown("<u>**Le café de Paris**</u>", unsafe_allow_html=True)
    st.write("⭐️⭐️⭐️⭐️")
    st.write("44 Rue Alphonse Penaud, Paris") 

st.subheader("Healthy")
st.title(" ")

resto1, resto2 = st.columns(2)

with resto1:
    image_path = os.path.join(image_dir, "salad_resto.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64, "salad_resto",200,200,href_page="resto"), unsafe_allow_html=True)

    st.title(" ")

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
        
    st.title(" ")
    st.markdown("<u>**Le café de Paris**</u>", unsafe_allow_html=True)
    st.write("⭐️⭐️⭐️⭐️")
    st.write("44 Rue Alphonse Penaud, Paris") 

with resto2:
    image_path = os.path.join(image_dir, "salad_resto.png")
    image_base64 = load_image_as_base64(image_path)
    st.markdown(button_with_image_base64(image_base64, "salad_resto",200,200,href_page="resto"), unsafe_allow_html=True)

    st.title(" ")

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

    st.title(" ")
    st.markdown("<u>**Le café de Paris**</u>", unsafe_allow_html=True)
    st.write("⭐️⭐️⭐️⭐️")
    st.write("44 Rue Alphonse Penaud, Paris") 