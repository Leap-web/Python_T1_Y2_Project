def main_menu():
    while True:
        print("Choose ur role")
        print("1. Admin")
        print("2. Employee")
        print("3. User")
        print("4. Exit")
    try:
        choice = int(input("Enter ur specific role: "))
        if choice == 1:
            admin_menu()
        elif choice == 2:
            employee_menu()
        elif choice == 3:
            user_menu()
        elif choice == 4:
            print("Exiting the program.............!!!")
            break
        else:
            print("Invalid option here")
    except ValueError as f:
        print(f)


