# remove
thislist = ['apple', 'lemon', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'blackcurrant', 'pineapple', 'papaya']
thislist.remove("lemon")
print(thislist)
#lemon will be removed
#          ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'blackcurrant', 'pineapple', 'papaya']


# pop
thislist.pop(1)
thislist.pop()
print(thislist)
#banana and papaya will be removed
#          ['apple', 'cherry', 'orange', 'kiwi', 'mango', 'blackcurrant', 'pineapple']



# del
del thislist[2]
print(thislist)
#          ['apple', 'cherry', 'kiwi', 'mango', 'blackcurrant', 'pineapple']


#clear
thislist.clear()
print(thislist)
#          []