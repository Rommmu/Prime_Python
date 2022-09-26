score = int(input("점수를 입력해주세요: "))

if score >= 90:
    score = 'A'
else:
    if score >= 80:
        score = 'B'
    else:
        if score >= 70:
            score = 'C'
        else:
            if score >= 60:
                score = 'D'
            else:
                score = 'F'

print(score)