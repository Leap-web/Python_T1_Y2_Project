import os
import platform

class FileUpdate:
    def __init__(self, filename):
        self.filename = filename
        self.data_dic = {}

    def clear_screen(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def convert(self):
        try:
            self.data_dic.clear()
            with open(self.filename) as file:
                id = 1
                for line in file:
                    self.data_dic[f"{id}"] = line.strip()
                    id += 1
        except FileNotFoundError:
            print("File not found.")
        print(f"Current Data: {self.data_dic}")

    def menu(self):
        while True:
            print("\n1. Add to File\n2. Update File\n3. Delete from File\n4. Exit")
            option = input("Enter your choice (1-4): ")
            if option == "1":
                self.clear_screen()
                self.add_to_file()
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

    def add_to_file(self):
        try:
            user_input = input("Enter items to add, separated by commas: ")
            items = user_input.split(",")
            with open(self.filename, "a") as file:
                for item in items:
                    file.write(item.strip() + "\n")
            print(f"Data written successfully to '{self.filename}'.")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
        finally:
            print("Add to file operation completed.")

    def update_items(self):
        # Convert the file to a dictionary and load the current data
        self.convert()
        
        try:
            # Ask for the key of the item to update
            items = int(input("Enter a key of items to update:"))
            
            # Check if the key exists in the data_dic
            if str(items) not in self.data_dic:
                print("There is no key")
                return

            # Ask for the new value
            value = input("Enter a new value:")

            # Update the dictionary with the new value
            self.data_dic[str(items)] = value
            
            # Read the current file contents
            with open(self.filename, "r") as file:
                lines = file.readlines()
            
            # Update the correct line or append a new one
            if (items - 1) < len(lines):  # Ensure we're updating a valid line index
                lines[items - 1] = f"{value}\n"
            else:
                lines.append(f"{items}:{value}\n")  # Append if the line index exceeds the current lines
            
            # Write the updated lines back to the file
            with open(self.filename, "w") as file:
                file.writelines(lines)
                print(f"File '{self.filename}' updated successfully.")
        
        except ValueError:
            print("Error: Please enter a valid integer for the key.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Update operation completed.")
            print("\n")
            self.convert()  # Re-convert to see the updated data
            print("\n")

    def delete_items(self):
        self.convert()
        try:
            print("Current Data:")
            for key, value in self.data_dic.items():
                print(f"{key}: {value}")

            key = input("Enter the key of the item to delete: ")
            if key not in self.data_dic:
                print("Key not found.")
                return

            del self.data_dic[key]


            with open(self.filename, "w") as file:
                for value in self.data_dic.values():
                    file.write(value + "\n")
            print(f"Item deleted successfully from '{self.filename}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Delete operation completed.")


filename = r"C:\Users\DELL\OneDrive - Cambodia Academy of Digital Technology\Desktop\File\W07_text.txt"
file_updater = FileUpdate(filename)
file_updater.menu()
