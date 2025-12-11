import qrcode
url=input("Enter the URL to generate QR code: ")
filename=input("Enter the filename to save the QR code as: ")
if not(filename.endswith('.png')):
       filename = filename + '.png'
img = qrcode.make(url)
img.save(filename)