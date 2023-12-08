from machine import Pin
from utime import sleep

Rled = Pin(22, Pin.OUT)
Lbutton = Pin(13, Pin.IN, Pin.PULL_UP)

Yled = Pin(28, Pin.OUT)
Rbutton = Pin(2, Pin.IN, Pin.PULL_UP)


while True:
    Lbtn_status = Lbutton.value() # Read button status
    Rled.value(not Lbtn_status) # Set LED status
    
    Rbtn_status = Rbutton.value() # Read button status
    Yled.value(not Rbtn_status) # Set LED status



