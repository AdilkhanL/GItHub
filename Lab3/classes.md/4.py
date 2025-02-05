import math
class Point:
    def __init__(self, x, y):
        self.x0 = x
        self.y0 = y
    def Show(self):
        print("\nYour Cordinates")
        print("Your X =", self.x0)
        print("Your Y =", self.y0)
    def Move(self):
        print("\nInput your move distance")
        self.x1 = int(input("X move: "))
        self.y1 = int(input("Y move: "))
        print("\nYour new Coordinates")
        print("X:", self.x0 + self.x1)
        print("Y:", self.y0 + self.y1)
    def Dist(self):
        self.x = self.x0 + self.x1
        self.y = self.y0 + self.y1
        D = math.sqrt(self.x**2 + self.y**2)
        print("\nDistance is ", D)
        


x0 = int(input("Start X: "))
y0 = int(input("Start Y: "))
P = Point(x0, y0)
P.Show()
P.Move()
P.Dist()