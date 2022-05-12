from PIL import Image
img = Image.open('C:/Users/hp/kakenkeyboard/keyboard/imagefile/pianoCE.jpg')
img_crop = img.crop((30, 535, 1890, 850))#切り出し
img_crop.save('C:/Users/hp/kakenkeyboard/keyboard/imagefile/pianoCE1.jpg', quality=95)#保存
