#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
def foo(x):
    sum = 0
    for i in range(0, x+1):
        x = (1 + 1/x)**x
        sum += x
    return sum
n = int(input('Введите количество чисел в последовательности: '))
answer = foo(n)
print('Сумма всех чисел последовательности:', answer)