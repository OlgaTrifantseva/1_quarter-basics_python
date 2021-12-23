a = int(input("Введите результат первого дня пробежки в км: "))
b = int(input("Введите желаемый результат в км: "))
days = 1
km = a
if a > b:
    print(days)
while a < b:
    a = a + a / 10
    days += 1
print("На", days, "день вы достигните результата -", a, "км!")
