class Password:
    def __init__(self):
        self.password = input("Enter a password to check its strength:")
    def check(self):
        symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        has_islower = False
        has_digit = False
        has_isupper = False
        has_symbols = False
        if len(self.password) < 8:
            print("Weak")
        elif len(self.password) >=8:
            for c in self.password:
                if c.islower():
                        has_islower = True
                if c.isupper():
                        has_isupper = True
                if c.isdigit():
                        has_digit = True
                if c in symbols:
                        has_symbols = True
            if has_symbols and has_isupper and has_digit and has_islower:
                print("Strong")
            elif (has_islower and has_isupper) or (has_digit and has_symbols):
                print("Moderate")
            else:
                print("Weak")
password = Password()
print("Password Strength:",password.check())
