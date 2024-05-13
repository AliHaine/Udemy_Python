from django.urls import path
from . import views

urlpatterns = [
	path("", views.ItemMenuList.as_view(), name="home"),
	path("menu_detail/<pk>", views.ItemDetail.as_view(), name="detail"),
]