class Bank():
    def __init__(self,balance,Membership):
        assert balance >= 0, f"Balance {balance} is not greater than or equal to zero!"
        
        self.__balance = balance
    # Balance can be read-only
    @property
    def balance(self):
        return self.__balance
    # Instead of use setter, using withdraw and ammout function to set balance of bank
    def withdraw(self,ammout):
        if ammout > self.__balance:
            raise Exception("The balance is not enough")
        else:
            self.__balance -= ammout
        print(f"The Balance is: {self.__balance}")
    def deposit(self,ammout):
        self.__balance += ammout
        print(f"The Balance is: {self.__balance}")
        
if __name__ == '__main__':
    User1 = Bank(1000,'gold')
    User1.deposit(1000)
    User1.withdraw(3000) # Raise exception because Withdraw ammout > Balance
    User1.balance = 100 # Decoration Property is read only --> cannot change the balance directly