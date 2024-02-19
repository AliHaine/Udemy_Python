user_input = input()


def parse(txt):
	parts = txt.split(" ")
	feet = float(parts[0])
	inches = float(parts[1])
	return {"feet": feet, "inches": inches}


def calcMeters(values):
	return values["feet"] * 0.3048 + values["inches"] * 0.0254

res = parse(user_input)
print(f"{res['feet']} and {res['inches']}. Meters = {calcMeters(res)}")
