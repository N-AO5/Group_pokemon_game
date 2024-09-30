import requests
import json
import random
"""
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
print('Ability: {}'.format(ability['name']))"""




random_number = random.randint(1, 100) # random number generated

# make a call to get a random pokemon using the random_number variable to get a new number in the url everytime
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_number}')

data_dict = response.json() # store response as a dictionary here

with open("example.json",'w') as file: # I'm storing the result as a file for no reason
    json.dump(data_dict, file, indent=4)

print(f"random pokemon chosen: {data_dict["name"]}" ) #printing to the terminal the random pokemon details I originally got from my response variable

for ability in data_dict["abilities"]: #prints the name of the pokemon abilities
    print(f"this pokemon can use: {ability["ability"]["name"]}")