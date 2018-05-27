# Another class with a class attribute, used for validation purposes
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']		# Class attribute, defining which animals species can be stored.

	def __init__(self, name, species):
		
		# allowed = ['cat', 'dog', 'fish', 'rat'], if we define here it would neither be a Class attribute or Instance attribute.
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:			# Pet.allowed means we are using a class attribute.
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

# tiger = Pet("Tiger", "tiger")
# raise error.

print("Showing that cat.allowed and dog.allowed are referring to same object")
print(f"cat.allowed is : "+ str(id(cat.allowed)))
print(f"dog.allowed is : "+ str(id(dog.allowed)))

#Showing that cat.allowed and dog.allowed are referring to same object
#cat.allowed is : 1862485423432
#dog.allowed is : 1862485423432



