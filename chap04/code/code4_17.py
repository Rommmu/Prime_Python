def print_sum():
    global a, b
    a = 100
    b = 200
    result = a + b
    print("print sum 내부:", a, b, result)

a = 10
b = 20
print_sum()
result = a + b
print("print sum 외부:", a, b, result)