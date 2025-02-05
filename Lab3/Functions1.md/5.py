import itertools
def per():
    x = input("Enter word: ")
    y = itertools.permutations(x)
    for x in y:
        print("".join(x))
per()