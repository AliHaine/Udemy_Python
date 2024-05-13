import qrcode

URL = "https://128.0.0.1:8000/"
img = qrcode.make(URL)
img.save("qr.png")
