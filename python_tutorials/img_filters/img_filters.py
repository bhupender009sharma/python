from PIL import Image
from PIL import ImageFilter

fat = Image.open('fat.jpg')
blur = fat.filter(ImageFilter.BLUR)
detail = fat.filter(ImageFilter.DETAIL)
emboss = fat.filter(ImageFilter.EMBOSS)

fat.show()
blur.show()
detail.show()
emboss.show()