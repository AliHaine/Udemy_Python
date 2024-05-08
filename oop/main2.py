import pandas as pd
from abc import ABC, abstractmethod

file = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
	watermark = "test"
	def __init__(self, hotel_id):
		self.hotel_id = hotel_id
		self.hotel_name = file.loc[file["id"] == hotel_id, "name"].squeeze()

	def book(self):
		file.loc[file["id"] == self.hotel_id, "available"] = "no"
		file.to_csv("hotels.csv", index=False)

	def available(self):
		return file.loc[file["id"] == self.hotel_id, "available"].squeeze()

	@classmethod
	def get_class_count(cls, data):
		return len(data)

	def __eq__(self, other):
		return self.hotel_id == other.hotel_id


class Ticker(ABC):
	@abstractmethod
	def test(self):
		pass

class ReservationTicket:
	def __init__(self, hotel, name):
		self.hotel = hotel
		self.name = name

	def generate(self):
		return f"""
		New resevation
		Name: {self.name}
		Hotel: {self.hotel.hotel_name}
		"""

	@property
	def the_customer_name(self):
		customer_name = self.name.strip()
		customer_name = customer_name.title()
		return customer_name


hotel1 = Hotel("134")
hotel2 = Hotel("134")


print(hotel1.watermark)
hotel1.watermark = "test2"
print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark)
print(Hotel.get_class_count(file))

rt = ReservationTicket(hotel1, "sa tes")
print(rt.the_customer_name)
print(hotel1 == hotel2)

