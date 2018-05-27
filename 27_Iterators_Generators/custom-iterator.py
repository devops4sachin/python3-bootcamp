class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):			# It defines the iter() method for our class. It makes our class iterable and not iterator.
		return self				# It uses the __next__() function.
		# return iter("hello")

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1		# This could also be customized to increase by 2,3.... so on.
			return num
			# return 1
		raise StopIteration




for x in Counter(50,70):
	print(x)