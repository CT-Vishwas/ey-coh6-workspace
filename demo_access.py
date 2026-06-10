class BankAccount:
    def __init__(self, account_holder_name, initial_deposit):
        self.account_holder = account_holder_name
        self.__bal = initial_deposit # Private variable
        # self._bal = initial_deposit # Protected Variable
    def get_balance(self):
        return self.__bal
        # return self._bal

class SBAccount(BankAccount):
    def __init__(self, account_holder_name, initial_deposit):
        super().__init__(account_holder_name, initial_deposit)
    
b1 = SBAccount("Vishwas",500)
# print(b1._bal) # For Protected
# print(b1.__bal) # For Private gives Attribute Error
print(b1.get_balance())