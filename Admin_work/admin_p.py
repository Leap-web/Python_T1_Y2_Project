from datetime import datetime
import sys
import msvcrt
import os
import bcrypt
from getpass import getpass
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
                employee_system = EmployeeInterface()
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
    admin_manage = r'C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\admin_manage.txt'
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

    def hash_password(self, password):
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def save_admin_to_file(self, admin_account_username, admin_account_id, admin_account_email, hashed_password):
        with open(self.admin_manage, "a") as file:
            file.write(f"ADMIN_NAME: {admin_account_username}, ADMIN_ID: {admin_account_id}, ADMIN_GMAIL: {admin_account_email}, ADMIN_PW: {hashed_password}\n")
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
                    if "@admin.iec.com" in admin_account_email and not any(c.isupper() for c in admin_account_email) and not any(c.isspace() for c in admin_account_email):
                        while True:
                            admin_account_id = input("Create admin_account ID (Eg: IDTB1234): ")
                            if admin_account_id.startswith("IDTB"):
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
                                        self.save_admin_to_file(admin_account_name, admin_account_id, admin_account_email, hashed_password)
                                        return
                                    else:
                                        print("Password must contain at least 8 characters, including uppercase, lowercase, a number, and a special character.")
                            else:
                                print("admin_account ID must start with 'IDTB'")
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

    def __init__(self):
        self.display_employee_account()

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
                    self.add_update_stock()
                elif choose == 2:
                    self.view_stock()
                elif choose == 3:
                    self.make_report()
                elif choose == 4:
                    sys.exit()
                else:
                    print("Invalid option")
            except ValueError as ve:
                print(ve)

    ##### EMPLOYEE PART ########
    

interface = FirstInterface()
interface.display()