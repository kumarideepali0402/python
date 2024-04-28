class Bank:
    def __init__(self,title,balance,acc_no):
        self.title=title
        self.balance=balance
        self.acc_no=acc_no
class Savings(Bank):
    def __init__(self,interest_rate):
        self.interest_rate=interest_rate
class Current(Bank):
    def __init__(self,)
a=Bank("najma",9000,562821)
print(a.acc_no)

