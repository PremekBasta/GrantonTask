import pytest
from app import app
from model import Model, parse_objects
from validations import Validator
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

class MockValidator:
    def validate_and_parse(self, data):
        print("mock")
        return data["input"], None

class MockModelPikachu:
    def detect_object(self, input):
        print("mock model object")
        return "OBJECT: Pikachu"
    
    def get_ai_pokemon_completiton(self, input):
        print("mock model pokemon completion")
        return """Name: Pikachu
Type: Electric
Body Description: Small, yellow rodent
Personality: Energetic, friendly, loyal
Special Powers: Thunderbolt, Thunder Shock
Characteristic Ability: Electric sacs in cheeks"""

def test_wrong_route(client):
    response = client.get('/wrong_route')
    assert response.status_code == 404

def test_short_input(client):    
    data = json.dumps({'input': 'x'})    
    response = client.post('/process_input', data=data, content_type='application/json')
    assert response.status_code == 400        
    assert response.json["error"] == "Input is too short"

def test_long_input(client):
    data = json.dumps({'input': 'This is a very long text, that our microservice will not be able to grasp. We need to make this text shorter and more specific. Also this input does not even contains name of any Pokemon.'})    
    response = client.post('/process_input', data=data, content_type='application/json')
    assert response.status_code == 400        
    assert response.json["error"] == "Input is too long"

def test_no_input(client):
    data = json.dumps({})    
    response = client.post('/process_input', data=data, content_type='application/json')
    assert response.status_code == 400        
    assert response.json["error"] == "No input"

def test_not_existing_pokemon(client):
    data = json.dumps({'input': 'Pokesaurus'})    
    response = client.post('/process_input', data=data, content_type='application/json')
    assert response.status_code == 400        
    assert response.json["error"] == "Pokesaurus is not existing Pokemon"

def test_existing_pokemon_with_mocked_model(client, monkeypatch):
    monkeypatch.setattr('app.model', MockModelPikachu())
    data = json.dumps({'input': 'Pikachu'})    
    response = client.post('/process_input', data=data, content_type='application/json')
    assert response.status_code == 200        
    assert response.json["Name"] == ["Pikachu"]
    assert response.json["Type"] == ["Electric"]
    assert response.json["Personality"] == ["Energetic", "friendly", "loyal"]

def test_parse_object(client):
    pokemons = parse_objects("OBJECT:  Geodude ")
    assert pokemons[0] == "Geodude"

def stest_real_call(client):
    data = json.dumps({'input': ' Geodude '})    
    response = client.post('/process_input', data=data, content_type='application/json')
    assert response.status_code == 200        
    assert response.json["Name"] == ["Geodude"]
    assert "Rock" in response.json["Type"]