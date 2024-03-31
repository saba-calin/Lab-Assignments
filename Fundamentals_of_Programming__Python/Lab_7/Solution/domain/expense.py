class Expense:
    def __init__(self, expense_day, expense_amount, expense_type):
        self.__day = expense_day
        self.__amount = expense_amount
        self.__type = expense_type

    def get_day(self):
        """
        :return: an integer representing the day
        """

        return self.__day

    def get_amount(self):
        """
        :return: an integer representing the amount
        """

        return self.__amount

    def get_type(self):
        """
        :return: a string representing the type
        """

        return self.__type

    def __str__(self):
        return f"day: {self.__day}, amount: {self.__amount}, type: {self.__type}"

    def to_text_file(self):
        return f"{self.__day}, {self.__amount}, {self.__type}\n"

    def to_binary_file(self):
        return self.__day, self.__amount, self.__type

    def to_json_file(self):
        return {"day": self.__day, "amount": self.__amount, "type": self.__type}

    def to_database_format(self, unique_id):
        return {"_id": unique_id, "day": self.__day, "amount": self.__amount, "type": self.__type}
