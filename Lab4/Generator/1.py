def  generator(n):
    lis = []
    for i in range(1, n + 1):
        lis.append(i ** 2)
    return lis
n = int(input("Сан енгізіңіз: "))
x = generator(n)
for i in x:
    print(i)