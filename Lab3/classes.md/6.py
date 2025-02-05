def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


x = input("Print numbers\n").split()
x = list(map(int, x))
print(x)
result = list(filter(lambda y:prime(y), x))
print(result)