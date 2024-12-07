print("Team6, Group2:\n1.Un Chhunly\n2.Savon Chanserey\n")
print("Exercise:1")
print("Romeng1:")
#1. Write a for loop that prints each element in the list numbers = [1, 2, 3, 4, 5].
list = [1,2,3,4]
for i in list:
    print(i)
#2. Create a while loop that counts from 1 to 10 and prints the numbers. Use break to exit the loop when the count reaches 6.
print("Exercise:2")
count = 1
while count<=10:
    print(count)
    count+=1
    if count == 6:
        break
#3. Modify the previous while loop to use continue to skip printing the number 4.
print("Exercise:3")
count = 1
while count<=10:
    if count == 4:
        count+=1
        continue
    print(count)
    count+=1

# Exercise:2
print("Romeng2:")
#1. Create a list of your favorite fruits and print it.
print("Exercise:1")
list = ['apple','orange','kiwi']
print(list)
#2. Add a new fruit to the list using the append method and print the updated list.
print("Exercise:2")
list.append('watermelon')
print(list)
#3. Remove a fruit from the list using the remove method and print the updated list.
print("Exercise:3")
list.remove('apple')
print(list)
#4. Sort the list in alphabetical order and print it.
print("Exercise:4")
list.sort()
print(list)

# Exercise:3
# print("Romeng3")
# #1. Create a tuple containing five integers and print it.
# print("Exercise:1")
# my_tuple = (4,5,6,7,8)
# print(my_tuple)
# #2. Attempt to change one of the integers in the tuple (this should raise an error).
# print("Exercise:2")
# # tuple.remove(4)
# # print(tuple)
# #3. Convert the tuple into a list and print the list.
# print("Exercise:3")
# my_tuple = (4,5,6,7,8)
# lst = list(my_tuple)
# print(lst)

# Exercise:4
print("Romeng4")
#1. Create a dictionary to store the ages of three people (e.g., {"Alice": 30, "Bob": 25, "Charlie": 35}) and print it.
print("Exercise:1")
dic = {"alice":30,"Bob":25,"Charlie":35}
print(dic)
#2. Add a new person to the dictionary and print the updated dictionary.
print("Exercise:2")
dic ["Dara"] = 40
print(dic)
print("Exercise:3")
#3. Remove one person from the dictionary using the pop method and print the updated dictionary.
dic.pop("alice")
print(dic)
print("Exercise:4")
#4. Print all keys and values in the dictionary using a loop.
for i,e in dic.items(): # i = key, e = value
    print(f"{i}:{e}")
    
# Exercise:5
print("Romeng:5")
#1. Write a function named add that takes two numbers as arguments and returns their sum. Call the function and print the result.
print("Exercise:1")
def add(a,b):
    return a+b
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(add(num1,num2))
print("Exercise:2")
#2. Create a function named greet that prints "Hello, World!" without returning a value. Call the function.
def greet():
    print('Hello, World!')
greet()
print("Exercise:3")
#3. Write a lambda function that takes one argument and returns the square of the number. Use this lambda function to print the square of 5.

x = lambda num:num**2
print(x(5))

# Bonus
print("Exercise:Bonus")
import os
def Register(user_list):
    username = input("Please input the username: ")
    while True:
        symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        password = input("Please input the password: ")
        
        has_islower = False
        has_digit = False
        has_isupper = False
        has_symbols = False
        
        if len(password) >= 8:
            for c in password:
                if c.islower():
                    has_islower = True
                if c.isupper():
                    has_isupper = True
                if c.isdigit():
                    has_digit = True
                if c in symbols:
                    has_symbols = True
            
            # Check if all password conditions are met
            if has_symbols and has_isupper and has_digit and has_islower:
                new_user = {
                    'Username': username,
                    'Password': password,
                }
                user_list.append(new_user)
                print(f"{username} is successfully registered!")
                return
       
        print("Please input a strong password!(Contain small and big letter,numbers and symbols)")
def Login(user_list):
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        old_user = input("Please input your username: ")
        old_pass = input("Please input your password: ")
        
        # Check if username and password match any user in the list
        for users in user_list:
            if users['Username'] == old_user and users['Password'] == old_pass:
                print(f"Welcome back, {old_user}")
                return
        
        # If no match found, show error and remaining attempts
        print("Your username or password is incorrect!")
        attempt_left = max_attempts - attempt
        if attempt_left > 0:
            print(f"Invalid credentials. You have {attempt_left} attempts left.")
        else:
            print("Too many failed attempts. Access blocked.")

        
def Forget_Password(user_list):
    forget_user = input("Enter your username to retrieve your password:")
    for user in user_list:
        if user['Username'] == forget_user:
            print(f"Your password is:{user['Password']}")
            break
        else:
            print(f"{forget_user} not found!")
user_list = []
user_input = True
while user_input:
    print("Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Forget Password")
    print("4. Exit")
    option = int(input("Choose an option (1-4): "))
    if option == 1:
        os.system('clear')
        Register(user_list)  
    elif option == 2:
        os.system('clear')
        Login(user_list)
    elif option == 3:
        os.system('clear')
        Forget_Password(user_list)
    elif option == 4:
        print("Exiting the program. Goodbye!")
        user_input = False
    else:
        print("Invalid option!")
