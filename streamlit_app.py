import streamlit as st
import pandas as pd
import requests



pokemon_number = st.slider("choose a pokemon!",1,155)
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"

response = requests.get(pokemon_url).json()

response.keys()

pokemon_name = response['name']
pokemon_image = response['sprites']['front_default']
pokemon_height = response['height']
pokemon_weight = response['weight']
pokemon_move = response['moves']

st.write(f"Name:{pokemon_name.title()}")
st.write(f"Height:{pokemon_height}")
st.write(f"weight:{pokemon_weight}")
st.write(f"moves:")

for move in pokemon_move[:3]:
    st.write(move['move']['name'].title())

def get_pokemon_data(pokemon_number):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(pokemon_url).json()
    return {
        'name': response['name'].title(),
        'height': response['height'],
        'weight': response['weight'],
        'image': response['sprites']['front_default']
    }

numbers_of_pokemon = range(1,151)

pokemon_data = [get_pokemon_data(num) for num in numbers_of_pokemon]

sorted_by_height = sorted(pokemon_data, key=lambda x: x['height'])
sorted_by_weight = sorted(pokemon_data, key=lambda x: x['weight'])


tallest = sorted_by_height[-2:]
shortest = sorted_by_height[:2]
heaviest = sorted_by_weight[-2:]
lightest = sorted_by_weight[:2]

# Plotting the data
fig, ax = plt.subplots(2, 1, figsize=(10,5))

# Tallest and Shortest Pokémon
heights = [pokemon['height'] for pokemon in tallest + shortest]
names = [pokemon['name'] for pokemon in tallest + shortest]
ax[0].bar(names, heights, color=['green', 'green', 'red', 'red'])
ax[0].set_title('Tallest and Shortest Pokémon')
ax[0].set_ylabel('Height')

# Heaviest and Lightest Pokémon
weights = [pokemon['weight'] for pokemon in heaviest + lightest]
names = [pokemon['name'] for pokemon in heaviest + lightest]
ax[1].bar(names, weights, color=['blue', 'blue', 'orange', 'orange'])
ax[1].set_title('Heaviest and Lightest Pokémon')
ax[1].set_ylabel('Weight')

st.pyplot(fig)


