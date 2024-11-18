class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2


side = int(input("Enter the length: "))
sq = Square(side)
print(f"Area of square: {sq.area()}")
