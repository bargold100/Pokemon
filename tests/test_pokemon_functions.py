from source import pokemon_functions


# Q1
def test_response_type():
    result = pokemon_functions.pokemon_response_type()
    assert result == dict


def test_pokemon_type_number():
    result = pokemon_functions.pokemon_type_number()
    assert result == 20


# Q2
def test_charmander_in_pokemon_list():
    # the id of "Fire" type is 10
    result = pokemon_functions.pokemon_names(10)
    assert "charmander" in result


def test_bulbasaur_not_in_pokemon_list():
    # the id of "Fire" type is 10
    result = pokemon_functions.pokemon_names(10)
    assert "bulbasaur" not in result


def test_pokemon_names_wrong_id_type():
    # the id of "Fire" type is 10
    result = pokemon_functions.pokemon_names(0)
    assert result is None


# Q3
def test_charizard_gmax_weight():
    # the id of "Fire" type is 10
    result = pokemon_functions.top_five_heaviest(10)["charizard-gmax"]
    assert result == 10000


def test_cinderace_gmax_weight():
    # the id of "Fire" type is 10
    result = pokemon_functions.top_five_heaviest(10)["cinderace-gmax"]
    assert result == 10000


def test_coalossal_gmax_weight():
    # the id of "Fire" type is 10
    result = pokemon_functions.top_five_heaviest(10)["coalossal-gmax"]
    assert result == 10000


def test_centiskorch_gmax_weight():
    # the id of "Fire" type is 10
    result = pokemon_functions.top_five_heaviest(10)["centiskorch-gmax"]
    assert result == 10000


def test_groudon_primal_weight():
    # the id of "Fire" type is 10
    result = pokemon_functions.top_five_heaviest(10)["groudon-primal"]
    assert result == 9997


def test_top_5_wrong_type_number():
    result = pokemon_functions.top_five_heaviest(0)
    assert result is None
