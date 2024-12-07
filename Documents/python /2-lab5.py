class Userprofile:
    def __init__(self,username,phone_number):
        self.__phone_number = phone_number
        self.__username = username
        
    def display_public_info(self):
        i = self.__phone_number[-4:]
        return f"Username: {self.__username}, Phone: XXX-XXX-{i}"
    
    def update (self,old_phone,new_phone):
        if (self.__phone_number == old_phone):
            self.__phone_number = new_phone
            return f"Contact info updated successfully."
user = Userprofile("serey","12345678")
print(user.display_public_info())
print(user.update("12345678","09876543"))
print(user.display_public_info())
