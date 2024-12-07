import os
class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

class UserManager:
    def __init__(self):
        self.user_list = [
            {"username": "alice", "email": "alice@gmail.com", "status": "active"},
            {"username": "charlie", "email": "charlie@gmaile.com", "status": "suspended"},
            {"username": "dave", "email": "dave@gmail.com", "status": "active"}
        ]
    def add_users(self):
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
                    self.user_list.append(new_user)
                    print(f"{username} is succesfully!")
                    return
            else:
                print("Please enter the correct format of email!")
                
    def remove_users(self):
        username = input("Enter the username that you want to delete:")
        for user in self.user_list:
            if user['username'] == username:
                self.user_list.remove(user)
                print("Remove user is succesfully!")
                break # dak break derm3 kom oy vea print tv kleng else
            else:
                print("User not found") # dak break derm3 oy vea print tae mdg ban hz
                break
    
    def update_users(self):
        username = input("Enter the username that you want to update:")
        for user in self.user_list:
            if user['username'] == username:
                self.user_list.remove(user)
                new_username = input("Enter your username:")
                email = input("Enter your email:")
                status = input("Enter status (active/inactive):")
                update_user = {
                    'username' : new_username,
                    'email' : email,
                    'status' : status,
                }
                self.user_list.append(update_user)
                print("Update user is succesfully!")
                break
            else:
                print("User not found!")
                break
            
    def display_users(self):
        print("Current user accounts:")
        print("Username\tEmail\t\t\tStatus")
        print("------------------------------------------------------------")
        for user in self.user_list:
            print(f"{user['username']}\t\t{user['email']}\t{user['status']}")
        total_active_users = sum(1 for user in self.user_list if user['status'] == 'active')
        print(f"\nTotal active users: {total_active_users}")
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
                self.add_users()
            elif choice == 2:
                os.system('clear')
                self.remove_users()
            elif choice == 3:
                os.system('clear')
                self.update_users()
            elif choice == 4:
                os.system('clear')
                self.display_users()
            elif choice == 5:
                print("Exit the program!")
                user_input= False
            else:
                print("That is not a valid choice")
if __name__ == "__main__":
    usermanager = UserManager()
    usermanager.display_users()



# import os
# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email

# class UserManager:
#     def __init__(self):
#         self.user_list = [
#             {"username": "alice", "email": "alice@gmail.com", "status": "active"},
#             {"username": "charlie", "email": "charlie@gmaile.com", "status": "suspended"},
#             {"username": "dave", "email": "dave@gmail.com", "status": "active"}
#         ]
#     def add_user(self):
#         while True:
#             username = input("Enter your username:")
#             email = input("Enter your email:")
#             if "@" in email and email.endswith("@gmail.com"):
#                 status = input("Enter status (active/suspended):").lower()
#                 if status != 'active ' and status !='suspended':
#                     print("Please input only active and suspended!")
#                 else:
#                     new_user = {
#                         'username' : username,
#                         'email' : email,
#                         'status' : status,
#                     }
#                     self.user_list.append(new_user)
#                     print(f"{username} is succesfully!")
#                     return
#             else:
#                 print("Please enter the correct format of email!")
                
#     def remove_users(self):
#         username = input("Enter the username that you want to delete:")
#         for user in self.user_list:
#             if user['username'] == username:
#                 self.user_list.remove(user)
#                 print("Remove user is succesfully!")
#                 break # dak break derm3 kom oy vea print tv kleng else
#             else:
#                 print("User not found") # dak break derm3 oy vea print tae mdg ban hz
#                 break
    
#     def update_users(self):
#         username = input("Enter the username that you want to update:")
#         for user in self.user_list:
#             if user['username'] == username:
#                 self.user_list.remove(user)
#                 new_username = input("Enter your username:")
#                 email = input("Enter your email:")
#                 status = input("Enter status (active/inactive):")
#                 update_user = {
#                     'username' : new_username,
#                     'email' : email,
#                     'status' : status,
#                 }
#                 self.user_list.append(update_user)
#                 print("Update user is succesfully!")
#                 break
#             else:
#                 print("User not found!")
#                 break
            
#     def display_users(self):
#         print("Current user accounts:")
#         print("Username\tEmail\t\t\tStatus")
#         print("------------------------------------------------------------")
#         for user in self.user_list:
#             print(f"{user['username']}\t\t{user['email']}\t{user['status']}")
#         total_active_users = sum(1 for user in self.user_list if user['status'] == 'active')
#         print(f"\nTotal active users: {total_active_users}")
#         user_input = True
#         while user_input:
#             print("User Accounts")
#             print("1.Add_users account:")
#             print("2.Remove_users account:")
#             print("3.Update_users account:")
#             print("4.Display all_users account")
#             print("5.Exit")
#             choice = int(input("Enter your choice(1-5):"))
#             if choice == 1:
#                 os.system('clear')
#                 self.add_user()
#             elif choice == 2:
#                 os.system('clear')
#                 self.remove_users()
#             elif choice == 3:
#                 os.system('clear')
#                 self.update_users()
#             elif choice == 4:
#                 os.system('clear')
#                 self.display_users()
#             elif choice == 5:
#                 print("Exit the program!")
#                 user_input= False
#             else:
#                 print("That is not a valid choice")
# if __name__ == "__main__":
#     usermanager = UserManager()
#     usermanager.display_users()