def  generator(n):
    lis = []
    i = n
    while i != 0:
        lis.append(i)
        i-=1
    return lis
n = int(input("Сан енгізіңіз: "))
x = generator(n)
print(", ".join(map(str, x)))