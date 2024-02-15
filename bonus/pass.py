password = input("enter pass\n")
if len(password) < 8 or password.isalpha() or password.islower():
	print("weak")
else:
	print("strong")
