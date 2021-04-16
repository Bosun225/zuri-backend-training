class budget:
    """created the budget class"""
    def __init__(self, account, deposit, withdraw, balance, transfer):
        self.account = account
        self.deposit = deposit
        self.balance = balance
        self.withdraw = withdraw        
        self.transfer = transfer

    
    def deposit(self):
        account = []
        print("How much do you want to deposit")
        amt = input(" \n >>>")
        amt.append(account)

    def balance(self):
        print(f'Your current balance is {amt}')

    def withdraw(self):
        print('How much would you like to withdraw')
        withdraw_amt = input("\n >>>") 

        if withdraw_amt < amt:
            new_balance = amt - withdraw_amt
            print(f'Your new balance is {new_balance} ')

        else:
            print("You have entered an invalid amount")

    def transfer(self):
        print('How much do you want to transfer')
        amt_transfer = input('n\ >>>')
        print(f'You have transfered {amt_transfer}')


