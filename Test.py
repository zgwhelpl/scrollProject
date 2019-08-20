from characters import *
from sentences import *
from showMessage import *
from sense_hat import SenseHat
sense = SenseHat()

x = [100, 0, 0]
y = [0, 0, 100]
r = [250, 0, 0]
w = [250, 250, 250]
b = [0, 0, 250]

usFlag = [
    b, w, b, w, r, r, r, r,
    w, b, w, b, w, w, w, w,
    b, w, b, w, r, r, r, r,
    w, b, w, b, w, w, w, w,
    r, r, r, r, r, r, r, r,
    w, w, w, w, w, w, w, w,
    r, r, r, r, r, r, r, r,
    w, w, w, w, w, w, w, w
    ]

showMessage("'Murica!'", BGimage = usFlag, font=[135,135,135])
sense.clear()
showMessage("Flags For Days", BGimage = usFlag, BGisFontColor=True)