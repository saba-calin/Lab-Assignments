import json


from src.domain.expense import Expense


class JsonRepository:
    def __init__(self):
        self.__expenses_json_file = "src/repository/expenses.json"
        self.__history_json_file = "src/repository/history.json"

        f = open(self.__expenses_json_file, "r+")
        if f.read() == "":
            data = {"expenses": []}
            json_data = json.dumps(data, indent = 4)
            f.write(json_data)
        f.close()

        f = open(self.__history_json_file, "r+")
        if f.read() == "":
            data = {"history": [{"expenses": []}]}
            json_data = json.dumps(data, indent = 4)
            f.write(json_data)
        f.close()

    def update_history(self):
        history = self.__get_history()
        expenses = self.get_expenses()
        expenses = [expense.to_json_file() for expense in expenses]
        expenses = {"expenses": expenses}
        history.append(expenses)
        new_dict = {"history": history}
        json_data = json.dumps(new_dict, indent = 4)

        f = open(self.__history_json_file, "w")
        f.write(json_data)
        f.close()

    def add_expense(self, expense):
        """
        This function adds an expense to the current list of expenses
        :param expense: an object of type Expense
        :return: -
        """

        expenses = self.get_expenses()
        expenses.append(expense)
        expenses = [elem.to_json_file() for elem in expenses]
        data = {"expenses": expenses}
        json_data = json.dumps(data, indent = 4)

        f = open(self.__expenses_json_file, "w")
        f.write(json_data)
        f.close()

    def remove_expense(self, expense):
        expenses = self.get_expenses()
        for elem in expenses:
            if elem.get_amount() <= expense.get_amount():
                expenses.remove(elem)

        expenses = [elem.to_json_file() for elem in expenses]
        new_dict = {"expenses": expenses}
        json_data = json.dumps(new_dict, indent = 4)
        f = open(self.__expenses_json_file, "w")
        f.write(json_data)
        f.close()

    def get_expenses(self):
        expenses = []
        f = open(self.__expenses_json_file, "r")

        data = json.load(f)
        for expense in data["expenses"]:
            expenses.append(Expense(expense["day"], expense["amount"], expense["type"]))

        f.close()
        return expenses

    def __get_history(self):
        history = []
        f = open(self.__history_json_file, "r")

        data = json.load(f)
        for elem in data["history"]:
            history.append(elem)

        f.close()
        return history

    def undo(self):
        history = self.__get_history()

        if len(history) == 2:
            raise Exception("Cannot undo anymore operations!")

        history.pop()
        new_dict = {"history": history}
        json_data = json.dumps(new_dict, indent = 4)
        f = open(self.__history_json_file, "w")
        f.write(json_data)
        f.close()

        expenses = history[-1]["expenses"]
        new_dict = {"expenses": expenses}
        json_data = json.dumps(new_dict, indent = 4)
        f = open(self.__expenses_json_file, "w")
        f.write(json_data)
        f.close()