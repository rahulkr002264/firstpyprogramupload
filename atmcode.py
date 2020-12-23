#           BANK COSTUMER SERVICE DEMO SOURCE CODE USING OOPS CONCEPT(PYTHON)


import sys
class Costumer:
    '''WELCOME'''
    bank="XYZ BANK"
    print("WELCOME TO XYZ BANK COSTUMER SERVICE")

    def __init__(self,name,bailance=0.0):
        self.name=name
        self.amount=bailance

    def withdraw(self,wamount):
        if wamount > self.amount:
            print("ivalid amount_low bailance.")
            sys.exit()
        elif wamount%100!=0:
            print("ENTER the valid amount in multiples of 100")

        elif wamount<100:
            print("Entr the amount > 100")

        else:
            self.amount=self.amount-wamount
            print("amount left in account is ",self.amount)

    def deposit(self,damount):
        self.amount=self.amount+damount
        print("your bailance after deposition is ",self.amount)

name=input("ENTR your name ")

c=Costumer(name)
while True:
    print()
    print("Entr W to withdraw\n D to deposit \n E to exit")
    i=input("Entr your choice").upper()
    if(i=="W"):
        wamount=int(input("Entr the amount to withdraw"))
        c.withdraw(wamount)

    if(i=="D"):
        damount=int(input("Entr the amount to deposit"))
        c.deposit(damount)

    if(i=="E"):
        print("THANKU")
        sys.exit()



		





































    
        

        















