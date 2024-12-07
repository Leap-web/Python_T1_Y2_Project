from datetime import datetime
import sys


# Dashboard show role of admin
def admin_dashboard():
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
                    break
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
    print("\nManage Employee accounts")
    print("1. Add new employee")
    print("2. View employee account")
    print("3. Delete employee account")
    print("4. Back to main menu")

    while True: 
        try:
            choose = int(input("Choose the task to do: "))
            if choose == 1:
                employee_add_name = input("Enter employee name: ")
                employee_add_email = input("Enter employee gmail address: ")
                employee_add_id = input("Create employee id number: ")
                employee_add_password = input("Create password for this employee: ")
                with open('manage_employee.txt', 'a') as file:
                    file.write(f"{employee_add_name}, {employee_add_email}, {employee_add_id}, {employee_add_password}\n")
                print("New Employee account created successfully")

            elif choose == 2:
                try:
                    with open('manage_employee.txt', 'r') as file:
                        print("Employee list in our company: ")
                        for line in file:
                            employee_add_name, employee_add_email, employee_add_id, employee_add_password = line.strip().split(', ')
                            print(f"Name: {employee_add_name}, Email: {employee_add_email}, ID: {employee_add_id}, Password: {employee_add_password}")
                except FileNotFoundError as no:
                    print(no)

            elif choose == 3:
                try:
                    with open('manage_employee.txt', 'r') as file:
                        employees = [line.strip() for line in file]
                    
                    if not employees:
                        print("No employee records to delete.")
                        continue

                    print("\nEmployee List:")
                    for emp in employees:
                        emp_id, emp_name, emp_email, emp_password = emp.split(', ')
                        print(f"ID: {emp_id}, Name: {emp_name}, Email: {emp_email}")
                    employee_id_to_delete = input("\nEnter the ID of the employee to delete: ").strip()
                    updated_employees = [emp for emp in employees if not emp.startswith(employee_id_to_delete + ",")]
                    if len(updated_employees) == len(employees):
                        print(f"Employee ID '{employee_id_to_delete}' not found.")
                    else:
                        with open('manage_employee.txt', 'w') as file:
                            for emp in updated_employees:
                                file.write(emp + '\n')
                        print(f"Employee ID '{employee_id_to_delete}' has been successfully deleted.")
                        print("\nUpdated Employee List:")
                        for emp in updated_employees:
                            emp_id, emp_name, emp_email, emp_password = emp.split(', ')
                            print(f"ID: {emp_id}, Name: {emp_name}, Email: {emp_email}")
                except FileNotFoundError:
                    print("Employee file not found. Please add employees first.")

            elif choose == 4:
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

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
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Please enter a valid number.")

def sales_report():
    pass

def log_action(action, username="Employee"):
    try:
        with open('', 'a') as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - {username}: {action}\n")
    except Exception as ex:
        print(f"Error logging action : {ex}")

def history_log():
    print("\nSystem Log Menu")
    print("1. View System Logs")
    print("2. Clear logs")
    print("3. Return to Main menu")

    while True:
        try:
            option = int(input("Choose an option to check the history_log: "))

            if option == 1:
                try:
                    with open ('system_log.txt', 'r') as log_file:
                        logs = log_file.readlines()
                    if logs:
                        print("\n System Logs: ")
                        for log in logs:
                            print(log.strip())
                    else:
                        print("No one log in yet")
                except FileNotFoundError as fe:
                    print(fe)

            elif option == 2:
                confirm = input("Are you sure you want to clear all history logs? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    with open('system_log.txt', 'w') as log_file:
                        pass
                    print("All log in history have been cleared.")
                else:
                    print("Clearing logs cancelled.")

            elif option == 3:
                print("Returning to the main menu...")
                break

            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as v:
            print(v)

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

# show log in as admin
def admin_log():
    print("======================= Admin Login ==========================")
    admin_username = input("Enter ur username: ")
    admin_id = input("Enter ID: ")
    admin_email = input("Enter ur gmail: ")
    admin_password = take_password()

    # Validate check for admin
    is_admin_username_valid = check_admin_name(admin_username)
    is_admin_id_valid = check_admin_id(admin_id)
    is_admin_email_valid = check_admin_email(admin_email)
    is_admin_passwords = check_admin_password(admin_password)

    if ( is_admin_username_valid and is_admin_passwords and is_admin_id_valid and is_admin_email_valid ):
        print(">>>>>>>>>>>>>>>>>>>>>> Admin Login Successful <<<<<<<<<<<<<<<<<<<<<<<<")
        admin_dashboard()
    else:
        print("Bro stop try to hack the admin account.")

def check_admin_name(username):
    try:
        with open('admin_name.txt', 'r') as fi:
            usernames = [line.strip() for line in fi]
            return username in usernames
    except FileNotFoundError:
        return False
    
def check_admin_id(id):
    try:
        with open('admin_id.txt', 'r') as fi:
            ids = [line.strip() for line in fi]
            return id in ids
    except FileNotFoundError:
        return False
    
def check_admin_email(email):
    try:
        with open('admin_email.txt', 'r') as fi:
            emails = [line.strip() for line in fi]
            return email in emails
    except FileNotFoundError:
        return False

def check_admin_password(password):
    try:
        with open('admin_pw.txt', 'r') as fi:
            passwords = [line.strip() for line in fi]
            return password in passwords
    except FileNotFoundError:
        return False
    
def main():
    admin_log()

if __name__ == '__main__':
    main()