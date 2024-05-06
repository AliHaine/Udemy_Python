import pandas as pd


file = pd.read_csv("hotels.csv", dtype={"id": str})
file_card = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
file_scard = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
	def __init__(self, hotel_id):
		self.hotel_id = hotel_id
		self.hotel_name = file.loc[file["id"] == hotel_id, "name"].squeeze()

	def book(self):
		file.loc[file["id"] == self.hotel_id, "available"] = "no"
		file.to_csv("hotels.csv", index=False)

	def available(self):
		return file.loc[file["id"] == self.hotel_id, "available"].squeeze()


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



class CreditCard:
	def __init__(self, number):
		self.number = number

	def validate(self, holder, expiration, cvc):
		tmp = {"number": self.number, "expiration": expiration, "cvc": cvc, "holder": holder}
		return tmp in file_card


class SecureCreditCard(CreditCard):
	def auth(self, given_pass):
		df_result = file_scard.loc[file_scard["number"] == self.number, "password"].squeeze()
		return given_pass == df_result

print(file)
hotel_id = input("Selection a hotel by \n")
hotel = Hotel(hotel_id)
if hotel.available():
	cart = SecureCreditCard("1234")
	if cart.validate("JOHN SMITH", "12/26", "123"):
		if cart.auth(input("Cart pass\n")):
			hotel.book()
			name = input("Enter your name\n")
			reservation = ReservationTicket(hotel, name)
			print(reservation.generate())
		else:
			print("incorrect password")
	else:
		print("Cart error")
else:
	print("Not possible")
