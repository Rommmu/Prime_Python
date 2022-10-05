question1 = input("당신은 성인인가요? (성인이면 1, 미성년이면 0):")

if question1 == "0":
    print("당신은 미성년자입니다")
else:
    question2 =  input("당신은 기혼자인가요? (기혼이면 1, 미혼이면 0):")
    if question2 == "1":
        print("당신은 성인인 기혼자입니다")
    else:
        print("당신은 성인인 미혼자입니다")