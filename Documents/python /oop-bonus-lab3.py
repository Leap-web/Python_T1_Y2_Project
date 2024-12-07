import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.user_list = []

    def register(self):
        username = input("Please input the username: ")
        while True:
            symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            password = input("Please input the password: ")
            
            has_islower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_isupper = any(c.isupper() for c in password)
            has_symbols = any(c in symbols for c in password)
            
            # Check if all password conditions are met
            if len(password) >= 8 and has_islower and has_digit and has_isupper and has_symbols:
                new_user = User(username, password)
                self.user_list.append(new_user)
                print(f"{username} is successfully registered!")
                break
            else:
                print("Please input a strong password! (Contain lowercase and uppercase letters, numbers, and symbols)")

    def login(self):
        # max_attempts = 3
        # for attempt in range(1, max_attempts + 1):
        #     username = input("Please input your username: ")
        #     password = input("Please input your password: ")
            
        #     # Check if username and password match any user in the list
        #     # user = next((user for user in self.user_list if user.username == username and user.password == password), None)
        #     for user in self.user_list:
        #         if user.username == username and user.password == password:
        #             print(f"Welcome back, {username}")
        #             break
        #     else:
        #         attempt_left = max_attempts - attempt
        #         print("Your username or password is incorrect!")
        #         if attempt_left > 0:
        #             print(f"Invalid credentials. You have {attempt_left} attempts left.")
        #         else:
        #             print("Too many failed attempts. Access blocked.")
        
        attempts = 0
        max_attempts = 3
        # is_running = True

        while attempts < max_attempts:
            old_user = input("Please input your username: ")
            if old_user in self.user_list:
                old_pass = input("Please input your password: ")
                for user in self.user_list:
                    if user['Username'] == old_user and user['Password'] == old_pass:
                        print(f"Welcome back, {old_user}")
                        is_running = False
                        break
    
                else:
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"Invalid credentials. You have {max_attempts - attempts} attempts left.")
                    else:
                        print("Too many failed attempts. Access blocked.")
                        is_running = False
            else:
                print(f"{old_user} not found!")
                
    def forget_password(self):
        username = input("Enter your username to retrieve your password: ")
        user = next((user for user in self.user_list if user.username == username), None)
        if user:
            print(f"Your password is: {user.password}")
        else:
            print(f"{username} not found!")

def main():
    user_manager = UserManager()
    while True:
        print("Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Forget Password")
        print("4. Exit")
        option = input("Choose an option (1-4): ")
        
        os.system('clear')
        if option == '1':
            user_manager.register()
        elif option == '2':
            user_manager.login()
        elif option == '3':
            user_manager.forget_password()
        elif option == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
