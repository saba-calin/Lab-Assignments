from pymongo.mongo_client import MongoClient


from Fundamentals_of_Programming__Python.Lab_7.Solution.domain.expense import Expense


class DatabaseRepository:
    def __init__(self):
        url = "mongodb+srv://saba:xE9D0fMH27g7705d@cluster0.5sdxo1u.mongodb.net/?retryWrites=true&w=majority"
        request = MongoClient(url)

        try:
            request.admin.command("ping")
        except Exception as exception:
            print(str(exception))

        database = request["CS_project"]
        self.__expenses = database["expenses"]
        self.__history = database["history"]

    def update_history(self):
        expenses = self.__expenses.find()
        arr = []
        for expense in expenses:
            arr.append({"_id": expense["_id"], "day": expense["day"], "amount": expense["amount"],
                        "type": expense["type"]})
        self.__history.insert_one({"Expenses": arr})

    def get_expenses(self):
        expenses = []
        arr = self.__expenses.find()
        for expense in arr:
            expenses.append(Expense(expense["day"], expense["amount"], expense["type"]))
        return expenses

    def __get_history(self):
        history = self.__history.find()
        return list(history)

    def remove_expense(self, expense):
        expenses = self.__expenses.find()
        expenses = list(expenses)
        for elem in expenses:
            if elem["amount"] == expense.get_amount():
                self.__expenses.delete_one({"_id": elem["_id"]})

    def get_highest_id(self):
        expenses = self.__expenses.find()
        unique_id = 0
        for expense in expenses:
            if expense["_id"] > unique_id:
                unique_id = expense["_id"]
        return unique_id + 1

    def add_expense(self, expense, unique_id):
        """
        This function adds an expense to the current list of expenses
        :param expense: an object of type Expense
        :param unique_id: an integer that is different from all other ids that belong to expenses in the list
        :return: -
        """

        self.__expenses.insert_one(expense.to_database_format(unique_id))

    def undo(self):
        history = self.__get_history()

        if len(history) == 1:
            raise Exception("Cannot undo any more operations!")

        self.__history.delete_one(history[-1])
        history.pop()
        self.__expenses.delete_many({})
        for expense in history[-1]["Expenses"]:
            self.__expenses.insert_one(expense)
