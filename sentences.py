from characters import *

def getRowValsForChar(row, char):
	vals = []
	if (char == 'a'):
		vals = char_a.self()[row]
	elif (char == '2'):
		vals = char_2.self()[row]
	elif (char == '3'):
		vals = char_3.self()[row]
	elif (char == '4'):
		vals = char_4.self()[row]
	elif (char == '5'):
		vals = char_5.self()[row]
	elif (char == '6'):
		vals = char_6.self()[row]
	elif (char == '7'):
		vals = char_7.self()[row]
	elif (char == '8'):
		vals = char_8.self()[row]
	elif (char == '9'):
		vals = char_9.self()[row]
	elif (char == '0'):
		vals = char_0.self()[row]
	elif (char == 'b'):
		vals = char_b.self()[row]
	elif (char == 'c'):
		vals = char_c.self()[row]
	elif (char == 'd'):
		vals = char_d.self()[row]
	elif (char == 'e'):
		vals = char_e.self()[row]
	elif (char == 'g'):
		vals = char_g.self()[row]
	elif (char == 'h'):
		vals = char_h.self()[row]
	elif (char == 'm'):
		vals = char_m.self()[row]
	elif (char == 'n'):
		vals = char_n.self()[row]
	elif (char == 'o'):
		vals = char_o.self()[row]
	elif (char == 'p'):
		vals = char_p.self()[row]
	elif (char == 'q'):
		vals = char_q.self()[row]
	elif (char == 's'):
		vals = char_s.self()[row]
	elif (char == 'u'):
		vals = char_u.self()[row]
	elif (char == 'v'):
		vals = char_v.self()[row]
	elif (char == 'w'):
		vals = char_w.self()[row]
	elif (char == 'x'):
		vals = char_x.self()[row]
	elif (char == 'y'):
		vals = char_y.self()[row]
	elif (char == 'z'):
		vals = char_z.self()[row]
	elif (char == 'A'):
		vals = char_A.self()[row]
	elif (char == 'B'):
		vals = char_B.self()[row]
	elif (char == 'C'):
		vals = char_C.self()[row]
	elif (char == 'D'):
		vals = char_D.self()[row]
	elif (char == 'E'):
		vals = char_E.self()[row]
	elif (char == 'F'):
		vals = char_F.self()[row]
	elif (char == 'G'):
		vals = char_G.self()[row]
	elif (char == 'H'):
		vals = char_H.self()[row]
	elif (char == 'J'):
		vals = char_J.self()[row]
	elif (char == 'K'):
		vals = char_K.self()[row]
	elif (char == 'L'):
		vals = char_L.self()[row]
	elif (char == 'M'):
		vals = char_M.self()[row]
	elif (char == 'N'):
		vals = char_N.self()[row]
	elif (char == 'O'):
		vals = char_O.self()[row]
	elif (char == 'P'):
		vals = char_P.self()[row]
	elif (char == 'Q'):
		vals = char_Q.self()[row]
	elif (char == 'R'):
		vals = char_R.self()[row]
	elif (char == 'S'):
		vals = char_S.self()[row]
	elif (char == 'T'):
		vals = char_T.self()[row]
	elif (char == 'U'):
		vals = char_U.self()[row]
	elif (char == 'V'):
		vals = char_V.self()[row]
	elif (char == 'W'):
		vals = char_W.self()[row]
	elif (char == 'X'):
		vals = char_X.self()[row]
	elif (char == 'Y'):
		vals = char_Y.self()[row]
	elif (char == 'Z'):
		vals = char_Z.self()[row]
	elif (char == '@'):
		vals = char_AtSymbol.self()[row]
	elif (char == '#'):
		vals = char_Hash.self()[row]
	elif (char == '$'):
		vals = char_Dollar.self()[row]
	elif (char == '%'):
		vals = char_Percent.self()[row]
	elif (char == '&'):
		vals = char_Ampersand.self()[row]
	elif (char == '*'):
		vals = char_Asterisk.self()[row]
	elif (char == '-'):
		vals = char_Dash.self()[row]
	elif (char == '_'):
		vals = char__.self()[row]
	elif (char == '='):
		vals = char_Equals.self()[row]
	elif (char == '+'):
		vals = char_Plus.self()[row]
	elif (char == '?'):
		vals = char_QuestionMark.self()[row]
	elif (char == 'f'):
		vals = char_f.self()[row]
	elif (char == 'j'):
		vals = char_j.self()[row]
	elif (char == 'k'):
		vals = char_k.self()[row]
	elif (char == 'r'):
		vals = char_r.self()[row]
	elif (char == 't'):
		vals = char_t.self()[row]
	elif (char == 'i'):
		vals = char_i.self()[row]
	elif (char == ' '):
		vals = char_Space.self()[row]
	elif (char == 'l'):
		vals = char_l.self()[row]
	elif (char == '1'):
		vals = char_1.self()[row]
	elif (char == 'I'):
		vals = char_I.self()[row]
	elif (char == '('):
		vals = char_LParen.self()[row]
	elif (char == ')'):
		vals = char_RParen.self()[row]
	elif (char == '['):
		vals = char_LBracket.self()[row]
	elif (char == ']'):
		vals = char_RBracket.self()[row]
	elif (char == '.'):
		vals = char_Period.self()[row]
	elif (char == ','):
		vals = char_Comma.self()[row]
	elif (char == ':'):
		vals = char_Colon.self()[row]
	elif (char == ';'):
		vals = char_SemiColon.self()[row]
	elif (char == '!'):
		vals = char_ExclamationPoint.self()[row]
	else :
		print("" +char + " not supported! (Sorry)")
	return vals

class sentence():
	def __init__(self, string):
		self.string = string
		self.matrix = matrix = [
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
		]
		for row in range(0, 8):
			for char in self.string:
				matrix[row] = matrix[row] + getRowValsForChar(row, char)

		for row in range (0, 8):
			matrix[row] = matrix[row] + [0, 0, 0, 0, 0, 0, 0, 0]
		self.maxIndex = len(self.matrix[0])-8

	def printGrid(self):
		for x in range(0, len(self.matrix)):
			string = ""
			for y in range(8, len(self.matrix[0])-8):
				if (self.matrix[x][y]):
					c = 'X'
				else : 
					if (x == 0 or x ==7):
						c = ' '
					else :
						c = ' '
				string = string + c
			print(string)
		print("")

	def frame(self, index):
		frame = [
		[], [], [], [], [], [], [], []
		]
		if (index > len(self.matrix[0])-8 or index < 0):
			print("Bad Index of " + str(index) + "! Range: 0 - " + str(self.maxIndex))
		else:
			for row in range(0, 8):
				for column in range (index, index+8):
					frame[row] = frame[row] + [self.matrix[row][column]]
		return frame







