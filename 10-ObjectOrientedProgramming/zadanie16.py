class Bank_account:
    def __init__(self):
        self.balance=0

    def bank_no(self, number):
        self.bank_no= number
        print(f"Bank Account No: {self.bank_no}")

    def bank_balace(self):
        print(f"Balance: PLN {self.balance}")

    def deposit(self,cash):
        self.balance+=cash

    def withdraw(self,money):
        if money > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance-=money

info=Bank_account()
info.bank_no('12 3456 5555 9090 1111 0000 7722')
info.bank_balace()
info.deposit(25.30)
info.bank_balace()
info.withdraw(31.70)
info.bank_balace()
info.withdraw(14)
info.bank_balace()