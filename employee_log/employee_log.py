import sys
import msvcrt
def take_password():
    password = ""
    print("Enter your password: ", end="", flush=True)
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':  # Enter key
            print()
            break
        elif char == '\b' or ord(char) == 127:  # Backspace key
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        else:
            password += char
            sys.stdout.write("*")
            sys.stdout.flush()

def check_employee_inf(username, email, ID, password):
    try:
        with open(r'C:\Users\User\OneDrive\ドキュメント\GitHub\Python_T1_Y2_Project\employee_log\inf_employee.txt', 'r') as file:
            for line in file:
                stored_username, stored_email, stored_ID, stored_password = line.strip().split(',')
                '''print(f"Comparing: {stored_username.strip()} == {username.strip()}?")'''
                if (stored_username.strip().lower() == username.strip().lower() and
                    stored_email.strip().lower() == email.strip().lower() and
                    stored_ID.strip() == ID.strip() and
                    stored_password.strip() == password.strip()):
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
        employee_password = take_password()
    
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

