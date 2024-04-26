class Bank:
    def __init__(self,title,balance,accountno,interest):
        self.__title=title
        self.__balance=0
        self.__ac_no=accountno
        self.__intrest=interest
    def getTitle(self):
        return self.__title
    def getBal(self):
        return self.__balance
    def getInterest():

    def deposit(self,ammount):
        self.__balance+=ammount
        print(self.__balance)
    def withdrawl(self,ammount):
        self.__balance-=ammount
        print(self.__balance)
    def interest(self,rate):
        self.__interest+=rate
        self.balance+=self.balance*(rate/100)
        print("the ammount after adding interest:",self.__balance)

class saving_account(Bank):
    def __init__(self,name,accountno,balance,interest):
        super().__init__(name,accountno,balance,interest)
    def 
class cur_account(Bank):
    def __init__(self,name,accountno,balance,interest):
        pass


f=Bank("deepali",123456,5000,3)
f.deposit(100)
f.withdrawl(500)
f.interest(2)

