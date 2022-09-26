print("a  n  a**n")

list = [2, 3, 4, 5, 6]

a = 1
n = 2

for number in list:
    a = a + 1
    if number <= 6:
        print(a, n, a**n)
    else:
        break