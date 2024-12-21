class bank_info:
    def __init__(self,cust_id,name):
        self.cust_id = cust_id
        self.name = name
        self.balance = None


    def display_balance(self):


        print(f'{self.cust_id} {self.balance}')
class account(bank_info):
    def __init__(self,account_no,account_type,balance,bank_info):
        super().__init__(bank_info.cust_id,bank_info.name,bank_info.balance)

        bank_info.balance+=self.balance
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance

bank_info.balance +=account.balance

class transaction:
    def __init__(self, from_account,to_account,amount,timestamp):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.timestamp = timestamp

    def process_transaction(self):
        if self.from_account.balance>=self.amount:
            self.from_account-= self.amount
            self.to_account+= self.amount
        else:
            print("Invalid transaction ")





customer1 = bank_info(cust_id = 1, name = "Ved",balance=0 )
customer2 = bank_info(cust_id = 2, name = "Dev",balance=0)

acc = account(account_no=1, account_type="savings", balance = 5000000,customer=customer1)
acc1 = account(account_no=2, account_type="savings",balance = 50000,customer=customer2)


send1 = transaction(from_account=acc.balance,to_account=acc1.balance,amount=1000,timestamp=1240)
transaction.process_transaction(send1)

print(f'{acc.balance},{acc1.balance}')





