from datetime import datetime
import sys
import msvcrt
import os
import bcrypt
from getpass import getpass
import ast
import hashlib

class FirstInterface:
    def display(self):
        while True:
            os.system('cls')
            print("=" * 50)
            print("\tWelcome to the E-Commerce System")
            print("=" * 50)
            print("1. 🛠️  Admin")
            print("2. 💻  Employee")
            print("3. 🛒  Customer")
            print("4. ❌  Exit")
            print("=" * 40)
            
            # Get the user's choice
            choose_role = input("Choose your role (1-4): ")
            
            if choose_role == '1':
                admin_system = AdminSystem()
                admin_system.display_admin_account()
            elif choose_role == '2':
                employee_system = EmployeeInterface
                employee_system.display_employee_account()
            elif choose_role == '3':
                pass
            elif choose_role == '4':
                print("\n❕Exiting the system. Thank you for using it!")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice. Please try again.")
                input("Press Enter to continue...")

    ######  ADMIN PART ######

class AdminSystem(FirstInterface):
    # File paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    admin_manage = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/admin_manage.txt'
    manage_employ = r'C:/Users/USER/Documents/GitHubLeapp/Python_T1_Y2_Project/Admin_work/manage_employee.txt'
    system_log = r'C:/Users/USER/Documents/GitHubLeapp/Python_T1_Y2_Project/Admin_work/system_log.txt'

    def __init__(self):
        self.display_admin_account()

    def display_admin_account(self):
        while True:
            try:
                os.system('cls')
                print("\nWelcome Admin")
                print("1. Create Account For Admin")
                print("2. Log in as Admin")
                print("3. Back To Main Menu")

                choose = int(input("Enter ur function to do: "))
                if choose == 1:
                    self.create_admin_account()
                elif choose == 2:
                    self.admin_log()
                elif choose == 3:
                    return
                    # main_menu()
                else:
                    print("Invalid option")
            except ValueError as v:
                print(v)


    def admin_dashboard(self):
        os.system('cls')
        print("\nAdmin Dashboard")
        print("1. Add or update stock")
        print("2. View stock")
        print("3. Delete stock")
        print("4. Manage Employee accounts")
        print("5. Manage Customer accounts")
        print("6. Sales Report")
        print("7. History system log")
        print("8. Exit")

        while True:
            try:
                choose = int(input("Choose your task to do: "))
                if choose == 1:
                    self.add_stock()
                elif choose == 2:
                    self.view_stock()
                elif choose == 3:
                    self.delete_stock()
                elif choose == 4:
                    self.manage_employee_acc()
                elif choose == 5:
                    self.manage_customer_acc()
                elif choose == 6:
                    self.sales_report()
                elif choose == 7:
                    self.history_log()
                elif choose == 8:
                    exit()
                else:
                    print("Choose a correct option")
            except ValueError as e:
                print(e)

    def get_existing_ids(self):
        existing_ids = set()  # Use a set for faster lookups
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) > 1 and parts[1].startswith("IDTB"):
                        existing_ids.add(parts[1].strip())
            return existing_ids  # Return the set of existing IDs
        except FileNotFoundError:
            return set()  # Return an empty set if the file is missing

    def suggest_available_id(self):
        existing_ids = self.get_existing_ids()  # Fetch the existing IDs
        base_id_prefix = "IDTB"
        available_ids = []

        for i in range(1, 100000):  # Loop through possible ID numbers
            candidate_id = f"{base_id_prefix}{i:04}"  # Generate IDs like IDTB0001, IDTB0002, etc.
            if candidate_id not in existing_ids:
                available_ids.append(candidate_id)  # Add unused IDs to the list
            if len(available_ids) == 5:  # Stop once 5 IDs are generated
                break
        return available_ids  # Return the list of 5 available IDs

    def is_valid_admin_id(self, admin_id):
        # Check if ID starts with 'IDTB' and is not already used
        return admin_id.startswith("IDTB") and admin_id not in self.get_existing_ids()


    def hash_password(self, password):
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def save_admin_to_file(self, admin_account_username, admin_account_id, admin_account_email, hashed_password):
        with open(self.admin_manage, "a") as file:
            file.write(f"{admin_account_username}, {admin_account_id}, {admin_account_email}, {hashed_password}\n")
        print("Admin account created successfully.")

    def create_admin_account(self):
        while True:
            print("Eg: Name: John_Doe")
            admin_account_name = input("Enter admin_account name: ")
            if (
                admin_account_name and "_" in admin_account_name 
                and not any(c.isspace() for c in admin_account_name) 
                and any(c.isupper() for c in admin_account_name) 
                and any (c.islower() for c in admin_account_name) 
                and any(c.islower() for c in admin_account_name) 
                and not any(c in '!@#$%^&*()+=-{}[]'';:,.' for c in admin_account_name)
            ):
                while True:
                    print("Eg: Email: john.doe@admin.iec.com")
                    admin_account_email = input("Enter admin_account email: ")
                    if (
                    "@admin.iec.com" in admin_account_email 
                    and not any(c.isupper() for c in admin_account_email) 
                    and not any(c.isspace() for c in admin_account_email)
                    ):
                        while True:
                            available_ids = self.suggest_available_id()
                            print("Available IDs: ", ", ".join(available_ids))

                            # Prompt the user to select or enter a custom admin ID
                            admin_account_id = input("Enter Admin ID: ").strip()

                            # Validate the entered Admin ID
                            while not self.is_valid_admin_id(admin_account_id):
                                print(f"Error: The Admin ID '{admin_account_id}' is either invalid or already in use.")
                                admin_account_id = input("Please enter a valid Admin ID: ").strip()
                            if self.is_valid_admin_id(admin_account_id):
                                if admin_account_id.startswith("IDTB") and admin_account_id not in self.get_existing_ids():
                                    if self.is_valid_admin_id(admin_account_id):
                                        while True:
                                            admin_account_passwords = input("Create password: ")
                                            if (
                                            len(admin_account_passwords) >= 8
                                            and any(c.isupper() for c in admin_account_passwords)
                                            and any(c.islower() for c in admin_account_passwords)
                                            and any(c.isdigit() for c in admin_account_passwords)
                                            and any(c in "!@#$%^&*()_+-=" for c in admin_account_passwords)
                                            ):
                                                self.log_action("Added new admin_account", "admin_account")
                                                hashed_password = self.hash_password(admin_account_passwords)

                                                # Save admin_account details to file
                                                self.save_admin_to_file(
                                                admin_account_name, 
                                                admin_account_id, 
                                                admin_account_email, 
                                                hashed_password
                                            )
                                                print("Admin account created successfully.")
                                                return
                                        else:
                                            print(
                                                "Password must contain at least 8 characters, including uppercase, "
                                                "lowercase, a number, and a special character."
                                                )
                            else:
                                print("admin_account ID must start with 'IDTB' or ID already exits")
                    else:
                        print("Invalid email format. Ensure it ends with '@admin_account.iec.com' and contains no spaces or uppercase letters.")
            else:
                print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")


    def admin_log(self):
        max_attempts = 3  # Maximum attempts per input
        attempts_remaining = max_attempts  # Remaining attempts for each step

        # Validate username
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            username = input("Enter username: ").strip()

            if self.validate_username(username):
                print("✅ Username validated!")
                break
            else:
                attempts_remaining -= 1
                print("❌ Invalid username.")

        if attempts_remaining == 0:
            print("❌ Too many failed attempts. Logging out.")
            sys.exit()

        # Reset attempts for next input
        attempts_remaining = max_attempts

        # Validate admin ID
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            admin_id_input = input("Enter admin ID: ").strip()

            if self.validate_admin_id(admin_id_input, username):
                print("✅ Admin ID validated!")
                break
            else:
                attempts_remaining -= 1
                print("❌ Invalid admin ID.")

        if attempts_remaining == 0:
            print("❌ Too many failed attempts. Logging out.")
            sys.exit()

        attempts_remaining = max_attempts

        # Validate email
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            email = input("Enter email: ").strip()

            if self.validate_email(email, username):
                print("✅ Email validated!")
                break
            else:
                attempts_remaining -= 1
                print("❌ Invalid email.")

        if attempts_remaining == 0:
            print("❌ Too many failed attempts. Logging out.")
            sys.exit()
        # Reset attempts for next input

        # Reset attempts for next input
        attempts_remaining = max_attempts

        # Validate password
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            password = self.take_password()

            if self.validate_password(username, password):
                print("✅ Login successful!")
                self.log_action("Logged in", username)
                self.admin_dashboard()
                return
            else:
                attempts_remaining -= 1
                print("❌ Invalid password.")

        print("❌ Too many failed attempts. Logging out.")
        sys.exit()

    def validate_username(self, username):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                if len(parts) == 4:
                    stored_username, _, _, _ = line.strip().split(', ')
                    if username == stored_username:
                        return True
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    def validate_admin_id(self, admin_id, username):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                if len(parts) == 4:
                    stored_username, stored_id, _, _ = line.strip().split(', ')
                    if username == stored_username and admin_id == stored_id:
                        return True
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    def validate_email(self, email, username):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                if len(parts) == 4:
                    stored_username, _, stored_email, _ = line.strip().split(', ')
                    if username == stored_username and email == stored_email:
                        return True
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    def take_password(self):
        password = ""
        print("Enter password: ", end="", flush=True)
        while True:
            char = msvcrt.getch()
            if char == b'\r':  # Enter key
                break
            elif char == b'\b':  # Backspace
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
            else:
                password += char.decode('utf-8')
                sys.stdout.write("*")
        print()  # Move to the next line after password input
        return password
    
    def validate_password(self, username, password):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    stored_username, _, _, stored_hashed_password = line.strip().split(', ')
                    if username == stored_username:
                        return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)
    

    ######  ADMIN PART ######



    ##### MANAGE EMPLOYEE PART ######

    def manage_employee_acc(self):
        os.system('cls')
        while True:
            print("\nManage Employee Accounts")
            print("1. Add new employee")
            print("2. View employee accounts")
            print("3. Delete employee account")
            print("4. Back to main menu")

            try:
                choice = int(input("Choose the task: "))
                if choice == 1:
                    self.add_employee()
                elif choice == 2:
                    self.view_employees()
                elif choice == 3:
                    self.delete_employee()
                elif choice == 4:
                    self.admin_dashboard()
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Enter a valid number.")

    def add_employee(self):
        while True:
            print("Eg: Name: John_Doe")
            admin_name = input("Enter admin name: ")
            if admin_name and "_" in admin_name and not any(c.isspace() for c in admin_name) and any(c.isupper() for c in admin_name) and any (c.islower() for c in admin_name) and any(c.islower() for c in admin_name):
                while True:
                    print("Eg: Email: john.doe@admin.iec.com")
                    admin_email = input("Enter admin email: ")
                    if "@admin.iec.com" in admin_email and not any(c.isupper() for c in admin_email) and not any(c.isspace() for c in admin_email):
                        while True:
                            admin_id = input("Create admin ID (Eg: IDTB1234): ")
                            if admin_id.startswith("IDTB"):
                                while True:
                                    admin_password = input("Create password: ")
                                    if (
                                        len(admin_password) >= 8
                                        and any(c.isupper() for c in admin_password)
                                        and any(c.islower() for c in admin_password)
                                        and any(c.isdigit() for c in admin_password)
                                        and any(c in "!@#$%^&*()_+-=" for c in admin_password)
                                    ):
                                        with open(self.manage_employ, 'a') as file:
                                            file.write(f"{admin_name}, {admin_email}, {admin_id}, {admin_password}\n")
                                        print("admin account created successfully.")
                                        self.log_action("Added new admin", "Admin")
                                    else:
                                        print("Password must contain at least 8 characters, including uppercase, lowercase, a number, and a special character.")
                            else:
                                print("admin ID must start with 'IDTB'")
                    else:
                        print("Invalid email format. Ensure it ends with '@admin.iec.com' and contains no spaces or uppercase letters.")
            else:
                print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")

    def view_employees(self):
        try:
            with open(self.manage_employ, 'r') as file:
                employees = file.readlines()
                if employees:
                    print("\nEmployee Accounts:")
                    for line in employees:
                        employee_name, employee_email, employee_id, _ = line.strip().split(', ')
                        print(f"Name: {employee_name}, Email: {employee_email}, ID: {employee_id}")
                else:
                    print("No employee found")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self):
        try:
            with open(self.manage_employ, 'r') as file:
                employees = file.readlines()
            if not employees:
                print("No employees to delete.")
                return
            print("\nEmployees:")
            for i, employee in enumerate(employees, 1):
                employee_name, employee_email, employee_id, _ = employee.strip().split(', ')
                print(f"{i}. {employee_name} (ID: {employee_id})")
            emp_to_delete = int(input("Enter the number of the employee to delete: "))
            if 1 <= emp_to_delete <= len(employees):
                del employees[emp_to_delete - 1]
                with open(self.manage_employ, 'w') as file:
                    file.writelines(employees)
                print("Employee deleted successfully.")
                self.log_action("Deleted employee", "Admin")
            else:
                print("Invalid selection.")
        except FileNotFoundError:
            print("No employee file found.")

    ##### MANAGE EMPLOYEE PART ######

    ##### LOG HISTORY ########

    def history_log(self):
        while True:
            print("\nSystem Log")
            print("1. View logs")
            print("2. Clear logs")
            print("3. Back to main menu")

            try:
                option = int(input("Choose an option: "))
                if option == 1:
                    try:
                        with open(self.system_log, 'r') as file:
                            logs = file.readlines()
                        if logs:
                            print("\nSystem Logs:")
                            for log in logs:
                                print(log.strip())
                        else:
                            print("No logs found.")
                    except FileNotFoundError:
                        print("System log file not found.")
                elif option == 2:
                    confirm = input("Are you sure you want to clear all logs? (yes/no): ").lower()
                    if confirm == 'yes':
                        with open(self.system_log, 'w') as file:
                            pass
                        print("Logs cleared.")
                        self.log_action("Cleared system logs", "Admin")
                    else:
                        print("Clear logs cancelled.")
                elif option == 3:
                    self.admin_dashboard()
                else:
                    print("Invalid option.")
            except ValueError:
                print("Enter a valid number.")

    def log_action(self, action, username="Admin"):
        try:
            with open(self.system_log, 'a') as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp} - {username}: {action}\n")
        except Exception as ex:
            print(f"Error logging action : {ex}")

    def sales_report(self):
        pass
    
    ##### LOG HISTORY ########

    #### MANAGE CUSTOMER PART ####

    def manage_customer_acc(self):
        print("\nManage Customer Account Menu: ")
        print("1. View Customer")
        print("2. Delete Customer")
        print("3. Return to Main Menu")

        while True:
            try:
                choose = int(input("Enter an option: "))
                if choose == 1:
                    self.view_customers()
                elif choose == 2:
                    self.delete_customer()
                elif choose == 3: 
                    print("Returning to the main menu...")
                    self.admin_dashboard()
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Please enter a valid number.")

    def view_customers(self):
        try:
            with open('', 'r') as file:  # Specify the correct file path for customer data
                users = [line.strip() for line in file]
            if not users:
                print("No users found.")
            else:
                print("\nCurrent User List: ")
                for index, user in enumerate(users, start=1):
                    user_name, user_email = user.split(', ')
                    print(f"{index}. Name: {user_name}, Email: {user_email}")
        except FileNotFoundError as e:
            print(e)

    def delete_customer(self):
        try:
            with open('', 'r') as file:  # Specify the correct file path for customer data
                users = [line.strip() for line in file]
            if not users:
                print("No customers found to delete.")
                return
            print("\nCurrent Customer List: ")
            for index, user in enumerate(users, start=1):
                user_name, user_email = user.split(', ')
                print(f"{index}. Name: {user_name}, Email: {user_email}")
            customer_to_delete = int(input("Enter the number of the customer to delete: "))
            if 1 <= customer_to_delete <= len(users):
                del users[customer_to_delete - 1]
                with open('', 'w') as file:  # Specify the correct file path for customer data
                    file.writelines([f"{user}\n" for user in users])
                print("Customer deleted successfully.")
                self.log_action("Deleted customer", "Admin")
            else:
                print("Invalid selection.")
        except FileNotFoundError:
            print("No customer file found.")
    
    #### MANAGE CUSTOMER PART ####

    #### CRUD FUNCTION #####

    def add_stock(self):
        pass

    def view_stock(self):
        pass

    def delete_stock(self):
        pass

    #### CRUD FUNCTION #####

    ##### EMPLOYEE PART ########

class EmployeeInterface(FirstInterface):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    employeefile = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\inf_employee.txt"
    recordstock = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\recordstock.txt"
    fileiphone_staff = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone.txt" 
    fileairpod_staff = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\airpod_user.txt"
    filemacbook_staff = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\macbook.txt"

    # view stock for users iphone
    fileiphone11_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone11_user.txt"
    fileiphone12_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone12_user.txt"
    fileiphone13_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone13_user.txt"
    fileiphone14_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone14_user.txt"
    fileiphone15_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone15_user.txt"

    # view stock for users mac
    mac_m1_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_m1_user.txt"
    mac_m2_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_m2_user.txt"
    mac_pro_14 = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_pro_14.txt"
    mac_pro_16 = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_pro_16.txt"

    # view stock for user airpod
    airpod_user =r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\airpod_user.txt"

    def __init__(self, employee_filename):
        self.display_employee_account()
        self.employee_filename = employee_filename
        self.employees = []
        self.load_employees()
    
    def display_employee_account(self):
        while True:
            try:
                os.system('cls')
                print("\nWelcome Employee")
                print("1. Log in as Employee")
                print("2. Back To Main Menu")

                choose = int(input("Enter ur function to do: "))
                if choose == 1:
                    self.employee_login()
                elif choose == 2:
                    return
                else:
                    print("Invalid option")
            except ValueError as v:
                print(v)

    def display_employee_task(self):
        while True:
            try:
                os.system('cls')
                print("Welcome our employee")
                print("1. Manage Stock (Add or Update): ")
                print("2. View Stock")
                print("3. Make Report")
                print("4. Exit")

                choose = int(input("Enter a task to do: "))
                if choose == 1:
                    self.add_stock()
                elif choose == 2:
                    self.view_stock()
                elif choose == 3:
                    self.make_report()
                elif choose == 4:
                    sys.exit(1)
                else:
                    print("Invalid option")
            except ValueError as ve:
                print(ve)

    def choose_option(self): 
        while True:
            print("\n**********EmployeeSystem*********")
            print("1. Create account employee.")
            print("2. Employee login.")
            print("3. Exit")
            option = input("Enter your choice: ")
            os.system('cls')
            if option == "1":
                self.create_employee_account()
            elif option == "2":
                self.employee_login()
            elif option ==  "3":
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
                        self.employees.append(employee_data)

        except FileNotFoundError:
            print(f"{self.epmployee_filename} not found.")

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

    def hash_password(self,password):
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
                            print("This user has already been existed. Please try again!\n")
                            break
                    else:
                        break

                while True:
                    email = input("Enter your email address (e.g:john.doe@employee.iec.com): ")
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
                        print("Password too short. Must be at least 8 Characters.\n")
                        continue
                    if not any(c.isupper()for c in password):
                        print("Password must contain at least one uppercase letter.\n")
                        continue
                    if not any(c.islower()for c in password):
                        print("password must contain at least one lowercase letter.\n")
                        continue
                    if not any(c.isdigit()for c in password):
                        print("Password must contain at least one digit.\n")
                        continue
                    if not any(c in '!@#$%^&*'for c in password):
                        print("Password must contain at least one special character.\n")
                        continue
                    confirm_password = self.masked_input("Confirm your Password: ")
                    if confirm_password != password:
                        print("Password do not match. Please try again.\n")
                        continue
                    break

                hashed_password = self.hash_password(password)
                employee_data = {"username": username, "email": email, "id": id, "password": hashed_password.hex()}
                self.employees.append(employee_data)
                file.write(f"username: {username}, email: {email}, ID: {id}, password: {hashed_password.hex()}\n")
                print("Create account employee successful!\n")
                    
        except Exception as e:
            print(f"Error while creating account: {e}. please try again!.")
        
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
                        self.display_employee_task()
                print(f"Invalid username, email or password. You have {attempts_left - 1} attempts left.")
            print("Too many failed attempts. Access denied.")
        except Exception as e:
            print(f"Error during login: {e}")


    def masked_input(self,prompt= ""):
        print(prompt, end="", flush=True)
        password = ""
        while True:
            char = msvcrt.getch()
            if char in {b'\r',b'\n'}:
                print()
                break
            elif char == b'\x80':
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end='', flush=True)
            else:
                password += char.decode()
                print('*', end='', flush=True)
        return password

    def check_employee_inf(self,username, email, ID, password):
        try:
            with open(self.employeefile, 'r') as file:
                for line in file:
                    stored_username, stored_email, stored_ID, stored_password = line.strip().split(',')
                    if (stored_username.strip().lower() == username.strip().lower() and
                        stored_email.strip().lower() == email.strip().lower() and
                        stored_ID.strip() == ID.strip() and
                        stored_password.strip() == password.strip()):
                        return True
                return False
        except FileNotFoundError:
            print("Employee information not found!")
            return False
        
    def employee_login(self):
        print("----------------------------------------------")
        print("||              EMPLOYEE_LOGIN              ||")
        print("----------------------------------------------")
        for attempt in range(3):  # Allow 3 attempts
            employee_username = input("Enter your username: ")
            employee_email = input("Enter your email: ")
            employee_id = input("Enter your ID: ")
            employee_password = input("Enter your password: ")  # Use input() instead of masked_input
            
            if self.check_employee_inf(employee_username, employee_email, employee_id, employee_password):
                print("\n<<<<<<<<<<<<<<<YOU ARE OUR EMPLOYEE>>>>>>>>>>>>>>>")
                self.logged_in_username = employee_username
                self.main_menu()
                return
            else:
                if attempt == 2:
                    print("\n############### LOGIN FAILED. NO MORE ATTEMPTS ALLOWED. ###############")
                    print("======/Access denied./======")
                    # self.logged_in_username = employee_username
                    self.main_menu()
                    return  # Exit the login function after the final failure
                else:
                    print("\n############### LOGIN FAILED. YOU HAVE {} MORE ATTEMPT{} ###############".format(2 - attempt, 'S' if 2 - attempt > 1 else ''))

    def main_menu(self):
        while True:
            print("*" * 50)
            print("Main Menu:")
            print("1. Change Stock\n2. Do Report\n3. View Stock\n4. Exit Program")
            print("*" * 50)

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.stock_menu()
            elif choice == "2":
                self.generate_report()
            elif choice == "3":
                self.view_stock()
            elif choice == "4":
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_stock(self): # menu view stock
        print("=" * 50)
        print("View Stock:")
        print("1.\tiPhone")
        print("2.\tMacbook")
        print("3.\tAirpod")
        print("4.\tExit to Main Menu")
        choice = input("Enter the model to add (1/2/3/4): ")
        if choice == "1":
            self.view_iphone()
        elif choice == "2":
            self.view_macbook()
        elif choice == "3":
            self.view_airpod()
        elif choice == "4":
            self.main_menu()
        else:
            print("Invalid choice. Please try again.")
            
    def view_iphone(self): #view iphone
        try:
            with open(self.fileiphone_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
                print(stock_data)
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
        
    def view_macbook(self): #view_mac
        try:
            with open(self.filemacbook_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
                print(stock_data)
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            
    def view_airpod(self): #view airpod
        try:
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
                print(stock_data)
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            
    def stock_menu(self):  # main menu
        while True:
            print("=" * 50)
            print("Stock Management:")
            print("1. Add Stock\n2. Delete Stock\n3. Exit to Main Menu")
            print("=" * 50)
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_stock()
            elif choice == "2":
                self.delete_stock()
            elif choice == "3":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_stock(self): # add stock
        # file_path = self.get_file_path()
        print("1.iPhone")
        print("2.Macbook")
        print("3.Airpod")
        choice = input("Enter the model to add (1/2/3): ")
        if choice == "1":
            self.add_iphone()
        elif choice == "2":
            self.add_macbook()
        elif choice == "3":
            self.add_airpod()
        else:
            print("Invalid choice. Please try again.")

    def delete_stock(self): #delete stock
        print("1.iPhone")
        print("2.Macbook")
        print("3.Airpods")
        
        choice = input("Enter the model to remove (1/2/3): ")
        if choice == "1":
            self.remove_iphone()
        elif choice == "2":
            self.remove_macbook()
        elif choice == "3":
            self.remove_airpod()
        else:
            print("Invalid choice. Please try again.")
            
    def add_iphone(self): # add iphone
            try:
                with open(self.fileiphone_staff, "r") as file:
                    stock_data = ast.literal_eval(file.read())
            except FileNotFoundError:
                print("Stock file not found. Creating a new one.")
                stock_data = {}
                
            model = input("Enter the model to add (11/12/13/14/15): ")
            model_key = f"iphone_{model}"
            if model_key not in stock_data:
                print (f"cannot add products.Model '{model}' not found.")
                return
            storage = input("Enter the storage size to add (64/128/256/512(GB)/1(TB)): ")
            if storage in ["64", "128", "256", "512"]:
                storage_key = f"{storage}GB"
            elif storage == "1":    
                storage_key = f"{storage}TB"
            else:
                print("Invalid storage size.Please enter 64,128,256,512(GB)or1(TB).")
                return
            if storage_key not in stock_data[model_key]:
                print (f"cannot add products.Storage '{storage}' not found for model '{model}'.")
                return

            try:
                quantity = int(input("Enter the quantity to add: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
            if model_key in stock_data:
                if storage_key in stock_data[model_key]:
                    if stock_data [model_key][storage_key] > 5:
                        print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key} ({storage_key}).")
                        return
                    else:
                        stock_data[model_key][storage_key] += quantity
                        
                else:
                    stock_data[model_key][storage_key] = quantity
            else:
                stock_data[model_key] = {storage_key: quantity}
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open (self.recordstock, 'a') as file:
                file.write(f"{timestamp} | {self.logged_in_username} | add |Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")
            
            try:
                with open(self.fileiphone_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully added {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")

    def remove_iphone(self): #remove iphone
            try:
                with open(self.fileiphone_staff, "r") as file:
                    stock_data = ast.literal_eval(file.read())
            except FileNotFoundError:
                print("Stock file not found. Creating a new one.")
                stock_data = {}
                
            model = input("Enter the model to remove (11/12/13/14/15): ")
            model_key = f"iphone_{model}"
            storage = input("Enter the storage size to remove (64/128/256/512(GB)/1(TB)): ")
            if storage == "64" or storage == "128" or storage == "256" or storage == "512":
                storage_key = f"{storage}GB"
            else:
                storage_key = f"{storage}TB"
            try:
                quantity = int(input("Enter the quantity to remove: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
            if model_key in stock_data:
                if storage_key in stock_data[model_key]:
                    if stock_data [model_key][storage_key] < quantity:
                        print(f"Cannot remove stock. Removing {quantity} would be less or equal the quantity of {model_key} ({storage_key}).")
                        return
                    else:
                        stock_data[model_key][storage_key] -= quantity
                else:
                    stock_data[model_key][storage_key] = quantity
            else:
                stock_data[model_key] = {storage_key: quantity}
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open (self.recordstock, 'a') as file:
            #   print(f"ADD | {timestamp} | {self.employee_username} | Model: {model_key} | Quantity: {quantity}\n")  
                file.write(f"{timestamp} | {self.logged_in_username} |remove | Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")

            try:
                with open(self.fileiphone_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully removing {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")

    def add_macbook(self): #add macbook
        try:
            # Load stock data from file
            with open(self.filemacbook_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            stock_data = {}

        # Predefined valid models
        valid_models = {
            "1": "MacBook_Air_M1",
            "2": "MacBook_Air_M2",
            "14": "MacBook_Pro_14inch",
            "16": "MacBook_Pro_16inch"
        }

        # User inputs
        model = input("Enter the model to add (1(AirM1)/2(AirM2)/14(Pro_14inch)/16(Pro_16inch)): ")

        # Check if the model is valid
        if model not in valid_models:
            print("Cannot add product. Model not found.")
            return

        model_key = valid_models[model]
        storage = input("Enter the storage size to add (256/512(GB)/1(TB)): ")

        # Validate storage and construct storage key
        if storage in ["256", "512"]:
            storage_key = f"{storage}GB"
        elif storage == "1":
            storage_key = "1TB"
        else:
            print("Invalid storage size. Please enter 256, 512 (GB) or 1 (TB).")
            return

        # Check if the storage type exists for the given model
        if storage_key not in stock_data.get(model_key, {}):
            print(f"Cannot add product. Storage '{storage}' not found for model '{model}'.")
            return

        try:
            quantity = int(input("Enter the quantity to add: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        # Check the existing stock level and limit
        if stock_data[model_key][storage_key] + quantity > 5:
            print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key} ({storage_key}).")
            return
        else:
            stock_data[model_key][storage_key] += quantity
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file: 
            file.write(f"{timestamp} | {self.logged_in_username} | add |Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")

        try:
            with open(self.filemacbook_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully added {quantity} of {model_key} ({storage_key}).")
        except IOError:
            print("Error writing to the stock file.")
            
    def remove_macbook(self): #remove mac
        try:
            with open(self.filemacbook_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found.")
            return

        model = input("Enter the model to remove (1(AirM1)/2(AirM2)/14(Pro_14inch)/16(Pro_16inch)): ")
        if model == "1" or model == "2":
            model_key = f"MacBook_Air_M{model}"
        else:
            model_key = f"MacBook_Pro_{model}inch"
        
        storage = input("Enter the storage size to remove (256/512(GB)/1(TB)): ")
        if storage == "256" or storage == "512":
            storage_key = f"{storage}GB"
        else:
            storage_key = f"{storage}TB"

        try:
            quantity = int(input("Enter the quantity to remove: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        if model_key in stock_data and storage_key in stock_data[model_key]:
            if stock_data[model_key][storage_key] < quantity:
                print(f"Cannot remove {quantity}. Only {stock_data[model_key][storage_key]} in stock for {model_key} ({storage_key}).")
                return
            else:
                stock_data[model_key][storage_key] -= quantity
                if stock_data[model_key][storage_key] == 0:
                    del stock_data[model_key][storage_key]
                if not stock_data[model_key]:
                    del stock_data[model_key]
        else:
            print(f"{model_key} ({storage_key}) not found in stock.")
            return
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file:  
            file.write(f"{timestamp} | {self.logged_in_username} | remove |Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")

        try:
            with open(self.filemacbook_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully removed {quantity} of {model_key} ({storage_key}).")
        except IOError:
            print("Error writing to the stock file.")

    def add_airpod(self): #add airpod
        try:
            # Load stock data from file
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            stock_data = {}

        # Predefined valid models
        valid_models = {
            "2ndGen": "Airpods_2nd_Gen",
            "Pro": "Airpods_Pro",
            "Max": "Airpods_Max"
        }

        # User input
        model = input("Enter the model to add (2ndGen/Pro/Max): ")

        # Check if the model is valid
        if model not in valid_models:
            print("Cannot add product. Model not found.")
            return

        model_key = valid_models[model]

        try:
            quantity = int(input("Enter the quantity to add: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        # Check the existing stock level and limit
        
        if stock_data[model_key] > 5:
            print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key}.")
            return
        else:
            stock_data[model_key] += quantity
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file:
            #   print(f"ADD | {timestamp} | {self.employee_username} | Model: {model_key} | Quantity: {quantity}\n")  
            file.write(f"{timestamp} | {self.logged_in_username} | add |Model: {model_key} | Quantity: {quantity}\n")

        try:
            with open(self.fileairpod_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully added {quantity} of {model_key}.")
        except IOError:
            print("Error writing to the stock file.")

    def remove_airpod(self): #remove airpod
        try:
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found.")
            return

        model = input("Enter the model to remove (2ndGen/Pro/Max): ")
        if model == "2ndGen":
            model_key = f"Airpods_2nd_Gen"
        elif model in ["Pro", "Max"]:
            model_key = f"Airpods_{model}"
        else:
            print("Invalid model. Please enter a valid model (2ndGen/Pro/Max).")
            return

        try:
            quantity = int(input("Enter the quantity to remove: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        if model_key in stock_data:
            if stock_data[model_key] < quantity:
                print(f"Cannot remove {quantity}. Only {stock_data[model_key]} in stock for {model_key}.")
                return
            else:
                stock_data[model_key] -= quantity
                if stock_data[model_key] == 0:
                    del stock_data[model_key]
        else:
            print(f"{model_key} not found in stock.")
            return
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file:
            #   print(f"ADD | {timestamp} | {self.employee_username} | Model: {model_key} | Quantity: {quantity}\n")  
            file.write(f"{timestamp} | {self.logged_in_username} | remove |Model: {model_key} | Quantity: {quantity}\n")

        try:
            with open(self.fileairpod_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully removed {quantity} of {model_key}.")
        except IOError:
            print("Error writing to the stock file.")


    ##### EMPLOYEE PART ########
    

interface = FirstInterface()
interface.display()