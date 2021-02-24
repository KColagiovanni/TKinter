#This program is a random color chooser
#It takes 3 random integers and converts them to hex
from random import randint

#r = 16
#g = 17
#b = 18
count = 1
#while len(hex_color_code) > 7 and count < 1000:
while count < 1000:
    r = randint(0, 254)
#    print("random r is " + str(r))
    hex_r = hex(r)
    if r < 16:
        hex_r = str(hex_r)
        hex_r = "0" + hex_r[2:]
    else:
        hex_r = hex_r[2:]

    g = randint(0, 254)
#    print("random g is " + str(g))
    hex_g = hex(g)
    if g < 16:
        hex_g = str(hex_g)
        hex_g = "0" + hex_g[2:]
    else:
        hex_g = hex_g[2:]

    b = randint(0, 254)
#    print("random b is " + str(b))
    hex_b = hex(b)
    if b < 16:
        hex_b = str(hex_b)
        hex_b = "0" + hex_b[2:]
    else:
        hex_b = hex_b[2:]

    hex_color_code = "#" + hex_r + hex_g + hex_b
    print(len(hex_color_code))
    print(hex_color_code)
    count += 1