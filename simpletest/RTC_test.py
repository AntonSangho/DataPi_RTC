# Write micropython code to test the RTC module on the board. 
# Get the current time from the RTC module and print it out every second.
# DS3231 is synchronized with system time when start up.
# Print system time and DS3231 time so that you can compare them.


# 1. Import the necessary modules.
import utime
from machine import Pin
from machine import I2C
from ds3231_port import DS3231
from machine import UART

uart = UART(0, 9600)

sdaPIN = Pin(8) # SDA pin
sclPIN = Pin(9) # SCL pin
i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # Init I2C using pins sda and scl

ds3231 = DS3231(i2c) # Create DS3231 object

def sync_time(uart):
    uart.write(b'time\n')  # Request time from PC
    while uart.any() == 0:
        pass  # Wait for the response
    line = uart.readline()  # Read the Unix timestamp as a string or None
    try:
        timestamp = int(line)  # Try to convert the string to an integer
    except (TypeError, ValueError):
        timestamp = 0  # Use 0 if it's None or can't be converted
    print('Received timestamp:', timestamp)
    print('Local time:', utime.localtime(timestamp))  # Convert the timestamp to local time

# Sync the time when the Pico is powered on
sync_time(uart)

print('Initial values')
print('DS3231 time:', ds3231.get_time())
print('RTC time:   ', utime.localtime())

print('Setting DS3231 from RTC')
ds3231.save_time()  # Set DS3231 from RTC
print('DS3231 time:', ds3231.get_time())
print('RTC time:   ', utime.localtime())

print('Running RTC test for 2 mins')
print('RTC leads DS3231 by', ds3231.rtc_test(120, True), 'ppm')


