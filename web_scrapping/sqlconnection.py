import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT band, date FROM events WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

new_rows = [("Salut", "city salut", "29.28.27"), ("Salut3", "city salut3", "29.28.29")]
cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

data = "salut, test, 2020"
split = data.split(',')
print(split)