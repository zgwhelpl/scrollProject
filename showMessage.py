from characters import *
from sentences import *
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

B = [0, 0, 0]

def checkColor(RGB):
	check = True
	if (len(RGB) != 3):
		print("invalid length")
		return False
	for value in RGB:
		if (value < 0 or value > 255):
			check = False
	#print("Final: " + str(check))		
	return check#'''
    
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
    if 'width' in kwargs:
        width = kwargs.get('width')
    else :
        width = 8
    flagRaised = False
    if 'BGimage' in kwargs:
        if len(kwargs.get('BGimage')) == 64:
            for color in kwargs.get('BGimage'):
                if not checkColor(color):
                    flagRaised = True
        if not flagRaised:
                BGimage = kwargs.get('BGimage')
        else:
            BGimage = False
               
    sen = sentence(text)
    
    for index in range(sen.maxIndex+1): #for each frame of the slide
        matrix = sen.frame(index) #this is the slide at that frame
        for inst in range(64): #for each part of the slide (all 64)
            if matrix[inst]: #they should be 1's and 0's, so if 1
                matrix[inst] = [t[0], t[1], t[2]] #set that inst to t = [255, 255, 255]
            else : #otherwise its a 0
                if (BGimage is not False):
                    matrix[inst] = BGimage[inst]
                else:
                    matrix[inst] = [b[0], b[1], b[2]] #so set it to b = [0, 0, 0] / background
                    #the final result should be [[],[],[],...x64]
        sense.set_pixels(matrix)#that type of matrix is feedable into set_pixels
        sleep(speed)
        