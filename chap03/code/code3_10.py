# if-else문을 이용해 음수 혹은 음수 아님 출력하기

number = int(input("숫자를 입력해주세요:"))

if number > 0:
    print(number, "은 음수 아님")
elif number == 0:
    print(number, "은 0임")
else:
    print(number, "은 음수")

