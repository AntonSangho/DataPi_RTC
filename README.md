# DataPi Project

### 하드웨어 연결 

| 구성 요소        | 연결된 GPIO 핀 |
|----------------|---------------|
| `Rbutton` (오른쪽 버튼) | GPIO 13번    |
| `Lbutton` (왼쪽 버튼)   | GPIO 2번     |
| `YLed`(노란색 LED)         | GPIO 22번    |
| `Rled` (빨간색 LED)         | GPIO 28번    |
| `buzzer`       | GPIO 15번    |
| `DS3231 RTC 모듈` | SDA (GPIO 8번), SCL (GPIO 9번) |
| `DS18x20 온도 센서` | GPIO 1번     |

### [하드웨어 연결 테스트](/simpletest/README.md)

# 온도 센서 측정하고 기록하기 : [main.py](/main.py) 

이 프로젝트는 Raspberry Pi Pico W 를 사용하여 DS18b20 센서로 온도를 측정하고, DS3231 RTC 모듈을 통해 시간을 기록하는 예제입니다. 두 개의 버튼을 사용하여 각각 센싱과 데이터 기록 기능을 제어할 수 있습니다.

### 기능
- `Rbutton` (오른쪽 버튼): 온도 센싱 기능을 시작/중단합니다. 이 기능이 활성화되면 `YLed`가 온도를 읽을 때마다 켜집니다.
- `Lbutton` (왼쪽 버튼): 온도 데이터 기록을 시작/중단합니다. 데이터는 `temperature_data.csv` 파일에 저장됩니다. 이 기능이 활성화되면 `Rled`가 켜지고, `buzzer`가 울립니다.


# 오픈 API를 활용한 세계 날씨 데이터 가져오기 : [Openweather.py](/Openweather.py)  

1. [openweathermap](https://openweathermap.org/)에 접속하기 
2. openweathermap에 회원 가입하기 
3. 알고 싶은 지역을 검색하기 
4. 해당 지역은 본인의 API를 이용해서 확인하기

