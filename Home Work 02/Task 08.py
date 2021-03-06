# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

BASE = 10

num = int(input("Введите количество чисел: "))
digit = int(input("Какую цифру подсчитать: "))
count = 0
for i in range(1, num + 1):
    ans = int(input(f'Введите число {i}: '))
    while ans > 0:
        if ans % BASE == digit:
            count += 1
        ans //= BASE  # ans = ans // 10

print(f'Цифра {digit} была введено {count} раз(а) ')
