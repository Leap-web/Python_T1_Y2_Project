class Car:
    make = ""
    model = ""
    year = 0
    
    def display_info(self):
        print("Car detail:")
        print("Make:{0}".format(self.make))
        print("Model:{0}".format(self.model))
        print("Year:{0}".format(self.year))
car = Car()
car.make = "Toyota"
car.model = "Corolla"
car.year = 2020
car.display_info()