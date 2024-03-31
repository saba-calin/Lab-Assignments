import random
import configparser


from src.repository.memory_repository import MemoryRepository
from src.repository.text_file_repository import TextFileRepository
from src.repository.binary_file_repository import BinaryFileRepository
from src.repository.json_repository import JsonRepository
from src.repository.database_repository import DatabaseRepository
from src.domain.expense import Expense


class Services:
    def __init__(self):
        config = configparser.RawConfigParser()
        config.read("src/repository/settings.properties")
        repository = config["Repository"]
        self.__repository = repository["Repository"]

        if self.__repository == "memory_repository":
            # Memory repository
            self.__test_repo = MemoryRepository()
            self.__run_all_tests()
            self.__repo = MemoryRepository()
            self.__generate_expenses()

        elif self.__repository == "text_file_repository":
            # Text file repository
            self.__repo = TextFileRepository()
            f = open("src/repository/expenses.txt")
            if f.read() == "":
                self.__generate_expenses()
            f.close()

        elif self.__repository == "binary_file_repository":
            # Binary file repository
            self.__repo = BinaryFileRepository()
            f = open("src/repository/expenses.dat", "rb")
            if f.read() == b"":
                self.__generate_expenses()
            f.close()

        elif self.__repository == "json_repository":
            # Json repository
            self.__repo = JsonRepository()
            if self.__repo.get_expenses() == []:
                self.__generate_expenses()

        elif self.__repository == "database_repository":
            # Database repository
            self.__repo = DatabaseRepository()
            if self.__repo.get_expenses() == []:
                self.__unique_id = 0
                self.__generate_expenses()
            else:
                self.__unique_id = self.__repo.get_highest_id()

        else:
            raise Exception("Error: the repository does not exist!")

    def undo(self):
        self.__repo.undo()

    def filter_expenses(self, value):
        removed = True
        while removed == True:
            removed = False
            expenses = self.__repo.get_expenses()
            for expense in expenses:
                if expense.get_amount() <= value:
                    self.__repo.remove_expense(expense)
                    removed = True

        self.__repo.update_history()

    def get_expenses(self):
        return self.__repo.get_expenses()

    def validate_and_add_expense(self, expense):
        """
        This function validates and adds an expense to the current list of expenses
        :param expense: an object of type Expense
        :return: -, if no exceptions are raised
        """

        self.__validate_expense(expense)
        if self.__repository == "database_repository":
            self.__repo.add_expense(expense, self.__unique_id)
            self.__unique_id += 1
        else:
            self.__repo.add_expense(expense)
        self.__repo.update_history()

    def __generate_expenses(self):
        expenses = ["Rent", "Utilities", "Groceries", "Transportation", "Dining out", "Entertainment",
                    "Healthcare", "Insurance", "Education", "Miscellaneous"]
        for i in range(1, 11):
            expense_day = random.randint(1, 30)
            expense_amount = random.randint(1, 100) * 100
            expense_type = random.choice(expenses)

            expense = Expense(expense_day, expense_amount, expense_type)
            if self.__repository == "database_repository":
                self.__repo.add_expense(expense, self.__unique_id)
                self.__unique_id += 1
            else:
                self.__repo.add_expense(expense)

        self.__repo.update_history()

    @staticmethod
    def __validate_expense(expense):
        """
        This function validates an object of type expense
        :param expense: an object of type Expense
        :return: -, if no exceptions are raised
        :raise: an error with a string message:
                - "The day has to be between 1 and 30!\n", if the day does not belong to the interval [1, 30]
                - "The amount has to be positive!\n", if the amount is not strictly positive
                - "The type cannot be empty!\n", if the type is empty
                - "The type cannot contain any special characters!\n", if the type contains any special characters
        """

        errors = ""

        if expense.get_day() < 1 or expense.get_day() > 30:
            errors += "The day has to be between 1 and 30!\n"
        if expense.get_amount() < 1:
            errors += "The amount has to be positive!\n"

        expense_type = expense.get_type()
        expense_type = expense_type.strip()
        if expense_type == "":
            errors += "The type cannot be empty!\n"
        if not expense_type.isalpha():
            errors += "The type cannot contain any special characters!\n"

        if len(errors) > 0:
            raise Exception(errors)

    def __test_validate_expense(self):
        """
        This function tests the __validate_expense function
        :return: -, if no exceptions are raised
        """

        expense_day = 12
        expense_amount = 5700
        expense_type = "Rent"
        expense = Expense(expense_day, expense_amount, expense_type)
        self.__validate_expense(expense)

        expense_day = 31
        expense_amount = -2
        expense_type = ";"
        expense = Expense(expense_day, expense_amount, expense_type)
        try:
            self.__validate_expense(expense)
            assert False
        except Exception as exception:
            assert  str(exception) == ("The day has to be between 1 and 30!\nThe amount has to be positive!\n"
                                       "The type cannot contain any special characters!\n")

    def __test_add_expense(self):
        """
        This function validates the add_expense function
        :return: -, if no exceptions are raised
        """

        expense_day = 12
        expense_amount = 5700
        expense_type = "Rent"
        expense = Expense(expense_day, expense_amount, expense_type)
        self.__test_repo.add_expense(expense)

        assert self.__test_repo.get_expenses()[0].get_day() == 12
        assert self.__test_repo.get_expenses()[0].get_amount() == 5700
        assert self.__test_repo.get_expenses()[0].get_type() == "Rent"

    @staticmethod
    def __test_create_expense():
        """
        This function tests the creation of an expense
        :return: -, if no exceptions are raised
        """

        expense_day = 12
        expense_amount = 5700
        expense_type = "Rent"
        expense = Expense(expense_day, expense_amount, expense_type)
        assert expense.get_day() == expense_day
        assert expense.get_amount() == expense_amount
        assert expense.get_type() == expense_type

    def __run_all_tests(self):
        """
        This function runs all test related to the first functionality
        :return: -, if no exceptions are raised
        """

        self.__test_create_expense()
        self.__test_validate_expense()
        self.__test_add_expense()
