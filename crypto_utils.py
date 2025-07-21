class wallet:
    #constructor to initialize the wallet with a balance
    def __init__(self, owner):
        self.owner= owner
        self.balance = {}
    
    #method to add funds to the wallet
    def deposit(self, token, amount):
        self.balance[token] = self.balance.get(token, 0) + amount
    
    #method to withdraw funds from the wallet
    def withdraw(self, token, amount):
        if token in self.balance and self.balance[token] >= amount:
            self.balance[token] -= amount
            return True
        else:
            return False
        
    #method to get the balance of a specific token
    def get_balance(self):
        return self.balance
    
    