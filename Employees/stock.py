class Stock:
    
    def __init__(self,fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user,mac_m1_user,mac_m2_user,mac_pro_14,mac_pro_16,airpod_user):
        self.iphone = {"iPhone11":5,"iPhone12":3,"iPhone13":20,"iPhone14":15, "iPhone15":8,"iPhone16":13}
        self.airpod = {"AirPods_2nd_Gen":10,"AirPods_Pro":7,"AirPods_Max":19}
        self.macbook = {"Air_M1":30,"Air_M2":22,"Pro_14-inch":20,"Pro_16-inch":18}
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
        
    # for employee to view the stock
    def view_stock(self):
        print(self.iphone)
        print(self.airpod)
        print(self.macbook)
    
    # for user to view the stock of iphone
    def iphone_menu(self):
        try:
            with open(self.fileiphone,"r") as file:
                content = file.read()
                print("Stock iPhone:")
                print(content)
                # for line in content:
                #     print(line.strip())
        except FileNotFoundError:
            print(f"The file {self.fileiphone} was not found. Please ensure it exists in the correct directory.")
            return
    def buy_iphone(self):       
        choice = input("Model:").strip()
        if choice == "iPhone11" :
            print("Model:iPhone_11")
            storage = input("Storage:")
            if storage == "64" :
                print("$599")
                confirm = input("Confirm your buy:(yes,no)")
                #if else one more
                if confirm == "yes":
                    # call function amount
                    # minus the value of item in the dictionary
                    if choice  not in self.iphone :
                        print("No Model exist")
                    else:
                        if choice in self.iphone:
                            if storage in self.iphone:
                                content[choice] = [storage -1]
                        print(self.iphone)
            elif storage == "128" :
                print("$699")
                confirm = input("Confirm your buy:(yes,no)")
            elif storage == "256" :
                print("$799")
                confirm = input("Confirm your buy:(yes,no)")
            else:
                print("Invalid storage option.")
                
        # import from user function to confirm the user
        
    # for user to view the stock of airpod
    def airpod_menu(self):
        with open("macbook.txt","r") as file:
            content = file.read()
            print("Stock iPhone:")
            print(content)
            
            
    # for user to view the stock of macbook
    def macbook_menu(self):
        with open("airpod.txt","r") as file:
            content = file.read()
            print("Stock iPhone:")
            print(content)
    
    # let user input
    def stock_menu(self):
        print("Stock Display:")
        print("1.Phone")
        print("2.Airpod")
        print("3.Macbook")
        print("4.Exit")
        while True:
            try:
                option = int(input("Option:"))
                if option == 1:
                    self.iphone_menu()
                elif option == 2:
                    self.airpod_menu()
                elif option == 3:
                    self.macbook_menu()
                elif option == 4:
                    print("Exit the stock!")
                    break
                else:
                    print("Invalid option, please choose again.")
            except ValueError:
                print("Please enter a valid number.")

# view stock for staff 
fileiphone_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/iphone.txt"
fileairpod_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/airpod.txt"
filemacbook_staff = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/macbook.txt"

# view stock for users iphone
fileiphone11_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/iphone11_user.txt"
fileiphone12_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/iphone12_user.txt"
fileiphone13_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/iphone13_user.txt"
fileiphone14_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/iphone14_user.txt"
fileiphone15_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/iphone15_user.txt"

# view stock for users mac
mac_m1_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/mac_m1_user.txt"
mac_m2_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/mac_m2_user.txt"
mac_pro_14 = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/mac_pro_14.txt"
mac_pro_16 = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/mac_pro_16.txt"

# view stock for user airpod
airpod_user = "/Users/savonchanserey/Documents/python /Python_T1_Y2_Project/Employees/airpod_user.txt"

stock = Stock(fileiphone_staff,fileairpod_staff,filemacbook_staff,fileiphone11_user,fileiphone12_user,fileiphone13_user,fileiphone14_user,fileiphone15_user)

stock.view_stock()
stock.stock_menu()