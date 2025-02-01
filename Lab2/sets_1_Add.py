#print
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

set_num = {1, 5, 7, 9, 3}
print(set_num)

set1 = {"abc", 34, True, 40, "male"}
print(set1)



#For If
thisset = {"apple", "banana", "cherry",}
for x in thisset:
    if "a" in x:
        print(x)
        
        
        
#Элементтерді қосу
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#thisset = {'apple', 'pineapple', 'banana', 'mango', 'papaya', 'cherry', 'orange', 'kiwi'}

#Элементтерді алып тастау
thisset.remove("banana")
print(thisset)

thisset.discard("banana")   #қате болса көрсетпейді
print(thisset)


#кез келген элеметті алып тастау
thisset.pop()
print(thisset)

#Бәрін кетіру
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Өзін кетіру
del thisset
print(thisset)