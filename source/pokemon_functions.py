import requests

#the base url for all requests
url_base = 'https://pokeapi.co/api/v2/'

#get the response type of the request
def pokemon_response_type():
    url = url_base + "type"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)

        else:
            data = response.json()
            return type(data)
    except:
        print("An exception occurred")


#get the number of types
def pokemon_type_number():
    url = url_base + "type"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)

        else:
            data = response.json()
            return data["count"]

    except:
        print("An exception occurred")


#get all pokemon types
def get_types():
    url = url_base + "type"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)

        else:
            data = response.json()
            return data['results']

    except:
        print("An exception occurred")


#get type id by pokemon name
def get_type_id(type_name):
    try:
        #get all pokemon types
        pokemon_type_list = get_types()

        # find the dictionary with the requested name
        name_dict = next(item for item in pokemon_type_list if item['name'].lower() == type_name.lower())

        # extract the ID from the URL
        url = name_dict['url']
        name_id = int(url.split('/')[-2])

        return name_id
    except:
        print("An exception occurred")


#get the pokemons names of specific type id
def pokemon_names(type_id):
    url = f"{url_base}type/{type_id}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)

        else:
            data = response.json()
            pokemon_dict = data["pokemon"]

            # Extracting all 'name' values
            names = [pokemon_entry['pokemon']['name'] for pokemon_entry in pokemon_dict]
            return names

    except:
        print("An exception occurred")


#get the weight of specipic pokemon
def get_pokemon_weight(pokemon_name):
    try:
        url = f"{url_base}pokemon/{pokemon_name}"
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)

        else:
            data = response.json()
            weight = data["weight"]
            return weight

    except:
        print("An exception occurred")


#find the five heaviest Pokémon of specific type id
def top_five_heaviest(type_id):
    url = f"{url_base}type/{type_id}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)

        else:
            data = response.json()
            pokemon_dict = data["pokemon"]

            # Extracting all 'name' values
            pokemon_names = [pokemon_entry['pokemon']['name'] for pokemon_entry in pokemon_dict]

            #get all pokemon names and theit weights
            pokemon_weights = [(pokemon_name, get_pokemon_weight(pokemon_name)) for pokemon_name in pokemon_names]

            #get top 5 heaviest Pokemon
            five_heaviest = sorted(pokemon_weights,key=lambda item: item[1], reverse=True)[:5]
            #return dictionary when the keys is the pokemon names and values is their weights
            return dict(five_heaviest)

    except:
        print("An exception occurred")


