import random
import math


# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def AddComplexNumber(var, realPart, imaginaryPart):
    '''
    :param var: list or dictionary
    :param realPart: an integer representing the real part of a number
    :param imaginaryPart: an integer representing the imaginary part of a number
    :return: the function adds a complex number to a list or dictionary
    '''
    if type(var) == list:  # Handling the list
        var.append((realPart, imaginaryPart))
    else:  # Handling the dictionary
        var[realPart] = imaginaryPart


def GetImaginaryPart(var, index: int) -> int:
    '''
    :param var: list or dictionary
    :param index: an integer representing the index where the imaginary part is extracted from
    :return: the imaginary part of an imaginary number
    '''
    if type(var) == list:  # Handling the list
        return var[index][1]
    else:  # Handling the dictionary
        return list(var.values())[index]


def GetRealPart(var, index: int) -> int:
    '''
    :param var: list or dictionary
    :param index: an integer representing the index where the real is extracted from
    :return: the real part of an imaginary number
    '''
    if type(var) == list:  # Handling the list
        return var[index][0]
    else:  # Handling the dictionary
        return list(var)[index]


def GenerateComplexNumbers(var):
    '''
    :param var: list or dictionary
    :return: the function generates 10 random imaginary numbers
    '''
    # A complex number is of the form z = a + b*i

    for i in range(10):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)

        if type(var) == list:  # Filling up the list
            var.append((a, b))
        else:  # Filling up the dictionary
            var[a] = b


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def CreateModulusArray(var):
    '''
    :param var: list or dictionary
    :return: return the modulus array of the complex numbers
    '''
    arr = [ ]
    for i in range(len(var)):
        realPart = GetRealPart(var, i)
        imaginaryPart = GetImaginaryPart(var, i)

        modulus = math.sqrt(realPart * realPart + imaginaryPart * imaginaryPart)
        arr.append(modulus)
    return arr


def CreateRealPartArray(var):
    '''
    :param var: list or dictionary
    :return: the real part array of the complex numbers
    '''
    arr = [ ]
    for i in range(len(var)):
        realPart = GetRealPart(var, i)

        arr.append(realPart)
    return arr


# Problem 3
def LongestSubarrayOfIncreasingModulus(var):
    '''
    :param var: list or dictionary
    :return: the function computes the longest subarray of increasing modulus
    '''
    arr = CreateModulusArray(var)  # Array used to store the modulus of complex numbers

    # O(n ^ 2) time complexity -> because of the while
    # O(n) space complexity -> because of the array that stores the modulus
    maxLength = -1
    start, end = 0, 0
    for i in range(len(arr)):
        j = i
        length = 1

        while j < len(arr) - 1 and arr[j] <= arr[j + 1]:
            length += 1
            j += 1

        if length > maxLength:
            maxLength = length
            start = i
            end = j

    PrintAnswerToLongestSubarrayOfIncreasingModulus(var, start, end)


# Problem 11
def MaxSubarraySumOfRealParts(var):
    '''
    :param var: list or dictionary
    :return: the function computes the maximum subarray of real parts
    '''
    arr = CreateRealPartArray(var)

    # O(n) time complexity -> because the algorithm iterates over the whole array
    # O(n) space complexity -> because of the array that stores the real part of each complex number
    maxSum = -0x3f3f3f3f  # ~ -1.000.000.000
    start, end, tempStart, sum = 0, 0, 0, 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > maxSum:
            maxSum = sum
            start = tempStart
            end = i
        if sum < 0:
            sum = 0
            tempStart = i + 1

    PrintAnswerToMaxSubarraySumOfRealParts(var, start, end, maxSum)


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#


def PrintAnswerToLongestSubarrayOfIncreasingModulus(var, start, end):
    '''
    :param var: list or dictionary
    :param start: an index from the array
    :param end: an index from the array
    :return: the function prints the answer to the longest subarray of increasing modulus
    '''
    print("The length of the longest subarray of numbers having increasing modulus is:", end - start + 1)
    print("The longest subarray of numbers having increasing modulus is composed of the following complex numbers:")
    for i in range(start, end + 1):
        print(ComplexToString(GetRealPart(var, i), GetImaginaryPart(var, i)))


def PrintAnswerToMaxSubarraySumOfRealParts(var, start, end, sum):
    '''\
    :param var: list or dictionary
    :param start: an index from the array
    :param end: an index from the array
    :param sum: an integer
    :return: the function prints the answer to the maximum subarray sum of real parts
    '''
    print("The maximum subarray sum is", sum)
    print("The length of the maximum subarray sum is:", end - start + 1)
    print("The elements of the maximum subarray sum are:")
    for i in range(start, end + 1):
        print(ComplexToString(GetRealPart(var, i), GetImaginaryPart(var, i)))


def PrintMenu():
    '''
    :return: prints the menu
    '''
    print("")
    print("Type 1 to read a list a complex numbers from the console")
    print("Type 2 to display the list of complex numbers to the console")
    print("Type 3 to find the longest subarray of numbers having increasing modulus")
    print("Type 4 to find the maximum subarray sum using real parts")
    print("Type \"exit\" to close the program")


def ComplexToString(realPart: int, imaginaryPart: int) -> str:
    '''
    :param realPart: integer representing the real part of a number
    :param imaginaryPart: integer representing the imaginary part of a number
    :return: a string of the for z = a + b*i
    '''
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


def PrintComplexNumbers(var):
    '''
    :param var: list or dictionary
    :return: prints all complex numbers in a list or dictionary
    '''
    for i in range(len(var)):
        print(ComplexToString(GetRealPart(var, i), GetImaginaryPart(var, i)))


def GetRealPartFromString(string: str) -> int:
    '''
    :param string: a string of the form z = a + b*i
    :return: an integer representing the real part of the number
    '''
    # Parsing the string in order to extract the real part
    # from the complex number

    idx, isNegative = 0, False
    while string[idx].isnumeric() == False:
        idx += 1

    if string[idx - 1] == "-":
        isNegative = True

    realPart = 0
    while string[idx].isnumeric() == True:
        realPart = realPart * 10 + int(string[idx])
        idx += 1

    if isNegative == True:
        realPart = -realPart

    return realPart


def GetImaginaryPartFromString(string: str) -> int:
    '''
    :param string: a string of the form z = a + b*i
    :return: an integer representing the real part of the number
    '''
    # Parsing the string in order to extract the imaginary part
    # from the complex number

    idx, isNegative = len(string) - 1, False
    while string[idx].isnumeric() == False:
        idx -= 1

    if string[idx - 2] == "-":
        isNegative = True

    imaginaryPart, pow = 0, 1
    while string[idx].isnumeric() == True:
        imaginaryPart = imaginaryPart + pow * int(string[idx])
        pow *= 10
        idx -= 1

    if isNegative == True:
        imaginaryPart = -imaginaryPart

    return imaginaryPart


def ReadComplexNumbers(var):
    '''
    :param var: list or dictionary
    :return: the function add complex numbers to a list or a dictionary
    '''
    numbers = int(input("Enter the amount of numbers you want to input: "))
    print("Enter", numbers, "numbers in the \"z = a + bi\" form")

    for i in range(numbers):
        complexNum = input()

        realPart = GetRealPartFromString(complexNum)
        imaginaryPart = GetImaginaryPartFromString(complexNum)

        AddComplexNumber(var, realPart, imaginaryPart)


def ReadString():
    '''
    :return: the function reads and returns a string
    '''
    string = input()
    return string


def HandleOptions(option, var):
    '''
    :param option: string
    :param var: list or dictionary
    :return: the function handles the options
    '''
    if option == "1":
        ReadComplexNumbers(var)
    elif option == "2":
        PrintComplexNumbers(var)
    elif option == "3":
        LongestSubarrayOfIncreasingModulus(var)
    elif option == "4":
        MaxSubarraySumOfRealParts(var)
    elif option == "exit":
        exit()
    else:
        print("Error: unexpected input")


def PrintPreferenceMenu():
    '''
    :return: the function prints the preference menu
    '''
    print("")
    print("Type 1 if you would like to use lists")
    print("Type 2 if you would like to use dictionaries")
    print("Type \"exit\" to close the program")


def GetPreference() -> bool:
    '''
    :return: the function returns a bool representing whether the user wants to use lists or dictionaries
    '''
    while True:
        PrintPreferenceMenu()
        option = ReadString()

        if option == "1":
            return True
        elif option == "2":
            return False
        elif option == "exit":
            exit()
        else:
            print("Error: unexpected input")


def main():
    li = [ ]
    di = { }

    usingLists = GetPreference()

    if usingLists == True:
        GenerateComplexNumbers(li)
    else:
        GenerateComplexNumbers(di)

    while True:
        PrintMenu()

        option = ReadString()
        if usingLists == True:
            HandleOptions(option, li)
        else:
            HandleOptions(option, di)


# Problems 3 and 11
main()