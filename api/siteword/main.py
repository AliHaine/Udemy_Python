from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/api/v1/<word>/")
def about(word):


	req = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
	print(req, req.json())
	content = req.json()[0]["meanings"][0]["definitions"][0]["definition"]
	return {"definition": content,
			"word": word}


if __name__ == "__main__":
	app.run(debug=True)
