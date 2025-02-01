a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b: print("a and b are equal")#Алдыңғы условие True болмаса
else: print("a is greater than b")#Ешқайсысы дұрыс болмаса


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 33
b = 200
if b > a: #this "if" is empty
  pass