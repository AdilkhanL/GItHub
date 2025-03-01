import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "z":

x = re.findall("[a-z]", txt)
print(x)





txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)







txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello.*", txt)
print(x)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")








txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall(".*t$", txt)
print(x)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
  
  

#Task7
txt = "Hello, world. How are you?"
x = re.split("[ ,.!?]{1}", txt)
x = re.sub("[ ,.?!_]+", "", txt)
print("Task 7")
print(x)