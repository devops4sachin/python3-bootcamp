####################### OOP Part 2 #######################


####### 1 : Inheritance and Objectives

		- Objectives
			- Implement inheritance, including multiple
			- Understand Method Resolution Order
			- Understand polymorphism
			- Add special methods to classes
			
		- Example : On reditt each account is a normal user, but for each subreditt there are moderator who moderate the cotents like remove,edit required things.
				On above subreditt there are more users like Admin users. Who can do any thing on any subreditt account. Thus we can have 3 classes here User, ModeratorUser, AdminUser.
					- Thus ModeratorUser and AdminUser can inherit properties from User Base class.
				
		- A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).
		
		- In Python, inheritance works by passing the parent class as an argument to the definition of a child class:
		
			#	class Animal:
			#		def make_sound(self, sound):
			#			print(sound)
			#	
			#		cool = True
			#	
			#	class Cat(Animal):
			#		pass
			#	
			#	gandalf = Cat()
			#	gandalf.make_sound("meow")  # meow
			#	gandalf.cool  # True		
			
			
		- Refer to "simple-inheritance.py" method.
			
			
			
####### 2 : All About Properties

		- Refer to file human.py.
		
		
		
####### 3 : Introduction to Super()

		- Refer to animal.py file.
		
		
		
####### 4 : Inheritance Example: User and Moderator

		- Replicating the scenario of the social network.
		
		- Refer to users.py file.
		

		
		
####### 5 : The Crazy World of Multiple Inheritance

		- Refer to animals.py file.
		

		
####### 6 : WTF is Method Resolution Order(MRO)

		- Refer to animals.py file

			jaws = Aquatic("Jaws")
			lassie = Ambulatory("Lassie")
			captain_cook = Penguin("Captain Cook")
			jaws.swim() # 'Jaws is swimming'
			jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
			jaws.greet() # 'I am Jaws of the sea!'
			
			lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
			lassie.walk() # 'Lassie is walking'
			lassie.greet() # 'I am Lassie of the land!'
			
			captain_cook.swim() # 'Captain Cook is swimming'
			captain_cook.walk() # 'Captain Cook is walking'
			captain_cook.greet() # 'I am Captain Cook of the sea!'

		- What about the greet method for our instance of Penguin?
			It is calling the Aquatic.greet() instead of Ambulatory.greet().
			
		- Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, which is the order in which Python will look for methods on instances of that class.
			- You can programmatically reference the MRO three ways:
				* __mro__ attribute on the class
				* use the mro() method on the class
				* use the builtin help(cls) method
				
					# Penguin.__mro__ 
					# 
					# # (<class 'multiple.Penguin'>, <class 'multiple.Aquatic'>, 
					# #  <class 'multiple.Ambulatory'>, <class 'object'>)
					# 
					# Penguin.mro() 
					# 
					# # [__main__.Penguin, __main__.Aquatic, __main__.Ambulatory, object]
					# 
					# help(Penguin) # best for HUMAN readability -> gives us a detailed chain 
				
				- This can be used at the time of programming.
				
				
		- Refer to mro.py file.
		
		
		
		
####### 7 : Polymorphism Introduction


		- Polymorphism :
		
			- A key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph).
			
			- While a formal definition of polymorphism is more difficult, here are two important practical applications:
			
				1. The same class method works in a similar way for different classes
					
					Cat.speak()  # meow
					Dog.speak()  # woof
					Human.speak()  # yo
					
					
				2. The same operation works for different kinds of objects
				
					sample_list = [1,2,3]
					sample_tuple = (1,2,3)
					sample_string = "awesome"
					
					len(sample_list)
					len(sample_tuple)
					len(sample_string)				
					
					
		- Polymorphism & Inheritance :
			
			1. The same class method works in a similar way for different classes
				
				- A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. This is called method overriding.
				
					class Animal():
						def speak(self):
							raise NotImplementedError("Subclass needs to implement this method")
					
					class Dog(Animal):
						def speak(self):
							return "woof"
					
					class Cat(Animal):
						def speak(self):
							return "meow"	
								
				- Each subclass will have a different implementation of the method.
				- If the method is not implemented in the subclass, the version in the parent class is called instead.
				
				
		- Special Methods :
			
			2. (Polymorphism) The same operation works for different kinds of objects
				
				- How does the following work in Python?
					
					8 + 2  # 10
					"8" + "2"  # 82
					
						- The answer is "special methods"!
						
				- Python classes have special (also known as "magic") methods, that are dunders (i.e. double underscore-named). 
				- These are methods with special names that give instructions to Python for how to deal with objects.
				
		

		
####### 8 : Special __magic__ methods


		- Special Methods Example
		
			- What is happening in our example?
				8 + 2  # 10
				"8" + "2"  # 82
		
			- The + operator is shorthand for a special method called __add__() that gets called on the first operand.
			- If the first (left) operand is an instance of int, __add__() does mathematical addition. If it's a string, it does string concatenation.
		
		
		- Special Methods Applied
			
			- Therefore, you can declare special methods on your own classes to mimic the behavior of builtin objects, like so using __len__:
			
					class Human:
						def __init__(self, height):
							self.height = height  # in inches
					
						def __len__(self):
							return self.height	

		
		- String Representation
		
			- The most common use-case for special methods is to make classes "look pretty" in strings.
			- By default, our classes look ugly:
			
					class Human:
						pass
					
					colt = Human()
					print(colt)  # <__main__.Human at 0x1062b8400>

			- We can use special methods to make it look way better!
			
			
			
		- String Representation Example
		
			- The __repr__ method is one of several ways to provide a nicer string representation.
			
			
					class Human:
					
						def __init__(self, name="somebody"):
							self.name = name
					
						def __repr__(self):
							return self.name
							
					dude = Human()
					print(dude)  # "somebody"
					colt = Human(name="Colt Steele")
					print(f"{colt} is totally rad (probably)") 
					# "Colt Steele is totally rad (probably)"
					
			- There are also several other dunders to return classes in string formats (notably __str__ and __format__), and choosing one is a bit complicated!
			
			
		
		- Example : Refer to special-methods.py file.
			
		

		
		
####### 9 : Making a Grumpy Dictionary - Overriding Dict

			- Refer to grumpy.py file.
