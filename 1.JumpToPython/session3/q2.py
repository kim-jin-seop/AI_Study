# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
sum = 0
for num in range(1,1001):
    if num % 3 == 0:
        sum = sum + num
print(sum)