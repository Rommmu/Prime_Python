n = int(input("숫자를 입력하세요"))
s = 0

for i in range(1, n+1):
    s = i + s

print("1부터 {}까지의 합은 {}".format(n, s))