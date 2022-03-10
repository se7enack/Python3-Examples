class Parent:
    def __init__(self):
        print("this is a parent class")
    def ParentFunc(self):
        print("this is a parent func")
    def test(self):
        print("this came from parent")        

class Child(Parent):
    def __init__(self):
        print("this is a child class")
    def ChildFunc(self):
        print("this is a child func")
    def test(self):
        print("this came from child")   




c = Child()
print(c.ParentFunc())
print(c.test())