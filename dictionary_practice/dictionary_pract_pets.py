import pprint

pet_0 = {'animal': 'dog', 'owner': 'stephen', 'nature': 'friendly'}
pet_1 = {'animal': 'cat', 'owner': 'rachel', 'nature': 'aggressive'}
pet_2 = {'animal': 'parrot', 'owner': 'alex', 'nature': 'quiet'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	pprint.pprint(pet)
