import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

stations = (pd.read_csv("../../jupyter/data_small/stations.txt", skiprows=17))
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
	return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/yearly/<station>/<date>")
def yearly(station, date):
	filename = "../../jupyter/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
	return df[df["    DATE"].astype(str).str.startswith(date)].to_html()

@app.route("/api/v1/<station>")
def all_data(station):
	filename = "../../jupyter/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
	df = pd.read_csv(filename, skiprows=20)
	return df.to_html()

if __name__ == "__main__":
	app.run(debug=True)
