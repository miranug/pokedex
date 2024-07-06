import streamlit as st
import requests

st.title("Pokédex")


pokemon_name = st.text_input("Zadejte jméno Pokémona:")
if pokemon_name:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 200:
        data = response.json()
        stats = {
            "name": data["name"].capitalize(),
            "hp": data["stats"][0]["base_stat"],
            "attack": data["stats"][1]["base_stat"],
            "defense": data["stats"][2]["base_stat"],
            "speed": data["stats"][5]["base_stat"],
            "type": ", ".join([t["type"]["name"].capitalize() for t in data["types"]]),
            "image_url": data["sprites"]["front_default"]
        }
        st.subheader(f"{stats['name']}")
        st.image(stats["image_url"], width=150)
        st.text(f"Typ: {stats['type']}")
        st.text(f"HP: {stats['hp']} ❤️")
        st.text(f"Útok: {stats['attack']} ⚔️")
        st.text(f"Obrana: {stats['defense']} 🛡️")
        st.text(f"Rychlost: {stats['speed']} 🏃")

