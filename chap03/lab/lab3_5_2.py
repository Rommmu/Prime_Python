microdust = int(input("미세먼지 농도를 입력하세요:"))

if microdust >= 76:
    print("매우나쁨")
elif microdust >= 36:
    print("나쁨")
elif microdust >= 16:
    print("보통")
elif microdust >= 0:
    print("좋음")
else:
    print("잘못된 입력입니다")