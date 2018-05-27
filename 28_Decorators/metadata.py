def log_function_data(fn):
	def wrapper(*args, **kwargs):
		""" I AM A WRAPPER FUNCTION """
		print(f"you are about to call {fn.__name__}")
		print(f"Here's the documentation {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper
	
@log_function_data
def add(x, y):
	""" THIS A FUNCTION TO ADD """
	return x*y
	
print(add.__name__)
print(add.__doc__)

################ output #############
C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\5_Decorators>python test.py
wrapper
 I AM A WRAPPER FUNCTION
 ####################################
 
 ### To get the correct output we use @wraps(fn) here.

#######################################################################################

from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)
help(add)
