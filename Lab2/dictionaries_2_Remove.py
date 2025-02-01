car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#update
car.update({"year": 2020})
print(car)


#pop
car.pop("model")
print(car)
#popitem
car.popitem() #deletes last
print(car)
#del
del car["brand"]
print(car)


#DEL
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


del car    #del completely


#For
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():  #We also can use values and keys
  print(x, y)




#Copy, dict
mydict = thisdict.copy()
#or
mydict = dict(thisdict)
print(mydict)



mydictionary = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Or

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(mydictionary["child1"]["name"])



kids = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in kids.items():
  print(x)
  for y in obj:  #obj = mini dictionary
    print(y + ":", obj[y])