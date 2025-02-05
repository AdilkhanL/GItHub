class MyClass:
    def getstring(a):
        print("Enter something: ")
        a.string = input()
    def printstring(a):
        print(a.string.upper())

b = MyClass()
b.getstring()
b.printstring()