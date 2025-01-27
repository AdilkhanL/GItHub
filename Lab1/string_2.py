a = "Notebook is Notebooke"
print(a.upper())
print(a.lower())


b = "   Next task    "
print(b.strip())
print(b.replace("x", "cs"))
print(b.split(" "))

print(a + ", " + b.strip())


age = 36
txt1 = "My name is John, I am"
txt2 = f"My name is John, I am {age}"
print(txt1, age)
print(txt2)

price = 2
print(f"The price is {price * 10:.2f} dollars")