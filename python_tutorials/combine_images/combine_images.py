from PIL import Image

phelps = Image.open('phelps.jpg')
dad = Image.open('dad.jpg')
crop_img = phelps.crop((70,200,400,450))
print(crop_img.size)
area = (45,150,375,400)
dad.paste(crop_img,area)
