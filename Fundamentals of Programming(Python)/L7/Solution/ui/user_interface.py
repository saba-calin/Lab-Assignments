from src.domain.expense import Expense
from src.services.services import Services


class UserInterface:
    def __init__(self):
        self.__services = Services()

    def start_program(self):
        while True:
            self.print_menu()
            option = input()

            try:
                if option == "1":
                    self.__add_expense()
                elif option == "2":
                    self.__print_expenses()
                elif option == "3":
                    self.__filter_expenses()
                elif option == "4":
                    self.__undo()
                elif option == "exit":
                    exit()
                else:
                    raise Exception("Invalid input!")

            except Exception as exception:
                print(str(exception))

    @staticmethod
    def print_menu():
        print("")
        print("Press 1 to add an expense.")
        print("Press 2 to print the list of expenses.")
        print("Press 3 to filter the list of expenses.")
        print("Press 4 to undo the last operation.")
        print("Type \"exit\" to close the program.")

    def __add_expense(self):
        """
        This function takes as input from the user the day, amount and type of an expense,
        creates an object of type Expense and adds it to the current list expenses
        :return: -, if no exceptions are raised
        """

        expense_day = int(input("day = "))
        expense_amount = int(input("amount = "))
        expense_type = input("type = ")

        expense = Expense(expense_day, expense_amount, expense_type)
        self.__services.validate_and_add_expense(expense)

    def __print_expenses(self):
        expenses = self.__services.get_expenses()

        if len(expenses) == 0:
            print("The list of expenses is empty!")
            return

        for expense in expenses:
            print(expense)

    def __filter_expenses(self):
        value = int(input("value = "))
        self.__services.filter_expenses(value)

    def __undo(self):
        self.__services.undo()


if __name__ == "__main__":
    ui = UserInterface()
    ui.start_program()
