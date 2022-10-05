# 팩토리얼 구하기
from re import L


n = int(input("숫자를 입력하세요: "))
s = 1

for i in range(1, n+1):
    s = s * i
print(s)