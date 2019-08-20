from characters import *
from sentences import *
from showMessage import *
from sense_hat import SenseHat
sense = SenseHat()

x = [100, 0, 0]
y = [0, 0, 100]

image = [
    x, y, x, y, x, y, x, y,
    y, x, y, x, y, x, y, x,
    x, y, x, y, x, y, x, y,
    y, x, y, x, y, x, y, x,
    x, y, x, y, x, y, x, y,
    y, x, y, x, y, x, y, x,
    x, y, x, y, x, y, x, y,
    y, x, y, x, y, x, y, x
    ]

sense.set_pixels(image)
sleep(1)
showMessage("Testy McGee*", BGimage = image)