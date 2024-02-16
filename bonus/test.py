todos = []

while True:
	txt = input("a")
	if ("test" in txt):
		print("yes")
	elif ("bug" in txt):
		try:
			todos[txt] = 0
		except:
			txt = input("try")