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