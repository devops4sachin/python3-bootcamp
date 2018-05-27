############################### Decorators ###########################################

####### 1 : Higher Order Functions

		- Refer to higher_order.py, return_func.py, nested_functions.py
		

####### 2 : Introduction to Decorators

		- Decorators are functions
		- Decorators wrap other functions and enhance their behavior
		- Decorators are examples of higher order functions
		- Decorators have their own syntax, using "@" (syntactic sugar)
		
		- Decorator is fucntion, which does something then call the other function and after that does something.

			- Decorators as Functions
			
			def be_polite(fn):
				def wrapper():
					print("What a pleasure to meet you!")
					fn()
					print("Have a great day!")
				return wrapper
			
			def greet():
				print("My name is Colt.")
			
			greet1 = be_polite(greet)
			# we are decorating our function 
			# with politeness!		

			
			- Decorator Syntax
			
			def be_polite(fn):
				def wrapper():
					print("What a pleasure to meet you!")
					fn()
					print("Have a great day!")
				return wrapper
			
			@be_polite
			def greet():
				print("My name is Matt.")
			
			# we don't need to set, greet = be_polite(greet) here.
			
			- Refer to dec.py and decorate_syntax.py file.
			
####### 3 : Decorators With Different Signatures

		
		- Functions with Different Signatures.
			
			- We get a issue here for function order, because wrapper has a different signature here.
		
				def shout(fn):
					def wrapper(name):
						return fn(name).upper()
					return wrapper
				
				@shout
				def greet(name):
					return f"Hi, I'm {name}."
				
				@shout
				def order(main, side):		# We get a issue here, because wrapper has a different signature here.
					return f"Hi, I'd like the {main}, with a side of {side}, please."
				
			
			- Decorator Pattern

				def my_decorator(fn):
					def wrapper(*args, **kwargs):
						# do some stuff with fn(*args, **kwargs)
						pass
					return wrapper
					
			- corrected example.
			
				def shout(fn):
					def wrapper(*args, **kwargs):
						return fn(*args, **kwargs).upper()
					return wrapper
					
				@shout
				def greet(name):
					return f"Hi my name is {name}"
					
				@shout
				def order(order, side):
					return f"Hi, I'd like to have {order}, with the side as {side}"
					
				@shout
				def lol():
					return "lol"
					
				print(greet("Sachin"))
				
				print(order("burger","fries"))

		- Refer to decorator_args.py file.

		
####### 4 : Using Wraps To Preserve Metadata			
		
		- We usethe wraps to use the functions documentation.
		- from functools import wraps
		
		- Refer to metadata.py file.
		
		
		- Refer to timing.py file.
		
		
		
		
		
####### 5 : Another Example: Ensuring Args With A Decorator

		- Refer to ensure.py file.
		
		
		
		
####### 6 : Writing an ensure_first_arg_is Decorator

		- Decorator that take an arguments.
		
		- Refer to args.py file for notes.
		
		- Refer to ensure-first-arg.py file.



####### 7 : Enforcing Argument Types With A Decorator
			
		- Refer to enforce.py file.