thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

x = 0
thislist = ["apple", "banana", "cherry"]
while x < len(thislist):
  print(thislist[x])
  x += 1

[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

newlist = [x for x in fruits if "a" in x]
print(newlist)
'''
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
'''

newlist2 = [x if x != "banana" else "orange" for x in fruits]
print(newlist2)