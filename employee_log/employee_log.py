import getpass

def check_employee_inf(username, email, ID, password):
    try:
        with open('inf_employee.txt', 'r') as file:
            for line in file:
                stored_username, stored_email, stored_ID, stored_password = line.strip().split(',')
                if (stored_username.strip().lower() == username.strip().lower() and
                    stored_email.strip().lower() == email.strip().lower() and
                    stored_ID.strip() == ID.strip() and
                    stored_password.strip() == password.strip()):
                    return True

                return False
    except FileNotFoundError:
        print("Employee informatioon not foun!")
        return False
def employee_login():
    print("===============EMPLOYEE_LOGIN===============")
    employee_username = input("Enter your username: ")
    employee_email = input("Enter your email: ")
    employee_id = input("Enter your ID: ")
    employee_password = getpass.getpass("Enter your password: ")
    
    if not check_employee_inf(employee_username,employee_email,employee_id,employee_password):
        print("###############YOU ARE NOT OUR EMPLOYEE YOU ARE HACKER###############")
        return
    print("<<<<<<<<<<<<<<<YOU ARE OUR EMPLOYEE>>>>>>>>>>>>>>>")
employee_login()

