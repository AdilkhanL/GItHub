thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)



thistuple2 = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))



tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)



thistuple_3 = ("apple", "banana", "cherry")
print(thistuple_3[1])
print(thistuple_3[-4:-1])



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
x = tuple(y)
print(x)


#Қосу
q = ("apple", "banana", "cherry")
w = ("orange",)
q += w

print(q)