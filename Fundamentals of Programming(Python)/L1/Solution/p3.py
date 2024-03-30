# 14.

# Function that takes input from the user and returns it
def Read():
    print("Enter your number")
    x = input()
    x = int(x)
    return x

# Function that computes and returns the 
# n-th element from the sequence
def NthElement(n):
    m = n
    for i in range(1, n + 1):
        arr = []
        temp, d, nrDiv = i, 2, 0

        while temp > 1:
            ok = False

            while temp % d == 0:
                temp /= d
                ok = True
                nrDiv += 1

            if ok == True:
                arr.append(d)

            d += 1
            if d * d > temp:
                d = int(temp)

        if nrDiv == 1 or i == 1: # If nrDiv is 1, then i is a prime number
            m -= 1
            if m == 0:
                return i
        else:
            for num in arr:
                m -= num
                if m <= 0:
                    return num

def main():
    n = Read()

    if n <= 0:
        print("Error: n should be a positive number")
    else:
        ans = NthElement(n)
        print("The", n, "-th element from the sequence is", ans)

main()
