class CreditCard:

    def __init__(self,customer,bank,acnt,limit):
        self.customer = customer
        self.bank = bank
        self.acnt = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.acnt

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance

    def charge(self,price):
        try:
            if type(price) != type(5):
                raise ValueError
            if price + self.balance > self.limit :
                return False
            else:
                self.balance += price
                return True
        except ValueError:
            print("Error of Type!")

    def make_payment(self,amount):
        try:
            if(amount <= 0):
                raise ValueError
            else:
                self.balance -= amount
        except ValueError:
            print("Value of amount should not be Negative")

obj = CreditCard('Dinesh','SBI',100,200)
obj.charge(199)
print(obj.get_balance())
print(obj.charge(200))
print(obj.get_balance())
obj.charge('hello')
obj.make_payment(-200)