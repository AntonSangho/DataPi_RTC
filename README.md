# AI Challenge for Biodiversity 발대식 실습교육 

파일 및 폴더           | 내용
:------------- |:-------------
[lib](/lib/ds3231_port.py) | DS3231 RTC 모듈 라이브러리 
[Micropython](/Micropython/RPI_PICO_W-20231005-v1.21.0.uf2) | 라즈베리파이 피코용 Micropython UF2파일   
[simpletest](/simpletest/README.md) | DataPi를 제어하기 위한 기본동작 코드 
[main.py](/main.py) |  DataPi로 온도데이터를 수집하는 Micropython 코드 
[Openweather.py](/Openweather.py) | Openweather API를 활용하여 날씨정보를 가져오는 예제   
[config_temp.py](/config_temp.py) | Openweather.py에서 필요로하는 Wifi정보와 API key 정보를 넣는 템플릿    

## 실습목록   
### DataPi로 데이터 수집   
1. DataPi에 Micropython 설치하기  
2. lib폴더를 Raspberry pi Pico에 업로드 하기  
3. `main.py` 실행하기   
4. 버튼(오른쪽)으로 제어하기 
    - **1초 이하**로 누르면 온도 센싱 기능을 시작/중단합니다.   
    - **1초 이상**을 누르면 온도 데이터 기록을 시작/중단합니다. 
4. 온도데이터를 시각화하기 
5. 온도데이터를 저장하기  
    - 데이터는 `temperature_data.csv` 파일에 저장되고 새로 기록할 때마다 추가됩니다.   

###  DataPi 제어하기 
1. [simpletest.md](/simpletest/simpletest.md)을 참고하여 폴더에 있는 코드를 하나씩 실행해보기  
2. 코드를 수정해서 실행해보기 
### Openweather API로 데이터 수집하기   
1. [openweathermap](https://openweathermap.org/)에 접속하기 
2. openweathermap에 회원 가입하기 
3. 알고 싶은 지역을 검색하기 
4. 해당 지역은 본인의 API를 이용해서 확인하기
5. [`config_temp.py`](/config_temp.py)에 Wifi정보와 Openweather API 키를 입력하고 `config.py`로 파일명 변경하기   
6. [`Openweather.py`](/Openweather.py)을 실행하기 

## 문의하기 
sangho@microschool.kr 으로 메일을 보내주세요. 


