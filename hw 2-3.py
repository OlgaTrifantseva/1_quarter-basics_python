# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = [['Зима', ['12', '1', '2']],
                ['Весна', ['3', '4', '5']],
                ['Лето', ['6', '7', '8']],
                ['Осень', ['9', '10', '11']]]

seasons_dict = {'Зима': ['12', '1', '2'],
                'Весна': ['3', '4', '5'],
                'Лето': ['6', '7', '8'],
                'Осень': ['9', '10', '11']}

while True:
    month = input("Введите номер месяца (число от 1 до 12): ")
    if month not in sum(seasons_dict.values(), []):
        print("Не верный номер месяца. Попробуйте еще раз: ")
        continue

    break

for season, months in seasons_list:
    if month in months:
        print(f'Месяц с номером {month} - это {season}')

for season, months in seasons_dict.items():
    if month in months:
        print(f'Месяц с номером {month} - это {season}')
