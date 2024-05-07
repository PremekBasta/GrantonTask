Flask Microservice for Generating Pokemon Descriptions
======================================================

This Flask microservice provides an API endpoint to generate structured JSON information about Pokemon based on textual questions. It utilizes the OpenAI API for natural language processing.

Installation
------------

To run the microservice, you'll need Python and a few dependencies installed. You can install them using pip:

~~~sh
pip install -r requirements.txt
~~~

The dependencies include Flask for the web framework, requests for making HTTP requests, and openai for interfacing with the OpenAI API.

Setting Up OpenAI API Key
-------------------------

Before running the microservice, you need to set up your OpenAI API key as a global environment variable called `OPENAI_API_KEY`. You can obtain an API key by signing up on the [OpenAi website](https://openai.com/)

~~~sh
export OPENAI_API_KEY="your-api-key"
~~~


Running as a Python Flask App
-----------------------------

To run the microservice as a Python Flask app, execute the following command:

~~~sh
python app.py
~~~

This will start the Flask development server, and the microservice will be accessible at `http://127.0.0.1:5000`.

Running through Docker
----------------------

To run the microservice through Docker, first, build the Docker image using the provided Dockerfile:

~~~sh
docker build --build-arg OPENAI_API_KEY=$OPENAI_API_KEY -t flask-app .
docker run -p 5000:5000 --name my-flask-app flask-app
~~~

The microservice will be accessible at `http://127.0.0.1:5000`.


API Endpoint
------------

The microservice exposes one API endpoint:

*   `/process_input`: Accepts a POST request with a JSON payload containing a textual question about a Pokemon. The input text should be under the key `"input"`. It processes the input using the OpenAI model and returns structured JSON information about the Pokemon.

Implemented Logic
-----------------

The microservice implements a Flask app with one method `process_input`. This method takes a textual question about a given Pokemon, passes it to the OpenAI language model, and generates a textual description of the Pokemon. The description is then parsed and returned as structured JSON information about the Pokemon.

Example Usage
-------------

Here's an example of how to use the microservice:

~~~sh
curl -X POST -H "Content-Type: application/json" -d '{"input": "I need you to give me detailed information about Geodude"}' http://localhost:5000/process_input
~~~