import qrcode

# สร้าง QRCode
img = qrcode.make('https://www.itgenius.co.th')
type(img)
img.save("demo_qrcode.png")
