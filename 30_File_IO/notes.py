########################## File IO #############################

###### 1 : Introduction

	- Objectives :
	
		- Read text files in Python
		- Write text files in Python
		- Use "with" blocks when reading / writing files
		- Describe the different ways to open a file
		- Read CSV files in Python
		- Write CSV files in Python
		
		
		
###### 2, 3 : Reading Text Files: Open and Read, Reading Files: Seek and Cursors

	- Cursor Movement
		- Python reads files by using a cursor
		- This is like the cursor you see when you're typing
		- After a file is read, the cursor is at the end
		- To move the cursor, use the seek method
		- To read only part of a file, pass a number of characters into read, or use readline
		- To get a list of all lines, use readlines
		
	
	- Reading and seeking a file.
	
			>>> file = open('story.txt')
			>>> file.read()
			'This short story is really short.\nNow its a little longer.\nThe end.'
			>>> file
			<_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>
			>>>
			>>> file.seek(0)
			0
			>>>
			>>> file.read()
			'This short story is really short.\nNow its a little longer.\nThe end.'
			>>> file.seek(30)
			30
			>>> file.read()
			'rt.\nNow its a little longer.\nThe end.'
			>>> file.read()
			''

	- Reading a single line.
	
			>>> file.readline()
			'This short story is really short.\n'
			>>> file.readline()
			'Now its a little longer.\n'
			>>> file.readline()
			'The end.'
			>>> file.readline()
			''
			>>>
			>>> file.seek(0)
			0
			>>>

	- Reading multiple lines.
	
			>>> file.readlines()
			['This short story is really short.\n', 'Now its a little longer.\n', 'The end.']
			>>>
			>>> file.seek(0)
			0
			>>>
			>>> lines = file.readlines()
			>>> for line in lines:
			...     print(line)
			...
			This short story is really short.
			
			Now its a little longer.
			
			The end.
			>>>

	- Closing the file and checking if closed.
	
			>>>
			>>> file.closed
			False
			>>> file.close()
			>>> file.closed
			True
			>>> file.read()
			Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
			ValueError: I/O operation on closed file.
			>>> file.seek(0)
			Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
			ValueError: I/O operation on closed file.
			
			
			
			
###### 4 : The With Statement


	- Reading a file using "with" statement.

			>>> with open("story.txt") as f:
			...     data = f.read()
			...
			>>> f.closed
			True
			>>> f.read()
			Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
			ValueError: I/O operation on closed file.
			>>>
			>>> data
			'This short story is really short.\nNow its a little longer.\nThe end.'
			>>>
			>>>
			>>> f = open("story.txt")
			>>> f.__enter__()
			<_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>
			>>> f.closed
			False
			>>> f.__exit__()
			>>> f.closed
			True
			>>>
			>>> ##### Any time "with" is called __enter__ is going to be called.
			... ##### Same we can use it with the Class also
			...
			
			
####### 5 : Writing to Text Files

	- You can also use open to write to a file
	- Need to specify the "w" flag as the second argument
	- IMPORTANT: If you open the file again to write, the original contents will be deleted!
	- You can write to an existing file or a non-existing file and it will be created.
	
		>>> with open("haiku.txt", "w") as file:
		...     file.write("text1 \n")
		...     file.write("text2 \n")
		...     file.write("text3 \n")
		...
		7
		7
		7

	- Reading in a list format
		>>> with open("haiku.txt") as f:
		...     data = f.readlines()
		...
		>>> data
		['text1 \n', 'text2 \n', 'text3 \n']
		
	- Reading a single line
		>>> with open("haiku.txt") as f:
		...     data = f.readline()
		...
		>>> data
		'text1 \n'
		
	- Reading all the lines.
		>>> with open("haiku.txt") as f:
		...     data = f.read()
		...
		>>> data
		'text1 \ntext2 \ntext3 \n'
		>>>
		
	- Refer to write.py file.	
		
####### 6 : File Modes

	- Modes for Opening Files

		r - Read a file (no writing) - this is the default
		w - Write to a file (previous contents removed)
		a - Append to a file (previous contents not removed)
		r+ - Read and write to a file (writing based on cursor)
		
		
	- Refer to "haiku.txt" file.