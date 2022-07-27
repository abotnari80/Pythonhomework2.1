#1. Задайте список из N элементов, заполненных числами 
#из промежутка [-N, N]. Найдите произведение элементов 
#на указанных позициях. Позиции хранятся в файле file.txt 
#в одной строке одно число.
#2. Реализуйте алгоритм перемешивания списка.
import random

def newList(x):
    list = [i for i in range(-x, x+1)]
    return list
def shuffleList(x):
    random.shuffle(x)
    return x
n = int(input('Введите количество чисел последовательности: '))
list = newList(n)
answer = shuffleList(list)
print(answer)