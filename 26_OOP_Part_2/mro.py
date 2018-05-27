class A:
	def do_something(self):
		print("Method defined in: A")
		
class B(A):
	def do_something(self):
		print("Method defined in: B")
		super().do_something()
		
class C(A):
	def do_something(self):
		print("Method defined in: C")
		
class D(B,C):
	def do_something(self):
		print("Method defined in: D")
		super().do_something()
		
thing = D()
thing.do_something()

	#		A
	#	   / \
	#	   B  C
	#	    \ /
	#		 D
	
	
print(D.__mro__)
print(D.mro())


help(D)

####################################### output ########################################
# Method defined in: D
# Method defined in: B
# Method defined in: C
#C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\3_OOP Part 2>python mro.py
#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#Help on class D in module __main__:
#
#class D(B, C)
# |  Method resolution order:
# |      D
# |      B
# |      C
# |      A
# |      builtins.object
# |
# |  Methods inherited from B:
# |
# |  do_something(self)
# |
# |  ----------------------------------------------------------------------
# |  Data descriptors inherited from A:
# |
# |  __dict__
# |      dictionary for instance variables (if defined)
# |
# |  __weakref__
# |      list of weak references to the object (if defined)
# 

# ####################################### output ########################################