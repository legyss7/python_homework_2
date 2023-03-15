# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

number_of_coins = int(input('Введите количество мотет: '))
arrow_of_coins = [random.randint(0, 1) for i in range(number_of_coins)]
print(arrow_of_coins)
count_zero = 0
count_one = 0
for i in range(number_of_coins):
    if arrow_of_coins[i] == True:
        count_one += 1
    else:
        count_zero += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


