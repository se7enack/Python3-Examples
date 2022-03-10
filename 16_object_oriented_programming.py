class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age      
    def getName(self):
        print("Your name is " + self.name)
    def getAge(self):
        print("Your age is " + self.age)    


p1 = Person("Logan", "14")

p1.getName()
p1.getAge()




