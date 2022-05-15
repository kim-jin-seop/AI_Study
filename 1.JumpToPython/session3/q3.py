# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

# *
# **
# ***
# ****
# *****
high = 1
while high <= 5 :
    cnt = 1
    str = ""
    while cnt <= high :
        str = str + "*"
        cnt = cnt + 1
    print(str)
    high = high + 1