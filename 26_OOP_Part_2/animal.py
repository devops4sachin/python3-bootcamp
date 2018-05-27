# Inheritance Example Using Super()
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
		super().__init__(name, species="Cat") # Call init on parent class, super will call the Parent class constructor.
							# Need not to specify the "self" here.
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")



blue = Cat("Blue","Scottish Fold", "String")	# 
blue.play()
blue.make_sound("Meow")

# print(isinstance(blue, Cat))		-- This is True
# print(isinstance(blue, Animal))	-- This is True
# print(isinstance(blue, object))	-- This is True


# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy