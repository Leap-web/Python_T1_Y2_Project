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
    username = input("Enter ur username: ")
    id_n = int("Enter ID: ")
    email = input("Enter ur gmail: ")
    passwords = input("Enter ur gmail: ")