# Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Parent Name: {self.name}")


class Child(Parent):
    def display(self):
        print(f"Child inherited: {self.name}")


c = Child("ParentClass")
c.display()


# Multiple Inheritance
class A:
    def feature1(self):
        print("Feature 1 from A")


class B:
    def feature2(self):
        print("Feature 2 from B")


class C(A, B):
    pass


obj = C()
obj.feature1()
obj.feature2()


# Multilevel Inheritance
class Base:
    def base_feature(self):
        print("Feature from Base")


class Intermediate(Base):
    def intermediate_feature(self):
        print("Feature from Intermediate")


class Final(Intermediate):
    def final_feature(self):
        print("Feature from Final")


obj = Final()
obj.base_feature()
obj.intermediate_feature()
obj.final_feature()
