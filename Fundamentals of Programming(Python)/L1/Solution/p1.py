# 5.e

# Function that takes input from the user and returns it
def Read():
    print("Enter your number")
    x = input()
    x = int(x)
    return x

# Function to check whether a number is prime or not
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

def main():
    n = Read()
    copy = n

    if n <= 2:
        print("There isn't any prime number smaller than", n)
    else:
        n -= 1
        while IsPrime(n) == False:
            n -= 1
        print("The largest prime number smaller than", copy, "is", n)

main()