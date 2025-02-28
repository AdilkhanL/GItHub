def  generator(n):
    lis = []
    for i in range(n + 1):
        if i % 2 == 0:
            lis.append(i)
    return lis
n = int(input("Сан енгізіңіз: "))
x = generator(n)
print(', '.join(map(str, x)))