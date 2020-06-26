from PIL import Image

phelps = Image.open('phelps.jpg')
print(phelps.size)

phelps_sq = phelps.resize( (200,200) )      # (400,400) is given as a tuple
phelps_flip = phelps.transpose(Image.FLIP_LEFT_RIGHT)
phelps_spin = phelps.transpose(Image.ROTATE_180)

phelps.show()
phelps_sq.show()
phelps_flip.show()
phelps_spin.show()