# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1
from random import randint
print("Введите количество монет")
n = int(input())
list_monet = []
reshka = 0
orel = 0

for i in range(n):
    list_monet.append(randint(0,1))

print(list_monet[:])
for i in list_monet:
    if i == 0: orel += 1     
    elif i == 1: reshka += 1
print(f'Всего Орлов: {orel}')
print(f'Всего Решек: {reshka}')
if orel == n or reshka == n: print('переворачивать ничего не нужно!')  
elif orel > reshka: print(f'нужно перевернуть монет в количестве {n - orel} на Орла')
elif orel < reshka: print(f'нужно перевернуть монет в количестве {n - reshka} на Решку') 
elif orel == reshka: print(f'нужно перевернуть монет в количестве {n - reshka} на Орла или Решку') 
 
