# 하드웨어 연결을 확인하기 위한 코드
- [Blink.py](/simpletest/Blink.py) : 라즈베리파이 피코 W에 장착되어 있는 LED 점등 
- [Button.py](/simpletest/Button.py) : 버튼 테스트
- [Buzzer.py](/simpletest/Buzzer.py) : 버저 테스트
- [LED.py](/simpletest/LED.py) : LED 테스트 
- [Temp.py](/simpletest/Temp.py) : 온도센서 테스트 
- [i2c.py](/simpletest/i2c.py) : 연결된 i2c장치 확인하기. 현재는 DS3231(0x68)와 at24c32(0x57)를 연결된 것을 확인가능 
- [Button_handler](/simpletest/Button_handler.py) : 버튼의 상태에 따라서 함수를 정의하는 예제 