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
