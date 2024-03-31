#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import functions as functions


def PrintMenu():
    """
    This function prints the menu
    :return: -
    """
    OutputString("")
    OutputString("Press 1 to add a complex number to the list.")
    OutputString("Press 2 to add a complex number to the list at a specific index.")
    OutputString("Press 3 to remove a number at a specific index.")
    OutputString("Press 4 to remove numbers between indices.")
    OutputString("Press 5 to replace all occurrences of a number with another number.")
    OutputString("Press 6 to print the list of complex numbers.")
    OutputString("Press 7 to print the real numbers between indices.")
    OutputString("Press 8 to print numbers based on their modulus.")
    OutputString("Press 9 to keep only the real numbers.")
    OutputString("Press 10 to keep only the numbers based on their modulus.")
    OutputString("Press 11 to undo the last operation.")
    OutputString("Type \"exit\" to close the program.")


def HandleOptions(option: str, complexNumbers: list, stack: list):
    """
    This function handles the options of the program
    :param option: a string representing the option
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: -, if no exceptions are raised
    :raises: an exception with the string message "Error: The input you provided is not valid!", if
             the option is invalid
    """
    try:
        if option == "1":
            complexNumbers, stack = functions.ManageAddNumberToList(complexNumbers, stack)
        elif option == "2":
            complexNumbers, stack = functions.ManageAddNumberToListAtPosition(complexNumbers, stack)
        elif option == "3":
            complexNumbers, stack = functions.ManageRemoveNumberAtPosition(complexNumbers, stack)
        elif option == "4":
            complexNumbers, stack = functions.ManageRemoveNumbersBetweenPositions(complexNumbers, stack)
        elif option == "5":
            complexNumbers, stack = functions.ManageReplaceComplexWithComplex(complexNumbers, stack)
        elif option == "6":
            complexNumbers, stack = functions.ManagePrintComplexNumbers(complexNumbers, stack)
        elif option == "7":
            complexNumbers, stack = functions.ManagePrintRealNumbersBetweenIndices(complexNumbers, stack)
        elif option == "8":
            complexNumbers, stack = functions.ManagePrintNumbersBasedOnModulus(complexNumbers, stack)
        elif option == "9":
            complexNumbers, stack = functions.ManageFilterReal(complexNumbers, stack)
        elif option == "10":
            complexNumbers, stack = functions.ManageFilterBasedOnModulus(complexNumbers, stack)
        elif option == "11":
            stack = functions.Undo(complexNumbers, stack)
        elif option == "exit":
            exit()
        else:
            raise Exception(HandleErrors(1))

    except Exception as exception:
        OutputString(str(exception))


def HandleErrors(errorCode: int) -> str:
    """
    This function handles the errors of the program
    :param errorCode: an integer representing the error code
    :return: a string of the form "Error: + custom message"
    """
    string = "Error: "

    if errorCode == 1:
        string += "The input you provided is not valid!"
    elif errorCode == 2:
        string += "The input you provided is not a valid integer!"
    elif errorCode == 3:
        string += "The index you provided is out of range!"
    elif errorCode == 4:
        string += "The list is empty!"
    elif errorCode == 5:
        string += "The first index should be smaller or equal than the second index!"
    elif errorCode == 6:
        string += "There are no real numbers in the list!"
    elif errorCode == 7:
        string += "There are no complex numbers with the given conditions!"
    elif errorCode == 8:
        string += "The adding a number to list functionality is not implemented correctly!"
    elif errorCode == 9:
        string += "The adding a number to list at position functionality is not implemented correctly!"
    elif errorCode == 10:
        string += "The removing a number at position functionality is not implemented correctly!"
    elif errorCode == 11:
        string += "The removing numbers between positions functionality is not implemented correctly!"
    elif errorCode == 12:
        string += "The replacing complex with complex functionality is not implemented correctly!"
    elif errorCode == 13:
        string += "Cannot undo any more operations!"
    elif errorCode == 14:
        string += "The input you provided is not a valid float!"

    return string


def PrintComplexNumbers(complexNumbers: list):
    """
    This function prints the complex numbers from the list
    :param complexNumbers: a list containing the complex numbers
    :return: -
    """
    for i in range(len(complexNumbers)):
        complexNumber = functions.ComplexToString(functions.GetRealPart(complexNumbers, i),
                                                  functions.GetImaginaryPart(complexNumbers, i))
        OutputString(complexNumber)


def PrintRealNumbersBetweenIndices(complexNumbers: list, startIndex: int, endIndex: int):
    """
    This function print the real numbers that belong to an interval from the list
    :param complexNumbers: a list containing the complex numbers
    :param startIndex: the lower bound of the interval
    :param endIndex: the upper bound of the interval
    :return: -
    """
    for i in range(startIndex, endIndex + 1):
        if functions.GetImaginaryPart(complexNumbers, i) == 0:
            complexNumber = functions.ComplexToString(functions.GetRealPart(complexNumbers, i),
                                                      functions.GetImaginaryPart(complexNumbers, i))
            OutputString(complexNumber)


def PrintNumbersBasedOnModulus(complexNumbers: list, modulusOption: str, modulus: float):
    """
    This function prints complex numbers whose modulus respect a certain condition
    :param complexNumbers: a list containing the complex numbers
    :param modulusOption: a string representing the option
    :param modulus: a float representing the modulus of a complex number
    :return: -
    """
    for i in range(len(complexNumbers)):
        realPart = functions.GetRealPart(complexNumbers, i)
        imaginaryPart = functions.GetImaginaryPart(complexNumbers, i)
        complexNumber = functions.ComplexToString(realPart, imaginaryPart)

        if modulusOption == '<' and functions.GetModulus(realPart, imaginaryPart) < modulus:
            OutputString(complexNumber)
        elif modulusOption == '=' and functions.GetModulus(realPart, imaginaryPart) == modulus:
            OutputString(complexNumber)
        elif modulusOption == '>' and functions.GetModulus(realPart, imaginaryPart) > modulus:
            OutputString(complexNumber)


def InputModulusOption() -> str:
    """
    This function takes as input from the user the modulusOption and returns it
    :return: a string representing the modulusOption
    """
    OutputString("")
    OutputString("Enter \"<\", \"=\" or \">\".")

    modulusOption = InputString()
    return modulusOption


def InputRealPart() -> str:
    """
    This function takes as input from the user the real part of a complex number and returns it
    :return: a string representing the real part of a complex number
    """
    OutputString("")
    OutputString("Enter the real part of the number.")

    realPart = InputString()
    return realPart


def InputImaginaryPart() -> str:
    """
    This function takes as input from the user the imaginary part of a complex number and returns it
    :return: a string representing the imaginary part of a complex number
    """
    OutputString("")
    OutputString("Enter the imaginary part of the number.")

    imaginaryPart = InputString()
    return imaginaryPart


def InputIndexToInsert() -> str:
    """
    This function takes as input from the user an index and returns it
    :return: a string representing the index where a complex number is to be inserted
    """
    OutputString("")
    OutputString("Enter the index where you want to add the number.")

    index = InputString()
    return index


def InputIndexToRemove() -> str:
    """
    This function takes as input from the user an index and returns it
    :return: a string representing the index where a complex number is to be removed
    """
    OutputString("")
    OutputString("Enter the index where you want to remove a number.")

    index = InputString()
    return index


def InputStartIndex() -> str:
    """
    This function takes as input from the user an index and returns it
    :return: a string representing the lower bound of an interval
    """
    OutputString("")
    OutputString("Enter the start index.")

    index = InputString()
    return index


def InputEndIndex() -> str:
    """
    This function takes as input from the user an index and returns it
    :return: a string representing the upper  bound of an interval
    """
    OutputString("")
    OutputString("Enter the end index.")

    index = InputString()
    return index


def InputModulus() -> str:
    """
    This function takes as input from the user the modulus of a complex number and returns it
    :return: a string representing the modulus of a complex number
    """
    OutputString("")
    OutputString("Enter the modulus.")

    modulus = InputString()
    return modulus


def InputString() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string
    """
    string = input()
    return string


def OutputString(string: str):
    """
    This function prints a string
    :param string: a string
    :return: -
    """
    print(string)
