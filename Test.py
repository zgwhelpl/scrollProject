from characters import *
from sentences import *
from showMessage import *
from sense_hat import SenseHat
sense = SenseHat()

x = [100, 0, 0]
y = [0, 0, 100]
r = [50, 0, 0]
w = [50, 50, 50]
b = [0, 0, 50]

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
showMessage("Flags For Days", BGimage = usFlag, BGisFontColor=True)