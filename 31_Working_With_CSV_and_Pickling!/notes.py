############################## Working With CSV and Pickling! ###############################

###### 1 : Reading CSV Files

	- CSV Module
		- reader - lets you iterate over rows of the CSV as lists
		- DictReader - lets you iterate over rows of the CSV as OrderedDicts
		- Keys are determined by the header row
		- An OrderedDict is like a dictionary, but it remembers the order in which keys were inserted
		
	- Refer to read.py file.
	
	- Other Delimiters : Readers accept a delimiter kwarg in case your data isn't separated by commas.
	
		from csv import reader
		with open("fighter2.csv") as file:
			csv_reader = reader(file, delimiter="|")
			for row in csv_reader:
				# each row is a list!
				print(row)
				
				
###### 2 : Writing to CSV Files: Writer (using list)

	- writer - creates a writer object for writing to CSV
	- writerow - method on a writer to write a row to the CSV

		from csv import writer
		with open("fighters.csv", "w") as file:
			csv_writer = writer(file)
			csv_writer.writerow(["Character", "Move"])
			csv_writer.writerow(["Ryu", "Hadouken"])
	
	- Refer to write.py and sream.py
	


###### 3 : Writing to CSV Files: DictWriter

	- DictWriter - creates a writer object for writing using dictionaries
	- fieldnames - kwarg for the DictWriter specifying headers
	- writeheader - method on a writer to write header row 
	- writerow - method on a writer to write a row based on a dictionary
	
	- Writing CSV Files Example, Using Dictionaries

		from csv import DictWriter
		with open("example.csv", "w") as file:
			headers = ["Character", "Move"]
			csv_writer = DictWriter(file, fieldnames=headers)
			csv_writer.writeheader()
			csv_writer.writerow({
				"Character": "Ryu", 
				"Move": "Hadouken"
			})
		########## output ###########
		Character,Movie
		
		Ryu,Movie1
		#############################
	
	- Refer to writer.py file.
	
	- Convert fighters height to inches. Refer to convert.py file.
	
	
	
###### 4 :	Pickling Time!
	
	- Writing a class data to a file.
	
	- We use a pickling here, We take something put it in a special python file and pickle module with serialize the data. And we can pull it again from the file whenever required.
	- The data is converted into a byte stream and unpickling is the inverse operation, where by byte stream is converted back to the original data.
	
	- Refer to pickling-example.py file.
	
	with open("pets.pickle", "wb") as file  << as it is a binary file.
	
	Note : This is meant only for manipulating the python objects and not the plain text. Its only meant for the python class.
	
	
	
###### 5 :	Extra Fancy JSON Pickling

	- Refer to json_demo.py, json_pickle.py
	
	- "import json" : It provides functions to encode and decode to JSON objects. It takes a python object and convert it to JSON object.
	
	- The below example convert the tuple to JSON format
	
		>>> import json
		>>> j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
		>>> print(j)
		["foo", {"bar": ["baz", null, 1.0, 2]}]
		
	- Normal JSON library cannot be used to convert complex Python objects to JSON format.
	- jsonpickle is Python library for serilization and deserialization of complex Python objects to and from JSON. jsonpickle build on the top of JSON library allows more complex Python objects to convert to JSON format.
	
	- Instruction to install it.
		# python3 -m pip install jsonpickle

  