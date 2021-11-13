from pyzbar import pyzbar
from PIL import Image

path = input("Enter the path of the image: \n")
def r_qr():
    img_path = path

    img1 = Image.open(img_path)
    out1 = pyzbar.decode(img1)
    print(out1[0].data.decode("utf-8"))
    

if __name__=='__main__':
    r_qr()