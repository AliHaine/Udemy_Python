import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"
time = datetime.now().strftime("%y-%M-%d-%H-%M-%S")

result = requests.get(URL)
extractor = selectorlib.Extractor.from_yaml_file("srcfile2.txt")
with open("data2.txt", "a") as file:
    value = extractor.extract(result.text)["temp"]
    file.write(f"{time},{value}\n")
