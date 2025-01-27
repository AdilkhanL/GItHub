x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is", x)

def myfunc_2():
  global y
  y = "Code"

myfunc_2()
print(y)