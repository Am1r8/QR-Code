import qrcode
from time import sleep

li = input("Enter the link: \n")
def qr():
    link = li
    save_path = 'QR_code.png'
    img = qrcode.make(link)
    img.save(save_path)
    print("QR code generated successfully")
    sleep(2)

if __name__=='__main__':
    qr()