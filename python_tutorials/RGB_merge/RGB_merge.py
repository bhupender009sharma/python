from PIL import Image

phelps = Image.open("phelps.jpg")
print(phelps.mode)          # it gives us the mode of the phelps.jpg image
phelps.show()
r,g,b = phelps.split()
new = Image.merge("RGB", (r,b,g))
print(r)
r.show()
b.show()
g.show()
dadp= Image.merge("RGB", (b,g,r))
dadp.show()

# we can also merge two photos , by taking their 2 different rgb values and merging them like(r1,g1,b2) or (r2,b1,g2)
