from sense_hat import SenseHat
sense = SenseHat()

chars = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
          'a', 'b', 'c', 'd', 'e', 'g', 'h', 'm', 'n', 'o',
          'p', 'q', 's', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
          'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&', '*',
          '-', '_', '=', '+', '?', 'f', 'j', 'k', 'r', 't',
          'i', 'l', 'I', '(', ')', '[', ']', '.', ',', ':',
          ';', '!']


sense.set_rotation(270)

def waitForClick():
    stay = True
    while stay:
        for event in sense.stick.get_events():
            if (event.direction == 'middle' and event.action == 'released'):
                stay = False
                
                
for char in chars:
    sense.show_letter(char)
    waitForClick()