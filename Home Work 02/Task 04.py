# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов ряда: '))

sum = 1
element = 1

for i in range(1, n):
    element /= -2
    sum += element

print(f'Сумма ряда из {n} элементов равна {sum}')
