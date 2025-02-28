import math
n = int(input("Қабырғалар саны: "))
a = int(input("Қабырға ұзындығы: "))
x = (n * a ** 2) / (4 * math.tan(math.pi / n))
print(f"{x:.0f}")