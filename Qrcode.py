import qrcode 
# For installing this module use this command pip install qrcode
print("Please select if you wish to create a QR code for Text or URL. ")
print("Choose 'T' for text , 'U' for URL")
choice=input()
choice=choice.upper()
match choice:
    case 'T':
        string=input("Enter the text that you want to appear when the QR-CODE is scanned : ")
    case 'U':   
        string=input("Enter the URL for which you want to generate QR-CODE : ")
qr_code=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr_code.add_data(string)
qr_code.make(fit=True)
image=qr_code.make_image(fill_color="Navy",back_color="Linen")
image.show()
