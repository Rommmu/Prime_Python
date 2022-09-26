score = int(input("점수를 입력해주세요: "))

if score >= 90 and score <= 100:
    score = 'A'
elif score >= 80 and score < 90:
    score = 'B'
elif score >= 70 and score < 80:
    score = 'C'
elif score >= 60 and score < 70:
    score = 'D'
else:
    score = 'D'
print(score)