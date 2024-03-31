# 8.

# Function that takes input from the user and returns it
def Read():
    print("Enter your number")
    x = input()
    x = int(x)
    return x

# Function that computes and returns the
# smallest Fibonacci number larger than a given parameter
def FindSmallestFibonacciNumberLargerThanN(n):
    x1, x2, ans = 1, 1, 2
    while ans <= n:
         x1 = x2
         x2 = ans
         ans = x1 + x2
    return ans

def main():
    n = Read()
    if n <= 0:
        print("The smallest number from the Fibonacci sequence larger than", n, "is 1")
    else:
        ans = FindSmallestFibonacciNumberLargerThanN(n)
        print("The smallest number from the Fibonacci sequence larger than", n, "is", ans)

main()