from machine import Pin
import utime

led1 = Pin(22, Pin.OUT) # RED LED 
led2 = Pin(28, Pin.OUT) # Yellow LED

INTERVAL1 = 300 
INTERVAL2 = 500

time_previous1 = utime.ticks_ms() # get millisecond counter
time_previous2 = time_previous1

while True:
    time_current = utime.ticks_ms() # get current time

    # Elapsed time
    time_elapsed1 = utime.ticks_diff(time_current, time_previous1)
    time_elapsed2 = utime.ticks_diff(time_current, time_previous2)

    if time_elapsed1 > INTERVAL1:
        led1.toggle()
        time_previous1 = time_current
    if time_elapsed2 > INTERVAL2:
        led2.toggle()
        time_previous2 = time_current
