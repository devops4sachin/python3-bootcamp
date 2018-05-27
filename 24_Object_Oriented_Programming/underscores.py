# _name		: Is used for private attribute.
# __name	: Is used for name mangling in case of Inheritance.
# __name__ 	: Its a convention to Python specific methods only. You should not declare your methods like this.


class Person:
	# Init is a "dunder" method
    def __init__(self):
        self.name = "Tony"
        # single underscore means "private" (sort of)
        self._secret = "hi!"
        # two leading underscores tells Python to "mangle" the name
        self.__msg = "I like turtles!"
        self.__lol = "HAHAHAHAH"


p = Person()

print(p.name)
print(p._secret) #Anyone can still directly access the attribute. Both will be printed.
				 # "_" is simply a convention, to tell developer about the private attribute/method in python.
				 # There is no such thing as private attribute or method in python. Other language supports them.
				 
# the double underscore "__" does something else.				 

print(dir(p)) # Notice what __msg and __lol have been "mangled" to.
			  # They are mangled to "_Person__lol" and "_Person__msg"

print(p._Person__msg)	# Its the way to access them, in a mangled form.
print(p._Person__lol)	# Its sole purpose is to make this attribute particular to class "Person". Usually used in Inheritance.
						# If Person is inherited by SalesPerson and if both are having the attribute "__msg". Then in that it is used.
