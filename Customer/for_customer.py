import hashlib
import getpass

    
    
class User:
    def __init__(self, filename):
        self.filename = filename
        self.users = []
        self.load_users()

    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
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
            print(f"{self.filename} not found.")

    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def hash_secret_pin(self,pin):
        return hashlib.sha256(pin.encode()).hexdigest()  

    def register(self):
        try:  
            with open(self.filename, 'a') as file:   
                while 1 > 0:
                    user = input("Enter a username to register: ")
                    for i in self.users:
                        if user == i["username"]:
                            print("This user has already been existed. Please try again!")
                            break
                    else:
                        break

                while 1 > 0:
                    email = input("Enter your email address: ")
                    if '@' in email and '.' in email: 
                        break
                    else:
                        print("Invalid email format. Please enter a valid email address.")
                        continue

                while 1 > 0:
                    pw = getpass.getpass("Enter a Password: ")
                    if len(pw) < 8:
                        print("Password too short. Must be at least 8 Characters.")
                        continue
                    if not any(c.isupper()for c in pw):
                        print("Password must contain at least one uppercase letter.")
                        continue
                    if not any(c.islower()for c in pw):
                        print("password must contain at least one lowercase letter.")
                        continue
                    if not any(c.isdigit()for c in pw):
                        print("Password must contain at least one digit.")
                        continue
                    if not any(c in '!@#$%^&*'for c in pw):
                        print("Password must contain at least one special character.")
                        continue
                    confirm_pw = getpass.getpass("Confirm your Password: ")
                    if confirm_pw != pw:
                        print("Password do not match. Please try again.")
                        continue
                    break

                while 1 > 0:
                    secret_pin = getpass.getpass("Enter a secret Pin: ")
                    if len(secret_pin) < 4:
                        print("Secret is too short. Must be a 4-digit number.")
                        continue
                    if not (s.isdigit() for s in secret_pin):
                        print("Pin must be a number.")
                        continue

                    hashed_pw = self.hash_password(pw)
                    hashed_secret_pin = self.hash_secret_pin(secret_pin)
                    new_user = {"username": user, "email": email, "password": hashed_pw, "secret pin": hashed_secret_pin}
                    self.users.append(new_user)
                    file.write(f"username: {new_user['username']}, email: {new_user['email']}, password: {new_user['password']}, secret pin: {new_user['secret pin']}\n")
                    break
        except Exception as e:
            print(f"There's an error with your registration: {e}. please try again!.")
        else:
            print("Registration account successful!")

    def login(self):
        try:
            for i in range(3, 0, -1):
                user = input("Enter your username: ")
                email = input("Enter your email: ")
                pw = getpass.getpass("Enter your password: ")
                hashed_pw = self.hash_password(pw)
                for j in self.users:
                    if j["username"] == user and j["email"] == email and j["password"] == hashed_pw :
                        break
                else:
                    print(f"Invalid credentials. You have {i - 1} attempts left")
                    continue
                break
            else:
                print("Too many failed attempts. Access blocked.")
        except Exception as e:
            print(f"There is an error with your logn: {e}. Please try again!.")
        else:
            print(f"Login successful! Welcome, {user}")

    def forgot(self):
        try:
            with open(self.filename, "w") as file:
                user = input("Enter your username: ")
                email = input("Enter your email: ")
                secret_pin = getpass.getpass("Enter your secret pin:")
                hashed_secret_pin = self.hash_secret_pin(secret_pin)
                for k in self.users:
                    if k["username"] == user and k["email"] == email and k["secret pin"] == secret_pin:
                        pw = getpass.getpass("Enter your new password: ")
                        for f in self.users:
                            if f["user"] == user and f["email"] == email and f["secret pin"] == secret_pin:
                                f["password"] = pw
                                file.write(f"username: {f['username']}, email: {f['email']}, password: {f['password']}, secret pin: {f['secret pin']}\n")
                                break
                            break
                    break
                else:
                    print(f"There is no valid account with {user} exist.")
        except Exception as e:
            print(f"There is an error occur in your forgot proceess: {e} Please try again!.")
        else:
            print("Reset password succesfully!.")
    def return_back(self):
        pass
    
    def browse_item(self):
        pass

    def place_order(self):
        pass

    def manage_balance(self):
        pass

    def user_menu(self):
        print("============================================================")
        print("|                         Role User                        |")
        print("============================================================")
        try:
            while 1 > 0:
                print("Menu:")
                print("1. login")
                print("2. Register")
                print("3. Forgot Password")
                print("4. Return")
                print("5. exit")
                option = int(input("Choose an option (1-4): "))
                if option == 1:
                    self.login()
                elif option == 2:
                    self.register()
                elif option == 3:
                    self.forgot() 
                elif option == 4:
                    self.return_back()
                elif option == 5:
                    print("Exiting the programs. Goodbye!\n")
                    break
        except ValueError:
            print("Invalid option. Please choose an option (1-4): ")

    def show_list(self):
        print(self.users)
filename = "Customer/customer_pw.txt"
user1 = User(filename)

user1.register()
# user1.show_list()
# user1.login()

def usage_menu():
    pass

