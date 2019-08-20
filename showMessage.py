from characters import *
from sentences import *
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

B = [0, 0, 0]
def showMessage(text, **kwargs):
    if 'font' in kwargs:
        t = kwargs.get('font')
    else :
        t = [255, 255, 255]
    if 'backGround' in kwargs:
        b = kwargs.get('backGround')
    else :
        b = [0, 0, 0]
    if 'speed' in kwargs:
        speed = kwargs.get('speed')
    else:
        speed = .1
    
    matrix = [
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
    ]
    
