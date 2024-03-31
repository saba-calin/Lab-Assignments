class MemoryRepository:
    def __init__(self):
        self.__expenses = []
        self.__history = []

    def add_expense(self, expense):
        """
        This function adds an expense to the current list of expenses
        :param expense: an object of type Expense
        :return: -
        """

        self.__expenses.append(expense)

    def remove_expense(self, expense):
        self.__expenses.remove(expense)

    def update_history(self):
        self.__history.append(self.__expenses[:])

    def get_expenses(self):
        return self.__expenses

    def undo(self):
        if len(self.__history) == 1:
            raise Exception("Cannot undo any more operations!")

        self.__history.pop()
        self.__expenses.clear()
        for expense in self.__history[-1]:
            self.__expenses.append(expense)
