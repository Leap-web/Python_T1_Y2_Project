print("Exercise:1")
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
print("\n")

print("Exercise:2")
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
print("\n")

print("Exercise:3")
class Malware:
    
    def describe(self):
        return "This is a malware."
    
class Ransomware(Malware):
    
    def encrypt_files(self):
        return "Files are being encrypted"
    
malware = Malware()
ransomware = Ransomware()
print("Malware Description:",malware.describe())
print("Ransomware Description:",ransomware.describe())
print("Ransomware Action:",ransomware.encrypt_files())
print("\n")

print("Exercise:4")
class Malware:
    
    def describe(self):
        return "This is a malware."
    
class Virus(Malware):
    
    def replicate(self):
        return "Virus is replicating"
    
class Trojan(Malware):
    
    def hide_in_file(self):
        return "Hiding in files."
    
class Keylogger(Trojan):
    
    def describe(self):
        return "This is a keylogger. Capturing keystrokes."
    
virus = Virus()
trojan = Trojan()
keylogger = Keylogger()

print("Virus Description:",virus.describe())
print("Virus Action:",virus.replicate())

print("Trojan Description:",trojan.describe())
print("Trojan Action:",trojan.hide_in_file())

print("Key logger Description:",keylogger.describe())
print("Keylogger Action:",keylogger.hide_in_file())
print("\n")

print("Exercise:5")
class Logger:
    
    def log(self,sms=None,error_code=None,detail=None):
        if sms is not None :
            print(f"Log:{sms}")
        elif error_code is not None and detail is not None:
            print(f"Error Code:{error_code}, Details: {detail}")
        else:
            print("Unknown format")

logger = Logger()
logger.log("System started")
logger.log(error_code=404, detail =  {'url': '/not-found'})
logger.log()
print("\n")

print("Exercise:6")
class FirewallRule:
    
    def apply_rule(self):
        return "Applying generic rule."
    
class IPBlockRule(FirewallRule):
    
    def apply_rule(self):
        return "Blocking IP address."
    
class PortBlockRule(FirewallRule):
    
    def apply_rule(self):
        return "Blocking port number."
    
firewallrule = [FirewallRule(),IPBlockRule(),PortBlockRule()]

for i in firewallrule:
    print("Firewall Action:",i.apply_rule())