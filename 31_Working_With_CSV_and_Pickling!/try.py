from csv import DictReader, DictWriter

def cm_to_inches(cm):
	return float(cm) * 0.393701
	
with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)
	
with open("inches_fighters.csv", "w") as file:
	headers = ("Name","Country","Height_iches")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name":f["Name"],
			"Country":f["Country"],
			"Height_iches":cm_to_inches(f["Height (in cm)"])
		})