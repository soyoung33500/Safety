# 부산 취약지역 예측 함수


```python
!git clone https://github.com/soyoung33500/Safety.git
```

    Cloning into 'Safety'...
    


```python
cd Safety
```

safety.py의 safety 클래스 호출


```python
from safety import safety
```

변수에 safety() 클래스 입력


```python
test = safety()
```

check() 함수 실행   
입력 칸에 검색하고 싶은 주소 입력   
확인하고 싶은 격자 단위 입력


```python
test.check()
```

    확인하고 싶으신 주소를 입력해주세요 (부산광역시 도로명 주소만 이용가능합니다)
    예시 : 부산 남구 용소로 45
    부산 남구 용소로 45
    확인하고 싶은 단위를 적어주세요 (50, 100, 150, 200) : 50
    ======================================================================
    해당 지역은 안전 등급입니다
    주변에 경찰서와 CCTV가 있습니다.
    ======================================================================
    

해당 지역의 등급과 등급을 예측하는데 영향을 준 변수들을 출력해줌

---
point() 함수 실행   
검색한 위치와 주변 변수들의 위치를 마크   
마크를 클릭하면 어떤 변수인지 알려줌


```python
test.point()
```
![image](https://github.com/user-attachments/assets/1e20d46a-ddd4-437d-983d-ed0ec1638e58)
