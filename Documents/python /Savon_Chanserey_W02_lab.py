#1
def rev_lst(lst):
    new_lst=lst[::-1]
    return new_lst
list=[]
n = int(input("Enter the number in list:")) 
for i in range(0,n):
    element = int(input()) #user input the element
    list.append(element) # add element that user input to the list
print(list)
print(rev_lst(list))

#2
list =  [i*i for i in range(2,21) if i%2 == 0 ]
print(list)

#3
def merge_list(lst1,lst2):
    list=[]
    return lst1 + [i for i in lst2 if i not in lst1]
print(merge_list([1,2,3],[2,3,4,5]))

#4
def max(tups):
    max = tups[0]
    for i in range(0,len(tups)):
        if tups[i] > max:
            max = tups[i]
    return max
def mini(tups):
    mini = tups[0]
    for i in range(0,len(tups)):
        if tups[i] < mini:
            mini = tups[i]
    return mini
tup = (10,5,8,12,3)
print(max(tup))
print(mini(tup))

#5
x = ("Phnom Penh",  "Siem Reap", "Battambang")
y = (11.5564, 13.3622,  13.0957)
z = (104.9282, 103.8597, 103.2022)

t = zip(x, y, z)
for (x, y, z) in t:
    print(f"City: {x}, Latitude: {y}, Longitude: {z}")

#6
a ={1: 10,2: 20,3: 30,4: 40}
new_a= {k: (lambda x: x * 2)(v)for k,v in  a.items()} # items mean 1:10 like key+value=item
print(new_a)

#7
def test_str(lst):
    list={}
    for i in lst.lower(): # want Hello to become all small letters
        if i in list:
            list[i] +=1
        else:
            list[i] =1
    return list
print(test_str("Hello")) 

#8
def merge_dic(dic1,dic2):
    final_dic = {}
    for i in dic1:
        final_dic[i] = dic1[i] + dic2.get(i,0) # if key ot mean in dic2, vea tv jea 0 ber mean vea plus
    for i in dic2:
        if i not in final_dic:
            final_dic[i] = dic2[i] # check tha ber in dic2 ot doch final yk dic2 tv final del
    return final_dic
d1 = {'a':1,'b':2}
d2 = {'b':3,'c':4}
result = merge_dic(d1,d2)
print("Final dictionary",result)
#bonus
import os # for system cleear
def add_users(user_accounts):
    while True:
        username = input("Enter your username:")
        email = input("Enter your email:")
        if "@" in email and email.endswith("@gmail.com"):
            status = input("Enter status (active/suspended):").lower()
            if status != 'active ' and status !='suspended':
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
            print(f"{username} is succesfully remove!")
            break # dak break derm3 kom oy vea print tv kleng else
        else:
            print(f"{username} not found") # dak break derm3 oy vea print tae mdg ban hz
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
            print(f"{new_username} is succesfully update!")
            break
        else:
            print(f"{new_username} not found!")
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
            {"username": "charlie", "email": "charlie@gmail.com", "status": "suspended"},
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