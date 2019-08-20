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

def checkImage(img):
    if len(img) is not 64:
        return False
    else :
        for i in range(64):
            if not checkColor(img[i]):
                return False
    return True
    
def showMessage(text, **kwargs):

    fontColor = [255, 255, 255]
    backGround = [0, 0, 0]
    speed = .1
    width = 8
    BGimage = False
    BGisFontColor = False
    if 'fontColor' in kwargs:
        fontColor = kwargs.get('fontColor')
    if 'backGround' in kwargs:
        backGround = kwargs.get('backGround')
    if 'speed' in kwargs:
        speed = kwargs.get('speed')
    if 'width' in kwargs:
        if (len(kwargs.get('width')) >= 1 and len(kwargs.get('width')) <= 8):
            width = kwargs.get('width')
    if 'BGimage' in kwargs:
        if checkImage(kwargs.get('BGimage')):
            BGimage = kwargs.get('BGimage')
            if 'BGisFontColor' in kwargs:
                BGisFontColor = kwargs.get('BGisFontColor')
                backGround = [0, 0, 0]
               
    sen = sentence(text)
    
    for index in range(sen.maxIndex+1): #for each frame of the slide
        matrix = sen.frame(index) #this is the slide at that frame
        for inst in range(64): #for each part of the slide (all 64)
            if matrix[inst]: #they should be 1's and 0's, so if 1
                if BGisFontColor:
                    matrix[inst] = BGimage[inst]
                else:
                    matrix[inst] = [fontColor[0], fontColor[1], fontColor[2]] #set that inst to t = [255, 255, 255]
            else : #otherwise its a 0
                if (BGimage is not False):
                    matrix[inst] = BGimage[inst]
                else:
                    matrix[inst] = [backGround[0], backGround[1], backGround[2]] #so set it to b = [0, 0, 0] / background
                    #the final result should be [[],[],[],...x64]
        sense.set_pixels(matrix)#that type of matrix is feedable into set_pixels
        sleep(speed)
        