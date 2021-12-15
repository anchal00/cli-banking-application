import mysql.connector

from user import User


class DB_CONNECTION:
    # TABLE DEFINITION ->
    # CREATE TABLE bank(
    #   account int PRIMARY KEY ,
    #   name varchar(20),
    #   balance int ,
    #   age int,
    #   CONSTRAINT ck CHECK(age >= 18 and age<= 100 and balance >= 0));

    def __init__(self):
        self.__db = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin123",
            database="pytest"
        )
        self.__cursor = self.__db.cursor()
    print("\n Connected To MYSQL successfully ! \n")

    def insert_record(self, USER):
        name = USER.get_name()
        age = USER.get_age()
        account = USER.get_account()
        balance = USER.get_balance()
        self.__cursor .execute("INSERT INTO bank(name, balance, age) VALUES(%s,%s,%s)",
                               (name, balance, age))

        self.__db.commit()

    def update_balance(self, USER):
        name = USER.get_name()
        age = USER.get_age()
        account = USER.get_account()
        balance = USER.get_balance()

        self.__cursor.execute(
            "UPDATE bank SET balance = %s WHERE account = %s", (balance, account))

        self.__db.commit()

    def check_record_exist(self, account):
        self.__cursor.execute(
            "SELECT account FROM bank WHERE account = %s", (account,))

        data = self.__cursor.fetchall()
        if data == None:
            return False
        return True

    def fetch_user_data(self, account):
        self.__cursor.execute(
            "SELECT * FROM bank WHERE account = %s", (account,))

        data = self.__cursor.fetchone()
        if data == None:
            return data

        account, name, balance, age = data

        return User(name=name, age=age, account=account, balance=balance)
