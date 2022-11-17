class Account:
    """
    A class representing details for a person's account
    """
    def __init__(self, account_name: str):
        """
        Constructor to create initial state of account
        :param account_name: Name under the account
        :param account_balance: Account balance
        """
        self.__account_name = account_name
        self.__account_balance = 0


    def deposit(self, amount: float) -> bool:
        """
        :param amount: amount of the intended deposit
        :return: return either successful or not successful transaction
        """

        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:

        """
        :param amount: amount of the intended withdraw
        :return: return either successful or not successful transaction
        """

        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        :return: return account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        :return: return the name under the account
        """
        return self.__account_name
