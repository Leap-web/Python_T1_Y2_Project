class User:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
        
    def get_username(self,username):
        if self.__username == username:
            return f"Username:{username}"
        else:
            return f"{username} not found!"
        
    def verify_password(self,password):
        if self.__password == password:
            return f"Password Verfied: True"
        else:
            return f"Password Verfied: False"
    
user = User("serey",1234)
print(user.get_username("serey"))
print(user.verify_password(1234))
print(user.verify_password(123))