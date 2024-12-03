print("*" * 40)
print("Welcome To Customer Support!")
print("*" * 40)
class MainStock:
    def __init__(self, filename):
        self.filename = filename
    def create_file(self):
        try:
            with open(self.filename) as file:
                print(f"File '{self.filename}' was opened successfully.")

        except IOError as e:
            print(f"An error occurred while opening the file: {e}")
        finally:
            print("Opening the file process completed.")
    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.readlines()
                print(f"Contents of '{self.filename}':")
                for line in content:
                    print(f"- {line.strip()}")
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
        finally:
            print("Read file operation is completed.")
file_paths = [
    r"C:\Python_T1_Y2_Project\Employees\iphone.txt",
    r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt",
    r"C:\Python_T1_Y2_Project\Employees\macbook.txt"
]
for path in file_paths:
    main_stock = MainStock(path)
    main_stock.create_file()
    main_stock.read_file()
 # make change in stock
print("Make some change in stock")
import os
import platform
class MainStock:
    def __init__(self, filename):
        self.filename = filename
    def create_file(self):
        try:
            with open(self.filename) as file:
                print(f"File '{self.filename}' was opened successfully.")
        except IOError as e:
            print(f"An error occurred while opening the file: {e}")
        finally:
            print("Opening the file process completed.")
    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.readlines()
                print(f"Contents of '{self.filename}':")
                for line in content:
                    print(f"- {line.strip()}")
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
        finally:
            print("Read file operation is completed.")
class UpdateStock:
    def __init__(self, filename):
        self.filename = filename
        self.product_dict = {}

    def clear_screen(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    def convert(self):
        try:
            self.product_dict = {}
            with open(self.filename) as file:
                id = 1
                for line in file:
                    self.product_dict[f"{id}"] = line.strip()
                    id += 1
        except FileNotFoundError:
            print("File not found.")
        print(f"Current Data: {self.product_dict}")
    def add_to_stock(self):
        try:
            employee_input = input("Enter the product to add to stock, separated by commas: ")
            products = employee_input.split(",")
            with open(self.filename, 'a') as file:
                for product in products:
                    file.write(product.strip() + "\n")
            print(f"Data written successfully to '{self.filename}'.")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
        finally:
            print("Add product to file successful.")
    def update_items(self):
        self.convert()
        try:
            product_key = input("Enter the key of the item to update: ")
            if product_key not in self.product_dict:
                print("There is no such key.")
                return
            value = input("Enter a new value: ")
            self.product_dict[product_key] = value

            with open(self.filename, "r") as file:
                lines = file.readlines()

            key_index = int(product_key) - 1
            if key_index < len(lines):
                lines[key_index] = f"{value}\n"

            with open(self.filename, "w") as file:
                file.writelines(lines)
            print(f"File '{self.filename}' updated successfully.")
        except ValueError:
            print("Error: Please enter a valid integer for the key.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Update operation completed.")
    def delete_items(self):
        self.convert()
        try:
            print("Current Data:")
            for key, value in self.product_dict.items():
                print(f"{key}: {value}")
            key = input("Enter the key of the item to delete: ")
            if key not in self.product_dict:
                print("Key not found.")
                return

            del self.product_dict[key]
            with open(self.filename, "w") as file:
                for value in self.product_dict.values():
                    file.write(value + "\n")
            print(f"Item deleted successfully from '{self.filename}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Delete operation completed.")
    def menu(self):
        while True:
            print("\n1. Add to Stock\n2. Update Stock\n3. Delete from Stock\n4. Exit")
            option = input("Enter your choice (1-4): ")
            if option == "1":
                self.clear_screen()
                self.add_to_stock()
                self.convert()
            elif option == "2":
                self.clear_screen()
                self.update_items()
            elif option == "3":
                self.clear_screen()
                self.delete_items()
            elif option == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
filename = r"C:\Users\DELL\OneDrive - Cambodia Academy of Digital Technology\Desktop\File\W07_text.txt"
file_updater = UpdateStock(filename)
file_updater.menu()
