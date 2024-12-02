def main_menu():
    while True:
        print("Choose ur role")
        print("1. Admin")
        print("2. Employee")
        print("3. User")
        print("4. Exit")

        choice = int(input("Enter ur specific role: "))
        if choice == 1:
            admin_menu()
        elif choice == 2:
            employee_menu()
        elif choice == 3:
            user_menu()
        elif choice == 4:
            print("Exiting the program.............!!!")
            exit()
        else:
            print("Invalid option here")


def admin_menu():
    pass

def employee_menu():
    pass

def user_menu():
    pass