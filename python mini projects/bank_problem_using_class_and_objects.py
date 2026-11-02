class BankAccount:
    def __init__ (self, AccountNumber: int, balance : float = 0.0):
        self.AccountNumber = AccountNumber
        self.balance = balance

    def deposit(self, amount: float = 0.0) -> float:
        if amount <=0:
            raise ValueError("negative amount or zero deposit is not possible")
        else :
            self.balance += amount
        return self.balance 

    def withdraw (self, amount: float = 0.0) -> float:
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        else :
            self.balance -= amount
        return self.balance 


acc1 = BankAccount(79816414121, 500)
acc2 = BankAccount(630315218012, 10000)

account_DB = {
    acc1.AccountNumber : acc1,
    acc2.AccountNumber : acc2
}

user_acc_num = int(input("ENTER YOUR BANK ACCOUNT NUMBER : "))

if user_acc_num in account_DB:
    target_acc = account_DB[user_acc_num]
    print (f"Account found. Avaliable Balance is : {target_acc.balance}")
    
    select_ = input("select required option (deposit/withdraw) :  ").strip().lower()
    if select_ == "deposit" :
        a = int(input("enter your amount : "))
        new_balance = target_acc.deposit(a)
    elif select_ == "withdraw" : 
        b = int(input("enter your amount : "))
        new_balance = target_acc.withdraw(b)
    else : 
        print ("Invalid option selected")

    print("\n---Transaction sucessfull","-"*3)
    print(f"\nAccount Number: {target_acc.AccountNumber}")
    print(f"Total Remaining Balance: ${target_acc.balance}")
else : 
    print("Account number not found in the database")















