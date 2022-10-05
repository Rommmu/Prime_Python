game_score = int(input("게임 점수를 입력하세요: "))
print("game_score = ", game_score)

if game_score < 1000:
    print("입문자입니다")
else:
    print("고수입니다")