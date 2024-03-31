'''
2. Consider a positive number `n`. Determine all its decompositions as sums of prime numbers.
'''

def InputNumber():
    print("Enter your number")
    x = input()
    x = int(x)
    return x

def IsPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True

def BacktrackIterative(n):
    arr = [0]
    sum = 0
    
    while len(arr) > 0:
        chosen = False

        while not chosen and sum < n:
            arr[-1] += 1
            sum += 1
            if IsPrime(arr[-1]) == True:
                chosen = True

        if chosen == True:
            if sum == n:
                print(arr)
            arr.append(0)
        else:
            sum -= arr[-1]
            arr.pop()

def main():
    n = InputNumber()
    if n <= 1:
        print(n, "cannot be written as a sum of prime numbers")
    else:
        BacktrackIterative(n)

main()