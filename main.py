import utime
from machine import Pin, I2C, PWM
from ds3231_port import DS3231
import onewire, ds18x20

# 글로벌 변수
sensing_active = False
recording_active = False
recording_interval = 1  # 기록 간격을 초 단위로 설정 (예: 1초)

# LED 및 버튼 설정
YLed = Pin(22, Pin.OUT)
Rled = Pin(28, Pin.OUT)
Rbutton = Pin(13, Pin.IN, Pin.PULL_UP)
Lbutton = Pin(2, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(15))

# I2C 설정
sdaPIN = Pin(8)
sclPIN = Pin(9)
i2c = I2C(0, sda=sdaPIN, scl=sclPIN)

# DS3231 RTC 및 DS18x20 온도 센서 설정
ds3231 = DS3231(i2c)
data = Pin(1)
temp_wire = onewire.OneWire(data)
temp_sensor = ds18x20.DS18X20(temp_wire)
roms = temp_sensor.scan()

# 버튼 핸들러 함수
def Rbutton_handler(pin):
    global sensing_active
    sensing_active = not sensing_active  # 상태 전환

def Lbutton_handler(pin):
    global recording_active, file
    recording_active = not recording_active
    if recording_active:
        buzzer.duty_u16(30000)
        buzzer.freq(1000)
        utime.sleep(0.1)
        buzzer.duty_u16(0)
        # 파일 초기화 및 시작
        file = open('temperature_data.csv', 'w')
        file.write('Time,Temperature\n')
    else:
        buzzer.duty_u16(30000)
        buzzer.freq(500)
        utime.sleep(0.1)
        buzzer.duty_u16(0)
        file.close()  # 파일 닫기

# 버튼에 핸들러 등록
Rbutton.irq(trigger=Pin.IRQ_FALLING, handler=Rbutton_handler)
Lbutton.irq(trigger=Pin.IRQ_FALLING, handler=Lbutton_handler)

# 메인 루프
while True:
    if sensing_active:
        for rom in roms:
            temp_sensor.convert_temp()
            utime.sleep_ms(100)
            t = temp_sensor.read_temp(rom)
            print(t)
            YLed.value(1)  # YLed 켜기
            utime.sleep_ms(500)
            YLed.value(0)  # YLed 끄기
    if recording_active:
        Rled.value(1)  # Rled 켜기
        for rom in roms:
            temp_sensor.convert_temp()
            utime.sleep_ms(100)
            t = temp_sensor.read_temp(rom)
            ds3231.save_time() # save_time()함수는 RTC 모듈이 초기화되지 않은 것으로 가정하고 사용한 것이므로 한번 초기화한 이후에는 사용하지 않아도 무방합니다.
            dateTime = ds3231.get_time()
            timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(dateTime[0], dateTime[1], dateTime[2], dateTime[3], dateTime[4], dateTime[5])
            data_line = "{}, {:6.2f}\n".format(timestamp, t)
            print(t)
            file.write(data_line)
            utime.sleep(recording_interval)  # 사용자가 설정한 기록 간격에 따라 대기
    else:
        Rled.value(0)  # Rled 끄기
    utime.sleep(0.1)
