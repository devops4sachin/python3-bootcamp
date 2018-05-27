class GrumpyDict(dict):		# We are inheriting from the "dict" class.
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()				# calling dictionary version of __repr__()

	def __missing__(self, key):					# __missing__() will be called on a dictionary while throwing the error incase the "key" is missing.
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	def __setitem__(self, key, value):			# you can check the documentation for Python dictionary, to see the details of this function.
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)			# calling super(), dictionary version of __setitem__()

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})	# Initialising the GrumpyDict.

print(data) 					# Here __repr__() is called.

data['city'] = 'Tokyo'			# Here __setitem__() is called.

print(data)

'city' in data					# Here __contains__() is called.

data['check']					# Here __missing__() is called.


##################### output #####################
# NONE OF YOUR BUSINESS
# {'first': 'Tom', 'animal': 'cat'}
# YOU WANT TO CHANGE THE DICTIONARY?
# OK FINE...
# NONE OF YOUR BUSINESS
# {'first': 'Tom', 'animal': 'cat', 'city': 'Tokyo'}
# NO IT AINT IN HERE!
# YOU WANT check?  WELL IT AINT HERE!





























class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"THAT THING YOU WANT ISN'T IN HERE")

	def __setitem__(self, key, value):
		print("Why do you always have to change things?")
		print(f"Ugh fine, setting {key} to {value}")
		super().__setitem__(key, value)