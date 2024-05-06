import requests
import selectorlib
import os
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        print("Email was sent! " + message)


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows


if __name__ == "__main__":
    while True:
        event = Event()
        database = Database("data.db")
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                Email.send(message="Hey, new event was found!")
        time.sleep(2)