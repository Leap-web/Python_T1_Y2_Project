import hashlib
import os
import msvcrt

class Employeesystem:

    employeefile = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\inf_employee.txt"

    def __init__(self):
        self.employee_filename = self.employeefile  # Correctly set the file name
        self.employees = []  # Initialize the employees list
        self.load_employees()

    def choose_option(self): 
        
        while True:
            print("\n********** Employee System *********")
            print("1. Create employee account.")
            print("2. Employee login.")
            print("3. Exit")
            option = input("Enter your choice: ")
            os.system('cls')
            if option == "1":
                self.create_employee_account()
            elif option == "2":
                self.employee_login()
            elif option == "3":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again!")

    def load_employees(self):
        
        try:
            with open(self.employee_filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    if ": " in line:
                        parts = line.split(", ")
                        employee_data = {}
                        for part in parts:
                            if ": " in part:
                                key, value = part.split(": ")
                                employee_data[key] = value
                        self.employees.append(employee_data)  # Add to the employees list
            print("Employees loaded successfully!")
        except FileNotFoundError:
            print(f"{self.employee_filename} not found. Starting with an empty employee list.")

    def masked_input(self, prompt=""):
        print(prompt, end="", flush=True)
        password = ""
        while True:
            char = msvcrt.getch()
            if char in {b'\r', b'\n'}:
                print()
                break
            elif char == b'\x08':
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end='', flush=True)
            else:
                password += char.decode()
                print('*', end='', flush=True)
        return password

    def hash_password(self, password):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt + hashed_password
    
    def verify_password(self, stored_password, input_password):
        salt = stored_password[:16]
        stored_hash = stored_password[16:]
        input_hash = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
        return stored_hash == input_hash

    def create_employee_account(self):
        try:  
            with open(self.employee_filename, 'a') as file:   
                while True:
                    print("\n============================== Create Account ==============================")
                    username = input("\nEnter a username to create account: ")
                    for i in self.employees:
                        if username == i["username"]:
                            print("This user already exists. Please try again!\n")
                            break
                    else:
                        break

                while True:
                    email = input("Enter your email address (e.g: john.doe@employee.iec.com): ")
                    if "@employee.iec.com" in email and not any(c.isupper() for c in email) and not any(c.isspace() for c in email):
                        break
                    else:
                        print("Invalid email format. Please enter a valid email address.\n")
                        continue

                while True:
                    id = input("Create employee account ID (Eg: IDTB1234): ")
                    if id.startswith("IDTB"):
                        break
                    else:
                        print("Invalid ID format. Please enter a valid ID.\n")

                while True:
                    password = self.masked_input("Enter a Password: ")
                    if len(password) < 8:
                        print("Password too short. Must be at least 8 characters.\n")
                        continue
                    if not any(c.isupper() for c in password):
                        print("Password must contain at least one uppercase letter.\n")
                        continue
                    if not any(c.islower() for c in password):
                        print("Password must contain at least one lowercase letter.\n")
                        continue
                    if not any(c.isdigit() for c in password):
                        print("Password must contain at least one digit.\n")
                        continue
                    if not any(c in '!@#$%^&*' for c in password):
                        print("Password must contain at least one special character.\n")
                        continue
                    confirm_password = self.masked_input("Confirm your Password: ")
                    if confirm_password != password:
                        print("Passwords do not match. Please try again.\n")
                        continue
                    break

                hashed_password = self.hash_password(password)
                employee_data = {"username": username, "email": email, "id": id, "password": hashed_password.hex()}
                self.employees.append(employee_data)
                file.write(f"username: {username}, email: {email}, id: {id}, password: {hashed_password.hex()}\n")
                print("Employee account created successfully!\n")
                    
        except Exception as e:
            print(f"Error while creating account: {e}. Please try again!")
            
    def employee_login(self):
        try:
            for attempts_left in range(3, 0, -1):
                print("\n================ Login =================")
                username = input("Enter your username: ")
                email = input("Enter your email: ")
                password = self.masked_input("Enter your password: ")

                for employee in self.employees:
                    if employee["username"] == username and employee["email"] == email and self.verify_password(bytes.fromhex(employee["password"]), password):
                        print(f"Welcome, {username}! Login successful.")
                        return
                print(f"Invalid username, email, or password. You have {attempts_left - 1} attempts left.")
            print("Too many failed attempts. Access denied.")
        except Exception as e:
            print(f"Error during login: {e}")

if __name__ == "__main__":
    system = Employeesystem()
    system.choose_option()
<<<<<<< HEAD













      
=======
>>>>>>> origin/main
