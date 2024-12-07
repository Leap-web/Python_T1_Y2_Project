import os
import ast

# File paths
file_paths = {
    "iphone": r"C:\Python_T1_Y2_Project\Employees\iphone.txt",
    "macbook": r"C:\Python_T1_Y2_Project\Employees\macbook.txt",
    "airpod": r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt"
}

# Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Display the contents of a file
def display_file_contents(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
            print(f"Contents of '{filename}':")
            for idx, line in enumerate(content, start=1):
                print(f"{idx}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# Add stock to a file
# def add_stock(filename):
#     try:
#         print("Input the products that you to add to stock.")
#         print('Example Format: iphone_15 = {"128GB": 8, "256GB": 8, "1TB": 8}')
#         product_input = input("Enter your product: ")

#         # Validate the input format
#         if "=" not in product_input:
#             print("Error: Input must be in the format '<product_name> = { ... }'")
#             return

#         product_name, product_data = map(str.strip, product_input.split("=", 1))

#         # Validate the dictionary format
#         try:
#             parsed_data = ast.literal_eval(product_data)
#             if not isinstance(parsed_data, dict):
#                 raise ValueError
#         except (SyntaxError, ValueError):
#             print("Error: The product data must be a dictionary. Example: {'128GB': 8, '256GB': 8}")
#             return

#         # Format the stock data to match the desired format
#         formatted_product_data = f"{product_name} = {{\n"
#         for key, value in parsed_data.items():
#             formatted_product_data += f"    \"{key}\": {value},\n"
#         formatted_product_data += "}\n"

#         # Write the new entry to the file
#         with open(filename, "a") as file:
#             file.write(formatted_product_data)

#         print(f"Product '{product_name}' added successfully to '{filename}'.")
#     except IOError as e:
#         print(f"An error occurred while writing to the file: {e}")
def add_stock(filename):
    try:
        print("Input the products that you want to add to stock.")
        print('Example Format: "iphone_16": {"128GB": 7, "256GB": 8, "1TB": 6}')
        product_input = input("Enter your product: ")

        # Validate the input format
        if ":" not in product_input:
            print("Error: Input must be in the format '<product_name>: { ... }'")
            return

        product_name, product_data = map(str.strip, product_input.split(":", 1))

        # Validate the dictionary format
        try:
            parsed_data = ast.literal_eval(product_data)
            if not isinstance(parsed_data, dict):
                raise ValueError
        except (SyntaxError, ValueError):
            print("Error: The product data must be a dictionary. Example: {'128GB': 8, '256GB': 8}")
            return

        # Read the existing file content and parse it into a dictionary
        try:
            with open(filename, "r") as file:
                existing_data = ast.literal_eval(file.read())
                if not isinstance(existing_data, dict):
                    raise ValueError("File content is not a valid dictionary.")
        except FileNotFoundError:
            existing_data = {}  # Start with an empty dictionary if the file doesn't exist
        except (SyntaxError, ValueError) as e:
            print(f"Error parsing the existing file: {e}")
            return

        # Add the new product to the dictionary
        if product_name in existing_data:
            print(f"Warning: Overwriting existing product '{product_name}'!")
        existing_data[product_name] = parsed_data

        # Write the updated dictionary back to the file
        with open(filename, "w") as file:
            file.write("{\n")
            for key, value in existing_data.items():
                file.write(f'    "{key}": {value},\n')
            file.write("}\n")

        print(f"Product '{product_name}' added successfully to '{filename}'.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")




# Delete stock from a file
def delete_stock(filename):
    try:
        # Display the current contents
        print("Current stock in the file:")
        display_file_contents(filename)

        # Ask the user to select an entry to delete
        entry_to_delete = input("Enter the number of the entry to delete: ")
        try:
            entry_to_delete = int(entry_to_delete) - 1
        except ValueError:
            print("Error: Please enter a valid number.")
            return

        # Read the file contents and delete the selected entry
        with open(filename, "r") as file:
            lines = file.readlines()

        if 0 <= entry_to_delete < len(lines):
            deleted_entry = lines.pop(entry_to_delete)
            with open(filename, "w") as file:
                file.writelines(lines)
            print(f"Deleted entry: {deleted_entry.strip()}")
        else:
            print("Error: Invalid entry number.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError as e:
        print(f"An error occurred while modifying the file: {e}")

# Generate a report by displaying all files
def generate_report():
    print("\n--- Report ---")
    for name, path in file_paths.items():
        print(f"\n{name.capitalize()} Stock:")
        display_file_contents(path)

# Main stock management menu
def stock_management():
    
    while True:
        print("*" * 40)
        print("\nStock Management")
        print("*" * 40)
        print("1. Add Stock\n2. Delete Stock\n3. Exit to Main Menu")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Add stock
            print("\n--- Add Stock ---")
            file_choice = input(f"Choose a file ({', '.join(file_paths.keys())}): ").strip().lower()
            if file_choice in file_paths:
                add_stock(file_paths[file_choice])
            else:
                print("Invalid file choice.")
        elif choice == "2":
            # Delete stock
            print("\n--- Delete Stock ---")
            file_choice = input(f"Choose a file ({', '.join(file_paths.keys())}): ").strip().lower()
            if file_choice in file_paths:
                delete_stock(file_paths[file_choice])
            else:
                print("Invalid file choice.")
        elif choice == "3":
            # Exit to main menu
            break
        else:
            print("Invalid choice. Please try again.")

# Main menu
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Change Stock\n2. Do Report\n3. Exit Program")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            clear_screen()
            stock_management()
        elif choice == "2":
            clear_screen()
            generate_report()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
