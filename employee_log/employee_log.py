import msvcrt

def masked_input(prompt= ""):
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
        print(f"\nATTEMPT {attempt +1} of 2")
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

