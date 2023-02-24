# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Ввод:
# 7
# 12
# Вывод
# 3 4 или 4 3
import math
from random import randint

x = randint(1, 1000)
# print(f'Первое число : {x}')

y = randint(1, 1000)
# print(f'Второе число : {y}')
summa = x + y
print(f'Сумма чисел: {summa}')
proizved = x * y
print(f'Произведение чисел: {proizved}')

discriminant = math.sqrt(summa * summa - 4 * proizved)
if discriminant < 0: print("таких натуральных чисел не существует")
elif discriminant == 0: print(f'Оба числа равны {int(summa/2)}')
else:
    x1 = int((summa + discriminant) / 2)
    y1 = int((summa - discriminant) / 2)
    print(f'Загаданные числа соответственно равны: {x1} и {y1}')