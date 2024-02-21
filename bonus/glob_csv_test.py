import glob
import csv

files = glob.glob('*.py')
print(files)

with open("text.csv", "r") as file:
	data = list(csv.reader(file))
print(data)
