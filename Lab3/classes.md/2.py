class Shape:
    class Square:
        def __init__():
            length = int(input("Enter length: "))
            s = length * length
            return s

a = Shape
b = a.Square.__init__()
print(b)

'''
Second way
a = Shape
b = a.Square
print(b.__init__())
'''