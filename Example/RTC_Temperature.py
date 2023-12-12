import utime 
from machine import Pin
from machine import I2C
from ds3231_port import DS3231
import onewire, ds18x20

#버튼 설정
Lbutton = Pin(2, Pin.IN, Pin.PULL_UP)
Rbutton = Pin(13, Pin.IN, Pin.PULL_UP)

#I2C 설정 
sdaPIN = Pin(8) # SDA pin
sclPIN = Pin(9) # SCL pin
i2c = I2C(0, sda=sdaPIN, scl=sclPIN) # Init I2C using pins sda and scl

#DS3231 RTC모듈 객체 생성 
ds3231 = DS3231(i2c) # Create DS3231 object

#ds3231.save_time() # Save current time to DS3231

#DS18x20 온도 센서 설정 
data = machine.Pin(1)
temp_wire = onewire.OneWire(data) # create a OneWire bus on GPIO1
temp_sensor = ds18x20.DS18X20(temp_wire) # create a DS18X20 temperature sensor object
roms = temp_sensor.scan() # scan for devices on the bus

while True:
    #버튼이 눌린 경우
    print(Lbutton.value())
    utime.sleep_ms(100)
    if Lbutton.value() == 0:
        for rom in roms:
            temp_sensor.convert_temp()
            utime.sleep_ms(100)
            t = temp_sensor.read_temp(rom)
            dateTime = ds3231.get_time() # Get current time from DS3231
            print("{:6.2f} {:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t, dateTime[0], dateTime[1], dateTime[2], dateTime[3], dateTime[4], dateTime[5]))
            #print('{:6.2f}'.format(t), end=' ')
            utime.sleep(1)


