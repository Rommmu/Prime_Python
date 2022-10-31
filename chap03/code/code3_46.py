n = int(input("합계를 구할 수를 입력하세요: "))
s = 0
i = 1
while i <= n:
    s = s + i
    i += 1

print(s)

from datetime import date,timedelta

startdate = date.today()
enddate = startdate + timedelta(days = 200)
print(startdate)
print(enddate)