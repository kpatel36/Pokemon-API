#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests as r
import random 

class Pokemon():
    def __init__(self, data):
        data = r.get(f'https://pokeapi.co/api/v2/pokemon/{user_choice}')
        object_data = data.json()
        object_data
        #self.data = data
        self.name = object_data['forms'][0]['name'].title()
        self.weight = object_data['weight']
        self.height = object_data['height']
        self.ability = ", ".join(list({x['ability']['name'] for x in object_data['abilities']}))
        self.type = ", ".join(list({x['type']['name'] for x in object_data['types']}))
        

def promptForPokemon():
    print('If you would like a few suggestions, type SUGGESTION\n\n')
    user_choice = input('What pokemon would you like to see information on:\n\n').lower()
    if user_choice == 'suggestion':
#         best_pokemon = ['alazakam', 'bulbasaur', 'charmander','drowzee', 'electrike', 'froslass', 'golbat', 'hitmonttop', 'ivysaur', 'jigglypuff', 'kabutops', 'lairon', 'mewtoo', 'noctowl', 'onix', 'pikachu', 'quilava', 'rapidash', 'squirtle', 'toxel', 'unfezant', 'vibrava', 'wartortle', 'xurkitree', 'yamper', 'zebstrika']
#         print("\nHere are a few suggestions: \n")
#         for i in range(5):
#             print (random.choice(best_pokemon).title())
#         user_choice = input('What pokemon would you like to see information on:\n\n').lower()
         return user_choice
    else:
        return user_choice

print ('Welcome to the Pokedex\n')
#promptForPokemon()
user_choice = input('What pokemon would you like to see information on:\n\n').lower()
pokemonpick = Pokemon(user_choice)
print('{}'.format(pokemonpick.__dict__).title())

view_another = input('Would you like to see another?').lower()
if view_another == 'yes':
#    promptForPokemon()
    user_choice = input('What pokemon would you like to see information on? :\n\n').lower()
    pokemonpick2= Pokemon(user_choice)
    print('{}'.format(pokemonpick2.__dict__).title())
else:
    print('OK')


# In[ ]:





# In[ ]:




