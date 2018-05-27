from functools import wraps

def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No Kwargs allowed")
		return fn(*args, **kwargs)
	return wrapper
	
	
@ensure_no_kwargs
def greet(name):
	print(f"Hi there {name}")
	
	
greet("Sachin")

# greet(name="Sachin")

###### This raises ########
# C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\5_Decorators>python test.py
# Hi there Sachin
# Traceback (most recent call last):
#   File "test.py", line 19, in <module>
#     greet(name="Sachin")
#   File "test.py", line 7, in wrapper
#     raise ValueError("No Kwargs allowed")
# ValueError: No Kwargs allowed