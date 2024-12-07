class PhoneBook:
    dic = {}
    
    def add_contact(self,name,number):
        # new_dict = {
        #     "Name": name,
        #     "Number": number,
        # }
        # self.dic[number]=new_dict
        self.dic[name] = number
        # name = key, number = value ,jg vea doch name:number
        return f"Added contact:{name} -> {number}"
    
    def find_contact(self,name):
        if name in self.dic:
            return f"{name}'s number: {self.dic[name]}"
        else:
            return f"{name} is not found in phone book."
        
phonebook = PhoneBook()
# print(phonebook.add_contact("John","123-456-7890"))
# print(phonebook.find_contact("John"))
print(phonebook.add_contact("John", "123-456-7890"))
print(phonebook.find_contact("John"))

