import random

def PrintMenu():
    print("Press 1 to generate a list of radom elements")
    print("Press 2 to sort the generated list using Cocktail Sort")
    print("Press 3 to sort the generated list using Shell Sort")
    print("Type \"exit\" to close the program")

def InputSize():
    print("Enter how many numbers you want to generate")
    size = input()
    size = int(size)
    return size

def InputStep():
    print("Enter the step")
    step = input()
    step = int(step)
    return step

def PrintArray(arr):
    for num in arr:
        print(num, end = " ")
    print("")

def HandlePrinting(arr, cnt, step):
    cnt += 1
    if cnt % step == 0:
        PrintArray(arr)
    return cnt

def CocktailSort(arr, step):
    cnt, start, end = 0, 0, len(arr) - 1
    hasSwapped = True

    while hasSwapped == True:
        hasSwapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                cnt = HandlePrinting(arr, cnt, step)
                hasSwapped = True
        end -= 1

        if hasSwapped == False:
            break

        hasSwapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                cnt = HandlePrinting(arr, cnt, step)
                hasSwapped = True
        start += 1


def ShellSort(arr, step):
    length = len(arr)
    cnt, gap = 0, length // 2

    while gap > 0:
        j = gap
        while j < length:
            i = j - gap
            while i >= 0:
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    cnt = HandlePrinting(arr, cnt, step)
                else:
                    break
                i -= gap
            j += 1
        gap //= 2

def main():
    isGenerated = False
    arr = []
    size = 0

    while True:
        PrintMenu()
        option = input()

        if option == "1":
            arr.clear()
            size = InputSize()
            for i in range(0, size):
                arr.append(random.randint(0, 100))
            print("The list you generated is:", arr)
            isGenerated = True
        elif option == "2":
            if isGenerated == False:
                print("Error: you need to generate the array first")
            else:
                step = InputStep()
                CocktailSort(arr, step)
        elif option == "3":
            if isGenerated == False:
                print("Error: you need to generate the array first")
            else:
                step = InputStep()
                ShellSort(arr, step)
        elif option == "exit":
            break
        else:
            print("Error: unexpected input")

main()