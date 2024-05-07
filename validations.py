import requests
from model import parse_objects

class Validator():
    def __init__(self, model):
        self.model = model

    def validate_and_parse(self, data):        
        """
        Validates input for basic constraints and returns detected object.
        Returns error message and error code when the input is invalid.
        """
        if "input" not in data:
            return None, "No input", 400
        
        input = data["input"]
        
        if len(input) < 5:
            return None, "Input is too short", 400
        
        if len(input) > 100:
            return None, "Input is too long", 400

        # single word on input is probably desired pokemon
        words = str.split(input, ' ')
        if len(words) == 1:
            pokemons = [words[0]]        
        else:
            # when input is more complex text, object detection is delegated to LLM
            result = self.model.detect_object(input)
            pokemons = parse_objects(result)

        if len(pokemons) > 1:
            return None, "Too many pokemons on input", 400
                
        pokemon = pokemons[0]
        
        if not self.pokemon_exists(pokemon):
            return None, f"{pokemon} is not existing Pokemon", 400
        
        return pokemon, None, None

    def pokemon_exists(self, pokemon):
        """
        Checks existence of pokemon through call to Pokemon API
        """
        pokemon_info = self.get_pokemon_info(pokemon)
        return pokemon_info is not None

    def get_pokemon_info(self, pokemon_name):
        """
        Calss Pokemon API for requested pokemon name
        """
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_info = {
                "name": pokemon_data["name"]
            }
            return pokemon_info
        if response.status_code == 404:
            return None