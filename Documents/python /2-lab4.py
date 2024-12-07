# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def is_vintage(self):
#         if  (2024-self.year > 25):
#             print(f"{self.model} is vintage:True")
#         else:
#             print(f"{self.model} is vintage:False")
            
            
        
# car1 = Car("Toyota","Corolla",2020)
# car2 = Car("Ford","Mustang",1999)

# car1.is_vintage()
# car2.is_vintage()



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def is_vintage(self):
        if 2024 - self.year <=25:
            # print(f"{self.model} is vintage: False")
            return "False"
        else:
            # print(f"{self.model} is vintage: True")
            return "True"

car1 = Car("Toyota", "Corolla", 1990)
print(f"Car 1 is vintage: {car1.is_vintage()}")
car2 = Car("Ford", "Ranger", 2020)
print(f"Car 2 is vintage: {car2.is_vintage()}")
