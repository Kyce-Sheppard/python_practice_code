#  A dictionary to store people's favorite places
favorite_places = {'kyce': ['london', 'alaska', 'maine'], 
					'kaden': ['germany', 'london'], 
					'tanner': ['japan'], 
					'korbin': []
}

#  Looping through the dictionary. The variable 'places' is used to hold each
#  value from the dictionary because it is a list.
for name, places in favorite_places.items():
	if len(places) == 1:
		print(f"\n{name.title()}'s favorite place is:")
	elif len(places) == 0:
		print(f"\n{name.title()}, you need to travel more!")
	else:
		print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")