#########################	Debugging and Error Handling    #########################

###### 2 : Common types of errors

		- SyntaxError : Occurs when Python encounters incorrect syntax (something it doesn't parse).
				
				>>> def first: # SyntaxError
				>>> None = 1 # SyntaxError
				>>> return # SyntaxError


		- NameError : This occurs when a variable is not defined, i.e. it hasn't been assigned.
		
				>>> test
				# NameError: name 'test' is not defined
				
				
		- TypeError : Occurs when, An operation or function is applied to the wrong type OR Python cannot interpret an operation on two data types.
		
				>>> len(5)  
				# TypeError: object of type 'int' has no len()
				
				>>> "awesome" + []  
				# TypeError: cannot concatenate 'str' and 'list' objects
				
		
		- IndexError : When you try to access an element in a list using an invalid index (i.e. one that is outside the range of the list or string):
		
				>>> list = ["hello"]
				>>> list[2]
				# IndexError: list index out of range
				
			
		- ValueError : Occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value.
		
				>>> int("foo")
				# ValueError: invalid literal for int() with base 10: 'foo'
		
		
		- KeyError : This occurs when a dictionary does not have a specific key.
				
				d = {}
				d["foo"]
				# KeyError: 'foo'
				
				
		
		- AttributeError : This occurs when a variable does not have an attribute.
		
				>>> 'len'.upper()
				'LEN'
				>>> 'awesome'.foo()
				# AttributeError: 'str' object has no attribute 'foo'
				
				
###### 3 : Raise Your Own Exception!
			
			- we can also throw errors using the "raise" keyword. This is helpful when creating your own kinds of exception and error messages.
			
			>>> raise ValueError('invalid value')
			# ValueError: invalid value

			
			- Another Example :
			
			def colorize(text, color):
				colors = ("cyan", "yellow", "blue", "green", "magenta")
				if type(text) is not str:
					raise TypeError("text must be instance of str")
				if color not in colors:
					raise ValueError("color is invalid color")
				print(f"Printed {text} in {color}")
			
			>>> colorize([], 'cyan')
			Traceback (most recent call last):
			File "<pyshell#33>", line 1, in <module>
				colorize([], 'cyan')
			File "<pyshell#32>", line 4, in colorize
				raise TypeError("text must be instance of str")
			TypeError: text must be instance of str
			
			>>> colorize('value', "red")
			Traceback (most recent call last):
			File "<pyshell#38>", line 1, in <module>
				colorize('value', "red")
			File "<pyshell#32>", line 6, in colorize
				raise ValueError("color is invalid color")
			ValueError: color is invalid color			

			
###### 4 : Try and Except Blocks.
		
			- Handle Errors = It is strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them.
			
				try: 
					foobar
				except NameError as err:
					print(err)			
					
					
			- Try to "catch" specific errors only and not all of them. Below is the wrong example.

				try: 
					colt
				except:
					print("You tried to use a variable that was never declared!")


			- Catching specific error ony as below.
			
				try: 
					colt
				except NameError:
					print("You tried to use a variable that was never declared!")


			- ​If you want to except a handful of exceptions, you can pass a tuple of errors into the except block as well.
			
				try: 
					colt.hello
				except (TypeError, AttributeError):
					print("That doesn't work with this thing.")

			
			- Another example :
			
				>>> def get(d,key):
					try:
						return d[key]
					except KeyError:
						return None
				>>> d = {"name": "Ricky"}
				>>> print(get(d, "city"))
				None		
			
			
			
			
###### 4 : Try, Except, Else and Finally!

		- Example login.
		
				while True:
					try:
						num = int(input("please enter a number: "))
					except ValueError:
						print("That's not a number!")
					else:
						print("Good job, you entered a number!")
						break
					finally:
						print("RUNS NO MATTER WHAT!")		<<<< This block run's always no matter if the exception is caught or not.
				print("REST OF GAME LOGIC RUNS!")
				
				
				please enter a number: sd
				That's not a number!
				RUNS NO MATTER WHAT!
				please enter a number: 
				That's not a number!
				RUNS NO MATTER WHAT!
				please enter a number: 12
				Good job, you entered a number!
				RUNS NO MATTER WHAT!
				REST OF GAME LOGIC RUNS!		
				
				
				
		- Another Example.
				>>> def divide(a,b):
					try:
						result = a/b
					except (ZeroDivisionError, TypeError) as err:
						print("Something went wrong!")
						print(err)
					else:
						print(f"{a} divided by {b} is {result}")
				
						
				>>> print(divide(1,'a'))
				Something went wrong!
				unsupported operand type(s) for /: 'int' and 'str'
				None
				>>> print(divide(1,0))
				Something went wrong!
				division by zero
				None
				>>> print(divide(1,2))
				1 divided by 2 is 0.5
				None
				>>> 		
				
				
				
###### 5 : Debugging with PDB "pdb".
# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list) : It shows where are you in the debugging.
# n (next line) : n (enter)
# p (print) : p var_name (enter)
# c (continue - finishes debugging)


		- Example : contents of "debug.py"
		
				import pdb
				first = "First"
				second = "Second"
				pdb.set_trace()
				result = first + second
				third = "Third"
				result += third
				print(result)
		- output :
					c:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO>python debug.py
					> c:\sachin_folder\pdf's books\python\python3\git_repo\debug.py(5)<module>()
					-> result = first + second
					(Pdb) p first
					'First'
					(Pdb) p second
					'Second'
					(Pdb) n
					> c:\sachin_folder\pdf's books\python\python3\git_repo\debug.py(6)<module>()
					-> third = "Third"
					(Pdb) p third
					*** NameError: name 'third' is not defined
					(Pdb) n
					> c:\sachin_folder\pdf's books\python\python3\git_repo\debug.py(7)<module>()
					-> result += third
					(Pdb) p result
					'FirstSecond'
					(Pdb) n
					> c:\sachin_folder\pdf's books\python\python3\git_repo\debug.py(8)<module>()
					-> print(result)
					(Pdb) n
					FirstSecondThird
					--Return--
					> c:\sachin_folder\pdf's books\python\python3\git_repo\debug.py(8)<module>()->None
					-> print(result)
					(Pdb) p third
					'Third'
					(Pdb) n
					--Call--

# Be careful with variable names!
# c : variable name that conflict with command. use >>> p c					
		- Example : Contents of other file.
					def add_numbers(a, b, c, d):
						import pdb; pdb.set_trace() 
					
						return a + b + c + d
					add_numbers(1,2,3,4)		
		- output :
					c:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO>python debug.py
					> c:\sachin_folder\pdf's books\python\python3\git_repo\debug.py(4)add_numbers()
					-> return a + b + c + d
					(Pdb) p a
					1
					(Pdb) p b
					2
					(Pdb) p c
					3
					(Pdb) p d
					4
					(Pdb) c		