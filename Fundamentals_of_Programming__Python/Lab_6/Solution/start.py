#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
import ui as ui
import functions as functions


def main():
    '''
    This is the main function of the program
    :return: -
    '''
    complexNumbers = [ ]  # Used to store complex numbers
    stack = [ ]  # Used to undo the last operation

    complexNumbers = functions.GenerateRandomNumbers(complexNumbers)
    stack = functions.UpdateStack(complexNumbers, stack)

    functions.RunAllTests()  # Testing the functionalities from A and B

    while True:
        ui.PrintMenu()
        option = ui.InputString()
        ui.HandleOptions(option, complexNumbers, stack)


if __name__ == "__main__":
    main()
