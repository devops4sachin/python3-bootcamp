# Lame function that returns a list of beats.  
# Only runs 100 times
def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0			# set i to 0 when it > 4
		result.append(nums[i])
		i += 1
	return result

# Infinite Generator - returns one beat a time, no list used!
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0			# set i to 0 when it > 4
		yield nums[i]
		i += 1


		
############################# output ################################
>>> def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0		# set i to 0 when it > 4
		result.append(nums[i])
		i += 1
	return result

>>> current_beat()
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

- Here is returns all the four number in repitition at once.
############### second similar generator function ###############
>>> def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

		
>>> counter = current_beat()
>>> next(counter)
1
>>> next(counter)
2
>>> next(counter)
3
>>> next(counter)
4
>>> next(counter)
1
>>> next(counter)
2
>>> next(counter)
3

- Here we have to call because of which we can keep control on it.
