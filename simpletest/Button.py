from machine import Pin
from utime import sleep
import utime 
Yled = Pin(22, Pin.OUT)
Rbutton = Pin(13, Pin.IN, Pin.PULL_UP)

Rled = Pin(28, Pin.OUT)
Lbutton = Pin(2, Pin.IN, Pin.PULL_UP)


while True:
    print(Lbutton.value())
    if Lbutton.value() == 0:
        Rled.value(True)
    else:
        Rled.value(False)
    print(Rbutton.value())
    if Rbutton.value() == 0:
        Yled.value(True)
    else:
        Yled.value(False)
    utime.sleep(0.1)




