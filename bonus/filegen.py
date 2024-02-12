file_content = ["c1", "c2", "c3"]
file_name = ["1", "2", "3"]

for content, name in zip(file_content, file_name):
	file = open(name, "w")
	file.write(content)
	file.close()
