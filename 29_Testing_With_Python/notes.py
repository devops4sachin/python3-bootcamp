########################## Testing With Python #############################

#### Search on this, explaination is not good.

###### 1 : Section Introduction

	- Describe what tests are and why they are essential
	- Explain what Test Driven Development is
	- Test Python code using doctests
	- Test Python code using assert
	- Explain what unit testing is
	- Write unit tests using the unittest module
	- Remove code duplication using before and after hooks
	
	
	
###### 2 : Why Test?

		- Reduce bugs in existing code
		- Ensure bugs that are fixed stay fixed
		- Ensure that new features don't break old ones
		- Ensure that cleaning up code doesn't introduce new bugs
		- Makes development more fun!
	
	- Test Driven Development
	
		- Development begins by writing tests
		- Once tests are written, write code to make tests pass
		- Once tests pass, a feature is considered complete
		
	- Red, Green, Refactor
	
		- Red - Write a test that fails
		- Green - Write the minimal amount of code necessary to make the test pass
		- Refactor - Clean up the code, while ensuring that tests still pass
		
		
		
####### 3 : Assertions

		- We can make simple assertions with the assert keyword
		- assert accepts an expression
		- Returns None if the expression is truthy
		- Raises an AssertionError if the expression is falsy
		- Accepts an optional error message as a second argument
		
		syntax :
			assert expression, "message for assertion"
			
		- Refer to assertions.py file.
		
		- if you want to ignore assertions the you can invoke below command. If a Python file is run with the -O flag, assertions will not be evaluated!
			# python -O assertions.py
			
			
	
	
###### 4 : Before and after hooks

	- setUp and tearDown
		- For larger applications, you may want similar application state before running tests
		- setUp runs before each test method : for example loading sample data in the database.
		- tearDown runs after each test method : removing the sample data once the testing is done.
		- Common use cases: adding/removing data from a test database, creating instances of a class
		
		
			class SomeTests(unittest.TestCase):
			
				def setUp(self):
					# do setup here
					pass
			
				def test_first(self):
					# setUp runs before
					# tearDown runs after
					pass
			
				def test_second(self):
					# setUp runs before
					# tearDown runs after
					pass
			
				def tearDown(self):
					# do teardown here
					pass
					
					
		- Refer to robot.py and robot-tests.py file.
		
		
		
####### 5 : Testing Card/Deck Solution

		- Refer to udemy lectures.
			
####### 4 : Doctests

	- We can write tests for functions inside of the docstring
	- Write code that looks like it's inside of a REPL
	
	- you write a test with in the documentation as below. It should match exactly the same.
	
		def add(x, y):
			"""add together x and y
		
			>>> add(1, 2)
			3
		
			>>> add(8, "hi")
			Traceback (most recent call last):
				...
			TypeError: unsupported operand type(s) for +: 'int' and 'str'
			"""
		
		- Run these tests with: 
			python3 -m doctest -v YOUR_FILE_NAME.py
			
		- This is called TDD.
		
	- Issues with doctests
		- Syntax is a little strange
		- Clutters up our function code
		- Lacks many features of larger testing tools
		- Tests can be brittle
		
		

####### 5 : Introduction to Unittest
	
	- This is the most popular and mostly used one. Its more powerful.
	
	- Test smallest parts of an application in isolation (e.g. units)
	- Good candidates for unit testing: individual classes, modules, or functions
	- Bad candidates for unit testing: an entire application, dependencies across several classes or modules
	
	- unittest 
		- Python comes with a built-in module called unittest
		- You can write unit tests encapsulated as classes that inherit from unittest.TestCase
		- This inheritance gives you access to many assertion helpers that let you test the behavior of your functions
		- You can run tests by calling unittest.main()
		
		- Refer to activities.py and tests.py file.
		
	- To see comments, run : python NAME_OF_TEST_FILE.py -v
	
	
	
###### 6 : Other Types of Assertions

	- Types of Assertions
		- self.assertEqual(x, y)
		- self.assertNotEqual(x, y)
		- self.assertTrue(x)
		- self.assertFalse(x)
		- self.assertIsNone(x)
		- self.assertIsNotNone(x)
		- self.assertIn(x, y)
		- self.assertNotIn(x, y)
		- ...and more!