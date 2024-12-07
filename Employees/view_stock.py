import ast

class StockManager:
    def __init__(self):
        self.fileiphone = r"C:\Python_T1_Y2_Project\Employees\iphone.txt"
        self.filemacbook = r"C:\Python_T1_Y2_Project\Employees\macbook.txt"
        self.fileairpod = r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt"

    def main_menu(self):
        while True:
            print("=" * 50)
            print("Main Menu:")
            print("1. Change Stock")
            print("2. Do Report")
            print("3. Exit Program")
            print("=" * 50)

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
            print("1. Add Stock")
            print("2. Delete Stock")
            print("3. Exit to Main Menu")
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
        file_path = self.get_file_path()
        try:
            with open(file_path, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Creating a new one.")
            stock_data = {}

        model = input("Enter the model to add (e.g., iphone_11): ").strip()
        storage = input("Enter the storage size to add (e.g., 128GB): ").strip()
        quantity = int(input("Enter the quantity to add: ").strip())

        if model in stock_data:
            if storage in stock_data[model]:
                stock_data[model][storage] += quantity
            else:
                stock_data[model][storage] = quantity
        else:
            stock_data[model] = {storage: quantity}

        with open(file_path, "w") as file:
            file.write(str(stock_data))

        print(f"Successfully added {quantity} of {model} ({storage}).")

    def delete_stock(self):
        file_path = self.get_file_path()
        try:
            with open(file_path, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Nothing to delete.")
            return

        model = input("Enter the model to delete from (e.g., iphone_11): ").strip()
        storage = input("Enter the storage size to delete (e.g., 128GB): ").strip()
        quantity = int(input("Enter the quantity to delete: ").strip())

        if model in stock_data and storage in stock_data[model]:
            if stock_data[model][storage] >= quantity:
                stock_data[model][storage] -= quantity
                if stock_data[model][storage] == 0:
                    del stock_data[model][storage]
                if not stock_data[model]:
                    del stock_data[model]
                print(f"Successfully deleted {quantity} of {model} ({storage}).")
            else:
                print(f"Not enough stock to delete. Current stock: {stock_data[model][storage]}")
        else:
            print("Model or storage not found in stock.")

        with open(file_path, "w") as file:
            file.write(str(stock_data))

    def generate_report(self):
        file_path = self.get_file_path()
        try:
            with open(file_path, "r") as file:
                stock_data = ast.literal_eval(file.read())
        except FileNotFoundError:
            print("Stock file not found. Cannot generate report.")
            return

        print("=" * 50)
        print("Stock Report:")
        for model, storages in stock_data.items():
            print(f"Model: {model}")
            for storage, quantity in storages.items():
                print(f"  Storage: {storage} - Quantity: {quantity}")
        print("=" * 50)

    def get_file_path(self):
        print("=" * 50)
        print("Choose the stock file:")
        print("1. iPhone")
        print("2. MacBook")
        print("3. AirPod")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            return self.fileiphone
        elif choice == "2":
            return self.filemacbook
        elif choice == "3":
            return self.fileairpod
        else:
            print("Invalid choice. Please try again.")
            return self.get_file_path()

# Initialize and start the program
if __name__ == "__main__":
    stock_manager = StockManager()
    stock_manager.main_menu()
