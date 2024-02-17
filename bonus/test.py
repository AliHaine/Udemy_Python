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


def func(a, b, c):
	print(a,b ,c)


func(1, 2, 3)
