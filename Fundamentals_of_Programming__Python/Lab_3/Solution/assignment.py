import random
import timeit

def PrintMenu():
    print("")
    print("Press 1 to sort a list using Cocktail Sort(best case)")
    print("Press 2 to sort a list using Cocktail Sort(average case)")
    print("Press 3 to sort a list using Cocktail Sort(worst case)")
    print("Press 4 to sort a list using Shell Sort(best case)")
    print("Press 5 to sort a list using Shell Sort(average case)")
    print("Press 6 to sort a list using Shell Sort(worst case)")
    print("Type \"exit\" to close the program")
    print("")

def InputSize():
    print("Enter the length of the list")
    size = input()
    size = int(size)
    return size

def CocktailSort(arr):
    start, end = 0, len(arr) - 1
    hasSwapped = True

    while hasSwapped == True:
        hasSwapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hasSwapped = True
        end -= 1

        if hasSwapped == False:
            break

        hasSwapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hasSwapped = True
        start += 1

def ShellSort(arr):
    length = len(arr)
    gap = length // 2

    while gap > 0:
        j = gap
        while j < length:
            i = j - gap
            while i >= 0:
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                else:
                    break
                i -= gap
            j += 1
        gap //= 2

def main():
    while True:
        PrintMenu()
        option = input()

        if option == "1":  
            # Cocktail Sort(best case)
            # O(n), when the list is already sorted(the algorithm stops after the first iteration)
            size = InputSize()
            for i in range(5):
                arr = []
                for j in range(size):
                    arr.append(j)

                start = timeit.default_timer()
                CocktailSort(arr)
                print("Time it took to sort a list of", size, "elements using Cocktail Sort(best case):",
                      timeit.default_timer() - start)

                size *= 2
        elif option == "2":  
            # Cocktail Sort(average case)
            # O(n ^ 2), when the elemets of the list are in a random order
            size = InputSize()
            for i in range(5):
                arr = []
                for j in range(size):
                    arr.append(random.randint(0, 100000))

                start = timeit.default_timer()
                CocktailSort(arr)
                print("Time it took to sort a list of", size, "elements using Cocktail Sort(average case):",
                      timeit.default_timer() - start)

                size *= 2
        elif option == "3":  
            # Cocktail Sort(worst case)
            # O(n ^ 2), when the list is sorted in reverse order
            size = InputSize()
            for i in range(5):
                arr = []
                for j in range(size, 0, -1):
                    arr.append(j)

                start = timeit.default_timer()
                CocktailSort(arr)
                print("Time it took to sort a list of", size, "elements using Cocktail Sort(worst case):",
                      timeit.default_timer() - start)

                size *= 2
        elif option == "4":  
            # Shell Sort(best case)
            # O(n log(n)), when the list is already sorted(the total count of comparisons of 
            # each interval is equal to the size of the given array)
            size = InputSize()
            for i in range(5):
                arr = []
                for j in range(size):
                    arr.append(j)

                start = timeit.default_timer()
                ShellSort(arr)
                print("Time it took to sort a list of", size, "elements using Shell Sort(best case):",
                      timeit.default_timer() - start)

                size *= 2
        elif option == "5":  
            # Shell Sort(average case)
            # O(n log(n) ^ 2) ~ O(n ^ 1.25), when the elemets of the list are in a random order
            size = InputSize()
            for i in range(5):
                arr = []
                for j in range(size):
                    arr.append(random.randint(0, 100000))

                start = timeit.default_timer()
                ShellSort(arr)
                print("Time it took to sort a list of", size, "elements using Shell Sort(average case):",
                    timeit.default_timer() - start)

                size *= 2
        elif option == "6":  
            # Shell Sort(worst case) - depends on the gap sequence
            # O(n ^ 2), when the list is sorted in reverse order and the gaps are 1, 2, ..., [n / 4], [n / 2]
            size = InputSize()
            for i in range(5):
                arr = []
                for j in range(size, 0, -1):
                    arr.append(j)

                start = timeit.default_timer()
                ShellSort(arr)
                print("Time it took to sort a list of", size, "elements using Shell Sort(worst case):",
                      timeit.default_timer() - start)

                size *= 2
        elif option == "exit":
            break
        else:
            print("Error: unexpected input")

main()