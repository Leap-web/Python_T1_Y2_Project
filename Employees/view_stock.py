file_paths = [
    r"C:\Python_T1_Y2_Project\Employees\iphone.txt",
    r"C:\Python_T1_Y2_Project\Employees\airpod_user.txt",
    r"C:\Python_T1_Y2_Project\Employees\macbook.txt"
]
for path in file_paths:
    try:
        with open(path, "r") as file:
            print(f"Contents of {path}:")
            print(file.read())
            print("-" * 50)
    except FileNotFoundError:
        print(f"Error: File not found - {path}")
    except Exception as e:
        print(f"Error: {e} - {path}")
