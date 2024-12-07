# # # # # 1.Write a Python program to diplay a following message:
# # # # print('Good day!\nMy name is Serey.\nI am a year 2 student.')
# # # # # 2.Write a Python program to sum between two number 10 and 19.
# # # # x = 10
# # # # y = 19
# # # # print(f'The result is:{x+y}')
# # # # # 3.Write a Python program to find the cube of 4
# # # # number = 4
# # # # cube = number**3
# # # # print(f'The result is:{cube}')
# # # # # 4.Write a Python program to convert 100000 Riels to US dollars.(4000 Riels = 1 Us dollars)
# # # # riel = 100000
# # # # convert = int(riel/4000)
# # # # print(f'The result is {convert} US dollars.')
# # # # # 5.Write a Python to convert 45 US dollars to Riels.(4000 Riels = 1 US dollars)
# # # # dollar = 45
# # # # convert = int(dollar * 4000)
# # # # print(f'The result is {convert} Riels.')
# # # # # 6.Write a Python to calculate the average of four numbers 4,6,8,10.
# # # # number = [4, 6, 8, 10]
# # # # result = sum(number)/len(number)
# # # # print(f'The avergae is {result}')
# # # # # 7.Write a Python program to calculate the average of four numbers.
# # # # num1 = float(input('Enter the first number:'))
# # # # num2 = float(input('Enter the second number:'))
# # # # num3 = float(input('Enter the third number:'))
# # # # num4 = float(input('Enter the fourth number:'))
# # # # average = num1 + num2 + num3 + num4/4
# # # # print(f'The average of the four number is {average}')
# # # # # 8.Write a Python program that can convert the time (hour, minute, second) to second.
# # # # hour = int(input('Enter hour:'))
# # # # minute = int(input('Enter minute:'))
# # # # second = int(input('Enter second:'))
# # # # convert_h = hour*3600
# # # # convert_m = minute*60
# # # # result = convert_h+convert_m+second
# # # # print(f'The above time is equal to {result} seconds')
# # # # # 9.Write a Python program that determines if a year entered by the user is a leap year or not. Print "Leap year" if the year is divisible by 4, otherwise print "Not a leap year".
# # # # year = int(input('Enter the year:'))
# # # # if year%4 == 0:
# # # #     print(f'{year} is a leap year.')
# # # # else:
# # # #     print(f'{year} is not a leap year.')
# # # # # 10.Write a Python program to accept two integers and check whether they are equal or not.
# # # # num1 = str(input('Enter the first number:'))
# # # # num2 = str(input('Enter the second number:'))
# # # # if num1 != num2:
# # # #     print(f'{num1} is not equal to {num2}')
# # # # else:
# # # #     print(f'{num1} is equal to {num2}')
# # # # # 11.Write a Python program that checks if a number entered by the user is positive negative or zero.
# # # # num = int(input('Enter the number:'))
# # # # if num ==0:
# # # #     print(f'{num} is zero.')
# # # # elif num > 0:
# # # #     print(f'{num} is positive number.')
# # # # else:
# # # #     print(f'{num} is negative number.')
# # # # # 12.Write a Python program that checks if a character entered by the user is a vowel or a consonant. Print "Vowel" if it's a vowel and "Consonant" if it's a consonant. (vowel: a, e, i, o, u)
# # # # c = input("Enter a character:").lower()
# # # # if c in 'aeiou':
# # # #     print(f'{c} is a vowel.')
# # # # else:
# # # #     print(f'{c} is a consontant.')
# # # # # 13.Write a program that asks the user for their name and then greets them with their name.
# # # # name = input('Enter your name:')
# # # # print('Hello' +' '+ name)
# # # # # 14.Write a program that asks the user for a number and then prints whether the number is odd or even.
# # # # num = int(input('Enter a number:'))
# # # # if num %2 == 0:
# # # #     print(f'{num} is even number.')
# # # # else:
# # # #     print(f'{num} is odd number.')
# # # # 14.Write a program that asks the user for a number (1-7) and prints the corresponding day of the week.
# # # # def switch(choice):
# # # #     if choice ==1:
# # # #         print('Monday')
# # # #     elif choice ==2:
# # # #         print('Tuesday')
# # # #     elif choice ==3:
# # # #         print('Wednesday')
# # # #     elif choice ==4:
# # # #         print('Thursday')
# # # #     elif choice ==5:
# # # #         print('Friday')
# # # #     elif choice ==6:
# # # #         print('Saturday')
# # # #     elif choice ==7:
# # # #         print('Sunday')
# # # # choice = int(input('Enter a number(1-7):'))
# # # # switch(choice)
# # # # 15.Write a Python program to ask a user for 3 numbers (3 variables). Find the maximum number and display on screen
# # # # num1 = int(input('Enter number#1:'))
# # # # num2 = int(input('Enter number#2:'))
# # # # num3 = int(input('Enter number#3:'))
# # # # max_num = max(num1, num2, num3)
# # # # print(f'The maximun number is{max_num}')
# # # # # Program to find the maximum of three numbers using if statements

# # # # # Get three numbers from the user
# # # # num1 = float(input("Enter the first number: "))
# # # # num2 = float(input("Enter the second number: "))
# # # # num3 = float(input("Enter the third number: "))

# # # # # Find the maximum number using if-elif-else
# # # # if num1 >= num2 and num1 >= num3:
# # # #     max_num = num1
# # # # elif num2 >= num1 and num2 >= num3:
# # # #     max_num = num2
# # # # else:
# # # #     max_num = num3

# # # # # Display the result
# # # # print(f"The maximum of the three numbers is: {max_num}")
# # # # 16.Write a Python program to ask a user for 3 numbers (3 variables). Find the minumum number and display on screen
# # # # num1 = int(input('Enter number#1:'))
# # # # num2 = int(input('Enter number#2:'))
# # # # num3 = int(input('Enter number#3:'))
# # # # mini = min(num1, num2, num3)
# # # # print(f'The minimun number is{mini}')
# # # # 17.Write a program that asks the user for two numbers and an operator (+, -, *, /). The program should then perform the corresponding operation and print the result.
# # # # num1 = int(input('Enter a number:'))
# # # # operator = str(input('Enter operator:'))
# # # # num2 = int(input('Enter a number:'))
# # # # if operator =='+':
# # # #     result = num1 + num2
# # # #     print(f'Result:{result}')
# # # # elif operator =='-':
# # # #     result = num1 - num2
# # # #     print(f'Result:{result}')
# # # # elif operator =='*':
# # # #     result = num1 * num2
# # # #     print(f'Result:{result}')
# # # # elif operator =='/':
# # # #     result = num1 / num2
# # # #     print(f'Result:{result}')
# # # # else:
# # # #     print('Ivalid operator!')
# # # # 18.Write a program to display numbers between 0 to 10 using while loops
# # # # i = 0
# # # # while i <= 10:
# # # #     print(i)
# # # #     i += 1
# # # # # 19.Write a program to display numbers between 0 to 10 using for loops
# # # # for i in range(11):
# # # #     print(i)
# # # # 20.Write a program to display “Hello World” 100 times.
# # # # for i in range(101):
# # # #     print(f'{i}.Hello World')
# # # # # 21.Write a program to display numbers between 10 to 100 using while loops.
# # # # i = 10
# # # # while i<=100:
# # # #     print(i)
# # # #     i += 1
# # # # 22.Write a program to display numbers between 10 to 100 using for loops.
# # # # for i in range(10,101):
# # # #     print(i)
# # # # 23.Write a program to display all even numbers in this range 2 to 2000 except the number 10.
# # # # print("All even numbers between [2, 2000] are:", end=" ")
# # # # for i in range(2, 2001):
# # # #     if i % 2 == 0 and i != 10:
# # # #         if i == 2000:
# # # #             print(i)  # No comma after the last number
# # # #         else:
# # # #             print(i, end=", ")
# # # # 24.Write a program to sum all even numbers between 1 and 50 using loops.
# # # # total_sum = 0
# # # # print("The summation of all even numbers between 1 and 50:", end=" ")
# # # # for i in range(1,51):
# # # #     if i % 2 == 0:
# # # #         total_sum +=i
# # # #         if i == 50:
# # # #             print(i, end="=")
# # # #         else:
# # # #             print(i, end="+")
# # # # print(total_sum)
# # # # # 25.Create a program that calculates and prints the power of 2 for the first 10 natural numbers.
# # # # base = 2
# # # # for i in range(1,11):
# # # #     result = base ** i
# # # #     print(f"{base}^{i}={result}")
# # # # 26.Write a program to sum all numbers from n to 1000 except the number 100, where n is an integer number input by the user.
# # # # total_sum = 0
# # # # n = int(input("Enter a number: "))
# # # # for i in range(n, 1001):
# # # #     if i != 100:
# # # #         total_sum += i
# # # # print(f"The total sum from {n} to 1000, excluding 100, is: {total_sum}")
# # # # 27.Write a program to compute summation and subtraction of all numbers from 500 to 10. Display output on screen, use for loop.
# # # # total_sum = 0
# # # # total_sub = 0
# # # # # Calculate the summation and prepare for subtraction
# # # # print("The summation:", end=" ")
# # # # for i in range(500, 9, -1):
# # # #     total_sum += i
# # # #     if i == 10:
# # # #         print(i, end=" = ")
# # # #     else:
# # # #         print(i, end=" + ")
# # # # print(total_sum) 
# # # # # Calculate and display the subtraction
# # # # print("The subtraction:", end=" ")
# # # # for i in range(500, 9, -1):
# # # #     total_sub -= i
# # # #     if i == 10:
# # # #         print(" -",i, end=" = ")
# # # #     elif i == 500:
# # # #         print(-500, end="")  # Print -500 without a leading minus
# # # #     else:
# # # #         print(" -", i, end="")
# # # # print(total_sub)  
# # # # 28.Write a program that calculates the average of a set of numbers input by the user. The user should be able to input as many numbers as desired, and the program should continue until the Informatique user input 0.
# # # # total_sum = 0
# # # # i =0
# # # # print("Enter a number(Enter 0 to stop)")
# # # # while True:
# # # #     n = int(input("Enter a number:"))
# # # #     i+=1
# # # #     if n == 0:
# # # #         break
# # # #     total_sum +=n
# # # #     avergae = total_sum/i
# # # # print(avergae)
# # # # 29.Generate one random number. Then create a simple number guessing game where theuser has to guess a number between 1 and 20. Using loop to continue prompting the user until they guess correctly. The program stops when the user guesses it correctly and tells the user how many that he/she has tried guessing.
# # # # i = 0
# # # # import random
# # # # random_number = random.randrange(1,20)
# # # # while True:
# # # #     n  = int(input("Enter a guess number between 1-20:"))
# # # #     i +=1
# # # #     if n == random_number:
# # # #         print("Correct!")
# # # #         print(f"You have tried {i} times to get it right.")
# # # #         break
# # # #     else:
# # # #         print("Not correct!")
# # # # 30.Write a program to ask a user for an integer number n. The program tells the user how many digits that this number has.
# # # # Hint: Use a while loop. Divide the number by 10 until reaching 0. Each time, try to increase a counter variable which represents the number of digits.
# # # # i = 0
# # # # n = int(input("Enter a number:"))
# # # # original_n = n
# # # # while n > 0:
# # # #     n //= 10
# # # #     i+=1
# # # # print(f'This number {original_n} has {i} digits.')
# # # # from tkinter import *

# # # # # Create the main window
# # # # win = Tk()

# # # # # Set window size and title
# # # # win.geometry("600x250")
# # # # win.title("Sign In")

# # # # # Create and place labels and entry fields
# # # # Label(win, text="Email Address: ", font=12).place(x=10, y=15)
# # # # Entry(win).place(x=10, y=45, width=580, height=35)  # Place the entry inside the window

# # # # Label(win, text="Password: ", font=12).place(x=10, y=75)
# # # # Entry(win, show="*").place(x=10, y=105, width=580, height=35)  # Mask password with 'show="*"'

# # # # # Create and place the login button
# # # # Button(win, text="Login", font=11).place(x=10, y=155, width=580, height=35)

# # # # # Run the Tkinter event loop
# # # # win.mainloop()
# # # # 31
# # # # from tkinter import *
# # # # win = Tk()
# # # # win.geometry("600x250")
# # # # win.title("Address Entry Form")
# # # # Label(win, text="First Name:",font=12).place(x=45,y=0)
# # # # Entry(win).place(x=120, y=0, width=450, height=25)
# # # # Label(win, text="Last Name:",font=12).place(x=45,y=25)
# # # # Entry(win).place(x=120, y=25, width=450, height=25)
# # # # Label(win, text=" Address Line 1:",font=12).place(x=16,y=50)
# # # # Entry(win).place(x=120, y=50, width=450, height=25)
# # # # Label(win, text="Address Line 2:",font=12).place(x=16,y=75) 
# # # # Entry(win).place(x=120, y=75, width=450, height=25)
# # # # Label(win, text="City:",font=12).place(x=82,y=100)
# # # # Entry(win).place(x=120, y=100, width=450, height=25)
# # # # Label(win, text="State/Province:",font=12).place(x=16,y=125)
# # # # Entry(win).place(x=120, y=125, width=450, height=25)
# # # # Label(win, text="Postal Code:",font=12).place(x=30,y=150)
# # # # Entry(win).place(x=120, y=150, width=450, height=25)
# # # # Label(win, text="Country:",font=12).place(x=54,y=175)
# # # # Entry(win).place(x=120, y=175, width=450, height=25)
# # # # Button(win,text='Clear',font=12).place(x=400, y=200, width=80, height=45)
# # # # Button(win,text='Submit',font=12).place(x=480, y=200, width=80, height=45)
# # # # win.mainloop()
# # # # 32.Calculator

# # # from tkinter import *
# # # win = Tk()
# # # win.geometry("300x400")
# # # win.title("Calculator")
# # # display = Entry(win)
# # # display.place(width=300, height=60, x=0, y=70)
# # # def button_click(value):
# # #     current = display.get()  # Get the current text in the display
# # #     display.delete(0, END)  # Clear the display
# # #     display.insert(END, current + str(value))  # Append the pressed button's value to the display
# # # def calculate():
# # #     try:
# # #         result = eval(display.get())  # Evaluate the expression entered in the display
# # #         display.delete(0, END)  # Clear the display
# # #         display.insert(END, str(result))  # Show the result
# # #     except:
# # #         display.delete(0, END)
# # #         display.insert(END, "Error")  # If there's a calculation error, show 'Error'
# # # def clear_display():
# # #     display.delete(0, END)  # Clears the entire display
# # # # Entry(win).place(width=300,height=60,x=0,y=70)
# # # Button(win,text=1,command=lambda:button_click(1)).place(width=50,height=50,x=25,y=130)
# # # Button(win,text=2,command=lambda:button_click(2)).place(width=50,height=50,x=75,y=130)
# # # Button(win,text=3,command=lambda:button_click(3)).place(width=50,height=50,x=125,y=130)
# # # Button(win,text=4,command=lambda:button_click(4)).place(width=50,height=50,x=25,y=180)
# # # Button(win,text=5,command=lambda:button_click(5)).place(width=50,height=50,x=75,y=180)
# # # Button(win,text=6,command=lambda:button_click(6)).place(width=50,height=50,x=125,y=180)
# # # Button(win,text=7,command=lambda:button_click(7)).place(width=50,height=50,x=25,y=230)
# # # Button(win,text=8,command=lambda:button_click(8)).place(width=50,height=50,x=75,y=230)
# # # Button(win,text=9,command=lambda:button_click(9)).place(width=50,height=50,x=125,y=230)
# # # Button(win,text='=',command=calculate).place(width=50,height=50,x=175,y=230)
# # # Button(win,text=0,command=lambda:button_click(0)).place(width=50,height=50,x=175,y=180)
# # # Button(win,text='+',command=lambda:button_click('+')).place(width=50,height=50,x=175,y=130)
# # # Button(win,text='-',command=lambda:button_click('-')).place(width=50,height=50,x=225,y=130)
# # # Button(win,text='/',command=lambda:button_click('/')).place(width=50,height=50,x=225,y=180)
# # # Button(win,text='*',command=lambda:button_click('*')).place(width=50,height=50,x=225,y=230)
# # # Button(win,text='Clear',command=clear_display).place(width=300,height=50,x=0,y=280)

# # # win.mainloop()


# # # from getpass import getpass
# # # name = input("Enter your name:")
# # # password = getpass("Enter your password:")

# # # print("Output:")
# # # print(name)
# # # print(password)



# # # class Car:
# # #     def __init__(self, model, year):
# # #         self.__model = model  # Private attribute
# # #         self.__year = year    # Private attribute

# # #     # Getter method for model
# # #     def modelx(self):
# # #         return self.__model

# # #     # Setter method for model with validation
# # #     def modely(self, model):
# # #         if len(model) > 2:  # Ensure model name is valid
# # #             self.__model = model
# # #         else:
# # #             print("Model name too short!")

# # # # Create a car object
# # # car = Car("Tesla", 2023)

# # # # Access and modify attributes through getter/setter (Encapsulation)
# # # print(car.modelx())  # Use getter method
# # # car.modely("BMW")  # Use setter method to modify the model
# # # print(car.modelx())

# # # # Try setting an invalid model
# # # car.modely("A")  # This will not change the model because the name is too short


# # class BankAccount:
# #     def __init__(self, account_holder, initial_balance=0):
# #         self.account_holder = account_holder
# #         self.balance = initial_balance  

# #     def get_balance(self):
# #         return self.balance

# #     def deposit(self, amount):
# #         if amount > 0:
# #             self.balance += amount
# #         else:
# #             print("Deposit amount must be positive")

# #     def withdraw(self, amount):
# #         if 0 < amount <= self.__balance:
# #             self.balance -= amount
# #         else:
# #             print("Invalid amount or insufficient balance")

# # # Usage
# # account = BankAccount("Alice", 100)
# # account.deposit(50)     
# # print(account.get_balance())  # output 150
# # account.balance = -1000     # nh kae value bos balance
# # print(account.get_balance())  # output -1000


# # class BankAccount:
# #     def __init__(self, account_holder, initial_balance=0):
# #         self.account_holder = account_holder
# #         self.__balance = initial_balance  

# #     def get_balance(self):
# #         return self.__balance

# #     def deposit(self, amount):
# #         if amount > 0:
# #             self.__balance += amount
# #         else:
# #             print("Deposit amount must be positive")

# #     def withdraw(self, amount):
# #         if 0 < amount <= self.__balance:
# #             self.__balance -= amount
# #         else:
# #             print("Invalid amount or insufficient balance")

# # # Usage
# # account = BankAccount("Alice", 100)
# # account.deposit(50)     
# # print(account.get_balance())  # output 150
# # account.__balance = -1000     # nh kae value bos balance
# # print(account.get_balance())  # output 150




# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder
#         self.__balance = initial_balance  # Private attribute

#     # Getter for balance
#     @property
#     def balance(self):
#         return self.__balance

#     # Setter for balance with validation
#     @balance.setter
#     def balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Balance cannot be negative")

#     # Deposit method
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive")

#     # Withdraw method
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Invalid amount or insufficient balance")

# # Usage
# account = BankAccount("Alice", 100)
# account.deposit(50)     
# print(account.balance)  # Output: 150

# # Attempting to set balance directly
# account.balance = 1000  # Output: Balance cannot be negative
# print(account.balance)   # Output: 150 (unchanged)
