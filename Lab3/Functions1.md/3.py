def solve(heads, legs):
    rabbit = (legs - 2* heads) / 2
    chicken = heads - rabbit
    print("chickens:", chicken)
    print("rabbits:", rabbit)

heads = int(input("How many heads: "))
legs = int(input("How many legs: "))
solve(heads, legs)

'''
35 = n + k
94 = 2n + 4k
24 = 2k
'''