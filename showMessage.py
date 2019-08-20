from characters import *
from sentences import *
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

W = [255, 255, 255]
B = [0, 0, 0]
R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]

matrix = [
	W, W, W, W, W, W, W, W,
	W, R, R, R, R, R, R, W,
	W, R, G, G, G, G, R, W,
	W, R, G, B, B, G, R, W, 
	W, R, G, B, B, G, R, W,
	W, R, G, G, G, G, R, W, 
	W, R, R, R, R, R, R, W,
	W, W, W, W, W, W, W, W
]

sense.set_pixels(matrix)
sleep(3)
sense.clear()