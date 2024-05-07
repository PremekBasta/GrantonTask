object_detection_prompt = """For a given sentence in natural language detect the main object and write it down on a new line prefixed with "OBJECT:".

"Describe who is George Washington.
OBJECT:George Washington

Tell me some information about Tyranosaurus Rex.
OBJECT:Tyranosaurus Rex

I would like to ask you a query about Sandshrew. Do you know him?
OBJECT:Sandshrew

"""

pokemon_desription_prompt="""When prompted for a specific Pokemon. Provide information containing it's name, type, body description, personality, special powers and characteristic ability. Describe these attribute only in few keywords eventually separated using commas.


Describe Pikachu:

Name: Pikachu
Type: Electric
Body Description: Small, yellow rodent
Personality: Energetic, friendly, loyal
Special Powers: Thunderbolt, Thunder Shock
Characteristic Ability: Electric sacs in cheeks


Describe Cubone:

Name: Cubone
Type: Ground
Body Description: Small, bipedal, skull helmet
Personality: Lonely, protective, sorrowful
Special Powers: Bone Club, Bonemerang
Characteristic Ability: Wears its mother's skull


Describe Landorus:

Name: Landorus
Type: Ground, Flying
Body Description: Legendary, muscular, humanoid
Personality: Proud, noble, protective
Special Powers: Earthquake, Fly
Characteristic Ability: Incarnate Forme, Therian Forme

Describe """

pokemon_properties = ["Name", "Type", "Body Description", "Personality", "Special Powers", "Characteristic Ability"]