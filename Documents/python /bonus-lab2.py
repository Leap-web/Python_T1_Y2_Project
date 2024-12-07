# # def users(info):
# #     # Sample data

# #     # Printing the header
# #     print("Current user accounts:")
# #     print("Username\tEmail\t\t\tStatus")
# #     print("------------------------------------------------------------")

# #     # Printing each user account
# #     for user in user_accounts:
# #         print(f"{user['username']}\t\t{user['email']}\t{user['status']}")

# #     # Count total active users
# #     total_active_users = sum(1 for user in user_accounts if user['status'] == 'active')
# # user_accounts = [
# #     {"username": "alice", "email": "alice@example.com", "status": "active"},
# #     {"username": "charlie", "email": "charlie@example.com", "status": "suspended"},
# #     {"username": "dave", "email": "dave@example.com", "status": "active"}
# # ]
# #     # Printing the total active users
# # print(f"\nTotal active users: {}")
import os # for system cleear
def add_users(user_accounts):
    # username = input("Enter your username:")
    # email = input("Enter your email:")
    # status = input("Enter status (active/inactive):")
    # new_user = {
    #     'username' : username,
    #     'email' : email,
    #     'status' : status,
    # }
    # user_accounts.append(new_user)
    # print("Add new user is succesfully!")
    while True:
        username = input("Enter your username:")
        email = input("Enter your email:")
        if "@" in email and email.endswith("@gmail.com"):
            status = input("Enter status (active/suspended):").lower()
            if status not in ("active", "suspended"):
                print("Please input only active and suspended!")
            else:
                new_user = {
                    'username' : username,
                    'email' : email,
                    'status' : status,
                }
                user_accounts.append(new_user)
                print(f"{username} is succesfully!")
                return
        else:
            print("Please enter the correct format of email!")
def remove_users(user_accounts):
    username = input("Enter the username that you want to delete:")
    for user in user_accounts:
        if user['username'] == username:
            user_accounts.remove(user)
            print("Remove user is succesfully!")
            break # dak break derm3 kom oy vea print tv kleng else
        else:
            print("User not found") # dak break derm3 oy vea print tae mdg ban hz
            break
def update_users(user_accounts):
    username = input("Enter the username that you want to update:")
    for user in user_accounts:
        if user['username'] == username:
            user_accounts.remove(user)
            new_username = input("Enter your username:")
            email = input("Enter your email:")
            status = input("Enter status (active/inactive):")
            update_user = {
                'username' : new_username,
                'email' : email,
                'status' : status,
            }
            user_accounts.append(update_user)
            print("Update user is succesfully!")
            break
        else:
            print("User not found!")
            break
def display_users(user_accounts):
    print("Current user accounts:")
    print("Username\tEmail\t\t\tStatus")
    print("------------------------------------------------------------")
    for user in user_accounts:
        print(f"{user['username']}\t\t{user['email']}\t{user['status']}")
    total_active_users = sum(1 for user in user_accounts if user['status'] == 'active')
    print(f"\nTotal active users: {total_active_users}")
user_accounts = [
            {"username": "alice", "email": "alice@gmail.com", "status": "active"},
            {"username": "charlie", "email": "charlie@gmaile.com", "status": "suspended"},
            {"username": "dave", "email": "dave@gmail.com", "status": "active"}
        ]
user_input = True
while user_input:
    print("User Accounts")
    print("1.Add_users account:")
    print("2.Remove_users account:")
    print("3.Update_users account:")
    print("4.Display all_users account")
    print("5.Exit")
    choice = int(input("Enter your choice(1-5):"))
    if choice == 1:
        os.system('clear')
        add_users(user_accounts)
    elif choice == 2:
        os.system('clear')
        remove_users(user_accounts)
    elif choice == 3:
        os.system('clear')
        update_users(user_accounts)
    elif choice == 4:
        os.system('clear')
        display_users(user_accounts)
    elif choice == 5:
        print("Exit the program!")
        user_input= False
    else:
        print("That is not a valid choice")