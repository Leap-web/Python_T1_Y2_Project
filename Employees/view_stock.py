import ast

class StockManager:
    def __init__(self,fileiphone_staff,fileairpod_staff,filemacbook_staff):
        self.fileiphone_staff = fileiphone_staff
        self.fileairpod_staff = fileairpod_staff
        self.filemacbook_staff = filemacbook_staff

    def main_menu(self):
        while True:
            print("*" * 50)
            print("Main Menu:")
            print("1. Change Stock\n2. Do Report\n3. Exit Program")
            print("*" * 50)

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.stock_menu()
            elif choice == "2":
                self.generate_report()
            elif choice == "3":
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def stock_menu(self):
        while True:
            print("=" * 50)
            print("Stock Management:")
            print("1. Add Stock\n2. Delete Stock\n3. Exit to Main Menu")
            print("=" * 50)
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_stock()
            elif choice == "2":
                self.delete_stock()
            elif choice == "3":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_stock(self):
        # file_path = self.get_file_path()
        print("1.iPhone")
        print("2.Macbook")
        print("3.Airpod")
        choice = input("Enter the model to add (1/2/3): ")
        if choice == "1":
            self.add_iphone()
        elif choice == "2":
            self.add_macbook()
        elif choice == "3":
            self.add_airpod()
        else:
            print("Invalid choice. Please try again.")

    def delete_stock(self):
        # file_path = self.get_file_path()
        print("1.iPhone")
        print("2.Macbook")
        print("3.Airpods")
        
        choice = input("Enter the model to remove (1/2/3): ")
        if choice == "1":
            self.remove_iphone()
        elif choice == "2":
            self.remove_macbook()
        elif choice == "3":
            self.remove_airpod()
        else:
            print("Invalid choice. Please try again.")
            
    def add_iphone(self):
            try:
                with open(self.fileiphone_staff, "r") as file:
                    stock_data = ast.literal_eval(file.read())
            except FileNotFoundError:
                print("Stock file not found. Creating a new one.")
                stock_data = {}
                
            model = input("Enter the model to add (11/12/13/14/15): ")
            model_key = f"iphone_{model}"
            storage = input("Enter the storage size to add (64/128/256/512(GB)/1(TB)): ")
            if storage == "64" or storage == "128" or storage == "256" or storage == "512":
                storage_key = f"{storage}GB"
            else:
                storage_key = f"{storage}TB"
            try:
                quantity = int(input("Enter the quantity to add: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
            if model_key in stock_data:
                if storage_key in stock_data[model_key]:
                    if stock_data [model_key][storage_key] >= 5:
                        print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key} ({storage_key}).")
                        return
                    else:
                        stock_data[model_key][storage_key] += quantity
                else:
                    stock_data[model_key][storage_key] = quantity
            else:
                stock_data[model_key] = {storage_key: quantity}

            try:
                with open(self.fileiphone_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully added {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")
    def remove_iphone(self):
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

            try:
                with open(self.fileiphone_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully removing {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")
    def add_macbook(self):
            try:
                with open(self.filemacbook_staff, "r") as file:
                    stock_data = ast.literal_eval(file.read())
            except FileNotFoundError:
                print("Stock file not found. Creating a new one.")
                stock_data = {}
                
            model = input("Enter the model to added (1(AirM1)/2(AirM2)/14(Pro_14inch)/16(Pro_16inch)): ")
            if model == "1" or model == "2":
                model_key = f"MacBook_Air_M{model}"
            else:
                model_key = f"MacBook_Pro_{model}inch"
            storage = input("Enter the storage size to added (256/512(GB)/1(TB)): ")
            if storage == "256" or storage == "512":
                storage_key = f"{storage}GB"
            else:
                storage_key = f"{storage}TB"
            try:
                quantity = int(input("Enter the quantity to added: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
            if model_key in stock_data:
                if storage_key in stock_data[model_key]:
                    if stock_data [model_key][storage_key] >= 5:
                        print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key} ({storage_key}).")
                        return
                    else:
                        stock_data[model_key][storage_key] += quantity
                else:
                    stock_data[model_key][storage_key] = quantity
            else:
                stock_data[model_key] = {storage_key: quantity}

            try:
                with open(self.filemacbook_staff, "w") as file:
                    file.write(str(stock_data))
                print(f"Successfully adding {quantity} of {model_key} ({storage_key}).")
            except IOError:
                print("Error writing to the stock file.")
    def remove_macbook(self):
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

        try:
            with open(self.filemacbook_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully removed {quantity} of {model_key} ({storage_key}).")
        except IOError:
            print("Error writing to the stock file.")

    def add_airpod(self):
        try:
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            stock_data = {}

        model = input("Enter the model to add (Gen(2ndGen)/Pro/Max): ")
        if model == "Gen":
            model_key = f"Airpods_2nd_{model}"
        else:
            model_key = f"Airpods_{model}"

        try:
            quantity = int(input("Enter the quantity to add: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        if model_key in stock_data:
            if stock_data[model_key] >= 5:
                print(f"Cannot add stock. Adding {quantity} would exceed the limit of 5 for {model_key}.")
                return
            else:
                stock_data[model_key] += quantity
        else:
            stock_data[model_key] = quantity

        try:
            with open(self.fileairpod_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully added {quantity} of {model_key}.")
        except IOError:
            print("Error writing to the stock file.")

    def remove_airpod(self):
        try:
            with open(self.fileairpod_staff, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found.")
            return

        model = input("Enter the model to remove (Gen(2ndGen)/Pro/Max): ")
        if model == "Gen":
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

        try:
            with open(self.fileairpod_staff, "w") as file:
                file.write(str(stock_data))
            print(f"Successfully removed {quantity} of {model_key}.")
        except IOError:
            print("Error writing to the stock file.")


fileiphone_staff = r"C:\Python_T1_Y2_Project\Employees\iphone.txt"
fileairpod_staff = r"C:\Python_T1_Y2_Project\Employees\airpod.txt"
filemacbook_staff = r"C:\Python_T1_Y2_Project\Employees\macbook.txt"


# stockmanager = StockManager(fileiphone_staff,fileairpod_staff,filemacbook_staff)
stockmanager = StockManager(fileiphone_staff, fileairpod_staff, filemacbook_staff)
stockmanager.main_menu()

    def svhfjkjlghj'k
l;
