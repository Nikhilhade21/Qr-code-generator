import qrcode as qr
img= qr.make("https://translate.google.co.in/?sl=en&tl=mr&op=translate")
img.save("nik.png")