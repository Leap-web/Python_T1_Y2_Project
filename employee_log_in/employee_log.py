
def check_employee_name(username):
    try:
        with open('employee_username.txt', 'r') as file:
            usernames = [line.strip() for line in file]
            return username in usernames
    except FileNotFoundError:
        return False 
    
def  check_employee_email(email):
    try:
        with open('employee_email.txt', 'r') as file:
            emails = [line.strip() for line in file]
            return email in  emails
    except FileNotFoundError:
            return False
    
def  check_employee_ID(id):
    try:
        with open('employee_email.txt', 'r') as file:
            ID = [line.strip() for line in file]
            return id in  ID
    except FileNotFoundError:
            return False
    
def  check_employee_password(password):
    try:
        with open('employee_email.txt', 'r') as file:
            passwords = [line.strip() for line in file]
            return password in  passwords
    except FileNotFoundError:
            return False

def employee_login():
    print("===============EMPLOYEE_LOGIN===============")
    employee_username = input("Enter your username: ")
    employee_email = input("Enter your email: ")
    employee_id = input("Enter your ID: ")
    employee_password = input("Enter your password: ")

    is_employee_username = check_employee_name(employee_username)
    is_employee_email = check_employee_email(employee_email)
    is_employee_id = check_employee_ID(employee_id)
    is_employee_password = check_employee_password(employee_password)

    if (is_employee_username and is_employee_email and is_employee_id and is_employee_password):
         print("<<<<<<<<<<<<<<<YOU ARE OUR EMPLOYEE>>>>>>>>>>>>>>>")
    else:
         print("###############YOU ARE NOT OUR EMPLOYEE YOUR ARE HACKER###############")
employee_login()
