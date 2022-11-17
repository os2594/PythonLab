class Account:
    """
    A class representing details for a person's account
    """
    def __init__(self, account_name, account_balance):
        """
        Constructor to create initial state of account
        :param: Person´s
        """
        self.__account_name = ''
        self.__account_balance = 0


    def deposit(self, amount):

        if self.__amount <= 0:
            return False
        else:
            return True

    def withdraw(self, amount) -> bool:

        if self.amount <= 0 or self.amount > self.__account_balance:
            return False
        else:
            return True

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name
