#########################	Modules    #########################

###### 1 : Introduction

	- Objectives :
			Define what a module is
			Import code from built-in modules
			Import code from other files
			Import code from external modules using pip 
			Describe common module patterns
			Describe the request/response cycle in HTTP
			Use the requests module to make requests to web apps	


			
###### 2 : Working with Built-In Modules

	- Why use modules
			Keep Python files small
			Reuse code across multiple files by importing
			A module is just a Python file!

	- Example :
				>>> import random
				>>> random.choice(["apple", "banana", "cherry", "durian"])
				'banana'
				>>> random.shuffle(["apple", "banana", "cherry", "durian"])
				>>> print(random.randint(1, 100))
				48	

	- Alias the module names using "as", just to prevent typing the long names of the module.
				>>> import random as rand
				>>> rand.choice(["apple", "banana", "cherry", "durian"])
				'apple'
				>>> rand.randint(1, 100)
				39
				
				
	- Importing parts of module :
			- The from keyword lets you import parts of a module
			- Handy rule of thumb: only import what you need!
			- If you still want to import everything, you can also use the "from MODULE import *" pattern
			
				>>> from random import choice, randint
				>>> choice(["apple", "banana", "cherry", "durian"])
				'banana'
				>>> randint(1,100)
				49			

			- Other option can be :
			
				>>> from random import choice as gimme_one, shuffle as mix_up_fruits
			
			
			
###### 3 : Custom Modules

			- You can import from your own code too
			- The syntax is the same as before
			- import from the name of the Python file
			
			- Example :
			########## file1.py #############
			def fn():
				return "do some stuff"
			
			def other_fn():
				return "do some other stuff"
			
			######### file2.py #############
			import file1
			
			file1.fn() # 'do some stuff'
			
			file2.fn() # 'do some other stuff'
			##################################
			
			
			
###### 4 : External Modules

		- PyPI : Python Package Index
		
		- Built-in modules come with Python
		- External modules are downloaded from the internet
		- You can download external modules using pip

		- pip : Package management system for Python
			- As of 3.4, comes with Python by default
			
			# python3 -m pip install NAME_OF_PACKAGE
			
			
# python3 -m pip install termcolor


		- "dir" gives the list of attributes of a libraries that we can use.
			>>> import termcolor
			>>> dir(termcolor)
			['ATTRIBUTES', 'COLORS', 'HIGHLIGHTS', 'RESET', 'VERSION', '__ALL__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'colored', 'cprint', 'os', 'print_function']			
			
		- If you don't get much details, you can use help(termcolor) as well.
		
				>>> from termcolor import colored
				>>> text = colored("HI THERE !!", color="magenta", on_color="on_cyan", attrs=["blink"])
				>>> print(text)

		
		- Another example :
		
				# python -m pip install pyfiglet
				Collecting pyfiglet
				Downloading pyfiglet-0.7.5.tar.gz (767kB)
					100% |████████████████████████████████| 768kB 729kB/s
				Installing collected packages: pyfiglet
				
		- Refer to my_ascii_art.py example.
		
		
		
		
		
###### 5 : Using The autopep8 Package to Clean Up Code

		- This package is used for auto-formatting the python code.
		
		# python -m pip install autopep8
		
		# autopep8 --in-place ugly_code.py
		
		
		
		
###### 6 : The Mysterious __name__ variable

			- When run, every Python file has a __name__ variable
			- If the file is the main file being run, its value is "__main__"
			- Otherwise, its value is the file name
			
			
			- If we execute the "name.py" file then we get following output.
					$ python.exe .\name.py
					Say Sup! My __name__ is say_sup
					Hi! My __name__ is __main__
					Say Sup! My __name__ is say_sup	
					
					- The value of __name__ is the name of the file which is being run.
					- The first "say_sup" is executed at the time of the import of the code. Thus the code is also executed at the time of the import. You can set the condition to run the code only when "__name__=__main__"
					
					
			- import Revisited : When you use import, then Python does below things.
				- Tries to find the module (if it fails, it throws an error),
				- Runs the code inside of the module being imported,
				- Creates variables in the namespace of the file with the import statement.
				
			- Ignoring Code on Import
				if __name__ == "__main__":
					# this code will only run
					# if the file is the main file!			