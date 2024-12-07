class BankAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print(f"Initial balance for {self.owner}: ${self.balance}")
        
    def deposit(self,amount):
        self.balance+=amount
        return f"Depositing: ${amount} \nNew balance: ${self.balance}"
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            return f"Withdrawing: ${amount}\nNew balance: ${self.balance}\nFinal balance: ${self.balance}"
        else:
            return f"Attemping to withdraw: ${amount}\nInsufficient funds. Withdrawal failed.\nFinal balance: ${self.balance}"
        
bankaccount = BankAccount("John",1000)
print(bankaccount.deposit(500))
print(bankaccount.withdraw(3000))



# owner_account = input("Enter bank account name: ")
# initial_balance = float(input("Enter your initial balance: "))
# bank_info = BankAccount(owner_account, initial_balance)
# print(f"Initial balance for {bank_info.owner}: ${bank_info.balance}")
# amount_deposit = float(input("Enter amount to be Deposited: "))
# bank_info.deposit(amount_deposit)
# amount_withdraw = float(input("Enter amount to be Withdrawn: "))
# bank_info.withdraw(amount_withdraw)
