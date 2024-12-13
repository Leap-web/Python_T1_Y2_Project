import hashlib
import os
import msvcrt

class EmployeeSystem:
    def __init__(self):
        self.employee = []
        self.load_employee()
    
    def choose_option(self): 
        
        while True:
            print("\n**********EmployeeSystem*********")
            print("1. Create account employee.")
            print("2. Employee login.")
            option = input("Enter your choice: ")
            os.system('cls')
            if option == "1":
                self.create_employee_account()
            elif option == "2":
                self.employee_login()
                break
            else:
                print("Invalid option. Please try again!")

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

    def encrypt_password(self, password):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt + hashed_password
    
    def verify_password(self, stored_password, input_password):
        salt = stored_password[:16]
        stored_hash = stored_password[16:]
        input_hash = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
        return input_hash == stored_hash

    def save_employee_to_file(self, username, email, id, hashed_password):
        os.makedirs("employee_log", exist_ok=True)
        with open("employee_log/employee_inf.txt", "a") as file:
            file.write(f"Username: {username}, Email: {email}, ID: {id},Password: {hashed_password.hex()}\n")

    def load_employee(self):
        try:
            with open("employee_log/employee_inf.txt", "r") as file:
                for line in file:
                    fields = dict(field.split(": ", 1) for field in line.strip().split(", "))
                    self.employee.append({
                        "username": fields["Username"],
                        "email": fields["Email"],
                        "id": fields["ID"],
                        "password": fields["Password"]
                    })
        except FileNotFoundError:
            pass
        except KeyError as e:
            print(f"KeyError: Missing key {e} in the file.")

    def create_employee_account(self):
        while True:
            print("Eg: Name: John_Doe")
            username = input("Enter employee account name: ")
            if username and "_" in username and not any(c.isspace() for c in username) and any(c.isupper() for c in username) and any(c.islower() for c in username):
                while True:
                    print("Eg: Email: john.doe@employee.iec.com")
                    email = input("Enter employee account email: ")
                    if "@employee.iec.com" in email and not any(c.isupper() for c in email) and not any(c.isspace() for c in email):
                        while True:
                            id = input("Create employee account ID (Eg: IDTB1234): ")
                            if id.startswith("IDTB"):
                                while True:
                                    passwords = self.masked_input("Create password: ")
                                    if (
                                        len(passwords) >= 8
                                        and any(c.isupper() for c in passwords)
                                        and any(c.islower() for c in passwords)
                                        and any(c.isdigit() for c in passwords)
                                        and any(c in "!@#$%^&*()_+-=" for c in passwords)
                                    ):
                                        hashed_password = self.encrypt_password(passwords)
                                        self.save_employee_to_file(username, email, id, hashed_password)
                                        self.employees.append({"username": username, "email": email, "id": id, "password": hashed_password.hex()})
                                        print("Employee account created successfully!")
                                        return
                                    else:
                                        print("Password must contain at least 8 characters, including uppercase, lowercase, a number, and a special character.")
                            else:
                                print("Employee account ID must start with 'IDTB'")
                    else:
                        print("Invalid email format. Ensure it ends with '@employee.iec.com' and contains no spaces or uppercase letters.")
            else:
                print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")

    

    def employee_login(self):
        print("----------------------------------------------")
        print("||              EMPLOYEE_LOGIN              ||")
        print("----------------------------------------------")
        for attempt in range(2):
            employee_username = input("Enter your username: ")
            employee_email = input("Enter your email: ")
            employee_id = input("Enter your ID: ")
            employee_password = self.masked_input("Enter your password: ")
            for employee in self.employee:
                if (
                    employee["username"] == employee_username and
                    employee["email"] == employee_email and
                    employee["id"] == employee_id and
                    self.verify_password(bytes.fromhex(employee["password"]), employee_password)
                ):
                    print(f"\nLogin successful! Welcome, {employee_username}.")
                    return
            else:
                if attempt == 0:
                    print("\n############### LOGIN FAILED. YOU HAVE 1 MORE ATTEMPT###############")
                else:
                    print("\n############### LOGIN FAILED. NO MORE ATTEMPTS ALLOWED. ###############")
        print("======/Access denied./======")


employee = EmployeeSystem()
employee.choose_option()
