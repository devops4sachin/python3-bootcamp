########################## Object Oriented Programming #################################

		- Objectives

			- Define what Object Oriented Programming is
			- Understand encapsulation and abstraction
			- Create classes and instances and attach methods and properties to each
			
			
######## 1 : Defining Classes and Objects

		- class - a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict).

		- instance - objects that are constructed from a class blueprint that contain their class's methods and properties.
		

		
######## 2 : Abstraction and Encapsulation

		- Goal of OOP :  to encapsulate your code into logical, hierarchical groupings using classes so that you can reason about your code at a higher level.
		
		- for example : A poker game can have following classes.
				- Game
				- Player
				- Card
				- Deck
				- Hand
				- Chip
				- Bet
				
		- example : Deck {class} can have following attributes.

			- _cards         {private list attribute}	: Actual cards in a deck
			- _max_cards     {private int attribute}	: If you are having more than one deck
			- shuffle        {public method}			: To shuffle the cards with in a deck
			- deal_card      {public method}			: That will take just one card at the top 
			- deal_hand      {public method}			: Will take 2,3,5 cards and will return them
			- count          {public method}			: How many cards are left in that deck
			
		- private : Python does not support private or public explicitly. To make any thing private we need to append it with "_" char.
		
		- Encapsulation : The grouping of public and private attributes and methods into a programmatic class, making abstraction possible.
			- Exposes only the bare minimum things and access the private things using the public method.
			
		- Example : 
			- Designing the Deck class, I make cards a private attribute (a list)
			- We decide that the length of the cards should be accessed via a public method called count() -- i.e. Deck.count()
			
		- Abstraction : exposing only "relevant" data in a class interface, hiding private attributes and methods (aka the "inner workings") from users.

		- Example : 
			- As a user of the Deck class, I never call len(Deck.cards), only Deck.count() because Deck.cards is "abstracted away" for me.
			
			
			
######## 3 : Creating Classes and Instances

		- variables, function names are snake_case.
		- class name are in Camel_Case.
		- refer to person.py file.
		
			class Person:
				pass
			
			p = Person()	# This is instantiating the class.
			print(type(p))	

			

######## 4 : The __init__ method

		- Creating a Class : refer to init.py file.
		
			class Vehicle:
			
				def __init__(self, make, model, year):
					self.make = make
					self.model = model
					self.year = year
					
					
		- Classes in Python can have a special __init__ method, which gets called every time you create an instance of the class (instantiate).
		
		- Python always calls "__init__" method at the time of creating the instances. We generally initiatise the data here.
		
		- Instantiating a Class : Creating an object that is an instance of a class is called instantiating a class.
			
			v = Vehicle("Honda", "Civic", 2017)
			
			- v becomes a Honda Civic, a new instance of Vehicle
			
			
		- self : The self keyword refers to the current class instance.
			- self must always be the first parameter to __init__ and any methods and properties on class instances.
			- You never have to pass it directly when calling instance methods, including __init__.
		
			class Vehicle:
			
				def __init__(self, make, model, year):
					self.make = make
					self.model = model
					self.year = year	

		- Example :
				#############################
				>>> class user:
					def __init__(self, first, last, age):
						self.first=first
						self.last=last
						self.age=age
						print(f"Class with name {first}{last} has been initiated")
				
						
				>>> user1 = user("Sachin", "Kesarkar", 34)
				Class with name SachinKesarkar has been initiated
				#############################		
		
		
		
######## 5 : Underscores: Dunder Methods, Name Mangling, and More!
		
		- Refer to file underscores.py
		
		# _name		: Is used for private attribute.
		# __name	: Is used for name mangling in case of Inheritance.
		# __name__ 	: Its a convention to Python specific methods only. You should not declare your methods like this.	



######## 6 : Adding Instance Methods

		- Refer to user-methods.py file.
		
		
		
######## 7 : Introducing Class Attributes

		- We can also define attributes directly on a class that are shared by all instances of a class and the class itself.
		
		- Refer to user-class-attributes.py file.
		
		####### Class Attributes continued
		
		- Refer to pet.py file.
		
		
		
		
		
######## 8 : Class Methods

		- Class methods are methods (with the @classmethod decorator) that are not concerned with instances, but the class itself.
		
				######### example ########		
				class Person():
					# ...
				
					@classmethod
					def from_csv(cls, filename):
						return cls(*params) # this is the same as calling Person(*params)
				
				Person.from_csv(my_csv)
				################################
				
				- The first argument is cls (for class) instead of self. Like self, it does not need to be passed in explicitly.
				- Class methods are available on the class itself and any instances of the class, and are mostly used for building new instances of classes.
				
		- Refer to file class-methods.py file.
		
		
		
		
		
######## 9 : More Advanced Class Methods
	
		- We can setup the class method for example to input the csv data we can use Class method like User.from_string("Tom,Jones,89")
		
		- Refer to file class-methods.py file, method "User.from_string("Tom,Jones,89")".
		
		
		
		
######## 10 : The __repr__ method
	
		- String representation of a Instance of a class.
		
		- The __repr__ method is one of serveral ways to provide a nicer string representation.
		
		- for example
			j = User("judy", "steele", 18)
			j = str(j)
			print(j)		