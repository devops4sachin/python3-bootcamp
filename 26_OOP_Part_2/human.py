class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0
			
			
	#def get_age(self):			# These are the getter and setter functions.
	#	return self._age
	#	
	#def set_age(self, new_age):
	#	if new_age >= 0:
	#		self._age = new_age
	#	else:
	#		self._age = 0
	
	# we can set the getter and setter using the properties decorator.
	
	@property					# This is a getter.
	def age(self):				# The name of the function "age" is the property.  Here "age" would be the property of a class.
		return self._age
		
	@age.setter
	def age(self, new_age):		# This is a setter.
		if new_age >= 0:
			self._age = new_age
		else:
			raise ValueError("Age can't be negative.")
	
	@property
	def full_name(self):
		return f"{self.first} {self.last}"
		
	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")
		
			
# Function called with the getter and setters			
jane = Human("Jane", "Goodall", 20)
#print(jane.get_age())
#jane.set_age(40)
#print(jane.get_age())

print(jane.age)	# This works like a attribute but this is a function. This is a getter function.

jane.age = 40	# Using the setter function.
print(jane.age)


print(jane.full_name)

jane.full_name = "Tim Kaka"


print(jane.__dict__)


print(jane.full_name)

##### output #######
# 20
# 40
# Jane Goodall
# {'first': 'Tim', 'last': 'Kaka', '_age': 40}
# Tim Kaka