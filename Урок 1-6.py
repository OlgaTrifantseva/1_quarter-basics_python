# Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное число — номер дня.

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
