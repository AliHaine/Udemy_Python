import requests
import selectorlib
import time

URL = "https://programmer100.pythonanywhere.com/tours/"


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

while(True):
    result = extractor(scrape(URL))
    print(result)
    if result != "No upcoming tours":
        if result not in open("data.txt", "r").read():
            store(result)
            send_email(result)
    time.sleep(2)
