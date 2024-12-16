from datetime import datetime
import platform
import sys
import msvcrt
import os
import bcrypt
import hashlib
import ast
import getpass

class FirstInterface:
    def display(self):
        while True:
            os.system('cls')
            print("=" * 60)
            print("\n\t 🌐 Welcome to the E-Commerce System 🌐 \n")
            print("=" * 60)
            print("\t🚀 Choose Your Role Below 🚀\n")
            print("\t1. 🛠️  Admin")
            print("\t2. 💻  Employee")
            print("\t3. 🛒  Customer")
            print("\t4. ❌  Exit")
            print("\n" + "=" * 60)
            
            # Get the user's choice
            choose_role = input("Choose your role (1-4): ")
            
            if choose_role == '1':
                admin_system = AdminSystem()
                admin_system.display_admin_account()
            elif choose_role == '2':
                employee_system = EmployeeInterface()
                employee_system.display_employee_account()
            elif choose_role == '3':
                user1.user_menu()
            elif choose_role == '4':
                print("\n❕Exiting the system. Thank you for using it!")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice. Please try again.")
                input("Press Enter to continue...")

class AdminEmployee(FirstInterface):

    employeefile = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\inf_employee.txt"
    recordstock = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\recordstock.txt"
    user_file = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\customer_pw.txt"
    system_log = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/system_log.txt'
    
    fileiphone_staff = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone.txt" 
    fileairpod_staff = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/airpod.txt"
    filemacbook_staff = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/macbook.txt"
    # balance_file = "C:\//Users\//KORNG\//OneDrive - Cambodia Academy of Digital Technology\//Documents\//GitHub\//Python_T1_Y2_Project/employee_log/customer_balance.txt"

    # view stock for users iphone
    fileiphone11_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone11_user.txt"
    fileiphone12_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone12_user.txt"
    fileiphone13_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone13_user.txt"
    fileiphone14_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone14_user.txt"
    fileiphone15_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone15_user.txt"

    # view stock for users mac
    mac_m1_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_m1_user.txt"
    mac_m2_user = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_m2_user.txt"
    mac_pro_14 = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_pro_14.txt"
    mac_pro_16 = r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_pro_16.txt"

        # view stock for user airpod
    airpod_user =r"C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/airpod_user.txt"

    def __init__(self):
        self.logged_in_username = None

    def load_employees(self):
        employees = []
        try:
            with open(self.manage_employ, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) == 4:
                        username, employee_id, email, hashed_password = parts
                        employees.append({
                            "username": username,
                            "id": employee_id,
                            "email": email,
                            "password": hashed_password  # This should be a hex string
                        })
        except FileNotFoundError:
            print("Employee data file is missing.")
        print(f"Loaded employees: {employees}")  # Debugging line
        return employees  # Ensure employees are returned correctly

    def log_action(self, action, username="Admin"):
        try:
            with open(self.system_log, 'a') as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp} - {username}: {action}\n")
        except Exception as ex:
            print(f"Error logging action : {ex}")

    #### MANAGE CUSTOMER PART ####

    def manage_customer_acc(self):
        os.system('cls')
        while True:
            print("\n" + "=" * 50)
            print("📂  Manage Customer Account Menu  📂")
            print("=" * 50)
            print("1️⃣  View Customers")
            print("2️⃣  Delete Customer")
            print("3️⃣  Return to Main Menu")
            print("=" * 50)

            try:
                choose = int(input("👉 Enter an option: "))
                if choose == 1:
                    self.view_customers()
                elif choose == 2:
                    self.delete_customer()
                elif choose == 3: 
                    print("Returning to the main menu...")
                    self.admin_dashboard()  
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def view_customers(self):
        try:
            with open(self.user_file, 'r') as file:
                users = [line.strip() for line in file]

            if not users:
                print("No users found.")
            else:
                print("\nCurrent User List: ")
                for index, user in enumerate(users, start=1):
                    # Extract only username and email
                    data = dict(item.split(": ", 1) for item in user.split(", "))
                    print(f"{index}. Username: {data['username']}, Email: {data['email']}")
        except FileNotFoundError:
            print("User file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_customer(self):
        try:
            file_path = self.user_file
            with open(file_path, 'r') as file:
                users = [line.strip() for line in file]

            if not users:
                print("No customers found to delete.")
                return

            print("\nCurrent Customer List: ")
            for index, user in enumerate(users, start=1):
                # Extract only username and email
                data = dict(item.split(": ", 1) for item in user.split(", "))
                print(f"{index}. Username: {data['username']}, Email: {data['email']}")

            customer_to_delete = int(input("Enter the number of the customer to delete: "))
            if 1 <= customer_to_delete <= len(users):
                del users[customer_to_delete - 1]
                with open(file_path, 'w') as file:
                    file.writelines([f"{user}\n" for user in users])
                print("Customer deleted successfully.")
            else:
                print("Invalid selection.")
        except FileNotFoundError:
            print("User file not found. Please ensure the file exists.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the customer.")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    #### MANAGE CUSTOMER PART ####

    #### CRUD FUNCTION #####

    def view_stock(self): # menu view stock
        while True:
            print("\n" + "=" * 50)
            print("📦  View Stock Menu  📦".center(50))
            print("=" * 50)
            print("1️⃣  iPhone")
            print("2️⃣  MacBook")
            print("3️⃣  AirPod")
            print("4️⃣  🔙 Exit to Main Menu")
            print("=" * 50)
            choice = input("Enter the model to add (1/2/3/4): ")
            if choice == "1":
                self.view_iphone()
            elif choice == "2":
                self.view_macbook()
            elif choice == "3":
                self.view_airpod()
            elif choice == "4":
                self.display_employee_task()
            else:
                print("Invalid choice. Please try again.")

            
    def view_iphone(self): #view iphone
        try:
            with open(self.fileiphone_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
                print(stock_data)
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
        
    def view_macbook(self): #view_mac
        try:
            with open(self.filemacbook_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
                print(stock_data)
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            
    def view_airpod(self): #view airpod
        try:
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
                print(stock_data)
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")


    def add_stock(self): # add stock
        # file_path = self.get_file_path()
        while True:
            print("\n" + "=" * 50)
            print("📈  Add Stock Menu  📈".center(50))
            print("=" * 50)
            print("1️⃣  Add iPhone")
            print("2️⃣  Add MacBook")
            print("3️⃣  Add AirPod")
            print("4️⃣  🔙 Exit to Employee Tasks")
            print("=" * 50)
            choice = input("Enter the model to add (1/2/3): ")
            if choice == "1":
                self.add_iphone()
            elif choice == "2":
                self.add_macbook()
            elif choice == "3":
                self.add_airpod()
            elif choice == "4":
                self.display_employee_task()
            else:
                print("Invalid choice. Please try again.")

    def delete_stock(self): #delete stock
        while True:
            print("\n" + "=" * 50)
            print("🗑️  Delete Stock Menu  🗑️".center(50))
            print("=" * 50)
            print("1️⃣  Remove iPhone")
            print("2️⃣  Remove MacBook")
            print("3️⃣  Remove AirPods")
            print("4️⃣  🔙 Back to Menu")
            print("=" * 50)
            
            choice = input("Enter the model to remove (1/2/3): ")
            if choice == "1":
                self.remove_iphone()
            elif choice == "2":
                self.remove_macbook()
            elif choice == "3":
                self.remove_airpod()
            elif choice == "3":
                self.display_employee_task()
            else:
                print("Invalid choice. Please try again.")
            
    def add_iphone(self): # add iphone
            try:
                with open(self.fileiphone_staff, "r") as file:
                    stock_data = ast.literal_eval(file.read())
            except FileNotFoundError:
                print("Stock file not found. Creating a new one.")
                stock_data = {}
                
            model = input("Enter the model to add (11/12/13/14/15): ")
            model_key = f"iphone_{model}"
            if model_key not in stock_data:
                print (f"cannot add products.Model '{model}' not found.")
                return
            storage = input("Enter the storage size to add (64/128/256/512(GB)/1(TB)): ")
            if storage in ["64", "128", "256", "512"]:
                storage_key = f"{storage}GB"
            elif storage == "1":    
                storage_key = f"{storage}TB"
            else:
                print("Invalid storage size.Please enter 64,128,256,512(GB)or1(TB).")
                return
            if storage_key not in stock_data[model_key]:
                print (f"cannot add products.Storage '{storage}' not found for model '{model}'.")
                return

            try:
                quantity = int(input("Enter the quantity to add: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
            if model_key in stock_data:
                if storage_key in stock_data[model_key]:
                    if stock_data [model_key][storage_key] > 5:
                        print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key} ({storage_key}).")
                        return
                    else:
                        stock_data[model_key][storage_key] += quantity
                        
                else:
                    stock_data[model_key][storage_key] = quantity
            else:
                stock_data[model_key] = {storage_key: quantity}
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open (self.recordstock, 'a') as file:
                file.write(f"{timestamp} | {self.logged_in_username} | add |Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")
            
            try:
                with open(self.fileiphone_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully added {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")

    def remove_iphone(self): #remove iphone
            try:
                with open(self.fileiphone_staff, "r") as file:
                    stock_data = ast.literal_eval(file.read())
            except FileNotFoundError:
                print("Stock file not found. Creating a new one.")
                stock_data = {}
                
            model = input("Enter the model to remove (11/12/13/14/15): ")
            model_key = f"iphone_{model}"
            storage = input("Enter the storage size to remove (64/128/256/512(GB)/1(TB)): ")
            if storage == "64" or storage == "128" or storage == "256" or storage == "512":
                storage_key = f"{storage}GB"
            else:
                storage_key = f"{storage}TB"
            try:
                quantity = int(input("Enter the quantity to remove: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
            if model_key in stock_data:
                if storage_key in stock_data[model_key]:
                    if stock_data [model_key][storage_key] < quantity:
                        print(f"Cannot remove stock. Removing {quantity} would be less or equal the quantity of {model_key} ({storage_key}).")
                        return
                    else:
                        stock_data[model_key][storage_key] -= quantity
                else:
                    stock_data[model_key][storage_key] = quantity
            else:
                stock_data[model_key] = {storage_key: quantity}
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open (self.recordstock, 'a') as file: 
                file.write(f"{timestamp} | {self.logged_in_username} |remove | Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")

            try:
                with open(self.fileiphone_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully removing {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")

    def add_macbook(self): #add macbook
        try:
            # Load stock data from file
            with open(self.filemacbook_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            stock_data = {}

        # Predefined valid models
        valid_models = {
            "1": "MacBook_Air_M1",
            "2": "MacBook_Air_M2",
            "14": "MacBook_Pro_14inch",
            "16": "MacBook_Pro_16inch"
        }

        # User inputs
        model = input("Enter the model to add (1(AirM1)/2(AirM2)/14(Pro_14inch)/16(Pro_16inch)): ")

        # Check if the model is valid
        if model not in valid_models:
            print("Cannot add product. Model not found.")
            return

        model_key = valid_models[model]
        storage = input("Enter the storage size to add (256/512(GB)/1(TB)): ")

        # Validate storage and construct storage key
        if storage in ["256", "512"]:
            storage_key = f"{storage}GB"
        elif storage == "1":
            storage_key = "1TB"
        else:
            print("Invalid storage size. Please enter 256, 512 (GB) or 1 (TB).")
            return

        # Check if the storage type exists for the given model
        if storage_key not in stock_data.get(model_key, {}):
            print(f"Cannot add product. Storage '{storage}' not found for model '{model}'.")
            return

        try:
            quantity = int(input("Enter the quantity to add: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        # Check the existing stock level and limit
        if stock_data[model_key][storage_key] + quantity > 5:
            print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key} ({storage_key}).")
            return
        else:
            stock_data[model_key][storage_key] += quantity
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file: 
            file.write(f"{timestamp} | {self.logged_in_username} | add |Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")

        try:
            with open(self.filemacbook_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully added {quantity} of {model_key} ({storage_key}).")
        except IOError:
            print("Error writing to the stock file.")
            
    def remove_macbook(self): #remove mac
        try:
            with open(self.filemacbook_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found.")
            return

        model = input("Enter the model to remove (1(AirM1)/2(AirM2)/14(Pro_14inch)/16(Pro_16inch)): ")
        if model == "1" or model == "2":
            model_key = f"MacBook_Air_M{model}"
        else:
            model_key = f"MacBook_Pro_{model}inch"
        
        storage = input("Enter the storage size to remove (256/512(GB)/1(TB)): ")
        if storage == "256" or storage == "512":
            storage_key = f"{storage}GB"
        else:
            storage_key = f"{storage}TB"

        try:
            quantity = int(input("Enter the quantity to remove: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        if model_key in stock_data and storage_key in stock_data[model_key]:
            if stock_data[model_key][storage_key] < quantity:
                print(f"Cannot remove {quantity}. Only {stock_data[model_key][storage_key]} in stock for {model_key} ({storage_key}).")
                return
            else:
                stock_data[model_key][storage_key] -= quantity
                if stock_data[model_key][storage_key] == 0:
                    del stock_data[model_key][storage_key]
                if not stock_data[model_key]:
                    del stock_data[model_key]
        else:
            print(f"{model_key} ({storage_key}) not found in stock.")
            return
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file:  
            file.write(f"{timestamp} | {self.logged_in_username} | remove |Model: {model_key} | Storage: {storage_key} | Quantity: {quantity}\n")

        try:
            with open(self.filemacbook_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully removed {quantity} of {model_key} ({storage_key}).")
        except IOError:
            print("Error writing to the stock file.")

    def add_airpod(self): #add airpod
        try:
            # Load stock data from file
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            stock_data = {}

        # Predefined valid models
        valid_models = {
            "2ndGen": "Airpods_2nd_Gen",
            "Pro": "Airpods_Pro",
            "Max": "Airpods_Max"
        }

        # User input
        model = input("Enter the model to add (2ndGen/Pro/Max): ")

        # Check if the model is valid
        if model not in valid_models:
            print("Cannot add product. Model not found.")
            return

        model_key = valid_models[model]

        try:
            quantity = int(input("Enter the quantity to add: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        # Check the existing stock level and limit
        
        if stock_data[model_key] > 5:
            print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key}.")
            return
        else:
            stock_data[model_key] += quantity
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file:
            #   print(f"ADD | {timestamp} | {self.employee_username} | Model: {model_key} | Quantity: {quantity}\n")  
            file.write(f"{timestamp} | {self.logged_in_username} | add |Model: {model_key} | Quantity: {quantity}\n")

        try:
            with open(self.fileairpod_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully added {quantity} of {model_key}.")
        except IOError:
            print("Error writing to the stock file.")

    def remove_airpod(self): #remove airpod
        try:
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found.")
            return

        model = input("Enter the model to remove (2ndGen/Pro/Max): ")
        if model == "2ndGen":
            model_key = f"Airpods_2nd_Gen"
        elif model in ["Pro", "Max"]:
            model_key = f"Airpods_{model}"
        else:
            print("Invalid model. Please enter a valid model (2ndGen/Pro/Max).")
            return

        try:
            quantity = int(input("Enter the quantity to remove: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        if model_key in stock_data:
            if stock_data[model_key] < quantity:
                print(f"Cannot remove {quantity}. Only {stock_data[model_key]} in stock for {model_key}.")
                return
            else:
                stock_data[model_key] -= quantity
                if stock_data[model_key] == 0:
                    del stock_data[model_key]
        else:
            print(f"{model_key} not found in stock.")
            return
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open (self.recordstock, 'a') as file:
            #   print(f"ADD | {timestamp} | {self.employee_username} | Model: {model_key} | Quantity: {quantity}\n")  
            file.write(f"{timestamp} | {self.logged_in_username} | remove |Model: {model_key} | Quantity: {quantity}\n")

        try:
            with open(self.fileairpod_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully removed {quantity} of {model_key}.")
        except IOError:
            print("Error writing to the stock file.")

    #### CRUD FUNCTION #####

    def masked_input(self, prompt=""):
        print(prompt, end="", flush=True)
        password = ""
        while True:
            char = msvcrt.getch()
            if char in {b'\r', b'\n'}:
                print()
                break
            elif char == b'\x08':
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end='', flush=True)
            else:
                password += char.decode()
                print('*', end='', flush=True)
        return password

    def hash_password(self, password):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt.hex() + hashed_password.hex()  # Convert both salt and hash to hex

    def verify_password(self, stored_password, input_password):
        salt = stored_password[:16]
        stored_hash = stored_password[16:]
        input_hash = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
        return stored_hash == input_hash

class EmployeeInterface(AdminEmployee):

    manage_employ = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/manage_employee.txt'

    def __init__(self):
        self.employees = self.load_employees()
        self.display_employee_account()
        super().__init__(self.masked_input, self.hash_password, self.verify_password, self.system_log, self.logged_in_username)

    def display_employee_account(self):
        os.system('cls')
        while True:
            try:
                print("\n" + "=" * 50)
                print("👔 Welcome, Employee Portal 👔".center(50))
                print("=" * 50)
                print("1️⃣  Log in as Employee")
                print("2️⃣  🔙 Back to Main Menu")
                print("=" * 50)

                choose = int(input("Enter ur function to do: "))
                if choose == 1:
                    self.employee_login()
                elif choose == 2:
                    first = FirstInterface()
                    first.display()
                else:
                    print("Invalid option")
            except ValueError as v:
                print(v)
    
    def employee_login(self):
        os.system('cls')
        for attempts_left in range(3, 0, -1):
            print("\n" + "=" * 50)
            print("🔑 Employee Login Portal".center(50))
            print("=" * 50)
            username = input("👤 Enter your username: ")
            employee_id = input("🆔 Enter your Employee ID: ")
            email = input("📧 Enter your email: ")
            password = self.masked_input("🔒 Enter your password: ")

            self.logged_in_username = username
            for employee in self.employees:
                # Validate credentials
                if (
                    employee["username"] == username and 
                    employee["email"] == email and 
                    employee["id"] == employee_id and
                    self.verify_password(bytes.fromhex(employee["password"]), password)  # Check password
                ):
                    print("Login successful!")
                    self.log_action("Logged in", username)
                    self.display_employee_task()
                    return

            print(f"Invalid credentials. You have {attempts_left - 1} attempts left.")
        print("Too many failed attempts. Access denied.")


    def display_employee_task(self):
        os.system('cls')
        while True:
            try:
                print("\n" + "=" * 50)
                print("📋 Employee Task Dashboard 📋".center(50))
                print("=" * 50)
                print("1️⃣  Manage Stock (Add or Update)")
                print("2️⃣  📦 View Stock")
                print("3️⃣  📝 Generate Report")
                print("4️⃣  ❌ Exit")
                print("=" * 50)

                choose = int(input("Enter a task to do: "))
                if choose == 1:
                    self.add_stock()
                elif choose == 2:
                    self.view_stock()
                elif choose == 3:
                    self.report()
                elif choose == 4:
                    sys.exit()
                else:
                    print("Invalid option")
            except ValueError as ve:
                print(ve)


    ##### EMPLOYEE PART ########
class Stock(EmployeeInterface):
    def __init__(self,fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user,):
        self.fileiphone_staff = fileiphone_staff
        self.fileairpod_staff = fileairpod_staff
        self.filemacbook_staff = filemacbook_staff
        self.fileiphone11_user = fileiphone11_user
        self.fileiphone12_user = fileiphone12_user
        self.fileiphone13_user = fileiphone13_user
        self.fileiphone14_user = fileiphone14_user
        self.fileiphone15_user = fileiphone15_user
        self.mac_m1_user = mac_m1_user
        self.mac_m2_user = mac_m2_user
        self.mac_pro_14 = mac_pro_14
        self.mac_pro_16 = mac_pro_16
        self.airpod_user = airpod_user
        self.total_amount = 0.0
        self.purchases = []

    def clear_screen(self):
        current_os = platform.system()

        if current_os == "Windows":
            os.system('cls')  # Windows command to clear the screen
        else:
            os.system('clear')
        
    def iphone_menu(self):      
        # Menu bar for user
        while True:
            print("=" * 80)
            print("\t📱 iPhone Models Menu 📱".center(80))  # Title centered
            print("=" * 80)
            print("1. iPhone 11")
            print("2. iPhone 12")
            print("3. iPhone 13")
            print("4. iPhone 14")
            print("5. iPhone 15")
            print("6. Back to Menu")
            print("=" * 80)
            choice = input("Option:").strip()
            if choice == "1":
                try: 
                    with open(self.fileiphone11_user, "r") as file:
                        content = file.read()
                        print(content)
                        user_buy = input("Do you interesting in our product? If you want to buy(yes), if not(no): ").lower()
                        while True:
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "iphone_11"
                                while True:
                                    storage = input("Storage(64/128/256): ")
                                    storage_key = f"{storage}GB"
                                    try:
                                        with open(self.fileiphone_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:   
                                            if storage_key in stock_data[model_key]:
                                                if storage == "64":
                                                    value = "$599"
                                                    break
                                                elif storage == "128":
                                                    value = "$699"
                                                    break
                                                elif storage == "256":
                                                    value = "$799"
                                                    break
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no): ").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", "").strip())
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key, total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.iphone_menu()
                                        return 
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.iphone_menu()
                                return 
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product? If you want to buy(yes), if not(no): ").lower()
                except FileNotFoundError:
                    print(f"The file {self.fileiphone11_user} was not found. Please ensure it exists in the correct directory.")
                    return

            elif choice == "2" :
                # print("Model:iPhone_12")
                try: 
                    with open(self.fileiphone12_user,"r") as file:
                        content = file.read()
                        print(content)
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "iphone_12"
                                while True:
                                    storage = input("Storage(64/128/256):")
                                    storage_key = f"{storage}GB"
                                    try:
                                        with open(self.fileiphone_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "64" :
                                                        # print("$599")
                                                    value = "$699"
                                                    break
                                                        # print(value)
                                                elif storage == "128" :
                                                        # print("$699")
                                                    value = "$799"
                                                    break
                                                        # print(value)
                                                elif storage == "256" :
                                                        # print("$799")
                                                    value = "$899"
                                                    break
                                                        # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.iphone_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.iphone_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                                
                except FileNotFoundError:
                    print(f"The file {self.fileiphone12_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "3" :
                # print("Model:iPhone_13")
                try: 
                    with open(self.fileiphone13_user,"r") as file:
                        content = file.read()
                        print(content)
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "iphone_13"
                                while True:
                                    storage = input("Storage(128/256/512):")
                                    storage_key = f"{storage}GB"
                                    try:
                                        with open(self.fileiphone_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "128" :
                                                        # print("$599")
                                                    value = "$799"
                                                    break
                                                        # print(value)
                                                elif storage == "256" :
                                                        # print("$699")
                                                    value = "$899"
                                                    break
                                                        # print(value)
                                                elif storage == "512" :
                                                        # print("$799")
                                                    value = "$999"
                                                    break
                                                        # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.iphone_menu()
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.iphone_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.fileiphone13_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "4" :
                # print("Model:iPhone_14")
                try: 
                    with open(self.fileiphone14_user,"r") as file:
                        content = file.read()
                        print(content)
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "iphone_14"
                                while True:
                                    storage = input("Storage(128/256/1):")
                                    if storage == "1":
                                        storage_key = f"{storage}TB"
                                    else:
                                        storage_key = f"{storage}GB"
                                    try:
                                        with open(self.fileiphone_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "128" :
                                                        # print("$599")
                                                    value = "$899"
                                                    break
                                                        # print(value)
                                                elif storage == "256" :
                                                        # print("$699")
                                                    value = "$999"
                                                    break
                                                        # print(value)
                                                elif storage == "1" :
                                                        # print("$799")
                                                    value = "1099"
                                                    break
                                                        # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                            print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                            return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.iphone_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                    
                            elif user_buy == "no":
                                print("Thank for viewing our stock!")
                                self.iphone_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.fileiphone14_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "5" :
                # print("Model:iPhone_15")
                try: 
                    with open(self.fileiphone15_user,"r") as file:
                        content = file.read()
                        print(content)
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "iphone_15"
                                while True:
                                    storage = input("Storage(128/256/1):")
                                    if storage == "1":
                                        storage_key = f"{storage}TB"
                                    else:
                                        storage_key = f"{storage}GB"
                                    try:
                                            with open(self.fileiphone_staff, "r") as file:
                                                content = file.read()
                                                stock_data = ast.literal_eval(content)
                                            if model_key in stock_data:
                                                if storage_key in stock_data[model_key]:
                                                    if storage == "128" :
                                                        # print("$599")
                                                        value = "$999"
                                                        break
                                                        # print(value)
                                                    elif storage == "256" :
                                                        # print("$699")
                                                        value = "$1199"
                                                        break
                                                        # print(value)
                                                    elif storage == "1" :
                                                        # print("$799")
                                                        value = "1299"
                                                        break
                                                        # print(value)
                                                    else:
                                                        print("Invalid storage option.")
                                                        return
                                    except FileNotFoundError:
                                        print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.iphone_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.iphone_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.fileiphone15_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "6":
                os.system("cls")
                self.stock_menu()
                break
            else:
                print("No such model exists.")
                return   
            
    def airpod_menu(self):
        try:
            with open(self.airpod_user,"r") as file:
                content = file.read()
                # print("Stock AirPods:")
                print(content)
        except FileNotFoundError:
            print(f"The file {self.airpod_user} was not found. Please ensure it exists in the correct directory.")
            return
        
        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
        while True:
            if user_buy == "yes" or user_buy == "y":
                choice = input("Option:(Gen,Pro,Max):")
                if choice == "Gen":
                    # print("Price:$159")
                    value = "$159"
                    # print(value)
                    choice_key = "Airpods_2nd_Gen"
                elif choice == "Pro":
                    # print("Price:$249")
                    value = "$249"
                    # print(value)
                    choice_key = "Airpods_Pro"
                elif choice == "Max":
                    # print("Price:$549")
                    value = "$549"
                    # print(value)
                    choice_key = "Airpods_Max"
                else:
                    print(f"{choice} doesn't has in our stock.")
                    continue
                while True:
                    item = input("Items (enter a valid number): ")
                    if item.isdigit():
                        item = int(item)
                        break
                    else:
                        print("Invalid input. Please enter a valid number.")
                while True:
                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                    if confirm == "yes" or confirm == "y":
                        try:
                            with open(self.fileairpod_staff, "r") as file:
                                stock_data = ast.literal_eval(file.read())
                                        # stock_data = ast.literal_eval(content)
                                if choice_key in stock_data:
                                        #check if there are enough stock and balance
                                    price = float(value.replace("$", ""))
                                    total_cost = price * item
                                        #check if theuser has enough balance
                                    if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                        if stock_data[choice_key] >= item:
                                            stock_data[choice_key] -=item
                                                # print(f"Purchase successful! Remaining stock for {choice_key} : {stock_data[choice_key]}")
                                            with open(self.fileairpod_staff, "w") as file: 
                                                file.write(str(stock_data))
                                            self.add_to_total(item, choice_key, None,total_cost)
                                            user1.calculate()
                                            print("Purchase successful!")
                                        else:
                                            print(f"Sorry, {choice_key} is out of stock.")
                                    else:
                                        print("Insufficient balance.")
                                    return
                        except FileNotFoundError:
                            print(f"The file {self.fileairpod_staff} was not found. Please ensure it exists in the correct directory.")
                    elif confirm == "no" or confirm == "n":
                        print("Purchase canceled.")
                        return
                    else:
                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")    
            elif user_buy == "no" or user_buy == "n":
                print("Thank for viewing our stock!")
                self.stock_menu()
                return
            else:
                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                continue
    # for user to view the stock of macbook
    def macbook_menu(self):
        while True:
            print("=" * 80)
            print("\t🍏 Mac Models Menu 🍏".center(80))  # Title centered with emoji
            print("=" * 80)
            print("1. MacBook M1")
            print("2. MacBook M2")
            print("3. MacBook Pro 14-inch")
            print("4. MacBook Pro 16-inch")
            print("5. Back to Menu")
            print("=" * 80)

            choice = input("Choose a model (1-5): ")
            if choice == "1":
                # print("Model:Mac_M1")
                try:
                    with open(self.mac_m1_user,"r") as file:
                        content = file.read()
                        # print("Stock:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        while True:
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "MacBook_Air_M1"
                                while True:
                                    storage = input("Storage(256/512):")
                                    storage_key = f"{storage}GB"
                                    try:
                                        with open(self.filemacbook_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "256" :
                                                    # print("$999")
                                                    value = "$999"
                                                    break
                                                    # print(value)
                                                elif storage == "512" :
                                                    # print("$1249")
                                                    value = "$1249"
                                                    break
                                                    # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")     
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.macbook_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.macbook_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.mac_m1_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "2":
                # print("Model:Mac_M2")
                try:
                    with open(self.mac_m2_user,"r") as file:
                        content = file.read()
                        # print("Stock:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        while True:
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "MacBook_Air_M2"
                                storage = input("Storage(256/512):")
                                storage_key = f"{storage}GB"
                                while True:
                                    try:
                                        with open(self.filemacbook_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "256" :
                                                    # print("$999")
                                                    value = "$999"
                                                    break
                                                    # print(value)
                                                elif storage == "512" :
                                                    # print("$1249")
                                                    value = "$1249"
                                                    break
                                                    # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.macbook_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.macbook_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.mac_m2_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "3":
                # print("Model:Mac_Pro_14")
                try:
                    with open(self.mac_pro_14,"r") as file:
                        content = file.read()
                        # print("Stock:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        while True:
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "MacBook_Pro_14inch"
                                storage = input("Storage(1(TB)/512):")
                                if storage == "1":
                                    storage_key = f"{storage}TB" 
                                else:
                                    storage_key = f"{storage}GB"
                                while True:
                                    try:
                                        with open(self.filemacbook_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "512" :
                                                    # print("$999")
                                                    value = "$1249"
                                                    break
                                                    # print(value)
                                                elif storage == "1" :
                                                    # print("$1249")
                                                    value = "$2499"
                                                    break
                                                    # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.macbook_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.macbook_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.mac_pro_14} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "4":
                # print("Model:Mac_Pro_16")
                try:
                    with open(self.mac_pro_16,"r") as file:
                        content = file.read()
                        # print("Stock:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        while True:
                            if user_buy == "yes" or user_buy == "y":
                                model_key = "MacBook_Pro_16inch"
                                storage = input("Storage(1(TB)/512):")
                                if storage == "1":
                                    storage_key = f"{storage}TB" 
                                else:
                                    storage_key = f"{storage}GB"
                                while True:
                                    try:
                                        with open(self.filemacbook_staff, "r") as file:
                                            content = file.read()
                                            stock_data = ast.literal_eval(content)
                                        if model_key in stock_data:
                                            if storage_key in stock_data[model_key]:
                                                if storage == "512" :
                                                    # print("$999")
                                                    value = "$2499"
                                                    break
                                                    # print(value)
                                                elif storage == "1" :
                                                    # print("$1249")
                                                    value = "$2999"
                                                    break
                                                    # print(value)
                                                else:
                                                    print("Invalid storage option.")
                                                    return
                                    except FileNotFoundError:
                                        print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")       
                                while True:
                                    item = input("Items (enter a valid number): ")
                                    if item.isdigit():
                                        item = int(item)
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid number.")
                                while True:
                                    confirm = input("Confirm your buy(yes,no):").strip().lower()
                                    if confirm == "yes" or confirm == "y":
                                        # user1.calculate()
                                        price = float(value.replace("$", ""))
                                        total_cost = price * item
                                        if user1.current_user in user1.balances and user1.balances[user1.current_user] >= total_cost:
                                            if  stock_data[model_key][storage_key] >= item:
                                                stock_data[model_key][storage_key] -= item
                                                # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                self.add_to_total(item, model_key, storage_key,total_cost)
                                                user1.calculate()
                                                print("Purchase successful!")
                                            else:
                                                print(f"Sorry, {model_key} for storage:{storage_key} is out of stock.")
                                        else:
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.macbook_menu()
                                        return
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
                                self.macbook_menu()
                                return
                            else:
                                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                except FileNotFoundError:
                    print(f"The file {self.mac_pro_16} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "5":
                # os.system("clear")
                os.system("cls")
                self.stock_menu()
                break
            else:
                print("No such model exists.")
                return   
    # let user input
    def stock_menu(self):
        os.system('cls')
        while True:
            print("=" * 80)
            print("\t📦 Stock Display 📦".center(80))  # Title centered with a box emoji
            print("=" * 80)
            print("1. 📱 iPhone")
            print("2. 🎧 Airpods")
            print("3. 💻 MacBook")
            print("4. 📊 View Total Stock")
            print("5. 🔙 Back to Usage Menu")
            print("6. ❌ Exit")
            print("=" * 80)
            option = input("Option:")
            if option == "1":
                self.clear_screen()
                self.iphone_menu()
            elif option == "2":
                self.clear_screen()
                self.airpod_menu()
            elif option == "3":
                self.clear_screen()
                self.macbook_menu()
            elif option == "4":
                self.clear_screen()
                user1.show_total()
            elif option == "5":
                self.clear_screen()
                user1.usage_menu()
            elif option == "6":
                self.clear_screen()
                print("Exit the stock!")
                sys.exit()
            else:
                print("Invalid option, please choose again.")

class User(Stock):
    def __init__(self, user_filename, balance_filename,history_filename, feedback_filename, fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user):
        #for stock
        super().__init__(fileiphone_staff, fileairpod_staff, filemacbook_staff, 
                        fileiphone11_user, fileiphone12_user, fileiphone13_user, 
                        fileiphone14_user, fileiphone15_user, mac_m1_user, 
                        mac_m2_user, mac_pro_14, mac_pro_16, airpod_user)
        self.user_filename = user_filename
        self.balance_filename = balance_filename
        self.history_filename = history_filename
        self.feedback_filename = feedback_filename
        self.users = []
        self.load_users()
        self.balance = 0.0
        self.balances = {}
        self.load_balance()
        #also for stock
        self.total_amount = 0
        self.purchases = []
        self.load_purchase()

    def add_to_total(self, item, model, storage, total_cost):
        try:
            self.total_amount += float(total_cost)
            purchase = {
                "username": self.current_user,
                "model" : model,
                "storage" : storage,
                "item" : item,
                "subtotal" : total_cost
            }
            self.purchases.append(purchase)
            self.save_purchase(purchase)
        except ValueError as e:
            print(f"[ERROR] Failed to add to total_amount: {e}")

    def save_purchase(self, purchase):
        try:
            with open(self.history_filename, "a") as file:
                # Format the purchase data in the new format
                purchase_data = f"username: {purchase['username']}; model: {purchase['model']}; storage: {purchase['storage']}; item: {purchase['item']}; subtotal: {float(purchase['subtotal']):.2f}\n"
                file.write(purchase_data)
        except Exception as e:
            print(f"Error saving purchase to file {e}.")

    def load_purchase(self):
        try:    
            with open(self.history_filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue

                    # Split the line by '; ' to separate each field
                    if "; " in line:
                        parts = line.split("; ")
                        purchase_data = {}
                        for part in parts:
                            if ":" in part:  # Ensure the part contains a key-value pair
                                key, value = part.split(": ")
                                purchase_data[key.strip()] = value.strip()  # Remove extra spaces if any

                        # Add the purchase to the list and update the total_amount
                        self.purchases.append(purchase_data)
                        self.total_amount += float(purchase_data["subtotal"])  
        except Exception as e:
            print(f"Error occur {e}")

    def show_total(self):
        self.clear_screen()
        print("="*80)
        print("\t\t\t\tYour Purchase:")
        print("="*80)
        dynamic_total = 0
        for purchase in self.purchases:
            if purchase["username"] == self.current_user:
                model = purchase["model"]
                storage = purchase["storage"]
                item = purchase["item"]
                subtotal = purchase["subtotal"]
                print(f"{item}x {model} ({storage}): ${subtotal:.2f}")  
                dynamic_total += subtotal 
        print(f"Total amount of purchases: ${dynamic_total:.2f}\n")

    def calculate(self):
        if self.total_amount > 0:
            if self.current_user in self.balances:  # Ensure the user exists in balances
                if self.balances[self.current_user] >= self.total_amount:  # Check sufficient balance
                    self.balances[self.current_user] -= self.total_amount  # Deduct total amount
                    print(f"New balance: {self.balances[self.current_user]}")
                    with open(self.balance_filename, "w") as balance_file:
                        for username, balance in self.balances.items():
                            balance_file.write(f"username: {username}, balance: {balance}\n")
                    self.total_amount = 0
                else:
                    print("Insufficient balance.")
            else:
                print("Insufficient balance.")
        else:
            print("User not found.")
        
    def load_users(self):
        try:
            with open(self.user_filename, 'r') as file:
                for line in file:
                    line = line.strip() 
                    if not line:  
                        continue
                    if ": " in line:
                        parts = line.split(", ")
                        user_data = {}
                        for part in parts:
                            if ": " in part:
                                key, value = part.split(": ")
                                user_data[key] = value
                        self.users.append(user_data)
        except FileNotFoundError:
            print(f"{self.user_filename} not found.")
            
    def save_user(self):
        with open(self.user_filename, "w") as file:
            for user in self.users: 
                file.write(f"username: {user['username']}, email: {user['email']}, password: {user['password']}, secret pin: {user['secret pin']}\n")
    
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def hash_secret_pin(self,pin):
        return hashlib.sha256(pin.encode()).hexdigest()  

    def register(self):
        try:  
            with open(self.user_filename, 'a') as file:   
                while True:
                    print("\n============================== Register ==============================")
                    username = input("\nEnter a username to register: ")
                    for i in self.users:
                        if username == i["username"]:
                            print("This user has already been existed. Please try again!\n")
                            break
                    else:
                        break

                while True:
                    email = input("Enter your email address: ")
                    if '@' in email and '.' in email: 
                        break
                    else:
                        print("Invalid email format. Please enter a valid email address.\n")
                        continue

                while True:
                    pw = getpass.getpass("Enter a Password: ")
                    if len(pw) < 8:
                        print("Password too short. Must be at least 8 Characters.\n")
                        continue
                    if not any(c.isupper()for c in pw):
                        print("Password must contain at least one uppercase letter.\n")
                        continue
                    if not any(c.islower()for c in pw):
                        print("password must contain at least one lowercase letter.\n")
                        continue
                    if not any(c.isdigit()for c in pw):
                        print("Password must contain at least one digit.\n")
                        continue
                    if not any(c in '!@#$%^&*'for c in pw):
                        print("Password must contain at least one special character.\n")
                        continue
                    confirm_pw = getpass.getpass("Confirm your Password: ")
                    if confirm_pw != pw:
                        print("Password do not match. Please try again.\n")
                        continue
                    break

                while True:
                    secret_pin = getpass.getpass("Enter a 4-digit secret Pin: ")
                    if len(secret_pin) < 4:
                        print("Secret is too short. Must be a 4-digit number.\n")
                        continue
                    if len(secret_pin) > 4:
                        print("Secret is too long. Must be a 4-digit number.\n")
                        continue
                    if not secret_pin.isdigit():
                        print("Pin must be a number.\n")
                        continue

                    hashed_pw = self.hash_password(pw)
                    hashed_secret_pin = self.hash_secret_pin(secret_pin)
                    new_user = {"username": username, "email": email, "password": hashed_pw, "secret pin": hashed_secret_pin}
                    self.users.append(new_user)
                    file.write(f"username: {new_user['username']}, email: {new_user['email']}, password: {new_user['password']}, secret pin: {new_user['secret pin']}\n")
                    print("Registration account successful!\n")
                    
                    with open(self.balance_filename, "a") as balance_file:
                        balance_file.write(f"username: {username}, balance: {self.balance}\n")
                    break
        except Exception as e:
            print(f"There's an error with your registration: {e}. please try again!.")
        
    def login(self):
        try:
            for i in range(3, 0, -1):
                print("\n============================== Login ==============================")
                username = input("\nEnter your username: ")
                email = input("Enter your email: ")
                pw = getpass.getpass("Enter your password: ")
                hashed_pw = self.hash_password(pw)
                for user in self.users:
                    if user["username"] == username and user["email"] == email and user["password"] == hashed_pw :
                        print(f"Login successfully! Welcome, {username}\n")
                        self.current_user = username
                        self.load_balance()
                        self.usage_menu()
                        break
                else:
                    print(f"Invalid credentials. You have {i - 1} attempts left")
                    continue
                break
            else:
                print("Too many failed attempts. Access blocked.\n")
        except Exception as e:
            print(f"There is an error with your login: {e}. Please try again!.")
            

    def forgot(self):
        try:
            print("\n============================== Forgot Password ==============================")
            username = input("\nEnter your username: ")
            email = input("Enter your email: ")
            secret_pin = getpass.getpass("Enter your secret pin:")
            hashed_secret_pin = self.hash_secret_pin(secret_pin)

            for k in self.users:
                if k["username"] == username and k["email"] == email and k["secret pin"] == hashed_secret_pin:
                    # user_found = True
                    while True:
                        new_pw = getpass.getpass("Enter your new password: ")
                        if len(new_pw) < 8:
                            print("Password too short. Must be at least 8 Characters.")
                            continue
                        if not any(c.isupper()for c in new_pw):
                            print("Password must contain at least one uppercase letter.")
                            continue
                        if not any(c.islower()for c in new_pw):
                            print("password must contain at least one lowercase letter.")
                            continue
                        if not any(c.isdigit()for c in new_pw):
                            print("Password must contain at least one digit.")
                            continue
                        if not any(c in '!@#$%^&*'for c in new_pw):
                            print("Password must contain at least one special character.")
                            continue
                        confirm_pw = getpass.getpass("Confirm your Password: ")
                        if confirm_pw != new_pw:
                            print("Password do not match. Please try again.")
                            continue
                        break
                    hashed_pw = self.hash_password(new_pw)
                    k["password"] = hashed_pw
                    print("Reset password successfully!.\n")

                    with open(self.user_filename, "w") as file:
                        for user in self.users: 
                            file.write(f"username: {user['username']}, email: {user['email']}, password: {user['password']}, secret pin: {user['secret pin']}\n")
                    break
            else:
                print(f"There is no valid account with {username} exist.\n")
        except Exception as e:
            print(f"There is an error occur in your forgot proceess: {e} Please try again!.")
            
    def load_balance(self):
        try:
            with open(self.balance_filename, 'r') as file:
                for line in file:
                    line = line.strip() 
                    if not line:  
                        continue
                    if ": " in line and ", " in line:
                        parts = line.split(", ")
                        username_part = parts[0].split(": ")[1]  
                        balance_part = parts[1].split(": ")[1]  
                        self.balances[username_part] = float(balance_part)
        except FileNotFoundError:
            print(f"{self.balance_filename} not found.")

    def manage_balance(self):
        try:
            self.clear_screen()
            while True:
                print("\n============================== Manage Balance ==============================")
                print(f"\nYour current balance: ${self.balances[self.current_user]}")
                print("1. Deposit Balance")
                print("2. Back")
                option = input("Choose Option(1,2): ")
                if option == "1":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------ Deposit Balance ------------------------------")
                        amount = float(input("\nInput the amount you want to deposit: "))
                        if amount > 0:
                            secret_pin = getpass.getpass("Enter your secret pin:")
                            hashed_secret_pin = self.hash_secret_pin(secret_pin)
                            
                            current_user_data = None
                            for user in self.users:
                                if user["username"] == self.current_user:
                                    current_user_data = user
                                    break
                            
                            if current_user_data and current_user_data["secret pin"] == hashed_secret_pin:
                                self.balances[self.current_user] += amount
                                print("Deposited successfully!")
                                print(f"Your balance now is ${self.balances[self.current_user]}\n")
                                with open(self.balance_filename, "w") as balance_file:
                                    for username, balance in self.balances.items():
                                        balance_file.write(f"username: {username}, balance: {balance}\n")
                                break
                            else:
                                print("Invalid pin please try again!") 
                                continue
                        else:
                            print("Invalid amount. Please enter a valid amount.")
                elif option == "2":
                    self.clear_screen()
                    print("\n")
                    break
                else:
                    print("Please input a valid option(1-2)!\n")
        except Exception as e:
            print(f"An error occur in your deposit process: {e}. Please try again!")
        
    def help_us(self):
        os.system('cls')
        while True:
            print("\n********** HELP US *********")
            print("1. Store Policies.")
            print("2. Product Repair.")
            print("3. Shipping and Delivery.")
            print("4. Privacy Policy.")
            print("5. Frequently Question.")
            print("6. Contact information.")
            print("7. Back to main menu.")
            option = input("Enter your choice option: ")
            self.clear_screen()
            if option == "1":
                self.store_policies()
            elif option == "2":
                self.product_repair()
            elif option == "3":
                self.shipping_delivery()
            elif option == "4":
                self.privacy_policy()
            elif option == "5":
                self.user_question()
            elif option == "6":
                self.contact_information()
            elif option == "7":
                self.clear_screen()
                break
            else:
                print("Invalid option. Please try again!")
                continue

    def store_policies(self):
        print("\n---------------Store_Policies---------------")
        print("1. Return & Exchange: You can return or exchange items within 14 days of purchase.")
        print("2. Warranty: All Apple products come with a 1_year warranty.")

    def product_repair(self):
        print("\n---------------Product Repair---------------")
        print("You can request repair for your Apple products by visiting an Apple Store or contacting Apple Support online.")
        print("Make sure your product in covered under warranty or AppleCare.")

    def shipping_delivery(self):
        print("\n---------------Shipping & Delivery---------------")
        print("We offer free shipping for orders over 1500$.")
        print("\nStandard delivery takes 1-2 days before order.")
        print("For expedited shipping, additional fees apply.")
        print("You can select your preferred shipping method at checkout.")

    def privacy_policy(self):
        print("\n---------------Privacy Policy---------------")
        print("Your privacy is important for us. We need only use your personal data for processing orders.")
        print("Read our full privacy policy on our website for more detail.")

    def user_question(self):
        print("\n---------------User FAQs---------------")
        print("Q: How can I reset my password?")
        print("A: Use the 'Forgot Password' option from the main menu.")
        print("\nQ: How can I update my profile details?")
        print("A: YES, go to 'Manage Profile' in the menu.")
        print("\nQ: How do I contact customer service?")
        print("A: Check the 'Contact Information' section for detail.")

    def contact_information(self):

        print("\n---------------Contact Information---------------")
        print("Customer Support Email: apple.store@gmail.iec.com")
        print("Contact Number: +855 123456789")
        print("Website: www.iec.com.kh")

    def edit_profile(self):
        try:
            while True:
                print("\n------------------------------ Edit Profile ------------------------------")
                print("1. Edit Name")
                print("2. Edit Email")
                print("3. Edit Secret Pin")
                print("4. Edit Password")
                print("5. Back")
                option = input("Choose option(1-5): ")
                if option == "1":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------Edit Name------------------------------")
                        new_name = input("Enter your new Name: ")
                        for user in self.users:
                            if user["username"] == new_name:
                                print("Username has exist. Please choose other name!\n")
                                break
                        else:
                            for user in self.users:
                                if user["username"] == self.current_user:
                                    if self.current_user in self.balances:
                                        self.balances[new_name] = self.balances.pop(self.current_user)
                                    
                                    for purchase in self.purchases:
                                        if purchase["username"] == self.current_user:
                                            purchase["username"] = new_name

                                    self.current_user = new_name
                                    user["username"] = self.current_user
                                    print(f"Successfully change Name into {self.current_user}")
                                        
                                    self.save_user()
                                    
                                    with open(self.history_filename, "w") as history_file:
                                        for purchase in self.purchases:
                                            history_file.write(f"username: {purchase['username']}; model: {purchase['model']}; storage: {purchase['storage']}; item: {purchase['item']}; subtotal: {float(purchase['subtotal']):.2f}\n")
                                    
                                    with open(self.balance_filename, "w") as balance_file:
                                        for username, balance in self.balances.items():
                                            balance_file.write((f"username: {username}, balance: {balance}\n"))
                                    break
                        break

                elif option == "2":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------ Edit Email ------------------------------")
                        new_email = input("Enter your new email: ")
                        if '@' in new_email and '.' in new_email: 
                            for user in self.users:
                                if user["email"] == new_email:
                                    print("Email has exist. Please choose other email!\n")
                                    break
                            else:
                                for user in self.users:
                                    if user["username"] == self.current_user and user["email"] != new_email:
                                        user["email"] = new_email
                                        print(f"Successfully change Email into {new_email}")
                            
                                        self.save_user()
                                        break
                        else:
                            print("Invalid email format. Please enter a valid email address.\n")
                            continue           
                        break
                                
                elif option == "3":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------ Edit Secret Pin ------------------------------")
                        old_secret_pin = getpass.getpass("Enter your old 4-digit secret pin: ")
                        hashed_old_secret_pin = self.hash_secret_pin(old_secret_pin)
                        for user in self.users:
                            if user["username"] == self.current_user and user["secret pin"] != hashed_old_secret_pin:
                                print("Wrong secret pin!\n")
                                break
                        else:
                            for user in self.users:
                                if user["username"] == self.current_user and user["secret pin"] == hashed_old_secret_pin:
                                    while True:
                                        new_secret_pin = getpass.getpass("Enter a new 4-digit secret Pin: ")
                                        if len(new_secret_pin) < 4:
                                            print("Secret is too short. Must be a 4-digit number.\n")
                                            continue
                                        if len(new_secret_pin) > 4:
                                            print("Secret is too long. Must be a 4-digit number.\n")
                                            continue
                                        if not new_secret_pin.isdigit():
                                            print("Pin must be a number.\n")
                                            continue
                                        hashed_new_secret_pin = self.hash_secret_pin(new_secret_pin)
                                        user["secret pin"] = hashed_new_secret_pin
                                        print(f"Successfully changed secret pin")
                            
                                        self.save_user()
                                        break
                        break           
                    
                elif option == "4":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------ Edit Password ------------------------------")
                        old_password = getpass.getpass("Enter your old password: ")
                        hashed_old_password = self.hash_password(old_password)
                        for user in self.users:
                            if user["username"] == self.current_user and user["password"] != hashed_old_password:
                                print("Wrong password!\n")
                                break
                        else:
                            for user in self.users:
                                if user["username"] == self.current_user and user["password"] == hashed_old_password:
                                    while True:
                                        new_password = getpass.getpass("Enter a new password: ")
                                        if len(new_password) < 8:
                                            print("Password too short. Must be at least 8 Characters.\n")
                                            continue
                                        if not any(c.isupper()for c in new_password):
                                            print("Password must contain at least one uppercase letter.\n")
                                            continue
                                        if not any(c.islower()for c in new_password):
                                            print("password must contain at least one lowercase letter.\n")
                                            continue
                                        if not any(c.isdigit()for c in new_password):
                                            print("Password must contain at least one digit.\n")
                                            continue
                                        if not any(c in '!@#$%^&*'for c in new_password):
                                            print("Password must contain at least one special character.\n")
                                            continue
                                        confirm_new_password = getpass.getpass("Confirm your Password: ")
                                        if confirm_new_password != new_password:
                                            print("Password do not match. Please try again.\n")
                                            continue
                                        hashed_new_password = self.hash_password(new_password)
                                        user["password"] = hashed_new_password
                                        print(f"Successfully changed password")
                            
                                        self.save_user()
                                        break
                        break
                elif option == "5":
                    self.clear_screen()
                    print("\n")
                    break
                else:
                    print("Please choose a valid option(1-5)!\n")
        except Exception as e:
            print(f"An error occur in your editing process: {e}. Please try again!")

    def manage_profile(self):
        try:
            while True:
                print("\n============================== Manage Profile ==============================")
                print("\n1. View Profile")
                print("2. Edit Profile")
                print("3. Back")
                option = input("Choose Option(1-3): ")
                if option == "1":
                    self.clear_screen()
                    print("\n------------------------------ View Profile ------------------------------")
                    for v in self.users:
                        if v['username'] == self.current_user:
                            print(f"\nName: {v['username']}")
                            print(f"Email: {v['email']}")
                        
                elif option == "2":
                    self.clear_screen()
                    self.edit_profile()
                    continue
                elif option == "3":
                    self.clear_screen()
                    break
                else:
                    print("Invalid option. Please choose option(1-3)!\n")
        except Exception as e:
            print(f"An error occur in your managing process: {e}. Please try again!")

    def browse_item(self):
        self.stock_menu()
        
    def user_menu(self):
        os.system('cls')
        try:
            while True:
                print("============================================================")
                print("|                         Role User                        |")
                print("============================================================")
                print("Menu:")
                print("1. Login")
                print("2. Register")
                print("3. Forgot Password")
                print("4. Help Us")
                print("5. Exit")
                option = input("Choose an option (1-6): ")
                if option == "1":
                    self.clear_screen()
                    self.login()
                    continue
                elif option == "2":
                    self.clear_screen()
                    self.register()
                    continue
                elif option == "3":
                    self.clear_screen()
                    self.forgot() 
                    continue
                elif option == "4":
                    self.clear_screen()
                    self.help_us()
                    continue
                elif option == "5":
                    self.clear_screen()
                    print("Exiting the programs. Goodbye!\n")
                    sys.exit()
                else:
                    print("Invalid option. Please choose an option (1-6)!\n")
                    continue
                
        except Exception as e:
            print(f"an error occur {e}")

    def usage_menu(self):
        os.system('cls')
        try:
            while True:
                print("============================================================")
                print("|                          Role User                       |")
                print("============================================================")
                for user in self.users:
                    if self.current_user == user["username"]:
                        print(f"Welcome, {self.current_user}")
                        print("Usage Menu:")
                        print("1. Browse Item")
                        print("2. Order History")
                        print("3. Manage Balance")
                        print("4. Manage Profile")
                        print("5. Back To Menu")
                        print("6. Help Us")
                        print("7. Exit")
                option = input("Choose an option (1-6): ")
                if option == "1":
                    self.clear_screen()
                    self.browse_item()
                    continue
                elif option == "2":
                    self.clear_screen()
                    self.show_total()
                    continue
                elif option == "3":
                    self.clear_screen()
                    self.manage_balance()
                    continue 
                elif option == "4":
                    self.clear_screen()
                    self.manage_profile()
                    continue
                elif option == "5":
                    self.clear_screen()
                    print("Return back to main menu.\n")
                    self.user_menu()
                    continue
                elif option == "6":
                    self.clear_screen()
                    self.help_us()
                    continue
                elif option == "7":
                    self.clear_screen()
                    print("Exiting the programs. Goodbye!\n")
                    sys.exit()
                else:
                    print("Invalid option. Please choose an option (1-6)!\n")
                    continue
        except Exception as e:
            print(f"An error occur : {e}")


    def show_list(self):
        print(self.balances)
        print(self.users)

###################################### Leap Path ####################################################

fileiphone_staff = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone.txt" 
fileairpod_staff = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\airpod.txt"
filemacbook_staff = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\macbook.txt"
# balance_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/employee_log/customer_balance.txt"

# view stock for users iphone
fileiphone11_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone11_user.txt"
fileiphone12_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone12_user.txt"
fileiphone13_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone13_user.txt"
fileiphone14_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone14_user.txt"
fileiphone15_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\iphone15_user.txt"

# view stock for users mac
mac_m1_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_m1_user.txt"
mac_m2_user = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_m2_user.txt"
mac_pro_14 = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_pro_14.txt"
mac_pro_16 = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\mac_pro_16.txt"

    # view stock for user airpod
airpod_user =r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\airpod_user.txt"

user_file = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\customer_pw.txt"
balance_file = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\customer_balance.txt"
history_file = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\customer_history.txt"
feedback_file = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\feedback.txt"

###################################### Leap Path ####################################################

user1 = User(user_file, balance_file, history_file, feedback_file, fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user)

 ######  ADMIN PART ######

class AdminSystem(AdminEmployee):

    admin_manage = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/admin_manage.txt'
    manage_employ = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/manage_employee.txt'
    system_log = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/system_log.txt'
    employeefile = r"C:\Users\USER\Documents\GitHubLeapp\Python_T1_Y2_Project\Admin_work\inf_employee.txt"

    def __init__(self):
        self.logged_in_username = None
        self.display_admin_account()
        super().__init__(self.add_macbook, self.add_employee, self.add_airpod, 
                        self.add_iphone, self.add_stock, self.log_action, self.admin_log, self.masked_input,
                        self.hash_password, self.verify_password, self.manage_customer_acc, self.delete_customer, self.view_customers,
                        self.recordstock, self.logged_in_username)

    def display_admin_account(self):
        while True:
            try:
                os.system('cls')
                print("\n" + "=" * 30 + " Welcome Admin " + "=" * 30)
                print("\n1. Create Account For Admin")
                print("2. Log in as Admin")
                print("3. Back To Main Menu")

                choose = int(input("Enter ur function to do: "))
                if choose == 1:
                    self.create_admin_account()
                elif choose == 2:
                    self.admin_log()
                elif choose == 3:
                    first = FirstInterface()
                    first.display()
                    # main_menu()
                else:
                    print("Invalid option")
            except ValueError as v:
                print(v)

    def admin_dashboard(self):
        os.system('cls')
        print("\n" + "=" * 40 + " Admin Dashboard " + "=" * 40)
        print("1. 🛠️  Add or Update Stock")
        print("2. 📦  View Stock")
        print("3. ❌  Delete Stock")
        print("4. 👨  Manage Employee Accounts")
        print("5. 🧑‍🤝‍🧑  Manage Customer Accounts")
        print("6. 📊  Sales Report")
        print("7. 📜  History System Log")
        print("8. 🚪  Exit")
        print("=" * 80)

        while True:
            try:
                choose = int(input("\nChoose your task to do: "))
                if choose == 1:
                    self.add_stocks()
                elif choose == 2:
                    self.view_stocks()
                elif choose == 3:
                    self.delete_stocks()
                elif choose == 4:
                    self.manage_employee_acc()
                elif choose == 5:
                    self.manage_customer_acc()
                elif choose == 6:
                    self.sales_report()
                elif choose == 7:
                    self.history_log()
                elif choose == 8:
                    sys.exit(1)
                else:
                    print("Choose a correct option")
            except ValueError as e:
                print(e)

    def get_existing_ids(self):
        existing_ids = set()  # Use a set for faster lookups
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) > 1 and parts[1].startswith("IDTB"):
                        existing_ids.add(parts[1].strip())
            return existing_ids  # Return the set of existing IDs
        except FileNotFoundError:
            return set()  # Return an empty set if the file is missing

    def suggest_available_id(self):
        existing_ids = self.get_existing_ids()  # Fetch the existing IDs
        base_id_prefix = "IDTB"
        available_ids = []

        for i in range(1, 100000):  # Loop through possible ID numbers
            candidate_id = f"{base_id_prefix}{i:04}"  # Generate IDs like IDTB0001, IDTB0002, etc.
            if candidate_id not in existing_ids:
                available_ids.append(candidate_id)  # Add unused IDs to the list
            if len(available_ids) == 5:  # Stop once 5 IDs are generated
                break
        return available_ids  # Return the list of 5 available IDs

    def is_valid_admin_id(self, admin_id):
        # Check if ID starts with 'IDTB' and is not already used
        return admin_id.startswith("IDTB") and admin_id not in self.get_existing_ids()


    def hash_password(self, password):
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def save_admin_to_file(self, admin_account_username, admin_account_id, admin_account_email, hashed_password):
        with open(self.admin_manage, "a") as file:
            file.write(f"{admin_account_username}, {admin_account_id}, {admin_account_email}, {hashed_password}\n")
        print("Admin account created successfully.")

    def create_admin_account(self):
        while True:
            print("Eg: Name: John_Doe")
            admin_account_name = input("Enter admin_account name: ")
            if (
                admin_account_name and "_" in admin_account_name 
                and not any(c.isspace() for c in admin_account_name) 
                and any(c.isupper() for c in admin_account_name) 
                and any (c.islower() for c in admin_account_name) 
                and any(c.islower() for c in admin_account_name) 
                and not any(c in '!@#$%^&*()+=-{}[]'';:,.' for c in admin_account_name)
            ):
                while True:
                    print("Eg: Email: john.doe@admin.iec.com")
                    admin_account_email = input("Enter admin_account email: ")
                    if (
                    "@admin.iec.com" in admin_account_email 
                    and not any(c.isupper() for c in admin_account_email) 
                    and not any(c.isspace() for c in admin_account_email)
                    ):
                        while True:
                            available_ids = self.suggest_available_id()
                            print("Available IDs: ", ", ".join(available_ids))

                            # Prompt the user to select or enter a custom admin ID
                            admin_account_id = input("Enter Admin ID: ").strip()

                            # Validate the entered Admin ID
                            while not self.is_valid_admin_id(admin_account_id):
                                print(f"Error: The Admin ID '{admin_account_id}' is either invalid or already in use.")
                                admin_account_id = input("Please enter a valid Admin ID: ").strip()
                            if self.is_valid_admin_id(admin_account_id):
                                if admin_account_id.startswith("IDTB") and admin_account_id not in self.get_existing_ids():
                                    if self.is_valid_admin_id(admin_account_id):
                                        while True:
                                            admin_account_passwords = input("Create password: ")
                                            if (
                                            len(admin_account_passwords) >= 8
                                            and any(c.isupper() for c in admin_account_passwords)
                                            and any(c.islower() for c in admin_account_passwords)
                                            and any(c.isdigit() for c in admin_account_passwords)
                                            and any(c in "!@#$%^&*()_+-=" for c in admin_account_passwords)
                                            ):
                                                self.log_action("Added new admin_account", "admin_account")
                                                hashed_password = self.hash_password(admin_account_passwords)

                                                # Save admin_account details to file
                                                self.save_admin_to_file(
                                                admin_account_name, 
                                                admin_account_id, 
                                                admin_account_email, 
                                                hashed_password
                                            )
                                                print("Admin account created successfully.")
                                                return
                                            else:
                                                print(
                                                    "Password must contain at least 8 characters, including uppercase, "
                                                    "lowercase, a number, and a special character."
                                                    )
                            else:
                                print("admin_account ID must start with 'IDTB' or ID already exits")
                    else:
                        print("Invalid email format. Ensure it ends with '@admin_account.iec.com' and contains no spaces or uppercase letters.")
            else:
                print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")


    def admin_log(self):
        max_attempts = 3  # Maximum attempts per input
        attempts_remaining = max_attempts  # Remaining attempts for each step

        # Validate username
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            username = input("Enter username: ").strip()

            if self.validate_username(username):
                print("✅ Username validated!")
                break
            else:
                attempts_remaining -= 1
                print("❌ Invalid username.")

        if attempts_remaining == 0:
            print("❌ Too many failed attempts. Logging out.")
            sys.exit()

        # Reset attempts for next input
        attempts_remaining = max_attempts

        # Validate admin ID
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            admin_id_input = input("Enter admin ID: ").strip()

            if self.validate_admin_id(admin_id_input, username):
                print("✅ Admin ID validated!")
                break
            else:
                attempts_remaining -= 1
                print("❌ Invalid admin ID.")

        if attempts_remaining == 0:
            print("❌ Too many failed attempts. Logging out.")
            sys.exit()

        attempts_remaining = max_attempts

        # Validate email
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            email = input("Enter email: ").strip()

            if self.validate_email(email, username):
                print("✅ Email validated!")
                break
            else:
                attempts_remaining -= 1
                print("❌ Invalid email.")

        if attempts_remaining == 0:
            print("❌ Too many failed attempts. Logging out.")
            sys.exit()
        # Reset attempts for next input

        # Reset attempts for next input
        attempts_remaining = max_attempts

        # Validate password
        while attempts_remaining > 0:
            os.system('cls')
            print(f"======= Admin Login =======")
            print(f"Attempts remaining: {attempts_remaining}")
            password = self.take_password()

            if self.validate_password(username, password):
                print("✅ Login successful!")
                self.log_action("Logged in", username)
                self.admin_dashboard()
                return
            else:
                attempts_remaining -= 1
                print("❌ Invalid password.")

        print("❌ Too many failed attempts. Logging out.")
        sys.exit()

    def validate_username(self, username):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                if len(parts) == 4:
                    stored_username, _, _, _ = line.strip().split(', ')
                    if username == stored_username:
                        return True
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    def validate_admin_id(self, admin_id, username):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                if len(parts) == 4:
                    stored_username, stored_id, _, _ = line.strip().split(', ')
                    if username == stored_username and admin_id == stored_id:
                        return True
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    def validate_email(self, email, username):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                if len(parts) == 4:
                    stored_username, _, stored_email, _ = line.strip().split(', ')
                    if username == stored_username and email == stored_email:
                        return True
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    def take_password(self):
        password = ""
        print("Enter password: ", end="", flush=True)
        while True:
            char = msvcrt.getch()
            if char == b'\r':  # Enter key
                break
            elif char == b'\b':  # Backspace
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
            else:
                password += char.decode('utf-8')
                sys.stdout.write("*")
        print()  # Move to the next line after password input
        return password
    
    def validate_password(self, username, password):
        try:
            with open(self.admin_manage, 'r') as file:
                for line in file:
                    stored_username, _, _, stored_hashed_password = line.strip().split(', ')
                    if username == stored_username:
                        return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
            return False
        except FileNotFoundError:
            print("Admin data file is missing.")
            sys.exit(1)

    ##### MANAGE EMPLOYEE PART ######

    def manage_employee_acc(self):
        os.system('cls')
        while True:
            print("\n" + "=" * 30 + " Manage Employee Accounts " + "=" * 30)
            print("1. ➕ Add New Employee")
            print("2. 👀 View Employee Accounts")
            print("3. ❌ Delete Employee Account")
            print("4. 🔙 Back to Main Menu")
            print("=" * 80)

            try:
                choice = int(input("Choose the task: "))
                if choice == 1:
                    self.add_employee()
                elif choice == 2:
                    self.view_employees()
                elif choice == 3:
                    self.delete_employee()
                elif choice == 4:
                    self.admin_dashboard()
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Enter a valid number.")

    def get_existing_id(self):
        existing_id = set()  # Use a set for faster lookups
        try:
            if os.path.exists(self.manage_employ):  # Check if file exists before opening
                with open(self.manage_employ, 'r') as file:
                    for line in file:
                        parts = line.strip().split(', ')
                        if len(parts) > 1 and parts[1].startswith("IDTB"):
                            existing_id.add(parts[1].strip())
            return existing_id  # Return the set of existing IDs
        except FileNotFoundError:
            return set()  # Return an empty set if the file is missing

    def suggest_available_id(self):
        existing_id = self.get_existing_id()  # Fetch the existing IDs
        base_id_prefix = "IDTB"
        available_id = []

        for i in range(1, 100000):  # Loop through possible ID numbers
            candidate_id = f"{base_id_prefix}{i:04}"  # Generate IDs like IDTB0001, IDTB0002, etc.
            if candidate_id not in existing_id:
                available_id.append(candidate_id)  # Add unused IDs to the list
            if len(available_id) == 5:  # Stop once 5 IDs are generated
                break
        return available_id  # Return the list of 5 available IDs

    def is_valid_employee_id(self, employee_account_id):
        # Check if ID starts with 'IDTB' and is not already used
        return employee_account_id.startswith("IDTB") and employee_account_id not in self.get_existing_id()

    def save_employee_to_file(self, employee_account_username, employee_account_id, employee_account_email, hashed_password):
        try:
            with open(self.manage_employ, "a") as file:
                file.write(f"{employee_account_username}, {employee_account_id}, {employee_account_email}, {hashed_password}\n")
            print("Employee account created successfully.")
        except IOError as e:
            print(f"Error saving employee to file: {e}")

    def add_employee(self):
        while True:
            print("Eg: Name: John_Doe")
            employee_account_name = input("Enter employee account name: ")
            if (
                employee_account_name and "_" in employee_account_name 
                and not any(c.isspace() for c in employee_account_name) 
                and any(c.isupper() for c in employee_account_name) 
                and any(c.islower() for c in employee_account_name)
                and not any(c in '!@#$%^&*()+=-{}[]'';:,.' for c in employee_account_name)
            ):
                while True:
                    print("Eg: Email: john.doe@employee.iec.com")
                    employee_account_email = input("Enter employee account email: ")
                    if (
                        "@employee.iec.com" in employee_account_email 
                        and not any(c.isupper() for c in employee_account_email) 
                        and not any(c.isspace() for c in employee_account_email)
                    ):
                        while True:
                            available_id = self.suggest_available_id()
                            print("Available IDs: ", ", ".join(available_id))

                            # Prompt the user to select or enter a custom employee ID
                            employee_account_id = input("Enter Employee ID: ").strip()

                            # Validate the entered Employee ID
                            while not self.is_valid_employee_id(employee_account_id):
                                print(f"Error: The Employee ID '{employee_account_id}' is either invalid or already in use.")
                                employee_account_id = input("Please enter a valid Employee ID: ").strip()
                            
                            if self.is_valid_employee_id(employee_account_id):
                                while True:
                                    employee_account_password = self.masked_input("Create password: ")
                                    if (
                                        len(employee_account_password) >= 8
                                        and any(c.isupper() for c in employee_account_password)
                                        and any(c.islower() for c in employee_account_password)
                                        and any(c.isdigit() for c in employee_account_password)
                                        and any(c in "!@#$%^&*()_+-=" for c in employee_account_password)
                                    ):
                                        hashed_password = self.hash_password(employee_account_password)
                                        # Save employee details to file
                                        self.save_employee_to_file(employee_account_name, employee_account_id, employee_account_email, hashed_password)
                                        return
                                    else:
                                        print(
                                            "Password must contain at least 8 characters, including uppercase, "
                                            "lowercase, a number, and a special character."
                                        )
                            else:
                                print("Employee ID must start with 'IDTB' or ID already exists.")
                    else:
                        print("Invalid email format. Ensure it ends with '@employee.iec.com' and contains no spaces or uppercase letters.")
            else:
                print("Invalid name format. Ensure it contains an underscore (_) and no spaces.")

    def view_employees(self):
        try:
            with open(self.manage_employ, 'r') as file:
                print("\nEmployee Accounts:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No employee data found.")

    def delete_employee(self):
        employee_id = input("Enter the Employee ID to delete: ").strip()

        # Check if the employee ID exists in the file
        employee_found = False
        try:
            with open(self.manage_employ, 'r') as file:
                lines = file.readlines()

            with open(self.manage_employ, 'w') as file:
                for line in lines:
                    # If the ID doesn't match, write the line back to the file
                    if line.split(', ')[1] != employee_id:
                        file.write(line)
                    else:
                        employee_found = True  # Flag that the employee was found and deleted
                        print(f"Employee with ID {employee_id} has been deleted.")

            if not employee_found:
                print(f"Employee ID '{employee_id}' not found.")

        except FileNotFoundError:
            print("No employee data found.")

    ##### MANAGE EMPLOYEE PART ######

    ##### LOG HISTORY ########

    def history_log(self):
        os.system('cls')
        while True:
            print("\n" + "=" * 30 + " System Log " + "=" * 30)
            print("1. 📝 View Logs")
            print("2. 🧹 Clear Logs")
            print("3. 🔙 Back to Main Menu")
            print("=" * 60)

            try:
                option = int(input("Choose an option: "))
                if option == 1:
                    try:
                        with open(self.system_log, 'r') as file:
                            logs = file.readlines()
                        if logs:
                            print("\nSystem Logs:")
                            for log in logs:
                                print(log.strip())
                        else:
                            print("No logs found.")
                    except FileNotFoundError:
                        print("System log file not found.")
                elif option == 2:
                    confirm = input("Are you sure you want to clear all logs? (yes/no): ").lower()
                    if confirm == 'yes':
                        with open(self.system_log, 'w') as file:
                            pass
                        print("Logs cleared.")
                        self.log_action("Cleared system logs", "Admin")
                    else:
                        print("Clear logs cancelled.")
                elif option == 3:
                    self.admin_dashboard()
                else:
                    print("Invalid option.")
            except ValueError:
                print("Enter a valid number.")
    
    ######  ADMIN PART ######

    def view_stocks(self):
        os.system('cls')
        while True:
            print("\n" + "=" * 50)
            print("📦  View Stock Menu  📦".center(50))
            print("=" * 50)
            print("1️⃣  iPhone")
            print("2️⃣  MacBook")
            print("3️⃣  AirPod")
            print("4️⃣  🔙 Exit to Main Menu")
            print("=" * 50)

            choice = input("Enter the model to add (1/2/3/4): ")
            if choice == "1":
                self.view_iphone()
            elif choice == "2":
                self.view_macbook()
            elif choice == "3":
                self.view_airpod()
            elif choice == "4":
                self.admin_dashboard()
            else:
                print("Invalid choice. Please try again.")

    def add_stocks(self): #add stock
        os.system('cls')
        while True:
            print("\n" + "=" * 50)
            print("📈  Add Stock Menu  📈".center(50))
            print("=" * 50)
            print("1️⃣  Add iPhone")
            print("2️⃣  Add MacBook")
            print("3️⃣  Add AirPod")
            print("4️⃣  🔙 Exit to Employee Tasks")
            print("=" * 50)
            choice = input("Enter the model to add (1/2/3): ")
            if choice == "1":
                self.add_iphone()
            elif choice == "2":
                self.add_macbook()
            elif choice == "3":
                self.add_airpod()
            elif choice == "4":
                self.admin_dashboard()
            else:
                print("Invalid choice. Please try again.")

    def delete_stocks(self): #delete stock
        os.system('cls')
        while True:
            print("\n" + "=" * 50)
            print("🗑️  Delete Stock Menu  🗑️".center(50))
            print("=" * 50)
            print("1️⃣  Remove iPhone")
            print("2️⃣  Remove MacBook")
            print("3️⃣  Remove AirPods")
            print("4️⃣  🔙 Back to Menu")
            print("=" * 50)
            
            choice = input("Enter the model to remove (1/2/3): ")
            if choice == "1":
                self.remove_iphone()
            elif choice == "2":
                self.remove_macbook()
            elif choice == "3":
                self.remove_airpod()
            elif choice == "3":
                self.admin_dashboard()
            elif choice == "4":
                self.admin_dashboard()
            else:
                print("Invalid choice. Please try again.")

interface = FirstInterface()
interface.display()