thislist_i = [100, 50, 65, 82, 23]
thislist_i.sort()
print(thislist_i)

thislist_s = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist_s.sort(reverse = True)
print(thislist_s)



def myfunc(n):
    return n % 2 == 0

thislist = [100, 50, 65, 82, 23]
thislist.sort()
thislist.sort(key = myfunc)

print(thislist)