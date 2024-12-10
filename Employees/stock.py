import ast, os

class Stock:
    
    def __init__(self,fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user):
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
        self.total_amount = 0
        self.exit = False
    # for employee to view the stock
    # def view_stock(self):
    #     print(self.iphone)
    #     print(self.airpod)
    #     print(self.macbook)
    
    # for user to view the stock of iphone
    
    
    def add_to_total(self, value):
        try:
            price = float(value.replace("$", ""))  
            self.total_amount += price
        except ValueError:
            print("Invalid price format.")

    def show_total(self):
        print("="*80)
        print("\t\t\t\tYour Purchase:")
        print("="*80)
        print(f"Total amount of purchases: ${self.total_amount:.2f}")
        
    def iphone_menu(self):      
        # Menu bar for user
        while not self.exit:
            print("="*80)
            print("\t\t\t\tModel iPhone:")
            print("="*80)
            print("1.iPhone11")
            print("2.iPhone12")
            print("3.iPhone13")
            print("4.iPhone14")
            print("5.iPhone15")
            print("6.Back to menu")
            choice = input("Model:").strip()
            if choice == "1" : 
                print("Model:iPhone_11")
                try: 
                    with open(self.fileiphone11_user,"r") as file:
                        content = file.read()
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes" or user_buy == "y":
                            model_key = "iphone_11"
                            storage = input("Storage:")
                            if storage == "64" :
                                # print("$599")
                                value = "$599"
                                print(value)
                            elif storage == "128" :
                                # print("$699")
                                value = "$699"
                                print(value)
                            elif storage == "256" :
                                # print("$799")
                                value = "$799"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                try:
                                    with open(self.fileiphone_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                            else:
                                                print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no" or user_buy == "n":
                            print("Thank for viewing our stock!")
                            self.iphone_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.fileiphone11_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "2" :
                print("Model:iPhone_12")
                try: 
                    with open(self.fileiphone12_user,"r") as file:
                        content = file.read()
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "iphone_11"
                            storage = input("Storage:")
                            if storage == "64" :
                                # print("$599")
                                value = "$699"
                                print(value)
                            elif storage == "128" :
                                # print("$699")
                                value = "$799"
                                print(value)
                            elif storage == "256" :
                                # print("$799")
                                value = "$899"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.fileiphone_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                            else:
                                                print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.iphone_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.fileiphone12_user} was not found. Please ensure it exists in the correct directory.")
                    return

            elif choice == "3" :
                print("Model:iPhone_13")
                try: 
                    with open(self.fileiphone13_user,"r") as file:
                        content = file.read()
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "iphone_11"
                            storage = input("Storage:")
                            if storage == "128" :
                                # print("$599")
                                value = "$799"
                                print(value)
                            elif storage == "256" :
                                # print("$699")
                                value = "$899"
                                print(value)
                            elif storage == "512" :
                                # print("$799")
                                value = "$999"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.fileiphone_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                            else:
                                                print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.iphone_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.fileiphone13_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "4" :
                print("Model:iPhone_14")
                try: 
                    with open(self.fileiphone14_user,"r") as file:
                        content = file.read()
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "iphone_11"
                            storage = input("Storage:")
                            if storage == "128" :
                                # print("$599")
                                value = "$899"
                                print(value)
                            elif storage == "256" :
                                # print("$699")
                                value = "$999"
                                print(value)
                            elif storage == "1" :
                                # print("$799")
                                value = "1099"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            if storage == "1":
                                storage_key = f"{storage}TB"
                            else:
                                storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.fileiphone_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                            else:
                                                print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.iphone_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.fileiphone14_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "5" :
                print("Model:iPhone_15")
                try: 
                    with open(self.fileiphone15_user,"r") as file:
                        content = file.read()
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "iphone_11"
                            storage = input("Storage:")
                            if storage == "128" :
                                # print("$599")
                                value = "$999"
                                print(value)
                            elif storage == "256" :
                                # print("$699")
                                value = "$1199"
                                print(value)
                            elif storage == "1" :
                                # print("$799")
                                value = "1299"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            if storage == "1":
                                storage_key = f"{storage}TB"
                            else:
                                storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.fileiphone_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.fileiphone_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                            else:
                                                print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.fileiphone_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.iphone_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.fileiphone15_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "6":
                os.system("clear")
                self.stock_menu()
                break
            else:
                print("No such model exists.")
                return   
            
    def airpod_menu(self):
        
        try:
            with open(self.airpod_user,"r") as file:
                content = file.read()
                print("Stock AirPods:")
                print(content)
        except FileNotFoundError:
            print(f"The file {self.airpod_user} was not found. Please ensure it exists in the correct directory.")
            return
        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
        if user_buy == "yes" or user_buy == "y":
            choice = input("Choose your model:(Gen,Pro,Max):")
            if choice == "Gen":
                # print("Price:$159")
                value = "$159"
                print(value)
                choice_key = "Airpods_2nd_Gen"
            elif choice == "Pro":
                # print("Price:$249")
                value = "$249"
                print(value)
                choice_key = "Airpods_Pro"
            elif choice == "Max":
                # print("Price:$549")
                value = "$549"
                print(value)
                choice_key = "Airpods_Max"
            else:
                print(f"{choice} doesn't has in our stock.")
                os.system("clear")
                return
            confirm = input("Confirm your buy:(yes,no):").strip().lower()
            if confirm == "yes" or confirm == "y":
                try:
                    with open(self.fileairpod_staff, "r") as file:
                        stock_data = ast.literal_eval(file.read())
                            # stock_data = ast.literal_eval(content)
                    if choice_key in stock_data:
                        if stock_data[choice_key] > 0:
                            stock_data[choice_key] -=1
                            print(f"Purchase successful! Remaining stock for {choice_key} : {stock_data[choice_key]}")
                            with open(self.fileairpod_staff, "w") as file: 
                                file.write(str(stock_data))
                                self.add_to_total(value)
                        else:
                            print(f"Sorry, {choice_key} is out of stock.")
                except FileNotFoundError:
                    print(f"The file {self.fileairpod_staff} was not found. Please ensure it exists in the correct directory.")
            elif confirm == "no" or confirm == "n":
                print("Purchase canceled.")
            else:
                print("Invalid confirmation input.")
        elif user_buy == "no" or user_buy == "n":
            print("Thank for viewing our stock!")
        self.stock_menu()
    # for user to view the stock of macbook
    def macbook_menu(self):
        while not self.exit:
            print("="*80)
            print("\t\t\t\tModel Mac:")
            print("="*80)
            print("1.M1")
            print("2.M2")
            print("3.Pro_14inch")
            print("4.Pro_16inch")
            print("5.Back to menu")
            choice = input("Choose model:")
            if choice == "1":
                print("Model:Mac_M1")
                try:
                    with open(self.mac_m1_user,"r") as file:
                        content = file.read()
                        print("Stock iPhone:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes" or user_buy == "y":
                            model_key = "MacBook_Air_M1"
                            storage = input("Storage:")
                            if storage == "256" :
                                # print("$999")
                                value = "$999"
                                print(value)
                            elif storage == "512" :
                                # print("$1249")
                                value = "$1249"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            if storage == "1":
                                storage_key = f"{storage}TB" 
                            else:
                                storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes" or confirm == "y":
                                try:
                                    with open(self.filemacbook_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                                # print(f"Purchase:\n{model_key}:{model_key[storage_key]}")
                                    else:
                                        print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no" or confirm == "n":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no" or user_buy == "n":
                            print("Thank for viewing our stock!")
                            self.macbook_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.mac_m1_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "2":
                print("Model:Mac_M2")
                try:
                    with open(self.mac_m2_user,"r") as file:
                        content = file.read()
                        print("Stock iPhone:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "MacBook_Air_M1"
                            storage = input("Storage:")
                            if storage == "256" :
                                # print("$999")
                                value = "$999"
                                print(value)
                            elif storage == "512" :
                                # print("$1249")
                                value = "$1249"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            if storage == "1":
                                storage_key = f"{storage}TB" 
                            else:
                                storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.filemacbook_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                                # print(f"Purchase:\n{model_key}:{model_key[storage_key]}")
                                    else:
                                        print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.macbook_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.mac_m2_user} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "3":
                print("Model:Mac_Pro_14")
                try:
                    with open(self.mac_pro_14,"r") as file:
                        content = file.read()
                        print("Stock iPhone:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "MacBook_Air_M1"
                            storage = input("Storage:")
                            if storage == "256" :
                                # print("$999")
                                value = "$999"
                                print(value)
                            elif storage == "512" :
                                # print("$1249")
                                value = "$1249"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            if storage == "1":
                                storage_key = f"{storage}TB" 
                            else:
                                storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.filemacbook_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                                # print(f"Purchase:\n{model_key}:{model_key[storage_key]}")
                                    else:
                                        print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.macbook_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.mac_pro_14} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "4":
                print("Model:Mac_Pro_16")
                try:
                    with open(self.mac_pro_16,"r") as file:
                        content = file.read()
                        print("Stock iPhone:")
                        print(content)
                        user_buy = input("Do you interesting in our product?If you want to buy(yes),if not(no):").lower()
                        if user_buy == "yes":
                            model_key = "MacBook_Air_M1"
                            storage = input("Storage:")
                            if storage == "256" :
                                # print("$999")
                                value = "$999"
                                print(value)
                            elif storage == "512" :
                                # print("$1249")
                                value = "$1249"
                                print(value)
                            else:
                                print("Invalid storage option.")
                                return
                            if storage == "1":
                                storage_key = f"{storage}TB" 
                            else:
                                storage_key = f"{storage}GB"
                            confirm = input("Confirm your buy:(yes,no):").strip().lower()
                            if confirm == "yes":
                                try:
                                    with open(self.filemacbook_staff, "r") as file:
                                        content = file.read()
                                        stock_data = ast.literal_eval(content)
                                    if model_key in stock_data:
                                        if storage_key in stock_data[model_key]:
                                            if  stock_data[model_key][storage_key] > 0:
                                                stock_data[model_key][storage_key] -= 1
                                                print(f"Purchase successful! Remaining stock for {model_key} ({storage_key}): {stock_data[model_key][storage_key]}")
                                                with open(self.filemacbook_staff, "w") as file: 
                                                    file.write(str(stock_data))
                                                    self.add_to_total(value)
                                                # print(f"Purchase:\n{model_key}:{model_key[storage_key]}")
                                    else:
                                        print(f"Sorry, {model_key} is out of stock.")
                                except FileNotFoundError:
                                    print(f"The file {self.filemacbook_staff} was not found. Please ensure it exists in the correct directory.")
                            elif confirm == "no":
                                print("Purchase canceled.")
                            else:
                                print("Invalid confirmation input.")
                        elif user_buy == "no":
                            print("Thank for viewing our stock!")
                            self.macbook_menu()
                        else:
                            print("Invalid output.")
                except FileNotFoundError:
                    print(f"The file {self.mac_pro_16} was not found. Please ensure it exists in the correct directory.")
                    return
            elif choice == "5":
                os.system("clear")
                self.stock_menu()
                break
            else:
                print("No such model exists.")
                return   
    # let user input
    def stock_menu(self):
        while not self.exit:
            print("="*80)
            print("\t\t\t\tStock Display:")
            print("="*80)
            print("1.iPhone")
            print("2.Airpod")
            print("3.Macbook")
            print("4.View Total")
            print("5.Exit")
            option = input("Option:")
            if option == "1":
                os.system("clear")
                self.iphone_menu()
            elif option == "2":
                os.system("clear")
                self.airpod_menu()
            elif option == "3":
                os.system("clear")
                self.macbook_menu()
            elif option == "4":
                os.system("clear")
                self.show_total()
            elif option == "5":
                print("Exit the stock!")
                self.exit = True
            else:
                print("Invalid option, please choose again.")

# view stock for staff 

# stock.view_stock()
# if __name__ == "__main": 
fileiphone_staff = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone.txt" 
fileairpod_staff = "/Users/savonchanserey/Desktop/my-repo/Employees/airpod.txt"
filemacbook_staff = "/Users/savonchanserey/Desktop/my-repo/Employees/macbook.txt"

    # view stock for users iphone
fileiphone11_user = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone11_user.txt"
fileiphone12_user = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone12_user.txt"
fileiphone13_user = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone13_user.txt"
fileiphone14_user = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone14_user.txt"
fileiphone15_user = "/Users/savonchanserey/Desktop/my-repo/Employees/iphone15_user.txt"

    # view stock for users mac
mac_m1_user = "/Users/savonchanserey/Desktop/my-repo/Employees/mac_m1_user.txt"
mac_m2_user = "/Users/savonchanserey/Desktop/my-repo/Employees/mac_m2_user.txt"
mac_pro_14 = "/Users/savonchanserey/Desktop/my-repo/Employees/mac_pro_14.txt"
mac_pro_16 = "/Users/savonchanserey/Desktop/my-repo/Employees/mac_pro_16.txt"

    # view stock for user airpod
airpod_user = "/Users/savonchanserey/Desktop/my-repo/Employees/airpod_user.txt"

stock = Stock(fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user)
stock.stock_menu()

# stock.total_amount()