    
    
    
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
                    pw = input("Enter a password: ")
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
                    new_user = {"username": user, "email": email, "password": pw}
                    self.users.append(new_user)
                    file.write(f"username: {new_user['username']}, email: {new_user['email']}, password: {new_user['password']}\n")
                    break
        except Exception as e:
            print(f"There's an error with your registration: {e}please try again!")
        else:
            print("Registration successful with a strong password!")

    def login(self):
        for i in range(3, 0, -1):
            user = input("Enter your username: ")
            pw = input("Enter your password: ")
            for j in self.users:
                if j["username"] == user and j["password"] == pw:
                    print(f"Login successfuf! Welcome, {user}")
                    break
            else:
                print(f"Invalid credentials. You have {i - 1} attempts left")
                continue
            break
        else:
            print("Too many failed attempts. Access blocked.")
                    
    def forgot(self):
            user = input("Enter your username to retrieve your password: ")
            for k in self.users:
                if k["username"] == user:
                    print(f"Your password is: {k["password"]}")
                    break
            else:
                print(f"There is no account with username {user}")
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
                print("3. Return")
                print("4. exit")
                option = int(input("Choose an option (1-4): "))
                if option == 1:
                    self.login()
                elif option == 2:
                    self.register()
                elif option == 3:
                    self.return_back()
                elif option == 4:
                    print("Exiting the programs. Goodbye!\n")
                    break
        except ValueError:
            print("Invalid option. Please choose an option (1-4): ")
filename = "Customer/customer_pw.txt"
user1 = User(filename)
user1.register()

def usage_menu():
    pass

