from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
	("plat", "Plat"),
	("accompagnement", "Accompagnement"),
	("dessert", "Desserts")
)

STATUS= (
	(0, "UNAVAILABLE"),
	(1, "AVAILABLE"),
)


class Item(models.Model):
	meal = models.CharField(max_length=1000, unique=True)
	description = models.CharField(max_length=2000, unique=False)
	price = models.DecimalField(decimal_places=2, max_digits=4)
	meal_type = models.CharField(max_length=2000, choices=MEAL_TYPE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.IntegerField(choices=STATUS, default=1)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.meal

