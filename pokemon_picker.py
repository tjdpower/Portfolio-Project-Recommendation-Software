from data import *
from welcome import *
from linked_list import LinkedList

#Note that LinkedList and Node come from the Coursework on data structures from Codecademy
# some functionality below is recycled from the example project for this unit as well, modified to fit the needs of this software

print_welcome()

# Write code to insert food types into a data structure (LinkedList) here. The data is in data.py
def insert_pokemon_types():
    pokemon_type_list = LinkedList()
    for pokemon_type in types:
        pokemon_type_list.insert_beginning(pokemon_type.lower())
    return pokemon_type_list


# Write code to insert restaurant data into a data structure (LinkedList of LinkedLists) here. The data is in data.py
def insert_pokemon_data():
    pokemon_data_list = LinkedList()
    for pokemon_type in types:
        pokemon_sublist = LinkedList()
        for pokemon in pokedex:
            for i in range(len(pokemon[2])):
                if pokemon[2][i] == pokemon_type:
                    pokemon_sublist.insert_beginning(pokemon)
        pokemon_data_list.insert_beginning(pokemon_sublist)
    return pokemon_data_list

my_type_list = insert_pokemon_types()
my_pokemon_list = insert_pokemon_data()

selected_pokemon_type = ""

#getting pokemon type from user
while len(selected_pokemon_type) == 0:
    user_input = str(input("""
        
        What type of pokemon are you fighting?
        Type the beginning of that pokemone type and
        hit enter to see if it's here.
        """
    )).lower()

    #find pokemon type in the list, if it exists
    matches = []
    type_list_head = my_type_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matches.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()
    
    #print list of matching types
    for pokemon in matches:
        print(pokemon)
    
    