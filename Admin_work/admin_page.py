from datetime import datetime
import sys
import msvcrt
import os

admin_name = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/admin_name.txt'
admin_id = r'C:\/Users\/USER\Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/admin_ID.txt'
admin_email = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/admin_email.txt'
admin_pw = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/admin_pw.txt'
manage_employ = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/manage_employee.txt'
system_log = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/system_log.txt'

# Dashboard show role of admin
def admin_dashboard():
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
                choose = int(input("Choose ur task to do: "))
                if choose == 1:
                    add_stock()
                elif choose == 2:
                    view_stock()
                elif choose == 3:
                    delete_stock()
                elif choose == 4:
                    manage_employee_acc()
                elif choose == 5:
                    manage_customer_acc()
                elif choose == 6:
                    sales_report()
                elif choose == 7:
                    history_log()
                elif choose == 8:
                    exit()
                else:
                    print("Choose a correct option")
            except ValueError as e:
                print(e)

# wait team
def add_stock():
    pass

def view_stock():
    pass
# wait team 

def delete_stock():
    pass

def manage_employee_acc():
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
                print("Eg: Name: John_Doe")
                employee_name = input("Enter employee name: ")
                if employee_name and "_" in employee_name and not any(c.isspace() for c in employee_name) and any(c.isupper() for c in employee_name) and any(c.islower() for c in employee_name):
                    print("Eg: Email: john.doe@employee.iec.com")
                    employee_email = input("Enter employee email: ")
                    if "@employee.iec.com" in employee_email and not any(c.isupper() for c in employee_email) and not any(c.isspace() for c in employee_email):
                        employee_id = input("Create employee ID (Eg: IDTB1234): ")
                        if employee_id.startswith("IDTB"):
                            employee_password = input("Create password (min 8 chars, uppercase, lowercase, number, special char): ")
                            if (
                                len(employee_password) >= 8
                                and any(c.isupper() for c in employee_password)
                                and any(c.islower() for c in employee_password)
                                and any(c.isdigit() for c in employee_password)
                                and any(c in "!@#$%^&*()_+-=" for c in employee_password)
                            ):
                                with open(manage_employ, 'a') as file:
                                    file.write(f"{employee_name}, {employee_email}, {employee_id}, {employee_password}\n")
                                print("Employee account created successfully.")
                                log_action("Added new employee", "Admin")
                            else:
                                print("Password must contain at least 8 characters, including uppercase, lowercase, a number, and a special character.")
                        else:
                            print("Employee ID must start with 'IDTB'")
                    else:
                        print("Invalid email format. Ensure it ends with '@employee.iec.com' and contains no spaces or uppercase letters.")
                else:
                    print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")
            elif choice == 2:
                try:
                    with open(manage_employ, 'r') as file:
                        employees = file.readlines()
                        if employees:
                            print("\nEmployee Accounts:")
                            for line in employees:
                                employee_name, employee_email, employee_id, employee_password = line.strip().split(', ')
                                print(f"Name: {employee_name}, Email: {employee_email}, ID: {employee_id}")
                        else:
                            print("No employee found")
                except FileNotFoundError:
                    print("No employee records found.")
            elif choice == 3:
                try:
                    with open(manage_employ, 'r') as file:
                        employees = file.readlines()
                    if not employees:
                        print("No employees to delete .")
                        continue
                    print("\nEmployees:")
                    for i, employee in enumerate(employees, 1):
                        employee_name, employee_email, employee_id, _ = employee.strip().split(', ')
                        print(f"{i}. {employee_name} (ID: {employee_id})")
                    emp_to_delete = int(input("Enter the number of the employee to delete: "))
                    if 1 <= emp_to_delete <= len(employees):
                        del employees[emp_to_delete - 1]
                        with open(manage_employ, 'w') as file:
                            file.writelines(employees)
                        print("Employee deleted successfully.")
                        log_action("Deleted employee", "Admin")
                    else:
                        print("Invalid selection.")
                except FileNotFoundError:
                    print("No employee file found.")
            elif choice == 4:
                admin_dashboard()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")

def manage_customer_acc():
    print("\nManage Customer Account Menu: ")
    print("1. View Customer")
    print("2. Delete Customer")
    print("3. Return to Main Menu")

    while True:
        try:
            choose = int(input("Enter an option: "))
            if choose == 1:
                try:
                    with open('', 'r') as file:
                        users = [line.strip() for line in file]
                    if not users:
                        print("No users found to delete.")
                    else:
                        print("\nCurrent User List: ")
                        for index, user in enumerate(users, start=1):
                            user_name, user_email = user.split(', ')
                            print(f"{index}. Name: {user_name}, Email: {user_email}")
                except FileNotFoundError as e:
                    print(e)

            elif choose == 2:
                try:
                    with open('', 'r') as file:
                        users = [line.strip() for line in file]
                    if not users:
                        print("No customers found to delete.")
                        continue
                    print("\nCurrent Customer List: ")
                    for index, user in enumerate(users, start=1):
                        user_name, user_email= user.split(', ')
                        print(f"{index}. Name: {user_name}, Email: {user_email}")
                    while True:
                        try:
                            user_index = int(input("\nEnter the number of the user to delete: "))
                            if 1 <= user_index <= len(users):
                                break
                            else:
                                print("Invalid number. Please choose a valid customer number.")
                        except ValueError:
                            print("Please enter a valid number.")

                    deleted_user = users.pop(user_index - 1)
                    with open('', 'w') as file:
                        for user in users:
                            file.write(user + '\n')
                    user_name, user_email, _ = deleted_user.split(', ')
                    print(f"Customer '{user_name}' with email '{user_email}' has been successfully deleted.")
                    print("\nUpdated Customer List: ")

                    for index, user in enumerate(users, start=1):
                        user_name, user_email = user.split(', ')
                        print(f"{index}. Name: {user_name}, Email: {user_email}")
                except FileNotFoundError:
                    print("User file not found. Please add users first.")
            
            elif choose == 3: 
                print("Returning to the main menu...")
                admin_dashboard()
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Please enter a valid number.")

def sales_report():
    pass

def log_action(action, username="Admin"):
    try:
        with open(system_log, 'a') as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - {username}: {action}\n")
    except Exception as ex:
        print(f"Error logging action : {ex}")

def history_log():
    while True:
        print("\nSystem Log")
        print("1. View logs")
        print("2. Clear logs")
        print("3. Back to main menu")

        try:
            option = int(input("Choose an option: "))
            if option == 1:
                try:
                    with open(system_log, 'r') as file:
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
                    with open(system_log, 'w') as file:
                        pass
                    print("Logs cleared.")
                    log_action("Cleared system logs", "Admin")
                else:
                    print("Clear logs cancelled.")
            elif option == 3:
                admin_dashboard()
            else:
                print("Invalid option.")
        except ValueError:
            print("Enter a valid number.")

# Function to hash a password using SHA-256
try:
    import msvcrt
    is_windows = True
except ImportError:
    is_windows = False

def take_password():
    password = ""
    print("Enter password: ", end="", flush=True)
    while True:
        ch = msvcrt.getch().decode('utf-8')
        if ch == '\r' or ch == '\n':  # Enter key
            print()
            break
        elif ch == '\b' or ord(ch) == 127:  # Backspace key
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            password += ch
            sys.stdout.write("*")
            sys.stdout.flush()
    return password

# show log in as admin
def admin_log():
    os.system('cls')
    print("======= Admin Login =======")
    username = input("Enter username: ").strip()
    admin_id_input = input("Enter admin ID: ").strip()
    email = input("Enter email: ").strip()
    password = take_password()

    if validate_login(username, admin_id_input, email, password):
        print("\n✅ Login successful!")
        log_action("Logged in", username)
        admin_dashboard()
    else:
        print("\n❌ Login failed.")

# Validate login credentials
def validate_login(username, admin_id_input, email, password):
    try:
        with open(admin_name, 'r') as name_file, \
             open(admin_id, 'r') as id_file, \
             open(admin_email, 'r') as email_file, \
             open(admin_pw, 'r') as pw_file:
            
            admin_records = zip(
                (line.strip() for line in name_file),
                (line.strip() for line in id_file),
                (line.strip() for line in email_file),
                (line.strip() for line in pw_file)
            )
            for record in admin_records:
                if (username, admin_id_input, email, password) == record:
                    return True
        return False
    except FileNotFoundError:
        print("Error: Data files are missing.")
        sys.exit(1)

def check_admin_name(username):
    try:
        with open(admin_name, 'r') as fi:
            usernames = [line.strip() for line in fi]
            return username in usernames
    except FileNotFoundError:
        return False
    
def check_admin_id(id):
    try:
        with open(admin_id, 'r') as fi:
            ids = [line.strip() for line in fi]
            return id in ids
    except FileNotFoundError:
        return False
    
def check_admin_email(email):
    try:
        with open(admin_email, 'r') as fi:
            emails = [line.strip() for line in fi]
            return email in emails
    except FileNotFoundError:
        return False

def check_admin_password(password):
    try:
        with open(admin_pw, 'r') as fi:
            passwords = [line.strip() for line in fi]
            return password in passwords
    except FileNotFoundError:
        return False
    
def main():
    admin_log()

if __name__ == '__main__':
    main()