def enforce(*types):
	def inner(fn):
		def wrapper(*args, **kwargs):
			# convert args into something mutable
			newargs = []
			for (arg, typ) in zip(args, types):
				newargs.append( typ(arg) )
			return fn(*newargs, **kwargs)
		return wrapper
	return inner
	
	
@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)
		
		
repeat_msg("Hello", "3")

# ("hello", str) ('3', int)

# ["hello", 3] = newargs

@enforce(float, float)
def divide(a,b):
	print (a/b)

divide("2", "4")

########### output ############
# C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\5_Decorators>python test.py
# Hello
# Hello
# Hello
# 0.5