from PIL import Image
import urllib.request

img_url = 'https://i.pinimg.com/originals/59/d8/14/59d814c2bd548ee955f3e0fee2651e65.jpg'
urllib.request.urlretrieve(img_url,'phelps.jpg')

img = Image.open('phelps.jpg')
print(img.size)
area = (70,200,480,450)               #area =  coordinates of top-left corner, and bottom right corner

cropped_img = img.crop(area)
cropped_img.show()