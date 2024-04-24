import streamlit as st
import requests

st.title("Test api")

url = "https://api.nasa.gov/planetary/apod?api_key=KcMmA4W4S8YUoeoC1z5YRRrWA8EBcR5PN9ziYbcC"

content = requests.get(url)

image_binary = requests.get(content.json()["url"]).content

with open("img.jpg", "wb") as f:
	f.write(image_binary)

st.image("img.jpg")

