# 음수 양수 판별하고 양수일 때만

number = int(input("숫자를 입력해주세요:"))

if number < 0:
    print("음수입니다")
else:
    if number % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")