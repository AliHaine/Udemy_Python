with open(input("Enter the today's date ") + ".txt", "w") as file:
	file.writelines("Mood: " + input("Mood from 0 to 10 ") + "\n" + "Desc:\n" + input("Short desc\n"))
