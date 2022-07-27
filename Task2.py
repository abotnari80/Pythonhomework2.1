#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def factorial(a):
    fac = 1
    for i in range(1,a+1):
        fac = fac*i
        print(fac, end=' ')
    return fac
n = int(input("введите число: "))
print('[', end=' ')
answer = factorial(n)
print(']')