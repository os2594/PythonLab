class Account:
    """
    A class representing details for an account object
    """
    def __init__(self, account_name: str) -> None:
        """
        Constructor to create initial state of an account object
        :param account_name: Name on the account
        """
        self.__account_name = account_name
        self.__account_balance = 0


    def deposit(self, amount: float) -> bool:
        """
        Method to deposit money
        :param amount: amount of the intended deposit
        :return: True or false to represent either a successful or not successful transaction
        """

        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:

        """
        Method to withdraw money
        :param amount: amount of the intended withdrawal
        :return: True or false to represent either a successful or not successful withdrawal
        """

        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access the balance on the account
        :return:  Balance on the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access the name on the account
        :return: Name on the account
        """
        return self.__account_name
