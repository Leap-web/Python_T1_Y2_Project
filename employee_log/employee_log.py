import hashlib
import msvcrt
def masked_input(prompt= ""):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b'\r',b'\n'}:
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

def encrypt_password(password):
        if len(password) == 64 and all(c in '1234567890!@#$%&*abcdef' for c in password.lower()):
            return password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

def save_admin_to_file(self, username, id, email, hashed_password):
    with open(self.employee_file, "a") as file:
            file.write(f"Username: {username}, ID: {id}, Email: {email}, Password: {hashed_password}\n")
    print("Employee account created successfully.")

def create_employee_account(self):
    while True:
        print("Eg: Name: John_Doe")
        username = input("Enter employee_account name: ")
        if username and "_" in username and not any(c.isspace() for c in username) and any(c.isupper() for c in username) and any (c.islower() for c in username) and any(c.islower() for c in username):
            while True:
                print("Eg: Email: john.doe@employee.iec.com")
                email = input("Enter employee_account email: ")
                if "@employee.iec.com" in email and not any(c.isupper() for c in email) and not any(c.isspace() for c in email):
                    while True:
                        id = input("Create employee_account ID (Eg: IDTB1234): ")
                        if id.startswith("IDTB"):
                            while True:
                                passwords = masked_input("Create password: ")
                                if (
                                    len(passwords) >= 8
                                    and any(c.isupper() for c in passwords)
                                    and any(c.islower() for c in passwords)
                                    and any(c.isdigit() for c in passwords)
                                    and any(c in "!@#$%^&*()_+-=" for c in passwords)
                                    ):
                                    self.log_action("Added new employee_account", "employee_account")
                                    hashed_password = self.hash_password(passwords)

                                        # Save_account details to file         
                                    self.save__to_file(username, id, email, hashed_password)
                                    return
                                else:
                                    print("Password must contain at least 8 characters, including uppercase, lowercase, a number, and a special character.")
                        else:
                                print("Employee_account ID must start with 'IDTB'")
                else:
                        print("Invalid email format. Ensure it ends with '@employee_account.iec.com' and contains no spaces or uppercase letters.")
        else:
                print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")

        hashed_pw = self.hash_password()
        self.save_employee_to_file(username, email, id, hashed_pw)
        self.employee.append({"username": username, "email": email, "id": id, "password": hashed_pw})
        print("Employee account create successful!\n")
        break

def check_employee_inf(username, email, ID, password):
    hashed_password = encrypt_password(password)
    try:
        with open(r'C:\Users\User\OneDrive\ドキュメント\GitHub\Python_T1_Y2_Project\employee_log\employee_log.py', 'r') as file:
            for line in file:
                stored_username, stored_email, stored_ID, stored_password = line.strip().split(',')
                if (stored_username.strip().lower() == username.strip().lower() and
                    stored_email.strip().lower() == email.strip().lower() and
                    stored_ID.strip() == ID.strip() and
                    stored_password.strip() == hashed_password):
                    return True
            return False
    except FileNotFoundError:
        print("Employee information not found!")
        return False
    
def employee_login():
    print("----------------------------------------------")
    print("||              EMPLOYEE_LOGIN              ||")
    print("----------------------------------------------")
    for attempt in range(2):
        employee_username = input("Enter your username: ")
        employee_email = input("Enter your email: ")
        employee_id = input("Enter your ID: ")
        employee_password = masked_input("Enter your password: ")
    
        if check_employee_inf(employee_username,employee_email,employee_id,employee_password):
            print("\n<<<<<<<<<<<<<<<YOU ARE OUR EMPLOYEE>>>>>>>>>>>>>>>")
            return
        else:
            if attempt == 0:
                print("\n############### LOGIN FAILED. YOU HAVE 1 MORE ATTEMPT ###############")
            else:
                print("\n############### LOGIN FAILED. NO MORE ATTEMPTS ALLOWED. ###############")
    print("======/Access denied./======")
employee_login()