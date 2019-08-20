from characters import *
from sentences import *
from sense_hat import SenseHat
sense = SenseHat()

B = [255, 255, 255]
B = [0, 0, 0]
B = [255, 0, 0]
B = [0, 255, 0]
B = [0, 0, 255]

matrix = [
	B, B, B, B, B, B, B, B,
	B, B, B, B, B, B, B, B,
	B, B, B, B, B, B, B, B,
	B, B, B, B, B, B, B, B, 
	B, B, B, B, B, B, B, B,
	B, B, B, B, B, B, B, B, 
	B, B, B, B, B, B, B, B,
	B, B, B, B, B, B, B, B
]

sense.set_pixels(matrix)
