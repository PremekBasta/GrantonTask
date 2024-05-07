from openai import OpenAI
import os 
import prompts

class Model:
    def __init__(self):
        self.client = OpenAI()
        self.client.api_key = os.environ.get("OPENAI_API_KEY")
    
    def detect_object(self, input):             
        """
        Wraps the input with object detection prompt and submits it to LLM
        """
        prompt = prompts.object_detection_prompt + input
        result = self.call_api(prompt)                
        
        return result

    def get_ai_pokemon_completiton(self, input):
        """
        Wraps the input with pokemon description completion prompt and submits it to LLM
        """
        prompt = prompts.pokemon_desription_prompt + input
        result = self.call_api(prompt)        
        
        return result


    def call_api(self, prompt):
      """
      Submits prompt onto chat gpt 3.5 turbo instruct model
      """  
      response = self.client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
      )

      return response.choices[0].text
    

def parse_objects(input):
  """
  Parses text into list of objects, where objects appear on standalone lines 
  starting with fixed string "OBJECT:" followed by the object itself
  """
  objects = []

  # each line of the result is parsed
  for line in input.splitlines():
    
    # object detected        
    if line.startswith("OBJECT:"):
      objects.append(line.removeprefix("OBJECT:").strip())

  return objects

def parse_pokemon(input):
  """
  Parses textual description into python dictionary of pokemon properties.  
  """
  pokemon_description = {}

  # each line of the result is parsed
  for line in input.splitlines():
        
    # looking for all pokemon properties
    for prop in prompts.pokemon_properties:
      if line.startswith(prop):

        # given property might have several values
        pokemon_description[prop] = [word.strip() for word in line.removeprefix(prop + ": ").split(',')]        
  
  return pokemon_description