# 윤년 검사하기

year = int(input("연도를 입력해주세요: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "는 윤년입니다")
        else:
            print(year, "는 평년입니다")
    else:
        print(year, "는 윤년입니다")
else:
    print(year, "는 평년입니다.")