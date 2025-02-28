def  generator(a, b):
    lis = []
    for i in range(a, b + 1):
        lis.append(i ** 2)
    return lis
print("Бір аралықты енгізіңіз: ")
a = int(input("Бірінші сан: "))
b = int(input("Екінші сан: "))
x = generator(a, b)
print(", ".join(map(str, x)))