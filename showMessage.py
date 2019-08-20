from characters import *
from sentences import *
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

B = [0, 0, 0]
def showMessage(text, **kwargs):
    if 'font' in kwargs:
        t = kwargs.get('font')
        print("the font is " + str(t))
    else :
        t = [255, 255, 255]
        print("no font set")
    if 'backGround' in kwargs:
        b = kwargs.get('backGround')
        print("the background is " + str(b))
    else :
        b = [0, 0, 0]
        print("no BG set")
    if 'speed' in kwargs:
        speed = kwargs.get('speed')
    else:
        speed = .1
        
    sen = sentence(text)
    
    for index in range(sen.maxIndex+1): #for each frame of the slide
        matrix = sen.frame(index) #this is the slide at that frame
        for inst in range(64): #for each part of the slide (all 64)
            if matrix[inst]: #they should be 1's and 0's, so if 1
                matrix[inst] = [t[0], t[1], t[2]] #set that inst to t = [255, 255, 255]
            else : #otherwise its a 0
                matrix[inst] = [b[0], b[1], b[2]] #so set it to b = [0, 0, 0] / background
                #the final result should be [[],[],[],...x64]
        sense.set_pixels(matrix)#that type of matrix is feedable into set_pixels
        sleep(speed)
        
'''showMessage("hello world", font=[255, 0, 255] )
showMessage("hello again", backGround=[100, 0, 0])
showMessage("fast ball! Vroom", speed = .05)#'''

showMessage("Supes is fast", font=[255, 0, 0], backGround=[0, 0, 255], speed= .05)
showMessage("turles", font = [0, 255, 0], backGround=[0, 100, 0], speed = .25)