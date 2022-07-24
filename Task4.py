n = int(input('Введите количество чисел в последовательности: '))
sum = 0
for i in range(0, n):
    input_value = int(input(f'Введите число #{i}: '))
    sum += input_value
print('Сумма всех чисел последовательности:', sum)