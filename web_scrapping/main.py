import requests
import selectorlib
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def scrape(url):
    result = requests.get(url)
    return result.text


def extractor(source):
    extractor = selectorlib.Extractor.from_yaml_file("srcfile.txt")
    return extractor.extract(source)["tours"]


def send_email(result):
    print("Sending email: " + result)


def store(result):
    with open("data.txt", "a") as f:
        f.write(result + "\n")


def store_sql(result):
    cursor.execute("INSERT INTO events VALUES(?,?,?)", result)
    connection.commit()

while(True):
    result = extractor(scrape(URL))
    if result != "No upcoming tours":
        result_splitted = result.split(',')
        cursor.execute("SELECT * FROM events WHERE band=?", (result_splitted[0],))
        if cursor.fetchone() is None:
            store_sql(result_splitted)
            send_email(result)
    time.sleep(1)
