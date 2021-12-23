n = int(input("Введи целое положительное число: "))
xn = 0
while n > 0:
    y = n % 10
    if y >= xn:
        xn = y
    n //= 10
    if n == int:
        print("Максимальная цифра в числе:", xn)
    else:
        print("Введите число")
