############################### Iterators & Generators ###########################################


####### 1 : OBJECTIVES

				- Define Iterator and Iterable
				- Understand the iter() and next() methods
				- Build our own for loop
				- Define what generators are and how they can be used
				- Compare generator functions and generator expressions
				- Use generators to pause execution of expensive functions
				- Define what decorators are and how they can be used
				- Create decorators to enhance the behavior of a function
				- Explain what the wraps function is, and why it's used when writing decorators
				- Create decorators that accept arguments
				
				
				
######## 2 : Iterators vs. Iterables?!?!?

		- Iterator : an object that can be iterated upon. An object which returns data, one element at a time when next() is called on it.
						for example : iter("Oprah"), iter([1,2,3,4,5])
		
		- Iterable : An object which will return an Iterator when iter() is called on it. example : "Oprah", [1,2,3,4,5]
		
		- example :
			- "HELLO" is an iterable, but it is not an iterator.
			- iter("HELLO") returns an iterator.
			
		- NEXT : When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.
		
				######## string example ########
					>>> iterable = "Oprah"
					>>> next(iterable)
					Traceback (most recent call last):
					File "<pyshell#4>", line 1, in <module>
						next(iterable)
					TypeError: 'str' object is not an iterator
					>>> ######## This is iterable but not iterator #########
					>>> 
					>>> iterator = iter("Oprah")
					>>> next(iterator)
					'O'
					>>> ######## This is iterator #########
					>>> 
					>>> next(iterator)
					'p'
					>>> next(iterator)
					'r'
					>>> next(iterator)
					'a'
					>>> iterable
					'Oprah'
					>>> iterator
					<str_iterator object at 0x00000225156E9B38>
					>>> 
					>>> next(iterator)
					'h'
					>>> next(iterator)
					Traceback (most recent call last):
					File "<pyshell#18>", line 1, in <module>
						next(iterator)
					StopIteration

				######## list example ########
					>>> iterable_nums = [1,2,3,4,5]
					>>> next(iterable_nums)
					Traceback (most recent call last):
					File "<pyshell#35>", line 1, in <module>
						next(iterable_nums)
					TypeError: 'list' object is not an iterator
					>>> 
					>>> iterator_nums = iter(iterable_nums)
					>>> next(iterator_nums)
					1
					>>> next(iterator_nums)
					2
					>>> next(iterator_nums)
					3
					>>> next(iterator_nums)
					4
					>>> next(iterator_nums)
					5
					>>> next(iterator_nums)
					Traceback (most recent call last):
					File "<pyshell#43>", line 1, in <module>
						next(iterator_nums)
					StopIteration
					>>>


					
					
######## 3 : Writing Our Own Version of for loops

			- Refer to for.py file.
			
			
			
			
######## 4 : Writing a Custom Iterator			

			- Refer to custom-iterator.py.
			
			
		
######## 5 : Making our Deck class Iterable

			- Refer to deck.py
			
			

######## 6 : Introduction to Generators


			- Generators are iterators : They are quick way to create the iterators.
			- Generators can be created with generator functions
			- Generator functions use the yield keyword
			- Generators can be created with generator expressions		
			
			- Functions vs Generator Functions
			
				- Functions	
					- uses return
					- returns once
					- When invoked, returns the return value
				- Generator Functions
					- uses yield
					- can yield multiple times
					- When invoked, returns a generator
					
			- example
				- In below example, when we hit next() on the count, the count value is returned and it wait there. Untill we call the next() again.
				- yield creates a generator object, and return the generator object.
				
						>>> def count_up_to(max):
							count = 1
							while count <= max:
								yield count
								count += 1
						
								
						>>> counter = count_up_to(5)
						>>> counter
						<generator object count_up_to at 0x000002021074FE08>
						>>> next(counter)
						1
						>>> next(counter)
						2
						>>> next(counter)
						3
						>>> next(counter)
						4
						>>> next(counter)
						5
						>>> next(counter)
						Traceback (most recent call last):
						File "<pyshell#10>", line 1, in <module>
							next(counter)
						StopIteration
						
				- Here is keep the most recent yield, stop and return it again after we call next. We keep going untill we get exception StopIteraton.
				
						>>> counter = count_up_to(10)
						>>> next(counter)
						1
						>>> next(counter)
						2
						>>> for num in counter:
							print(num)
						
							
						3
						4
						5
						6
						7
						8
						9
						10
						>>>	
								
				- Here it goes to every item and creates a list.

						>>> counter = count_up_to(10)
						>>> list(counter)
						[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]				
			
			
			- Exhausting a Generator
					- Calling next on a generator with nothing left to yield will throw a StopIteration error
					- When we loop over a generator, the loop will stop before the StopIteration error gets thrown			
			
			
######## 7 : Writing a Beat Making Generator

			- Refer to inifinite.py file.
			
			


######## 8 : Testing Memory Usage With Generators

			- Refer to fib.py file.
			
			

######## 9 : Generator Expressions AND Speed Testing!
		
		- Similar to List comprehension on a single line for a list, generator expressions if for creating a generator object on a single list.
		
		
		- You can also create generators from generator expressions
		- Generator expressions look a lot like list comprehensions
		- Generator expressions use () instead of []
		
		
		- Generator expresions means Generator comprehension.
		- example:
		
			- Simple generator
			>>> def nums():
				for num in range(1,10):
					yield num
			
					
			>>> g1 = nums()
			>>> g1
			<generator object nums at 0x000002021074FE08>	# This is a generator object.
			>>> next(g1)
			2
			>>> next(g1)
			3
			>>> next(g1)
			4
			>>> 
			>>> g2 = (num for num in range(1,10))
			>>> g2
			<generator object <genexpr> at 0x000002021074FF68>	# This is a generator expression.
			>>> 
			>>> next(g2)
			1
			>>> next(g2)
			2
			>>> next(g2)
			3
			>>> sum([num for num in range(1,10)])		# We are using list comprehension
			45
			>>> sum(num for num in range(1,10))			# we are using a generator expresions/comprehension here.
			45
			
			
		- Refer to gen-expression-speed-test.py file.