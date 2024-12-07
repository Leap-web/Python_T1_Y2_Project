import os
class FileManager:
    
    def __init__(self,filename):
        self.filename = filename
    def create_file(self):
        try :
            with open(self.filename) as file:
                print(f"File {self.filename}created successfully.")
        except FileNotFoundError:
            print(f"File {self.filename} created not successfully.")
        finally :
            print("File creation process completed.")
        print("\n")
        
    def write_to_file(self,items):
        try:
            with open(self.filename,"w") as file:
                for item in items:
                    file.write(item.strip() + "\n")
                print(f"Data written successfully to {self.filename}")
        except FileNotFoundError:
            print(f"Data written wasn't successfully to {self.filename}.")
        finally:
            print("Write operation completed.")
        print("\n")
        
    def read_file(self):
        try:
            with open(self.filename,"r") as file:
                content = file.readlines()
                print("File Content:")
                for line in content:
                    print(line.strip())
                print(f"\nFile {self.filename} read successfully.")
        except FileNotFoundError:
            print(f"File {self.filename} wasn't read successfully.")
        finally:
            print("Read operation completed.")
        print("\n")  
        
class FileUpdate(FileManager):
    
    def __init__(self,filename):
        self.filename = filename
        self.dic = {}
    def convert(self):
        try:
            self.dic.clear()
            with open(self.filename) as file:
                id = 1
                for line in file:
                    self.dic [f"{id}"] = line.strip()
                    id += 1
        except FileNotFoundError:
            print("Can't convert.")
        print(f"Current Data:{self.dic}")
        
    def add_items(self):
        # self.convert()
        items = input("Enter a new items:").split(',')
        try:
            with open(self.filename,"a") as file:
                for item in items:
                    file.writelines(item.strip() + "\n")
                print(f"Data written successfully to {self.filename}")
        except FileNotFoundError:
            print(f"Data written wasn't successfully to {self.filename}.")
        except KeyError and ValueError:
            print(f"Data written wasn't successfully to {self.filename}.")
        finally:
            print("Write operation completed.")
        print("\n")
        fileupdate.read_file()
        print("\n")
        
    def update_items(self):
        # self.convert()
        items = int(input("Enter a key of items to update:"))
        if str(items) not in self.dic:
            print("There is no key")
            return
        
        value = input("Enter a new value:")
        self.dic[str(items)] = value
        try:
            with open(self.filename,"r") as file:
                lines = file.readlines()
            if (items -1 < len(self.dic)):
                lines[items - 1] = f"{value}\n"
            else:
                lines.append(f"{items}:{value}\n")
            with open(self.filename,"w") as file:
                    file.writelines(lines)
                    print(f"File {self.filename} updated successfully.")
        except ValueError:
            print("Error: Please enter a valid integer for the key.")
        finally:
            print("Update operation completed.")
        print("\n")
        fileupdate.read_file()
        print("\n")
        
    def delete_items(self):
        self.convert()
        item = int(input("Enter a key of items to delete:"))
        try:
            with open(self.filename,"r") as file:
                lines = file.readlines()
            if 1 <= item <= len(lines):
                lines.pop(item - 1)
                self.dic.pop(str(item))
            with open(self.filename,"w") as file:
                file.writelines(lines)
        except ValueError:
            print("Error: Please enter a valid integer for the key.")
        print("\n")
        fileupdate.read_file()
        print("\n")
        
filename = "/Users/savonchanserey/Documents/python /W07_text.txt"

filemanager = FileManager(filename)

filemanager.create_file()
items = input("Enter items seperated by commas:").split(',')
filemanager.write_to_file(items)
filemanager.read_file()

fileupdate = FileUpdate(filename)

is_running = True
while is_running:
    print("Choose an action:")
    print("1.Add_item:")
    print("2.Update_item:")
    print("3.Delete_item:")
    print("4.Exit")
    choice = int(input("Enter your choice(1-4):"))
    if choice == 1:
        os.system('clear')
        fileupdate.add_items()
        fileupdate.convert()
    elif choice == 2:
        os.system('clear')
        fileupdate.update_items()
        fileupdate.convert()
    elif choice == 3:
        os.system('clear')
        fileupdate.delete_items()
        fileupdate.convert()
    elif choice == 4:
        print("Exit the program!")
        is_running = False
    else:
        print("Invalid")


