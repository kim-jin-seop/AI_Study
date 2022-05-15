# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java

f = open("test.txt","r")
a = f.read()
f.close()

f = open("test.txt","w")
f.write(a.replace("java","python"))
f.close()
