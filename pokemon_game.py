import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()
my_pokemon = choice
print("My pokemon is", my_pokemon)

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
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

print(my_pokemon)

#pokemon of cpu>Random select
cpu_pokemon_id = random.randint(1, 151)
url = f'https://pokeapi.co/api/v2/pokemon/{cpu_pokemon_id}/'
response = requests.get(url)
cpu_pokemon_data = json.loads(response.text)

# Extract height, weight, hp and attack for CPU
# to get ability
abilities = cpu_pokemon_data['abilities'][0]
cpu_ability = abilities['ability']

# to format height and weight properly
cpu_height = int(cpu_pokemon_data['height'])
cpu_weight = int(cpu_pokemon_data['weight'])

cpu_height_formatted = height / 10
cpu_weight_formatted = weight / 10

# Print the pokemon's data
print('Name cpu pokemon: {}'.format(cpu_pokemon_data['name']))
print('Weight: {}'.format(cpu_weight_formatted) + "(kgs)")
print('Height: {}'.format(cpu_height_formatted) + "(m)")
print('Ability: {}'.format(cpu_ability['name']))

# Print the initial battle message showing both Pokémon
print(f"Your {pokemon_data['name']} VS my {cpu_pokemon_data['name']}! Start the fight!")