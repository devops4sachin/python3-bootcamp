# Let's define a speed_test decorator
import time
from functools import wraps

def timecal(fn):
	
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = fn(*args, **kwargs)		# don't return here, otherwise the below statement won't be printed in the output.
		total_time = time.time() - start_time
		print(f"time taken by {fn.__name__} is {total_time} ")
		return result
	return wrapper
	
@timecal
def list_comprehention(num):
	return sum([n for n in range(num)])
	
@timecal
def generator(num):
	return sum((n for n in range(num)))
	
print(list_comprehention(1000000))

print(generator(1000000))



#################### output #####################
#C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\5_Decorators>python test.py
#time taken by list_comprehention is 0.11392521858215332
#499999500000
#time taken by generator is 0.1002812385559082
#499999500000