# ABSTRACTION is one of the four fundamental concepts of Object
# Oriented Programming. It is the hiding of details that are not necessary
# for the user. By creating objects with interface methods, a programmer
# can hide away the details that aren't needed for that interaction.
#
# Another explanation: https://www.youtube.com/watch?v=L1-zCdrx8Lk
#
# This program shows the OOP concept of ABSTRACTION. The withdraw()
# method includes a block of code that does checks to make sure the
# withdrawal request is valid (not a negative number, not a number
# greater than the account's balance). But the interface for withdrawing
# money is simple and 'hides' all of that code away, so only
# it can be accessed simply by doing my_account.withdraw(amount)
#
# By using ABSTRACTION this way, anyone interacting with the
# withdrawal system doesn't need to know about all of the messy
# details.



class SavingsAccount():
    def __init__(self, balance, account_id):
        self.__balance = balance
        self.__account_id = account_id

    def withdraw(self, amount): # all of this method's code is necessary but complicated.
        if amount > 0:
            if amount > self.__balance:
                print("Sorry, you don't have enough in your account to do that.")
            else:
                self.__balance = self.__balance - amount
                print(f"You withdrew {withdrawal_amount}")
                print(f"New balance: {self.__balance}")
        else:
            print("Sorry, you can't withdraw negative money.")

my_account = SavingsAccount(1000, "FREER1234")

withdrawal_amount = int(input("How much would you like to withdraw? "))

my_account.withdraw(withdrawal_amount) # by using abstraction, the way the user can
# interact with the object is simplified, ignoring all the complicated stuff inside
# the method.
