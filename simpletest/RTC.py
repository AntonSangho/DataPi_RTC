import utime 
from machine import Pin
from machine import I2C
from ds3231_port import DS3231

sdaPIN = Pin(8) # SDA pin
sclPIN = Pin(9) # SCL pin
i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # Init I2C using pins sda and scl

ds3231 = DS3231(i2c) # Create DS3231 object

ds3231.save_time() # Save current time to DS3231

while True:
    localtime = utime.localtime()
    print(localtime)
    dateTime = ds3231.get_time() # Get current time from DS3231
    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(dateTime[0], dateTime[1], dateTime[2], dateTime[3], dateTime[4], dateTime[5]))
    utime.sleep(1) # Sleep 1 second

