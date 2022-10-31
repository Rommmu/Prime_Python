i = 0 # 초기값
while i < 5: # 루프의 조건식이 참이면 내부 블록이 실행됨
    print('welcome')
    i += 1

from datetime import datetime
now = datetime.now()
now_date = now.date()
now_time = now.time()
weekday = now.weekday()

print(now_time)
