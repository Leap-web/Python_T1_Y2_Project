# 1
print("Exercise:1")
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

# 2
print("Exercise:2")
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

# 3
print("Exercise:3")
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Grade:{self.grade}")
    def update_grade(self, grade):
        self.grade = grade

student = Student("John",20,"B")
print("Before grade update:")
student.display()
student.update_grade("A")
print("After grade update:")
student.display()

# 4
print("Exercise:4")
class BankAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print(f"Initial balance for {self.owner}: ${self.balance}")
        
    def deposit(self,amount):
        self.balance+=amount
        return f"Depositing: ${amount} \nNew balance: ${self.balance}"
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            return f"Withdrawing: ${amount}\nNew balance: ${self.balance}\nFinal balance: ${self.balance}"
        else:
            return f"Attemping to withdraw: ${amount}\nInsufficient funds. Withdrawal failed.\nFinal balance: ${self.balance}"
        
bankaccount = BankAccount("John",1000)
print(bankaccount.deposit(500))
print(bankaccount.withdraw(3000))

# 5
print("Exercise:5")
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
class Library:
    def __init__(self):
        self.list = []
        
    def add_book(self,book):
        newlist =[
            f"Title:{book.title}",
            f"Author:{book.author}",
            f"Price:{book.price}",
        ]
        self.list.append(newlist)
    
    def show_book(self):
        for i in self.list:
            print(f"\n{i}\n")

book1 = Book("Great Man","F. Ane Fit","$10.99")
book2 = Book("The story about APT","Fake Man","$12.50")
book3 = Book(1984,"George Orwell","$9.75")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Books in library:")
print(library.show_book())

# 6
print("Exercise:6")
class Classroom:
    class_name = ""
    list = []
    
    def add_student(self,student):
        self.list.append(student)
        return f"Added student:{student}"
    def list_account(self):
        for i in self.list:
            print(f"-{i}\n")
            
classroom = Classroom()

print(classroom.add_student("Alice"))
print(classroom.add_student("Bob"))
print(classroom.add_student("Charlie"))

classroom.class_name = "Math 101:"
print(f"Students in {classroom.class_name}")
classroom.list_account()

# 7
print("Exercise:7")
class PhoneBook:
    dic = {}
    
    def add_contact(self,name,number):
        # new_dict = {
        #     "Name": name,
        #     "Number": number,
        # }
        # self.dic[number]=new_dict
        self.dic[name] = number
        # name = key, number = value ,jg vea doch name:number
        return f"Added contact:{name} -> {number}"
    
    def find_contact(self,name):
        if name in self.dic:
            return f"{name}'s number: {self.dic[name]}"
        else:
            return f"{name} is not found in phone book."
        
phonebook = PhoneBook()
print(phonebook.add_contact("John", "123-456-7890"))
print(phonebook.find_contact("John"))

# 8
print("Exercise:8")
class SportLeague:
    
    def __init__(self):
        self.dic = {}
        self.team_name = None  
    
    def add_team(self, team_name):
        if team_name not in self.dic:
            self.dic[team_name] = []
            self.team_name = team_name  
            return f"Team {team_name} added."
        return f"Team {team_name} already exists."
    
    def add_player(self, id_player, name, position):
        if self.team_name is None or self.team_name not in self.dic:
            return "No team selected. Please add or select a team first."

        if any(player['ID'] == id_player and player['Name'] == name for player in self.dic[self.team_name]):
            return f"Player {name} already exists in team {self.team_name}."
        
        new_player = {"ID": id_player, "Name": name, "Position": position}
        self.dic[self.team_name].append(new_player)
        return f"Player {name} added to team {self.team_name}"
    
    def view_team(self, team_name):
        if team_name in self.dic:
            players = "\n".join(
                f"ID: {player['ID']}, Name: {player['Name']}, Position: {player['Position']}"
                for player in self.dic[team_name]
            )
            return f"Team {team_name} players:\n{players}"
        return f"Team {team_name} not found."
    
    def update_player(self, team_name, id_player, name=None, position=None):
        if team_name in self.dic:
            for player in self.dic[team_name]:
                if player['ID'] == id_player:
                    if name is not None:
                        player['Name'] = name  
                    if position is not None:
                        player['Position'] = position  
                    return f"Player {id_player} updated in team {team_name}."
            
            new_player = {"ID": id_player, "Name": name, "Position": position}
            self.dic[team_name].append(new_player)
            return f"Player {id_player} added to team {team_name}."
        else:
            return f"Team {team_name} does not exist."

    def remove_player(self, team_name, id_player):
        if team_name not in self.dic:
            return f"Team {team_name} does not exist."
        
        for index, player in enumerate(self.dic[team_name]):
            if player['ID'] == id_player:
                removed_player = self.dic[team_name].pop(index)
                return f"Player {removed_player} removed from team {team_name}."
        
        return f"Player with ID {id_player} not found in team {team_name}."

sportleague = SportLeague()

print(sportleague.add_team("Tiger"))
print(sportleague.add_player(1, "Serey", "Goalkeeper"))
print(sportleague.add_player(2, "Dy", "Goalkeeper"))

print(sportleague.add_team("Lion"))
print(sportleague.add_player(1, "Dara", "Striker"))
print(sportleague.add_player(2, "Ly", "Defender"))

print(sportleague.update_player("Tiger", 1, "Serey", "Goalkeeper"))

print(sportleague.view_team("Tiger"))
print(sportleague.remove_player("Tiger", 2))  
print(sportleague.view_team("Tiger"))