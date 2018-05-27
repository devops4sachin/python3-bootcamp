# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
with open("fighters.csv") as file:
    data = file.read()
############## Don't use this ##########

# Using reader, reading the full line
from csv import reader
with open("fighters.csv") as file:
	csv_reader = reader(file)
	for fighter in csv_reader:
		print(fighter)			
		
############ output ##########
#C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\8_Working With CSV and Pickling!>python try.py
#['Name', 'Country', 'Height (in cm)']	<<<< It reads the header as well as a list.
#['Ryu', 'Japan', '175']
#['Ken', 'USA', '175']
#['Chun-Li', 'China', '165']
#['Guile', 'USA', '182']
#['E. Honda', 'Japan', '185']
#['Dhalsim', 'India', '176']
#['Blanka', 'Brazil', '192']
#['Zangief', 'Russia', '214']


# Using reader
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) 			#To skip the headers
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}")
		
############ output ###########
C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\8_Working With CSV and Pickling!>python try.py
Ryu is from country Japan
Ken is from country USA
Chun-Li is from country China
Guile is from country USA
E. Honda is from country Japan
Dhalsim is from country India
Blanka is from country Brazil
Zangief is from country Russia



# Example where data is cast into a list, if you want to have access to the data later after completion of the cursor.
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)			# Please note that csv_reader is an iterator, once it iterates you cannot read the data again.
    data = list(csv_reader)
    print(data)
	
###### output ######
C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\8_Working With CSV and Pickling!>python try.py
[['Name', 'Country', 'Height (in cm)'], ['Ryu', 'Japan', '175'], ['Ken', 'USA', '175'], ['Chun-Li', 'China', '165'], ['Guile', 'USA', '182'], ['E. Honda', 'Japan', '185'], ['Dhalsim', 'India', '176'], ['Blanka', 'Brazil', '192'], ['Zangief', 'Russia', '214']]
	
	



# Reading/Parsing CSV Using a DictReader:
from csv import DictReader

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		print(row)
		

###### output ######		
# C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\8_Working With CSV and Pickling!>python try.py
# OrderedDict([('Name', 'Ryu'), ('Country', 'Japan'), ('Height (in cm)', '175')])		# Each row is an ordered Dict object.
# OrderedDict([('Name', 'Ken'), ('Country', 'USA'), ('Height (in cm)', '175')])
# OrderedDict([('Name', 'Chun-Li'), ('Country', 'China'), ('Height (in cm)', '165')])
# OrderedDict([('Name', 'Guile'), ('Country', 'USA'), ('Height (in cm)', '182')])
# OrderedDict([('Name', 'E. Honda'), ('Country', 'Japan'), ('Height (in cm)', '185')])
# OrderedDict([('Name', 'Dhalsim'), ('Country', 'India'), ('Height (in cm)', '176')])
# OrderedDict([('Name', 'Blanka'), ('Country', 'Brazil'), ('Height (in cm)', '192')])
# OrderedDict([('Name', 'Zangief'), ('Country', 'Russia'), ('Height (in cm)', '214')])
	
	
	
# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data
		
###### output ######
# C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\8_Working With CSV and Pickling!>python try.py
# Ryu
# Ken
# Chun-Li
# Guile
# E. Honda
# Dhalsim
# Blanka
# Zangief



# Reading a file with different delimiter, for example "|"
from csv import reader

with open("fighters2.csv") as file:
	csv_reader = reader(file, delimiter="|")
	for row in csv_reader:
		# each row is a list!
		print(row)

####### output #########
# C:\Sachin_Folder\PDF's Books\Python\python3\GIT_REPO\8_Working With CSV and Pickling!>python try.py
# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun-Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
# ['Dhalsim', 'India', '176']
# ['Blanka', 'Brazil', '192']
# ['Zangief', 'Russia', '214']