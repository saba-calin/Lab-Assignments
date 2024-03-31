import pickle


from Fundamentals_of_Programming__Python.Lab_7.Solution.domain.expense import Expense


class BinaryFileRepository:
    def __init__(self):
        self.__expenses_binary_file = "../repository/expenses.dat"
        self.__history_binary_file = "../repository/history.dat"

    def add_expense(self, expense):
        """
        This function adds an expense to the current list of expense
        :param expense: an object of type Expense
        :return: -
        """

        f = open(self.__expenses_binary_file, "ab")
        pickle.dump(expense.to_binary_file(), f)
        f.close()

    def get_expenses(self):
        f = open(self.__expenses_binary_file, "rb")
        expenses = []
        data = b' '

        try:
            while data:
                data = pickle.load(f)
                expenses.append(Expense(data[0], data[1], data[2]))
        except Exception:
            pass

        f.close()
        return expenses

    def remove_expense(self, expense):
        expenses = self.get_expenses()
        f = open(self.__expenses_binary_file, "wb")
        for elem in expenses:
            if elem.get_amount() > expense.get_amount():
                pickle.dump(elem.to_binary_file(), f)
        f.close()

    def update_history(self):
        f = open(self.__history_binary_file, "ab")
        expenses = self.get_expenses()
        pickle.dump([expense.to_binary_file() for expense in expenses], f)
        f.close()

    def undo(self):
        f = open(self.__history_binary_file, "rb")
        data = b' '
        lines = []
        try:
            while data:
                data = pickle.load(f)
                lines.append(data)
        except Exception:
            pass
        f.close()

        if len(lines) == 1:
            raise Exception("Cannot undo anymore operations!")

        lines.pop()
        f = open(self.__history_binary_file, "wb")
        for line in lines:
            pickle.dump(line, f)
        f.close()

        print(lines[-1])

        f = open(self.__expenses_binary_file, "wb")
        for elem in lines[-1]:
            pickle.dump(elem, f)
        f.close()
