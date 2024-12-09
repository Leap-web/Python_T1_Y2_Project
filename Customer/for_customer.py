import hashlib
import getpass
import sys


class User:
    def __init__(self, user_filename, balance_filename):
        self.user_filename = user_filename
        self.balance_filename = balance_filename
        self.users = []
        self.load_users()
        self.balance = 0.0
        self.balances = {}
        self.load_balance()

    def load_users(self):
        try:
            with open(self.user_filename, 'r') as file:
                for line in file:
                    line = line.strip() 
                    if not line:  
                        continue
                    if ": " in line:
                        parts = line.split(", ")
                        user_data = {}
                        for part in parts:
                            if ": " in part:
                                key, value = part.split(": ")
                                user_data[key] = value
                        self.users.append(user_data)
        except FileNotFoundError:
            print(f"{self.user_filename} not found.")

    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def hash_secret_pin(self,pin):
        return hashlib.sha256(pin.encode()).hexdigest()  

    def register(self):
        try:  
            with open(self.user_filename, 'a') as file:   
                while True:
                    print("\n==============================Register==============================")
                    username = input("\nEnter a username to register: ")
                    for i in self.users:
                        if username == i["username"]:
                            print("This user has already been existed. Please try again!\n")
                            break
                    else:
                        break

                while True:
                    email = input("Enter your email address: ")
                    if '@' in email and '.' in email: 
                        break
                    else:
                        print("Invalid email format. Please enter a valid email address.\n")
                        continue

                while True:
                    pw = getpass.getpass("Enter a Password: ")
                    if len(pw) < 8:
                        print("Password too short. Must be at least 8 Characters.\n")
                        continue
                    if not any(c.isupper()for c in pw):
                        print("Password must contain at least one uppercase letter.\n")
                        continue
                    if not any(c.islower()for c in pw):
                        print("password must contain at least one lowercase letter.\n")
                        continue
                    if not any(c.isdigit()for c in pw):
                        print("Password must contain at least one digit.\n")
                        continue
                    if not any(c in '!@#$%^&*'for c in pw):
                        print("Password must contain at least one special character.\n")
                        continue
                    confirm_pw = getpass.getpass("Confirm your Password: ")
                    if confirm_pw != pw:
                        print("Password do not match. Please try again.\n")
                        continue
                    break

                while True:
                    secret_pin = getpass.getpass("Enter a secret Pin: ")
                    if len(secret_pin) < 4:
                        print("Secret is too short. Must be a 4-digit number.\n")
                        continue
                    if len(secret_pin) > 4:
                        print("Secret is too long. Must be a 4-digit number.\n")
                        continue
                    if not secret_pin.isdigit():
                        print("Pin must be a number.\n")
                        continue

                    hashed_pw = self.hash_password(pw)
                    hashed_secret_pin = self.hash_secret_pin(secret_pin)
                    new_user = {"username": username, "email": email, "password": hashed_pw, "secret pin": hashed_secret_pin}
                    self.users.append(new_user)
                    file.write(f"username: {new_user['username']}, email: {new_user['email']}, password: {new_user['password']}, secret pin: {new_user['secret pin']}\n")
                    print("Registration account successful!\n")
                    
                    with open(self.balance_filename, "a") as balance_file:
                        balance_file.write(f"username: {username}, balance: {self.balance}\n")
                    break
        except Exception as e:
            print(f"There's an error with your registration: {e}. please try again!.")
        
    def login(self):
        try:
            for i in range(3, 0, -1):
                print("\n==============================Login==============================")
                username = input("\nEnter your username: ")
                email = input("Enter your email: ")
                pw = getpass.getpass("Enter your password: ")
                hashed_pw = self.hash_password(pw)
                for user in self.users:
                    if user["username"] == username and user["email"] == email and user["password"] == hashed_pw :
                        print(f"Login successfully! Welcome, {username}\n")
                        self.current_user = username
                        self.load_balance()
                        self.usage_menu()
                        break
                else:
                    print(f"Invalid credentials. You have {i - 1} attempts left")
                    continue
                break
            else:
                print("Too many failed attempts. Access blocked.\n")
        except Exception as e:
            print(f"There is an error with your login: {e}. Please try again!.")
            

    def forgot(self):
        try:
            print("\n==============================Forgot==============================")
            username = input("\nEnter your username: ")
            email = input("Enter your email: ")
            secret_pin = getpass.getpass("Enter your secret pin:")
            hashed_secret_pin = self.hash_secret_pin(secret_pin)
            # user_found = False
            for k in self.users:
                if k["username"] == username and k["email"] == email and k["secret pin"] == hashed_secret_pin:
                    # user_found = True
                    while True:
                        new_pw = getpass.getpass("Enter your new password: ")
                        if len(new_pw) < 8:
                            print("Password too short. Must be at least 8 Characters.")
                            continue
                        if not any(c.isupper()for c in new_pw):
                            print("Password must contain at least one uppercase letter.")
                            continue
                        if not any(c.islower()for c in new_pw):
                            print("password must contain at least one lowercase letter.")
                            continue
                        if not any(c.isdigit()for c in new_pw):
                            print("Password must contain at least one digit.")
                            continue
                        if not any(c in '!@#$%^&*'for c in new_pw):
                            print("Password must contain at least one special character.")
                            continue
                        confirm_pw = getpass.getpass("Confirm your Password: ")
                        if confirm_pw != new_pw:
                            print("Password do not match. Please try again.")
                            continue
                        break
                    hashed_pw = self.hash_password(new_pw)
                    k["password"] = hashed_pw
                    print("Reset password successfully!.\n")

                    with open(self.user_filename, "w") as file:
                        for user in self.users: 
                            file.write(f"username: {user['username']}, email: {user['email']}, password: {user['password']}, secret pin: {user['secret pin']}\n")
                    break
            else:
                print(f"There is no valid account with {username} exist.\n")
        except Exception as e:
            print(f"There is an error occur in your forgot proceess: {e} Please try again!.")
            
    def load_balance(self):
        try:
            with open(self.balance_filename, 'r') as file:
                for line in file:
                    line = line.strip() 
                    if not line:  
                        continue
                    # if (": "* 2) in line:
                    if ": " in line and ", " in line:
                        parts = line.split(", ")
                        username_part = parts[0].split(": ")[1]  
                        balance_part = parts[1].split(": ")[1]  
                        self.balances[username_part] = float(balance_part)
        except FileNotFoundError:
            print(f"{self.balance_filename} not found.")

    def manage_balance(self):
        try:
            print("\n==============================Manage Balance==============================")
            while True:
                print(f"\nYour current balance: ${self.balances[self.current_user]}")
                print("1. Deposit Balance")
                print("2. Back")
                option = int(input("Choose Option(1,2): "))
                if option == 1:
                    print("\n------------------------------Deposit Balance------------------------------")
                    amount = float(input("\nInput the amount you want to deposit: "))
                    if amount > 0:
                        secret_pin = getpass.getpass("Enter your secret pin:")
                        hashed_secret_pin = self.hash_secret_pin(secret_pin)
                        for i in self.users:
                            if i["username"] == self.current_user and i["secret pin"] == hashed_secret_pin:
                                self.balances[self.current_user] += amount
                                print("Deposited successfully!")
                                print(f"Your balance now is ${self.balances[self.current_user]}")
                                with open(self.balance_filename, "w") as balance_file:
                                    for username, balance in self.balances.items():
                                        balance_file.write(f"username: {username}, balance: {balance}\n")
                            else:
                                print("Invalid pin please try again!") 
                    else:
                        print("Invalid amount. Please enter a valid amount.")
                elif option == 2:
                    print("\n")
                    break
                else:
                    print("Please input a valid option(1-2)!\n")
        except Exception as e:
            print(f"An error occur in your deposit process: {e}. Please try again!")
        
    def edit_profile(self):
        try:
            while True:
                print("\n------------------------------Edit Profile------------------------------")
                print("1. Edit Name")
                print("2. Edit Email")
                print("3. Edit Secret Pin")
                print("4. Edit Password")
                print("5. Back")
                option = int(input("Choose option(1-5): "))
                if option == 1:
                    print("\n------------------------------Edit Name------------------------------")
                elif option == 2:
                    print("\n------------------------------Edit Email------------------------------")
                elif option == 3:
                    print("\n------------------------------Edit Secret Pin------------------------------")
                elif option == 4:
                    print("\n------------------------------Edit Password------------------------------")
                elif option == 5:
                    print("\n")
                    break
                else:
                    print("Invalid option. Please choose option(1-4)!")

        except Exception as e:
            print(f"An error occur in your editing process: {e}. Please try again!")

    def manage_profile(self):
        try:
            print("\n==============================Manage Profile==============================")
            while True:
                print("\n1. View Profile")
                print("2. Edit Profile")
                print("3. Back")
                option = int(input("Choose Option(1-3): "))
                if option == 1:
                    print("\n------------------------------View Profile------------------------------")
                    for v in self.users:
                        print(f"\nName: {self.current_user}")
                        print(f"Email: {v['email']}\n")
                        
                elif option == 2:
                    self.edit_profile()
                    continue
                elif option == 3:
                    break
                else:
                    print("Invalid option. Please choose option(1,3)!\n")
        except Exception as e:
            print(f"An error occur in your managing process: {e}. Please try again!")

    def browse_item(self):
        pass

    def place_order(self):
        pass

    def order_history(self):
        pass

    def user_menu(self):
        try:
            while True:
                print("============================================================")
                print("|                         Role User                        |")
                print("============================================================")
                print("Menu:")
                print("1. Login")
                print("2. Register")
                print("3. Forgot Password")
                print("4. Back")
                print("4. Help Us")
                print("6. Exit")
                option = int(input("Choose an option (1-6): "))
                if option == 1:
                    self.login()
                    continue
                elif option == 2:
                    self.register()
                    continue
                elif option == 3:
                    self.forgot() 
                    continue
                elif option == 4:
                    print("Return back to Role.\n")
                    continue
                # elif option == 5:
                #     self.help_us()
                    continue
                elif option == 6:
                    print("Exiting the programs. Goodbye!\n")
                    sys.exit()
                else:
                    print("Invalid option. Please choose an option (1-6)!\n")
                
        except ValueError:
            print("Invalid option. Please choose an option (1-6)!\n")

    def usage_menu(self):
        try:
            while True:
                print("============================================================")
                print("|                         Role User                        |")
                print("============================================================")
                print(f"Welcome, {self.current_user}")
                print("Usage Menu:")
                print("1. Browse Item")
                print("2. Order History")
                print("3. Manage Balance")
                print("4. Manage Profile")
                print("5. Back")
                print("6. Help Us")
                print("7. Exit")
                option = int(input("Choose an option (1-6): "))
                if option == 1:
                    self.browse_item()
                    continue
                elif option == 2:
                    self.order_history()
                    continue
                elif option == 3:
                    self.manage_balance()
                    continue 
                elif option == 4:
                    self.manage_profile()
                    continue
                elif option == 5:
                    print("Return back to main menu.\n")
                    break
                # elif option == 6:
                #     self.help_us()
                    continue
                elif option == 7:
                    print("Exiting the programs. Goodbye!\n")
                    sys.exit()
                else:
                    print("Invalid option. Please choose an option (1-6)!\n")
        except ValueError:
            print("Invalid option. Please choose an option (1-6)!\n")


    def show_list(self):
        print(self.balances)
user_file = "Customer/customer_pw.txt"
balance_file = "Customer/customer_balance.txt"
user1 = User(user_file, balance_file)
user1.show_list()
user1.user_menu()



