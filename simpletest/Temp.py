import time
import machine
import onewire, ds18x20

data = machine.Pin(1)
temp_wire = onewire.OneWire(data) # create a OneWire bus on GPIO1

temp_sensor = ds18x20.DS18X20(temp_wire) # create a DS18X20 temperature sensor object

roms = temp_sensor.scan() # scan for devices on the bus
print(len(roms), 'temperature sensros found')

while True:
    print('temperatures:', end=' ')
    temp_sensor.convert_temp()
    time.sleep_ms(100)

    for rom in roms:
        t = temp_sensor.read_temp(rom)
        print('{:6.2f}'.format(t), end=' ')
    print()
