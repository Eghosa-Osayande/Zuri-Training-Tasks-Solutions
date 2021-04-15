class Budget():
    '''
    class representing a budget for a category
    such as food, clothing etc
    '''
    def __init__(self, category, balance):
        self.category = category
        self.balance = balance
        print(f"Created {category} Budget : Balance ${balance}")

    def deposit(self, amount):
        '''
        This deposits into the budget class
        '''
        self.balance += amount
        print(f"Deposited {amount} into {self.category}; New Balance is ${self.balance}")

    def withdraw(self, amount):
        '''
        This withdraws from the budget class
        '''
        if amount <= self.balance :
            self.balance -= amount
            print(f"Withdrew {amount} from {self.category}; New Balance is ${self.balance}")
            return amount
        else:
            print(f"Insufficient Balance in {self.category}")
            return 0

    def get_balance(self):
        '''
        prints the value of the current budget balance
        '''
        print(f'{self.category} balance is {self.balance}')
        
    def transfer(self, amount, other_budget):
        '''
        amount : int
        other_budget : Budget
        
        this transfers money from one budget class to another
        '''
        amount =self.withdraw(amount)
        other_budget.deposit(amount)

        
if __name__ == "__main__":
    clothing = Budget('clothing', 100)
    food = Budget('food', 200)
    entertainment = Budget('entertainment', 10)
    
    food.get_balance()
    amt = food.withdraw(50)
    clothing.deposit(amt)
    clothing.transfer(60, entertainment)
    amt2 = food.withdraw(500)