import getpass                                  
def check_employee_name(username):
    try:
        with open('employee_username.txt', 'r') as file:
            usernames = [line.strip().lower() for line in file]
            return username.strip().lower() in usernames
    except FileNotFoundError:
        return False 
    
def  check_employee_email(email):
    try:
        with open('employee_email.txt', 'r') as file:
            emails = [line.strip().lower() for line in file]
            return email.strip().lower() in emails
    except FileNotFoundError:
        return False
    
def  check_employee_ID(employee_id):
    try:
        with open('employee_id.txt', 'r') as file:
            IDs = [line.strip() for line in file]
            return employee_id.strip() in IDs
    except FileNotFoundError:
        return False
    
def  check_employee_password(password):
    try:
        with open('employee_password.txt', 'r') as file:
            passwords = [line.strip() for line in file]
            return password.strip() in passwords
    except FileNotFoundError:
        return False

def employee_login():
    print("===============EMPLOYEE_LOGIN===============")
    employee_username = input("Enter your username: ")
    employee_email = input("Enter your email: ")
    employee_id = input("Enter your ID: ")
    employee_password = getpass.getpass("Enter your password: ")

    if not (check_employee_name(employee_username) and check_employee_email(employee_email) and check_employee_ID(employee_id) and check_employee_password(employee_password)):
        print("###############YOU ARE NOT OUR EMPLOYEE YOU ARE HECKER###############")
        return
    print("<<<<<<<<<<<<<<<YOU ARE OUR EMPLOYEE>>>>>>>>>>>>>>>")
employee_login()
