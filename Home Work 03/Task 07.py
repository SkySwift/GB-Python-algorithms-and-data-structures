# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

for i in range(2, len(array)):
    if array[i] < array[min_first]:
        spam = min_first
        min_first = i
        if array[spam] < array[min_second]:
            min_second = spam

    elif array[i] < array[min_second]:
        min_second = i

print(f'Число {array[min_first]} в ячейке {min_first}')
print(f'Число {array[min_second]} в ячейке {min_second}')
