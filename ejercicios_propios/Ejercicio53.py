class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("ERROR")  
            return
        self.__balance += amount
    
    def withdraw(self, amount):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0 or amount > self.get_balance():
            print("ERROR")
            return
        self.__balance -= amount
    
    def show_balance(self):
        print(f"Your balance: {self.__balance}")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(0)

while True:
    print("== MENU ==")
    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] Total money in acocunt")
    print("[4] Exit")
    option = int(input("Enter an option: "))

    match(option):
        case 1:
            money = int(input("Enter the money: "))
            account.deposit(money)
        case 2:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        case 3:
            account.show_balance()
        case 4:
            break
