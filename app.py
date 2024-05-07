from flask import Flask, request, jsonify
from validations import Validator
from model import Model, parse_pokemon
from prompts import pokemon_properties

app = Flask(__name__)
model = Model()
validator = Validator(model)


@app.route('/process_input', methods=['POST'])
def process_input():
    try:
        data = request.json
        print(data)
        pokemon_name, error_message, error_code = validator.validate_and_parse(data)
        
        if error_code is not None:
            return jsonify({"error": error_message}), error_code
        
        pokemon_completion = model.get_ai_pokemon_completiton(pokemon_name)
        pokemon_description = parse_pokemon(pokemon_completion)
                
        return jsonify(pokemon_description), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500



@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.error(error)
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == "__main__":    
    app.run(host="0.0.0.0")
    