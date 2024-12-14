import ast, os, sys
import hashlib
import getpass
import sys
import platform

class Stock:
    
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
        # self.exit = False
        self.purchases = []
        # self.history_filename = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/customer_history.txt"
    # for employee to view the stock
    # def view_stock(self):
    #     print(self.iphone)
    #     print(self.airpod)
    #     print(self.macbook)
    
    # for user to view the stock of iphone
    
    # def add_to_total(self, item, model, storage, total_cost):
    #     try:
    #         self.total_amount += float(total_cost)
    #         purchase = {
    #             "username": user1.current_user,
    #             "model" : model,
    #             "storage" : storage,
    #             "item" : item,
    #             "subtotal" : total_cost
    #         }
    #         self.purchases.append(purchase)
    #         self.save_purchase(purchase)
    #     except ValueError as e:
    #         print(f"[ERROR] Failed to add to total_amount: {e}")

<<<<<<< HEAD
=======
    # def save_purchase(self, purchase):
    #     try:
    #         with open(user1.history_filename, "a") as file:
    #             file.write(str(purchase) + "\n")
    #     except Exception as e:
    #         print(f"Error saving purchase to file {e}.")
            
    # def load_purchase(self):
    #     try:
    #         with open(self.history_filename, "r") as file:
    #             for line in file:
    #                 record = eval(line.strip())
    #                 if record["username"] == self.current_user:
    #                     self.purchases.append(record)
    #                     self.total_amount += record["subtotal"]
    #     except FileNotFoundError:
    #         pass
    #     except IOError:
    #         print("Error loading purchase history from file.")

>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
    # def show_total(self):
        
    #     print("="*80)
    #     print("\t\t\t\tYour Purchase:")
    #     print("="*80)
<<<<<<< HEAD
=======
    #     dynamic_total = 0
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
    #     for purchase in self.purchases:
    #         model = purchase["model"]
    #         storage = purchase["storage"]
    #         item = purchase["item"]
    #         subtotal = purchase["subtotal"]
    #         print(f"{item}x {model} ({storage}): ${subtotal:.2f}")  
<<<<<<< HEAD
    #     print(f"Total amount of purchases: ${self.total_amount:.2f}")
=======
    #         dynamic_total += subtotal 
    #     print(f"Total amount of purchases: ${dynamic_total:.2f}")
        
    def clear_screen(self):
        current_os = platform.system()

        if current_os == "Windows":
            os.system('cls')  # Windows command to clear the screen
        else:
            os.system('clear')
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
        
    def iphone_menu(self):      
        # Menu bar for user
        while True:
            print("="*80)
            print("\t\t\t\tModel iPhone:")
            print("="*80)
            print("1.iPhone11")
            print("2.iPhone12")
            print("3.iPhone13")
            print("4.iPhone14")
            print("5.iPhone15")
            print("6.Back to menu")
            choice = input("Option:").strip()
            if choice == "1":
                try: 
                    with open(self.fileiphone11_user, "r") as file:
                        content = file.read()
                        print(content)
<<<<<<< HEAD
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        
                        if user_buy == "yes" or user_buy == "y":
                            model_key = "iphone_11"
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
                                                value = "$599"
                                                break
                                                # print(value)
                                            elif storage == "128" :
                                                # print("$699")
                                                value = "$699"
                                                break
                                                # print(value)
                                            elif storage == "256" :
                                                # print("$799")
                                                value = "$799"
                                                break
                                                # print(value)
                                            else:
                                                print("Invalid storage option.")
                                                return
                                except FileNotFoundError:
                                    print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            item = int(input("Items:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            
                            if confirm == "yes" or confirm == "y":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.fileiphone_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key}:{storage_key} is out of stock.")

                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
<<<<<<< HEAD
                            item = int(input("Items:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.fileiphone_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key};{storage_key} is out of stock.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
<<<<<<< HEAD
                                            print("Invalid storage option.")
                                            return
                            except FileNotFoundError:
                                print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            item = int(input("Items:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.fileiphone_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key}:{storage_key} is out of stock.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
                                            print("Insufficient balance.")
                                        return
                                    elif confirm == "no" or confirm == "n":
                                        print("Purchase canceled.")
                                        self.iphone_menu()
                                    else:
                                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                            elif user_buy == "no" or user_buy == "n":
                                print("Thank for viewing our stock!")
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
<<<<<<< HEAD
                                                print("Invalid storage option.")
                                                return
                                except FileNotFoundError:
                                        print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            item = int(input("Items:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.fileiphone_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key}:{storage_key} is out of stock.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
<<<<<<< HEAD
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
                            item = int(input("Items:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.fileiphone_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key}:{storage_key} is out of stock.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
<<<<<<< HEAD
        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
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
                os.system("cls")
                return
            confirm = input("Confirm your buy(yes,no):").strip().lower()
            if confirm == "yes" or confirm == "y":
                item = int(input("Item:"))
                try:
                    with open(self.fileairpod_staff, "r") as file:
                        stock_data = ast.literal_eval(file.read())
                            # stock_data = ast.literal_eval(content)
                    if choice_key in stock_data:
                        if stock_data[choice_key] >= item:
                            stock_data[choice_key] -=item
                            # print(f"Purchase successful! Remaining stock for {choice_key} : {stock_data[choice_key]}")
                            with open(self.fileairpod_staff, "w") as file: 
                                file.write(str(stock_data))
                                self.add_to_total(value, item, choice_key, None)
                                user1.calculate()
                        else:
                            print(f"Sorry, {choice_key} is out of stock.")
                except FileNotFoundError:
                    print(f"The file {self.fileairpod_staff} was not found. Please ensure it exists in the correct directory.")
            elif confirm == "no" or confirm == "n":
                print("Purchase canceled.")
                self.airpod_menu()
=======
        while True:
            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
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
                    os.system("cls")
                    return
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
                        self.airpod_menu()
                        return
                    else:
                        print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")    
            elif user_buy == "no" or user_buy == "n":
                print("Thank for viewing our stock!")
                self.stock_menu()
                return
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
            else:
                print("Invalid output. Please enter 'yes', 'y', 'no', or 'n'.")
                user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
    # for user to view the stock of macbook
    def macbook_menu(self):
        while True:
            print("="*80)
            print("\t\t\t\tModel Mac:")
            print("="*80)
            print("1.M1")
            print("2.M2")
            print("3.Pro_14inch")
            print("4.Pro_16inch")
            print("5.Back to menu")
            choice = input("Option:")
            if choice == "1":
                # print("Model:Mac_M1")
                try:
                    with open(self.mac_m1_user,"r") as file:
                        content = file.read()
                        # print("Stock:")
                        print(content)
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
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
<<<<<<< HEAD
                                                print("Invalid storage option.")
                                                return
                                except FileNotFoundError:
                                    print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")     
                            item = int(input("Item:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.filemacbook_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key}:{storage_key} is out of stock.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes":
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
<<<<<<< HEAD
                                                print("Invalid storage option.")
                                                return
                                except FileNotFoundError:
                                    print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                            item = int(input("Item:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes":
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.filemacbook_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
                                else:
                                    print(f"Sorry, {model_key}:{storage_key} is out of stock.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes":
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
<<<<<<< HEAD
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
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
                            item = int(input("Item:"))
                            confirm = input("Confirm your buy(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                # user1.calculate()
                                if  stock_data[model_key][storage_key] >= item:
                                    stock_data[model_key][storage_key] -= item
                                    # print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                    with open(self.filemacbook_staff, "w") as file: 
                                        file.write(str(stock_data))
                                        self.add_to_total(value, item, model_key, storage_key)
                                        user1.calculate()
=======
                        while True:
                            user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                            if user_buy == "yes":
                                model_key = "MacBook_Pro_16inch"
                                storage = input("Storage(1(TB)/512):")
                                if storage == "1":
                                    storage_key = f"{storage}TB" 
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
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
        while True:
            print("="*80)
            print("\t\t\t\tStock Display:")
            print("="*80)
            print("1.iPhone")
            print("2.Airpod")
            print("3.Macbook")
            print("4.View Total")
            print("5.Back to usage menu")
            print("6.Exit")
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

# view stock for staff 
# fileiphone_staff = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone.txt'
# fileairpod_staff = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/airpod.txt'
# filemacbook_staff = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/macbook.txt'
# fileiphone_staff = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone.txt" 
# fileairpod_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/airpod.txt"
# filemacbook_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/macbook.txt"
# <<<<<<< HEAD:Employees/stock.py
# =======
# <<<<<<< HEAD:Admin_work/stock.py
# fileiphone_staff = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone.txt'
# fileairpod_staff = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/airpod.txt'
# filemacbook_staff = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/macbook.txt'
# =======
# fileiphone_staff = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone.txt" 
# fileairpod_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/airpod.txt"
# filemacbook_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/macbook.txt"
# >>>>>>> a2935373dad76e4f7e2e620d8a408a9a84d6003b:Employees/stock.py

# # view stock for users iphone
# fileiphone11_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone11_user.txt'
# fileiphone12_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone12_user.txt'
# fileiphone13_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone13_user.txt'
# fileiphone14_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone14_user.txt'
# fileiphone15_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/iphone15_user.txt'

# # view stock for users mac
# mac_m1_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_m1_user.txt'
# mac_m2_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_m2_user.txt'
# mac_pro_14 = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/mac_pro_14.txt'
# mac_pro_16 = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\mac_pro_16.txt'

# # view stock for user airpod
# airpod_user = r'C:\/Users\/USER\/Documents\/GitHubLeapp\/Python_T1_Y2_Project\/Admin_work\/airpod_user.txt'

# stock = Stock(fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user)
# >>>>>>> origin/main:Admin_work/stock.py

# stock.view_stock()
# if __name__ == "__main": 

# stock.total_amount()


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
            with open(user1.history_filename, "a") as file:
                file.write(str(purchase) + "\n")
        except Exception as e:
            print(f"Error saving purchase to file {e}.")
            
    def load_purchase(self):
        try:
            with open(self.history_filename, "r") as file:
                for line in file:
                    record = eval(line.strip())
                    self.purchases.append(record)
                    self.total_amount += record["subtotal"]
        except FileNotFoundError:
            pass
        except IOError:
            print("Error loading purchase history from file.")

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
<<<<<<< HEAD
        if self.current_user in self.balances:  # Ensure the user exists in balances
            if self.balances[self.current_user] >= self.total_amount:  # Check sufficient balance
                self.balances[self.current_user] -= self.total_amount  # Deduct total amount
                print(f"New balance: {self.balances[self.current_user]}")
                with open(self.balance_filename, "w") as balance_file:
                    for username, balance in self.balances.items():
                        balance_file.write(f"username: {username}, balance: {balance}\n")
=======
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
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
            else:
                print("Insufficient balance.")
        else:
            print("User not found.")

    def show_total(self):
        
        print("="*80)
        print("\t\t\t\tYour Purchase:")
        print("="*80)
        for purchase in self.purchases:
            model = purchase["model"]
            storage = purchase["storage"]
            item = purchase["item"]
            subtotal = purchase["subtotal"]
            print(f"{item}x {model} ({storage}): ${subtotal:.2f}")  
        print(f"Total amount of purchases: ${self.total_amount:.2f}")
        

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
                                key, value = part .split(": ")
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
                    print("\n==============================Register==============================")
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
                print("\n==============================Login==============================")
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
            print("\n==============================Forgot==============================")
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
                print("\n==============================Manage Balance==============================")
                print(f"\nYour current balance: ${self.balances[self.current_user]}")
                print("1. Deposit Balance")
                print("2. Back")
                option = input("Choose Option(1,2): ")
                if option == "1":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------Deposit Balance------------------------------")
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
        self.clear_screen()
        while True:
            print("\n------------------------------Help Us------------------------------")
            print("1. Provide feedback.")
            print("2. Frequently ask questions.")
            print("3. Contact information.")
            print("4. Back to main menu.")
            option = input("Enter your choice (1-4): ")
            if option == "1":
                self.clear_screen()
                self.provide_feedback()
                continue
            elif option == "2":
                self.clear_screen()
                self.user_question()
                continue
            elif option == "3":
                self.clear_screen()
                self.contact_information()
                continue
            elif option == "4":
                self.clear_screen()
                break
            else:
                print("Invalid option. Please try again!")
                continue

    def provide_feedback(self):
        print("\n------------------------------Provide Feedback------------------------------")
        try:
            username = input("Enter your username: ").strip()
            if not username:
                raise ValueError("User name cannot empty")
            feedback = input("Enter your feedback: ").strip()
            if not feedback:
                raise ValueError("Feedback connot empty.")
            with open('Customer/feedback.txt', 'a') as file:
                file.write(f"Username: {username}, Feedback: {feedback}\n")
            print("Thank you for your feedback!")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    def user_question(self):
        print("\n------------------------------User FAQs------------------------------")
        print("Q: How can I reset my password?")
        print("A: Use the 'Forgot Password' opption from the main menu.")
        print("\nQ: Can I update my profile details?")
        print("A: YES, go to 'Manage Profile' in the menu.")
        print("\nQ: How do I contact customer service?")
        print("A: Check the 'Contact Information' section for detail.")

    def contact_information(self):
        print("\n------------------------------Contact Information------------------------------")
        print("Customer Support Email: support@gmail.iec.com")
        print("Contact Number: +855 123456789")
        print("Website: www.iec.com.kh")

    def edit_profile(self):
        try:
            while True:
                print("\n------------------------------Edit Profile------------------------------")
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
                                    self.current_user = new_name
                                    user["username"] = self.current_user
                                    print(f"Successfully change Name into {self.current_user}")
                                        
                                    self.save_user()
                                    break
                        break
                elif option == "2":
                    while True:
                        self.clear_screen()
                        print("\n------------------------------Edit Email------------------------------")
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
                        print("\n------------------------------Edit Secret Pin------------------------------")
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
                        print("\n------------------------------Edit Password------------------------------")
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
                print("\n==============================Manage Profile==============================")
                print("\n1. View Profile")
                print("2. Edit Profile")
                print("3. Back")
                option = input("Choose Option(1-3): ")
                if option == "1":
                    self.clear_screen()
                    print("\n------------------------------View Profile------------------------------")
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
<<<<<<< HEAD
        user1 .stock_menu()
        user1.iphone_menu()
        

    def place_order(self):
        
        user1.iphone_menu()
        user1.airpod_menu()
        user1.macbook_menu()
        
    def order_history(self):
        user1.show_total()
        pass
=======
        self.stock_menu()
        
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
    def user_menu(self):
        try:
            while True:
                print("============================================================")
                print("|                         Role User                        |")
                print("============================================================")
                print("Menu:")
                print("1. Login")
                print("2. Register")
                print("3. Forgot Password")
                print("4. Back")
                print("5. Help Us")
                print("6. Exit")
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
                    print("Return back to Role.\n")
                    continue
                elif option == "5":
                    self.clear_screen()
                    self.help_us()
                    continue
                elif option == "6":
                    self.clear_screen()
                    print("Exiting the programs. Goodbye!\n")
                    sys.exit()
                else:
                    print("Invalid option. Please choose an option (1-6)!\n")
                    continue
                
        except Exception as e:
            print(f"an error occur {e}")

    def usage_menu(self):
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
<<<<<<< HEAD
        print(self.users)
        
        
import ast
import msvcrt
from datetime import datetime
=======
        print(self.balances)
        print(self.users)
user_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/customer_pw.txt"
balance_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/customer_balance.txt"
history_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/customer_history.txt"
feedback_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/feedback.txt"
fileiphone_staff = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone.txt" 
fileairpod_staff = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/airpod.txt"
filemacbook_staff = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/macbook.txt"
>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800



# stockmanager = StockManager(fileiphone_staff,fileairpod_staff,filemacbook_staff)

# stockmanager.main_menu()


# stockmanager = StockManager(fileiphone_staff,fileairpod_staff,filemacbook_staff)
# stockmanager.main_menu()

# user_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/employee_log/customer_pw.txt"

fileiphone_staff = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone.txt" 
fileairpod_staff = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/airpod.txt"
filemacbook_staff = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/macbook.txt"
# balance_file = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/employee_log/customer_balance.txt"

# view stock for users iphone
fileiphone11_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone11_user.txt"
fileiphone12_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone12_user.txt"
fileiphone13_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone13_user.txt"
fileiphone14_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone14_user.txt"
fileiphone15_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/iphone15_user.txt"

    # view stock for users mac
mac_m1_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/mac_m1_user.txt"
mac_m2_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/mac_m2_user.txt"
mac_pro_14 = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/mac_pro_14.txt"
mac_pro_16 = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/mac_pro_16.txt"

    # view stock for user airpod
airpod_user = "C:/Users/KORNG/OneDrive - Cambodia Academy of Digital Technology/Documents/GitHub/Python_T1_Y2_Project/Admin_work/airpod_user.txt"

# stock = Stock()
# stock.stock_menu()
# user_file = "/Users/savonchanserey/Desktop/my-repo/employee_log/customer_pw.txt"
# balance_file = "/Users/savonchanserey/Desktop/my-repo/employee_log/customer_balance.txt"
# history_file = "/Users/savonchanserey/Desktop/my-repo/Admin_work/customer_history.txt"

# fileiphone_staff = "/Users/savonchanserey/Desktop/my-repo/Admin_work/iphone.txt" 
# fileairpod_staff = "/Users/savonchanserey/Desktop/my-repo/Admin_work/airpod.txt"
# filemacbook_staff = "/Users/savonchanserey/Desktop/my-repo/Admin_work/macbook.txt"

# #     # view stock for users iphone
# fileiphone11_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/iphone11_user.txt"
# fileiphone12_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/iphone12_user.txt"
# fileiphone13_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/iphone13_user.txt"
# fileiphone14_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/iphone14_user.txt"
# fileiphone15_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/iphone15_user.txt"

# #     # view stock for users mac
# mac_m1_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/mac_m1_user.txt"
# mac_m2_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/mac_m2_user.txt"
# mac_pro_14 = "/Users/savonchanserey/Desktop/my-repo/Admin_work/mac_pro_14.txt"
# mac_pro_16 = "/Users/savonchanserey/Desktop/my-repo/Admin_work/mac_pro_16.txt"

# # #     # view stock for user airpod
# airpod_user = "/Users/savonchanserey/Desktop/my-repo/Admin_work/airpod_user.txt"



user1 = User(user_file, balance_file, history_file, feedback_file, fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user)

# user1.show_list()
user1.user_menu()
<<<<<<< HEAD
stockmanager.employee_login()
=======
# stockmanager.employee_login()


>>>>>>> ba1948982b5cf930b9af9b0483aed82435d68800
