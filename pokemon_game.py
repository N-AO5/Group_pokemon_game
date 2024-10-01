import requests
import json
import random


# Get the list of pokemon from the API
#url = 'https://pokeapi.co/api/v2/pokemon/'
#response = requests.get(url)
#pokemon_list = json.loads(response.text)['results']

def pokemon_data(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/{cpu_pokemon_id}/'
    response = requests.get(url)
    return json.loads(response.text)


cpu_pokemon_id = random.randint(1, 1302)  # found the count of pokemon IDs possible
cpu_pokemon_data = pokemon_data(cpu_pokemon_id)

cpu_height = (cpu_pokemon_data['height'])
cpu_weight = (cpu_pokemon_data['weight'])
cpu_hp = (cpu_pokemon_data['hp'])
cpu_attack = (cpu_pokemon_data['attack'])

print(f"CPU chose {cpu_pokemon_data['name']}:")
print(f'Name: {cpu_pokemon_data["name"]}')
print(f'Weight: {cpu_weight} kg')
print(f'Height: {cpu_height} m')
print(f'HP: {cpu_hp}')
print(f'Attack: {cpu_attack}')

# Ask the user to choose a pokemon


# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API

pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))

#make the cpu choose a pokemon from random



cpu_pokemon = pokemon_data['name']
print(f"Your opponent is {cpu_pokemon}")

player_input = input("Enter your pokemon name: ")
if player_input == pokemon_data['name']:
    print(player_input)
else:
    player_input = ""
    player_pokemon_id = cpu_pokemon_id




#response = requests.get(url)  #get a response
#data_dict = response.json()

#with open('pokemon.json', 'w') as file:
    #json.dump(data_dict, file)

#print(f"CPU pokemon: {data_dict["name"]}")
#print(f"{data_dict["name"]} is type {data_dict['type']}")