#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def sumFloat(num):
    x = num.split(".") 
    a = int(x[0]) 
    b = int(x[1])
    sum = 0
    while a != 0:
        sum = sum + (a % 10)
        a = a // 10
    while b != 0:
        sum = sum + (b % 10)
        b = b // 10
    return sum
num = input("Введите число: ")
answer = sumFloat(num)       
print('Сумма равна: ', answer)