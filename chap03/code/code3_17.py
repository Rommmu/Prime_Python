score = int(input("점수를 입력해주세요: "))

if score >= 90:
    score = 'A'
elif score >= 80:
    score = 'B'
elif score >= 70:
    score = 'C'
elif score >= 70:
    score = 'D'
else:
    score = 'F'

print(score)