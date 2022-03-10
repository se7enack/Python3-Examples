class car():
    def __init__(self, make, model, year, new):
        self.new = new
        self.make = make
        self.model = model
        self.year = year
    def welcome(self):
        if self.new:
            x = "brand new"
        else:
            x = "used"
        print("Enjoy your", x, self.year, self.make, self.model + "!" )

sbCar = car("Tesla", "Model 3", 2021, True)
mbCar = car("Toyota", "Highlander", 2020, False)

print(sbCar.welcome())
print(mbCar.welcome())
