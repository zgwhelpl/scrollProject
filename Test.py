from characters import *
from sentences import *

'''char_2.printMatrix()
char_2.printGrid()

print(" -- Characters ^^ Characters --")
print(" -- Sentences  vv  Sentences --")'''

mySentence = sentence("ABC123")
string = ""
for c in range(len(mySentence.matrix[0])-16):
	string = string + str((c+8)%10)
print string
mySentence.printGrid()

for x in range(40, 43):
	frame = mySentence.frame(x)
	for i in range(8):
		print(frame[i])
	print("-=-=-=-=-=-=-=-=-=-=-=-=-")