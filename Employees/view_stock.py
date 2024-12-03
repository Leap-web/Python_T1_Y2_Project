file_paths = [
    r"C:\Python_T1_Y2_Project\Employees\iphone.txt",
    r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt",
    r"C:\Python_T1_Y2_Project\Employees\macbook.txt"
]
print("Select a file to open:")
for idx, file_path in enumerate(file_paths, 1):
    print(f"{idx}. {file_path}")
while True:
    try:
        file_choice = int(input("\nWhich file you want to open(1 to 3):")) - 1 
        if 0 <= file_choice < len(file_paths):
            selected_file = file_paths[file_choice]
            with open(selected_file, "r") as file:
                print(f"\nContents of {selected_file}:")
                print(file.read())
            break
        else:
            print("Invalid selection! Please enter a valid file number.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except FileNotFoundError:
        print(f"Error: File not found - {selected_file}")
    except Exception as e:
        print(f"Error: {e}")