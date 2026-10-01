class bankAccount:
    def __init__(this, owner, balance):
        this.owner = owner
        this.__balance = balance

# method to get private attribute
    def get_amount(this):
        return this.__balance
# set the method to modify the private attribute
    def deposite(this,amount):
        if amount > 0:
            this.__balance += amount
            return f"deposite {amount}, new balane is {this.__balance}"
        return "invalid balance"

# create an object of bank account
account = bankAccount("asim",1000)
print(account.get_amount())
print(account.deposite(500))
# print(account.__balance)

# ? Accessing Private Members of Parent Class

class Parent:
    def __init__(self):
        self.__private__attr = "this is private attribute"

    def _get__private(self):
       return self.__private__attr #accessing the private attribute

class Child(Parent):
    def access_private(self):
        try:
            return self.__private__attr
        except AttributeError as e:
            return f"can not access private attribute"

parent = Parent()
child =  Child()

print(parent._get__private())
print(child.access_private())