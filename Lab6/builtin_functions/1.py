def multiple(l):
    cnt = 1
    for i in range(len(l)):
        cnt = cnt * l[i]
    return cnt
l = input().split()
l = list(map(int, l))
print(multiple(l))