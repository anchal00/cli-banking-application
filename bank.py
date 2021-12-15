import user as userModel
from bankdb import DB_CONNECTION


class Bank:

    def __init__(self):
        self.DB_CONNECTION = DB_CONNECTION()

    def get_account_info(self, acc):
        if self.DB_CONNECTION.check_record_exist(acc) == False:
            raise Exception("Account doesn't exist")
        else:
            return self.DB_CONNECTION.fetch_user_data(acc)

    def __generate_account_number(self):
        self.__acc_counter += 1
        return self.__acc_counter

    def __save_info(self, user_account):
        self.DB_CONNECTION.insert_record(user_account)

    def __update_record(self, user_account):
        self.DB_CONNECTION.update_balance(user_account)

    def _open_account(self, user_name, user_age, balance):
        user_account = self.__generate_account_number()
        user = userModel.User(user_name, user_age, user_account, balance)
        self.__save_info(user)

        print("Account opened successfully for {} with account no. = {} \n".format(
            user_name, user_account))
        return user

    def _send_money(self, sender_account, receiver_account, amount_to_transfer):
        if (self.DB_CONNECTION.check_record_exist(sender_account) == False
                or self.DB_CONNECTION.check_record_exist(receiver_account) == False):
            raise Exception(
                "Either sender's or receriver's account doesnt exist!")
        else:
            sender_info_object = self.DB_CONNECTION.fetch_user_data(
                sender_account)
            receiver_info_object = self.DB_CONNECTION.fetch_user_data(
                receiver_account)

            sender_account_balance = sender_info_object.get_balance()

            if sender_account_balance < amount_to_transfer:
                raise Exception("In-sufficient Funds to Transfer !")
            else:
                sender_info_object.deduct_amount(amount_to_transfer)
                receiver_info_object.add_amount(amount_to_transfer)

                self.__update_record(sender_info_object)
                self.__update_record(receiver_info_object)

                print("\n \n Funds transferred successfully from " + sender_info_object.get_name() +
                      "\'s account to " + receiver_info_object.get_name() + "\'s account \n\n")
                return


def _show_menu():

    print("Choose one of the following options : ")

    print("1 -> To Open a Bank Account.")
    print("2 -> To Send Money.")
    print("3 -> To Show info about an account.")

    print("Any Other Number -> To Exit.")
    print("\n")


if __name__ == '__main__':
    bank = Bank()

    print("### Welcome to My Bank ### \n")

    while True:

        _show_menu()
        user_input = int(input("Enter your operation choice ::: \n"))

        if user_input == 1:
            name = str(input("Enter name of User :"))
            age = int(input("Enter age of User :"))
            amount = int(input("Enter amount to add into your account :"))

            bank._open_account(user_name=name, user_age=age, balance=amount)
            continue

        elif user_input == 2:
            sender_account_number = int(input("Enter account of Sender :"))
            receiver_account_number = int(input("Enter account of Receiver :"))
            amount = int(input("Enter Amount to Transfer :"))

            try:
                bank._send_money(sender_account=sender_account_number,
                                 receiver_account=receiver_account_number, amount_to_transfer=amount)
            except Exception:
                str(Exception)
                print("\n\n Something went wrong ! \n")
            continue

        elif user_input == 3:
            acc = int(input("Enter account number :"))
            print(bank.get_account_info(acc))

        else:
            break

        print("\n\n")
