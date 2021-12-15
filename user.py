class User:
    def __init__(self, name, age, account, balance):
        self.__name = name
        self.__age = age
        self.__account = account
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_account(self):
        return self.__account

    def get_balance(self):
        return self.__balance

    def deduct_amount(self, amount):
        self.__balance -= amount

    def add_amount(self, amount):
        self.__balance += amount
        
    def __str__(self):
        return ("User : { \n"
                + "\t name  :" + self.__name + "\n"
                + "\t age   :" + str(self.__age) + "\n"
                + "\t account   :" + str(self.__account) + "\n" 
                + "\t balance  :" + str(self.__balance) + "\n}")
