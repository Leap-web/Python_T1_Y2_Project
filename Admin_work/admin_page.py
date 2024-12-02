# Dashboard show role of admin
def admin_dashboard():
    while True:
        print("\nAdmin Dashboard")
        print("1. Add or update stock")
        print("2. View stock")
        print("3. Check Report")
        print("4. Log out")
        print("5. Exit")

        choose = int(input("Choose ur task to do: "))
        if choose == 1:
            add_stock()
        elif choose == 2:
            view_stock()
        elif choose == 3:
            check_report()
        elif choose == 4:
            log_out()
        elif choose == 5:
            exit()


def add_stock():
    pass

def view_stock():
    pass

def check_report():
    pass

def log_out():
    pass

# show log in as admin
def admin_log():
    print("======================= Admin Login ==========================")
    admin_username = input("Enter ur username: ")
    admin_id = input(int("Enter ID: "))
    admin_email = input("Enter ur gmail: ")
    admin_password = input("Enter ur gmail: ")

    # Validate check for admin
    is_admin_username_valid = check_admin_name(admin_username)
    is_admin_id_valid = check_admin_id(admin_id)
    is_admin_email_valid = check_admin_email(admin_email)
    is_admin_passwords = check_admin_password(admin_password)

    if (is_admin_username_valid and is_admin_passwords and is_admin_id_valid and is_admin_email_valid):
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