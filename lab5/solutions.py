import re

#Task 1
txt = "aaaaaabbbbbbbbbbbb"
x = re.findall("a*b*", txt) is not None
print("Task 1")
print(x)

#Task2
txt = "abbbbbbbbbbbb"
txt2 = "aabbbbbbbbbbbb"
x = re.fullmatch(r"ab*", txt) is not None  #True
x2 = re.fullmatch(r"ab*", txt2) is not None #False
print("Task 2")
print(x)
print(x2)

#Task3
txt = "this_is_a_test example_text"
x = re.findall("[a-z]+_[a-z]*", txt)
print("Task 3")
print(x)

#Task4
txt = "This_is a_Test example_text HelLo World"
x = re.findall("[A-Z][a-z]*", txt)
print("Task 4")
print(x)

#Task5
txt = "axxxb axcvbt"
x = re.findall("a.*b", txt)
print("Task 5")
print(x)

#Task6
txt = "Hello, world. How are you?"
x = re.sub("[ ,.]+", ":", txt)
print("Task 6")
print(x)
print("")

#Task7
print("Task 7")
txt = "this_is_a_test"
x = ''.join(word.title() if i > 0 else word for i, word in enumerate(txt.split('_')))
print(x)

#Task8
print("Task 8")
txt = "SplitAtUppercase"
x = re.findall("[A-Z][a-z]*", txt)
print(x)

#Task9
print("Task 9")
txt = "InsertSpacesBetweenCapitals"
x = re.sub(r'(?<!^)(?=[A-Z])', ' ', txt)
print(x)


#Task10
print("Task 10")
txt = "CamelCaseString"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower()
print(x)