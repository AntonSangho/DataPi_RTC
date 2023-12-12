import utime
from machine import Pin, I2C
from ds3231_port import DS3231
import onewire, ds18x20

# 데이터 기록 상태를 추적하기 위한 전역 변수
recording = False

# 버튼 핸들러 함수
def Lbutton_handler(pin):
    global recording
    recording = not recording  # 상태 전환
    if recording:
        # 기록 시작 시, 현재 시간을 DS3231에 저장
        ds3231.save_time()

# 버튼 설정
Lbutton = Pin(2, Pin.IN, Pin.PULL_UP)
Lbutton.irq(trigger=Pin.IRQ_FALLING, handler=Lbutton_handler)

# I2C 설정
sdaPIN = Pin(8)
sclPIN = Pin(9)
i2c = I2C(0, sda=sdaPIN, scl=sclPIN)

# DS3231 RTC 모듈 객체 생성
ds3231 = DS3231(i2c)

# DS18x20 온도 센서 설정
data = Pin(1)
temp_wire = onewire.OneWire(data)
temp_sensor = ds18x20.DS18X20(temp_wire)
roms = temp_sensor.scan()

# CSV 파일 초기화
with open('temperature_data.csv', 'w') as file:
    file.write('Time,Temperature\n')

while True:
    if recording:
        for rom in roms:
            temp_sensor.convert_temp()
            utime.sleep_ms(100)
            t = temp_sensor.read_temp(rom)
            print(t)
            dateTime = ds3231.get_time()
            timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(dateTime[0], dateTime[1], dateTime[2], dateTime[3], dateTime[4], dateTime[5])
            data_line = "{}, {:6.2f}\n".format(timestamp, t)

            # CSV 파일에 데이터 기록
            with open('temperature_data.csv', 'a') as file:
                file.write(data_line)

            utime.sleep(1)
    else:
        utime.sleep(0.1)
