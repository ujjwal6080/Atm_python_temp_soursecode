# #atm machine
class Atm:

    def __init__(self):      #init is a constructor(constructor is a special
                              # method whis is automatically executed when we make the obj of the class
        self.pin=""
        self.balance=0

        self.menu()
    def menu(self):
        user_input = input("""hellow , how wouls you like to proceed?
        1.enter 1 to create pin
        2.enter 2 to deposit
        3.enter 3 to withdraw
        4.enter 4 to check balance
        5.enter 5 to exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposite()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.pin=input("enetr your pin = ")
        print("pin set sucessfully")

    def deposite(self):
        temp = input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            self.balance=self.balance+amount
            print("deposite sucessfully")
        else:
            print("dekh ke likh")

    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("operation sucessfully")
            else:
                print("teri maa shod ke gai thi ya tera bapp")
        else:
            print("pehli fursat me nikl")

    def check_balance(self):
            temp=input("enter your pin")
            if temp==self.pin:
                print("check_balance")
                print(self.balance)
            else:
                print("chlaja bdsk")


atm=Atm()
atm.deposite()
atm.check_balance()
atm.withdraw()
atm.check_balance()


