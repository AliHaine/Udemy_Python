import json

save = []


def is_answer_correct(user_answer, correct_answer):
	if user_answer == correct_answer:
		return "Correct answer"
	return "Incorrect answer"


def save_answer(user_answer, correct_answer):
	save.append({"selected": user_answer, "correct": correct_answer, "success": is_answer_correct(user_answer, correct_answer)})


def display_question(question, answer):
	print("Question: " + question)
	for index, txt in enumerate(answer):
		print(str(index) + " " + txt)


def display_resume():
	score = 0
	for value in save:
		if value["success"] == "Correct answer":
			score += 1
		print(value["success"] + ". Correct answer: " + value["correct"] + " Your answer: " + value["selected"])
	print("Score: " + str(score) + "/" + str(len(save)))


with open("quest.json") as file:
	content = file.read()
json_content = json.loads(content)


for value in json_content:
	display_question(value["question"], value["answer"])
	selected = input()
	save_answer(selected, value["correct"])

display_resume()
