# print("*" * 40)
# print ("Welcome To Customer Support!")
# print("*" * 40)
# class MainStock:
#     def __init__(self, filename):
#         self.filename=filename
#     def create_file(self):
#         try:
#             with open(self.file, 'w') as file:
#                 print(f"File '{self.filename}' was open successfully.")
#         except IOError as e:
#             print(f"An error occured while opening the file: {e}")
#         finally:
#             print("Opening the file process completed.")
#     def read_file(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 content=file.readlines()
#                 print(f"contents of '{self.filename}':")
#                 for line in content:
#                     print(f"-{line.strip()}")
#         except FileNotFoundError:
#             print(f"File '{self.filename}'not found.")
#         except IOError as e:
#             print(f"An error accurred while reading the file: {e}")
#         finally:
#             print("Read file operation is completed.")
# filename =[
#     r"C:\Python_T1_Y2_Project\Employees\iphone.txt",
#     r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt",
#     r"C:\Python_T1_Y2_Project\Employees\macbook.txt"
# ]
# filename=MainStock(filename)
# main_stock=MainStock(filename)
# main_stock.create_file()
# main_stock=read_file()
print("*" * 40)
print("Welcome To Customer Support!")
print("*" * 40)
class MainStock:
    def __init__(self, filename):
        self.filename = filename
    # def create_file(self):
    #     try:
    #         with open(self.filename, 'w') as file:
    #             print(f"File '{self.filename}' was opened successfully.")
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


# file_paths = [
#     r"C:\Python_T1_Y2_Project\Employees\iphone.txt",
#     r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt",
#     r"C:\Python_T1_Y2_Project\Employees\macbook.txt"
# ]
# print("Select a file to open:")
# for idx, file_path in enumerate(file_paths, 1):
#     print(f"{idx}. {file_path}")
# while True:
#     try:
#         file_choice = int(input("\nWhich file you want to open(1 to 3):")) - 1 
#         if 0 <= file_choice < len(file_paths):
#             selected_file = file_paths[file_choice]
#             with open(selected_file, "r") as file:
#                 print(f"\nContents of {selected_file}:")
#                 print(file.read())
#             break
#         else:
#             print("Invalid selection selection file.")
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#     except FileNotFoundError:
#         print(f"Error: File not found - {selected_file}")
#     except Exception as e:
#         print(f"Error: {e}")