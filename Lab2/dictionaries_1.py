thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))



#Get value
print(thisdict.get("model")) #Return Mustang



thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)



#keys and values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = thisdict.keys()
y = thisdict.values()
print(x)
print(y)


#New key value
thisdict["electrick"] = {False}
print(thisdict)




z = thisdict.items()
print(z)



print("model" in thisdict)