hour = int(input("시간을 입력하세요:"))
if hour < 12:
    print("오전입니다")
elif hour >=12 and hour <= 24:
    print("오후입니다")