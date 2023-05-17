import qrcode as qr
img = qr.make("https://www.linkedin.com/in/anujsoni45/")
img.save("MyLinkedin_profile.png")
