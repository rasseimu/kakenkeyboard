from PIL import Image
img = 'C:/Users/hp/kakenkeyboard/keyboard/imagefile/sample.jpg'
img_crop = img.crop((400, 150, 700, 500))#切り出し
img_crop.save('C:/Users/hp/kakenkeyboard/keyboard/imagefile/sample1.jpg', quality=95)#保存
