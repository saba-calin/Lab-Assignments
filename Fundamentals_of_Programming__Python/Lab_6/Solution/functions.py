#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import ui as ui

import random
import math


def GenerateRandomNumbers(complexNumbers: list) -> list:
    """
    This function generates and appends 10 random complex numbers to the list of complex numbers
    :param complexNumbers: a list containing the complex numbers
    :return: the list of complex numbers
    """
    for i in range(10):
        realPart = random.randint(-100, 100)
        imaginaryPart = random.randint(-100, 100)

        AddNumberToList(complexNumbers, realPart, imaginaryPart)

    return complexNumbers


def AddNumberToList(complexNumbers: list, realPart: int, imaginaryPart: int) -> list:
    """
    This function appends a complex number to the list of complex numbers
    :param complexNumbers: a list containing the complex numbers
    :param realPart: an integer representing the real part of the complex number
    :param imaginaryPart: an integer representing the imaginary part of the complex number
    :return: the modified list of complex numbers
    """
    complexNumbers.append((realPart, imaginaryPart))
    return complexNumbers


def ManageAddNumberToList(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the AddNumberToList function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    realPart = ui.InputRealPart()
    imaginaryPart = ui.InputImaginaryPart()

    ValidatePart(realPart)
    ValidatePart(imaginaryPart)

    realPart = int(realPart)
    imaginaryPart = int(imaginaryPart)

    complexNumbers = AddNumberToList(complexNumbers, realPart, imaginaryPart)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def AddNumberToListAtPosition(complexNumbers: list, realPart: int, imaginaryPart: int, index: int):
    """
    This function adds a complex number at a given index in the complexNumbers list
    :param complexNumbers: a list containing the complex numbers
    :param realPart: an integer representing the real part of the complex number
    :param imaginaryPart: an integer representing the imaginary part of the complex number
    :param index: an integer representing the position where the complex number will be inserted
    :return: the modified list of complex numbers
    """
    complexNumbers.append(complexNumbers[-1])

    for i in range(len(complexNumbers) - 1, index, -1):
        complexNumbers[i], complexNumbers[i - 1] = complexNumbers[i - 1], complexNumbers[i]  # Swap
    complexNumbers[index] = (realPart, imaginaryPart)

    return complexNumbers


def ManageAddNumberToListAtPosition(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the AddNumberToListAtPosition function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    realPart = ui.InputRealPart()
    imaginaryPart = ui.InputImaginaryPart()
    index = ui.InputIndexToInsert()

    ValidatePart(realPart)
    ValidatePart(imaginaryPart)
    ValidateIndex(index, complexNumbers)

    realPart = int(realPart)
    imaginaryPart = int(imaginaryPart)
    index = int(index)

    complexNumbers = AddNumberToListAtPosition(complexNumbers, realPart, imaginaryPart, index)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def RemoveNumberAtPosition(complexNumbers: list, index: int):
    """
    This function removes a complex number from a given index in the complexNumbers list
    :param complexNumbers: a list containing the complex numbers
    :param index: an integer representing the position where the complex number will be removed
    :return: the modified list of complex numbers
    """
    for i in range(index, len(complexNumbers) - 1):
        complexNumbers[i], complexNumbers[i + 1] = complexNumbers[i + 1], complexNumbers[i]  # Swap
    complexNumbers.pop()

    return complexNumbers


def ManageRemoveNumberAtPosition(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the RemoveNumberAtPosition function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    index = ui.InputIndexToRemove()
    ValidateIndex(index, complexNumbers)
    index = int(index)

    complexNumbers = RemoveNumberAtPosition(complexNumbers, index)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def RemoveNumbersBetweenPositions(complexNumbers: list, startIndex: int, endIndex: int):
    """
    This function removes all the complex numbers in the interval [startIndex, endIndex] from the complexNumbers list
    :param complexNumbers: a list containing the complex numbers
    :param startIndex: an integer representing the lower bound of the interval
    :param endIndex: an integer representing the upper bound of the interval
    :return: the modified list of complex numbers
    """
    for i in range(startIndex, endIndex + 1):
        complexNumbers = RemoveNumberAtPosition(complexNumbers, startIndex)

    return complexNumbers


def ManageRemoveNumbersBetweenPositions(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the RemoveNumbersBetweenPositions function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    startIndex = ui.InputStartIndex()
    endIndex = ui.InputEndIndex()

    ValidateIndex(startIndex, complexNumbers)
    ValidateIndex(endIndex, complexNumbers)

    startIndex = int(startIndex)
    endIndex = int(endIndex)

    ValidateStartAndEndIndices(startIndex, endIndex)

    complexNumbers = RemoveNumbersBetweenPositions(complexNumbers, startIndex, endIndex)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def ReplaceComplexWithComplex(complexNumbers: list, realPartToReplace: int, imaginaryPartToReplace: int,
                              realPart: int, imaginaryPart: int):
    """
    This function replaces all occurrences of a complex numbers with another complex number
    :param complexNumbers: a list containing the complex numbers
    :param realPartToReplace: an integer representing the real part of the complex number to be replaced
    :param imaginaryPartToReplace: an integer representing the imaginary of the complex number to be replaced
    :param realPart: an integer representing the real part of the complex number that is going to replace the old one
    :param imaginaryPart: an integer representing the imaginary port of the complex number that is going
                          to replace the old one
    :return: the modified list of complex numbers
    """
    for i in range(len(complexNumbers)):
        if (GetRealPart(complexNumbers, i) == realPartToReplace and
            GetImaginaryPart(complexNumbers, i) == imaginaryPartToReplace):
            temp = (realPart, imaginaryPart)
            complexNumbers[i] = temp

    return complexNumbers


def ManageReplaceComplexWithComplex(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the ReplaceComplexWithComplex function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    realPartToReplace = ui.InputRealPart()
    imaginaryPartToReplace = ui.InputImaginaryPart()
    realPart = ui.InputRealPart()
    imaginaryPart = ui.InputImaginaryPart()

    ValidatePart(realPartToReplace)
    ValidatePart(imaginaryPartToReplace)
    ValidatePart(realPart)
    ValidatePart(imaginaryPart)

    realPartToReplace = int(realPartToReplace)
    imaginaryPartToReplace = int(imaginaryPartToReplace)
    realPart = int(realPart)
    imaginaryPart = int(imaginaryPart)

    complexNumbers = ReplaceComplexWithComplex(complexNumbers, realPartToReplace, imaginaryPartToReplace,
                                               realPart, imaginaryPart)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def ComplexToString(realPart: int, imaginaryPart: int) -> str:
    """
    This function generates a string based on the real and imaginary part of a complex number
    :param realPart: an integer representing the real part of a complex number
    :param imaginaryPart: an integer representing the imaginary part of a complex number
    :return: a string of the form "z = a + b*i"
    """
    # A complex number is of the form z = a + b*i
    string = "z = "

    if realPart == 0 and imaginaryPart == 0:
        string += "0"
    elif realPart == 0:
        string += str(imaginaryPart) + "*i"
    elif imaginaryPart == 0:
        string += str(realPart)
    else:
        string += str(realPart)
        if imaginaryPart < 0:
            string += " - "
        else:
            string += " + "
        string += str(abs(imaginaryPart)) + "*i"

    return string


def ManagePrintComplexNumbers(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the PrintComplexNumbers function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    ui.PrintComplexNumbers(complexNumbers)

    return complexNumbers, stack


def ManagePrintRealNumbersBetweenIndices(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the PrintRealNumbersBetweenIndices function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)
    CheckIfThereAreRealNumbers(complexNumbers)

    startIndex = ui.InputStartIndex()
    endIndex = ui.InputEndIndex()

    ValidateIndex(startIndex, complexNumbers)
    ValidateIndex(endIndex, complexNumbers)

    startIndex = int(startIndex)
    endIndex = int(endIndex)

    ValidateStartAndEndIndices(startIndex, endIndex)

    ui.PrintRealNumbersBetweenIndices(complexNumbers, startIndex, endIndex)

    return complexNumbers, stack


def ManagePrintNumbersBasedOnModulus(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the PrintNumbersBasedOnModulus function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    modulusOption = ui.InputModulusOption()
    modulus = ui.InputModulus()

    ValidateModulusOption(modulusOption)
    ValidateModulus(modulus)

    modulus = float(modulus)

    CheckIfThereAreNumbersBasedOnModulus(complexNumbers, modulusOption, modulus)

    ui.PrintNumbersBasedOnModulus(complexNumbers, modulusOption, modulus)

    return complexNumbers, stack


def CheckIfThereAreRealNumbers(complexNumbers: list):
    """
    This function checks if the list of complex numbers contains any real numbers
    :param complexNumbers: a list containing the complex numbers
    :return: -, if no exceptions are raised
    :raises: an exception with the string message "Error: There are no real numbers in the list!", if
             there are no real numbers in the complexNumbers list
    """
    for i in range(len(complexNumbers)):
        if GetImaginaryPart(complexNumbers, i) == 0:
            return

    raise Exception(ui.HandleErrors(6))


def CheckIfThereAreNumbersBasedOnModulus(complexNumbers: list, modulusOption: str, modulus: float):
    """
    This function checks if there are any complex numbers whose modulus respect a certain condition
    :param complexNumbers: a list containing the complex numbers
    :param modulusOption: a string representing the option ("<", "=", ">")
    :param modulus: a float representing the modulus of a complex number
    :return: -, if no exceptions are raised
    :raises: an exception with the string message "Error: There are no complex numbers with the given conditions!", if
             there are no complex numbers whose modulus respect a certain condition
    """
    for i in range(len(complexNumbers)):
        realPart = GetRealPart(complexNumbers, i)
        imaginaryPart = GetImaginaryPart(complexNumbers, i)

        if modulusOption == '<' and GetModulus(realPart, imaginaryPart) < modulus:
            return
        elif modulusOption == '=' and GetModulus(realPart, imaginaryPart) == modulus:
            return
        elif modulusOption == '>' and GetModulus(realPart, imaginaryPart) > modulus:
            return

    raise Exception(ui.HandleErrors(7))


def FilterReal(complexNumbers: list) -> list:
    """
    This function keep only the real numbers in the list
    :param complexNumbers: a list containing the complex numbers
    :return: the modified list of complex numbers
    """
    temp = [ ]

    for i in range(len(complexNumbers)):
        if GetImaginaryPart(complexNumbers, i) == 0:
            temp.append(complexNumbers[i])

    complexNumbers.clear()
    for i in range(len(temp)):
        complexNumbers.append(temp[i])

    return complexNumbers


def ManageFilterReal(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the FilterReal function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    complexNumbers = FilterReal(complexNumbers)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def FilterBasedOnModulus(complexNumbers: list, modulusOption: str, modulus: float) -> list:
    """
    This function keeps only the complex numbers that satisfy a certain condition based on their modulus in the list
    :param complexNumbers: a list containing the complex numbers
    :param modulusOption: a string representing the option ("<", "=", ">")
    :param modulus: a float representing the modulus of a complex number
    :return: the modified list of complex numbers
    """
    temp = [ ]

    for i in range(len(complexNumbers)):
        realPart = GetRealPart(complexNumbers, i)
        imaginaryPart = GetImaginaryPart(complexNumbers, i)

        if modulusOption == '<' and GetModulus(realPart, imaginaryPart) < modulus:
            temp.append(complexNumbers[i])
        elif modulusOption == '=' and GetModulus(realPart, imaginaryPart) == modulus:
            temp.append(complexNumbers[i])
        elif modulusOption == '>' and GetModulus(realPart, imaginaryPart) > modulus:
            temp.append(complexNumbers[i])

    complexNumbers.clear()
    for i in range(len(temp)):
        complexNumbers.append(temp[i])

    return complexNumbers


def ManageFilterBasedOnModulus(complexNumbers: list, stack: list) -> (list, list):
    """
    This function takes in and validates all parameters for the FilterBasedOnModulus function
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a tuple of lists representing the list of complex numbers and the stack of previous versions of
             the list of complex numbers, if no exceptions are raised
    """
    CheckIfListIsEmpty(complexNumbers)

    modulusOption = ui.InputModulusOption()
    modulus = ui.InputModulus()

    ValidateModulusOption(modulusOption)
    ValidateModulus(modulus)

    modulus = float(modulus)

    complexNumbers = FilterBasedOnModulus(complexNumbers, modulusOption, modulus)
    stack = UpdateStack(complexNumbers, stack)

    return complexNumbers, stack


def GetRealPart(complexNumbers: list, index: int) -> int:
    """
    This function returns the real part of a complex number at a given index in the list
    :param complexNumbers: a list containing the complex numbers
    :param index: an integer representing the index of a complex number in the list
    :return: the real part of a complex number at a specific index
    """
    return complexNumbers[index][0]


def GetImaginaryPart(complexNumbers: list, index: int) -> int:
    """
    This function returns the imaginary part of a complex number at a given index in the list
    :param complexNumbers: a list containing the complex numbers
    :param index: an integer representing the index of a complex number in the list
    :return: the imaginary part of a complex number at a specific index
    """
    return complexNumbers[index][1]


def GetModulus(realPart: int, imaginaryPart: int) -> float:
    """
    The function computes and returns the modulus of a complex number
    :param realPart: an integer representing the real part of a complex number
    :param imaginaryPart: an integer representing the imaginary part of a complex number
    :return: a float representing the modulus of a complex number
    """
    return math.sqrt(realPart * realPart + imaginaryPart * imaginaryPart)


def UpdateStack(complexNumbers: list, stack: list) -> list:
    """
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a list representing the updated stack
    """
    stack.append(complexNumbers[:])
    return stack


def Undo(complexNumbers: list, stack: list) -> list:
    """
    This function undoes the last operation of the program, if it can be undone
    :param complexNumbers: a list containing the complex numbers
    :param stack: a list containing previous versions of the list of complex numbers
    :return: a list representing the modified stack, if no exception are raised
    :raises: an exception with the string message "Error: Cannot undo any more operations!", if
             the operation cannot be undone
    """
    try:
        if len(stack) == 1:
            raise Exception(ui.HandleErrors(13))

        stack.pop()

        complexNumbers.clear()
        for i in range(len(stack[len(stack) - 1])):
            AddNumberToList(complexNumbers, stack[len(stack) - 1][i][0], stack[len(stack) - 1][i][1])

        return stack

    except Exception as exception:
        ui.OutputString(str(exception))


def ValidatePart(part: str):
    """
    This function validates the real or imaginary part of a complex number
    :param part: a string representing the real or imaginary part of a complex number
    :return: -, if no exception are raised
    :raises: an exception with the string message "Error: The input you provided is not a valid integer!", if
             the part is not a valid integer
    """
    if not (part.isdigit() == True or (part[0] == '-' and part[1:].isdigit() == True)):
        raise Exception(ui.HandleErrors(2))


def ValidateIndex(index: str, complexNumbers: list):
    """
    This function validates an index in the complexNumbers list
    :param index: a string
    :param complexNumbers: a list containing the complex numbers
    :return: -, if no exception are raised
    :raises: an exception with the string message "Error: The index you provided is out of range!", if
             the index is out of range or "The input you provided is not a valid integer!", if
             the index is not a valid integer
    """
    if index.isdigit() == True or (index[0] == '-' and index[1:].isdigit() == True):
        string = int(index)
        if string >= 0 and string < len(complexNumbers):
            return

        raise Exception(ui.HandleErrors(3))

    raise Exception(ui.HandleErrors(2))


def ValidateStartAndEndIndices(startIndex: int, endIndex: int):
    """
    This function validates an interval based on its two boundaries
    :param startIndex: an integer representing the lower bound of the interval
    :param endIndex: an integer representing the upper bound of the interval
    :return: -, if no exception are raised
    :raise: an exception with the string message "Error: The first index should be smaller or equal than the second
            index!", if the interval is not valid
    """
    if startIndex > endIndex:
        raise Exception(ui.HandleErrors(5))


def ValidateModulusOption(modulusOption: str):
    """
    This function validates the modulusOption
    :param modulusOption: a string representing the option
    :return: -, if no exception are raised
    :raises: an exception with the string message "Error: The input you provided is not valid!", if
             the modulusOption is not valid
    """
    if modulusOption == '<' or modulusOption == '=' or modulusOption == '>':
        return modulusOption
    raise Exception(ui.HandleErrors(1))


def ValidateModulus(modulus: str):
    """
    This function validates the modulus of a complex number
    :param modulus: a string representing the modulus of a complex number
    :return: -, if no exception are raised
    :raises: an exception with the string message "Error: The input you provided is not a valid float!", if
             the modulus is not valid
    """
    if len(modulus) == 1 and modulus[0] == '0':
        return

    cnt = 0
    for i in range(len(modulus)):
        if modulus[i] == '-':
            cnt += 1

    if cnt > 1:
        raise Exception(ui.HandleErrors(14))
    elif cnt == 1 and modulus[0] != '-':
        raise Exception(ui.HandleErrors(14))

    temp = ""
    for i in range(len(modulus)):
        if modulus[i] != '-':
            temp += modulus[i]

    if temp[0] == '0' and temp[1] != '.':
        raise Exception(ui.HandleErrors(14))

    cnt = 0
    for i in range(len(temp)):
        if temp[i] == '.':
            cnt += 1

    if cnt > 1:
        raise Exception(ui.HandleErrors(14))
    elif cnt == 1 and (temp[0] == '.' or temp[len(temp) - 1] == '.'):
        raise Exception(ui.HandleErrors(14))

    modulus = ""
    for i in range(len(temp)):
        if temp[i] != '.':
            modulus += temp[i]

    if modulus.isdigit() == False:
        raise Exception(ui.HandleErrors(14))


def CheckIfListIsEmpty(complexNumbers: list):
    """
    This function checks if the complexNumbers list in empty
    :param complexNumbers: a list containing the complex numbers
    :return: -, if no exception are raised
    :raises: an exception with the string message "Error: The list is empty!", if
             the list is empty
    """
    if len(complexNumbers) == 0:
        raise Exception(ui.HandleErrors(4))


def RunAllTests():
    """
    This function runs all tests related from functionalities from A and B
    :return: -
    """
    # Testing functionalities for A
    TestAddNumberToList()
    TestAddNumberToListAtPosition()

    # Testing functionalities for B
    TestRemoveNumberAtPosition()
    TestRemoveNumbersBetweenPositions()
    TestReplaceComplexWithComplex()


def TestAddNumberToList():
    """
    This function tests the AddNumberToList function
    :return: -
    """
    assert (AddNumberToList([(1, 2), (1, 2)], 1, -4) ==
            [(1, 2), (1, 2), (1, -4)]), ui.HandleErrors(8)
    assert (AddNumberToList([(1, 4), (34, -54), (12, -11), (423, -43)], 0, 0) ==
            [(1, 4), (34, -54), (12, -11), (423, -43), (0, 0)]), ui.HandleErrors(8)
    assert (AddNumberToList([ ], 1, 3) ==
            [(1, 3)]), ui.HandleErrors(8)


def TestAddNumberToListAtPosition():
    """
    This function tests the AddNumberToListAtPosition function
    :return: -
    """
    assert (AddNumberToListAtPosition([(1, 2), (1, 2)], 1, 4, 1) ==
            [(1, 2), (1, 4), (1, 2)]), ui.HandleErrors(9)
    assert (AddNumberToListAtPosition([(-12, -3), (1, -4), (-5, 10), (-1, -4)], -3, -2, 3) ==
            [(-12, -3), (1, -4), (-5, 10), (-3, -2), (-1, -4)]), ui.HandleErrors(9)
    assert (AddNumberToListAtPosition([(1, 4), (34, -54), (12, -11), (423, -43)], 4, 6, 2) ==
            [(1, 4), (34, -54), (4, 6), (12, -11), (423, -43)]), ui.HandleErrors(9)


def TestRemoveNumberAtPosition():
    """
    This function tests the RemoveNumberAtPosition function
    :return: -
    """
    assert (RemoveNumberAtPosition([(1, 2), (1, 3), (1, 4)], 0) ==
            [(1, 3), (1, 4)]), ui.HandleErrors(10)
    assert (RemoveNumberAtPosition([(-12, -3), (1, -4), (-5, 10), (-1, -4)], 3) ==
            [(-12, -3), (1, -4), (-5, 10)]), ui.HandleErrors(10)
    assert (RemoveNumberAtPosition([(1, 4)], 0) ==
            [ ]), ui.HandleErrors(10)


def TestRemoveNumbersBetweenPositions():
    """
    This function tests the RemoveNumbersBetweenPositions function
    :return: -
    """
    assert (RemoveNumbersBetweenPositions([(-12, -3), (1, -4), (-5, 10), (-1, -4)], 0, 2) ==
            [(-1, -4)]), ui.HandleErrors(11)
    assert (RemoveNumbersBetweenPositions([(1, 4), (34, -54), (12, -11), (423, -43)], 1, 3) ==
            [(1, 4)]), ui.HandleErrors(11)
    assert (RemoveNumbersBetweenPositions([(2, 45), (6, 2), (34, 90), (50, 2)], 0, 3) ==
            [ ]), ui.HandleErrors(11)


def TestReplaceComplexWithComplex():
    """
    This function tests the ReplaceComplexWithComplex function
    :return: -
    """
    assert (ReplaceComplexWithComplex([(3, 4), (3, 4), (3, 4)], 3, 4, 1, 2) ==
            [(1, 2), (1, 2), (1, 2)]), ui.HandleErrors(12)
    assert (ReplaceComplexWithComplex([(-1, -3), (1, 3)], 1, 3, -1, -3) ==
            [(-1, -3), (-1, -3)]), ui.HandleErrors(12)
    assert (ReplaceComplexWithComplex([(1, 2)], 1, 2, 2, 1) ==
            [(2, 1)]), ui.HandleErrors(12)