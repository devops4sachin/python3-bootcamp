import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)

# To unpickle something:
# with open("pets.pickle", "rb") as file:
# 	zombie_blue = pickle.load(file)			# load the class data into a variable.
# 	print(zombie_blue)						# This runs the __repr__ method of the class.
# 	print(zombie_blue.play())				# Run the "Play" method of the class.

