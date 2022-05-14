# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
num = "881120-1068234"
date = num[:6]
back = num [7:]
print(f"date : {date}")
print(f"back : {back}")