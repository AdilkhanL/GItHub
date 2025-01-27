thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = "blackcurrant"
print(thislist)


thislist.insert(3, "watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["watermelon"]
print(thislist)

# append
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.append("blackcurrant")

# insert
thislist.insert(1, "lemon")

#extend
newlist = ["pineapple", "papaya"]
thislist.extend(newlist)
print(thislist)