# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in scores :
    sum = sum + score
avg = sum / len(scores)
print(avg)