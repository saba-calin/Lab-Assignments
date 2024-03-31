from Fundamentals_of_Programming__Python.Lab_7.Solution.domain.expense import Expense


class TextFileRepository:
    def __init__(self):
        self.__expenses_text_file = "../repository/expenses.txt"
        self.__history_text_file = "../repository/history.txt"

    def add_expense(self, expense):
        """
        This function adds an expense to the current list of expenses
        :param expense: an object of type Expense
        :return: -
        """

        f = open(self.__expenses_text_file, "a")
        f.write(expense.to_text_file())
        f.close()

    def remove_expense(self, expense):
        expenses = self.get_expenses()
        f = open(self.__expenses_text_file, "w")
        for elem in expenses:
            if elem.get_amount() > expense.get_amount():
                f.write(elem.to_text_file())
        f.close()

    def update_history(self):
        f = open(self.__history_text_file, "a")

        expenses = self.get_expenses()
        f.write(str([expense.to_text_file() for expense in expenses]))
        f.write("\n")

        f.close()

    def undo(self):
        f = open(self.__history_text_file, "r")
        lines = f.readlines()
        if len(lines) == 1:
            raise Exception("Cannot undo any more operations!")
        f.close()

        lines.pop()
        f = open(self.__history_text_file, "w")
        for line in lines:
            f.write(line)
        f.close()

        f = open(self.__expenses_text_file, "w")
        expenses = lines[-1].split(r"\n")
        for elem in expenses:
            elem = elem.strip("[],' ")
            if len(elem) < 5:
                continue
            f.write(elem + "\n")
        f.close()

    def get_expenses(self):
        expenses = []

        f = open(self.__expenses_text_file, "r")
        lines = f.readlines()
        for line in lines:
            info = line.split(", ")
            expense = Expense(int(info[0]), int(info[1]), info[2].split("\n")[0])
            expenses.append(expense)
        f.close()

        return expenses
