from sense_hat import SenseHat

sense = SenseHat()

blank     = [  0,   0,   0]
tm_yellow = [255, 207, 132]
tm_orange = [255, 161, 104]
tm_red    = [255,  70,  18]
tm_purple = [209,  99, 206]

b = blank

y = tm_yellow
o = tm_orange
r = tm_red
p = tm_purple


image = [
    b,b,b,b,b,b,b,b,
    b,b,o,b,b,r,b,b,
    y,b,o,o,r,r,b,p,
    y,y,o,o,r,r,p,p,
    y,y,o,o,r,r,p,p,
    y,b,o,o,r,r,b,p,
    b,b,o,b,b,r,b,b,
    b,b,b,b,b,b,b,b
]

sense.set_pixels(image)
