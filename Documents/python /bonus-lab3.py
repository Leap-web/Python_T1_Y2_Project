import os
def Register(user_list):
    username = input("Please input the username: ")
    while True:
        symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        password = input("Please input the password: ")
        
        has_islower = False
        has_digit = False
        has_isupper = False
        has_symbols = False
        
        if len(password) >= 8:
            for c in password:
                if c.islower():
                    has_islower = True
                if c.isupper():
                    has_isupper = True
                if c.isdigit():
                    has_digit = True
                if c in symbols:
                    has_symbols = True
            
            # Check if all password conditions are met
            if has_symbols and has_isupper and has_digit and has_islower:
                new_user = {
                    'Username': username,
                    'Password': password,
                }
                user_list.append(new_user)
                print(f"{username} is successfully registered!")
                break
       
        print("Please input a strong password!(Contain small and big letter,numbers and symbols)")
def Login(user_list):
    # max_attempts = 3
    # old_user = input("Please input your username: ")
    # old_pass = input("Please input your password: ")
        
    #     # Check if username and password match any user in the list
    # for users in user_list:
    #     if users['Username'] == old_user and users['Password'] == old_pass:
    #         print(f"Welcome back, {old_user}")
    #         break
        
    #     # If no match found, show error and remaining attempts
    # else:
    #     for attempt in range(1, max_attempts + 1):
    #         print("Your username or password is incorrect!")
    #         attempt_left = max_attempts - attempt
    #         if attempt_left > 0:
    #             print(f"Invalid credentials. You have {attempt_left} attempts left.")
    #             old_user = input("Please input your username: ")
    #             old_pass = input("Please input your password: ")
    #             for users in user_list:
    #                 if users['Username'] == old_user and users['Password'] == old_pass:
    #                     print(f"Welcome back, {old_user}")
    #                     break
    #         else:
    #             print("Too many failed attempts. Access blocked.")
    attempts = 0
    max_attempts = 3
    is_running = True

    while is_running:
        old_user = input("Please input your username: ")
        old_pass = input("Please input your password: ")
        
        for user in user_list:
            if user['Username'] == old_user and user['Password'] == old_pass:
                print(f"Welcome back, {old_user}")
                is_running = False
                break
        
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Invalid credentials. You have {max_attempts - attempts} attempts left.")
            else:
                print("Too many failed attempts. Access blocked.")
                is_running = False

def Forget_Password(user_list):
    forget_user = input("Enter your username to retrieve your password:")
    for user in user_list:
        if user['Username'] == forget_user:
            print(f"Your password is:{user['Password']}")
            break
        else:
            print(f"{forget_user} not found!")
user_list = []
user_input = True
while user_input:
    print("Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Forget Password")
    print("4. Exit")
    option = int(input("Choose an option (1-4): "))
    if option == 1:
        os.system('clear')
        Register(user_list)  
    elif option == 2:
        os.system('clear')
        Login(user_list)
    elif option == 3:
        os.system('clear')
        Forget_Password(user_list)
    elif option == 4:
        print("Exiting the program. Goodbye!")
        user_input = False
    else:
        print("Invalid option!")
