import qrcode
import os
from PIL import Image
from time import sleep

li = input("Enter the link: \n")
def qr_logo():

    link = li
    save_path = 'QR_code.png'
    logo = "logo.png"

    img = qrcode.make(link)
    img.save(save_path)
    img=img.convert("RGBA")

    if logo and os.path.exists(logo):
        icon=Image.open(logo)

        img_w,img_h=img.size

        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)

        
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
      
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
      
        img.paste(icon,(w,h),icon)
        
    img.save(save_path)
    print("QR code generated successfully")

if __name__=='__main__':
    qr_logo()