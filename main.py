import qrcode
import os

data_to_encode = input("Enter the data or link to be encoded in the QR code: ")
file_name = input("Enter the file name (with .png extension) to save the QR code image: ")

#Handle file_name extension
base_name, ext = os.path.splitext(file_name)
if ext != ".png":
    file_name = base_name + ".png"

qr_code = qrcode.QRCode(version=4, box_size=80, border=5)

#data that will be encoded in the qr code
qr_code.add_data(data_to_encode) 
qr_code.make(fit=True)

#make_image generates an image, fill color for boxes and back color for the background
generate_image = qr_code.make_image(fill_color="black",back_color="white")
generate_image.save(file_name)

