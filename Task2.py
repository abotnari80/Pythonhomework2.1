n = int(input("введите число: "))
fac = 1
print('[', end=' ')
for i in range(1,n+1):
    fac = fac*i
    print(fac, end=' ')
print(']')