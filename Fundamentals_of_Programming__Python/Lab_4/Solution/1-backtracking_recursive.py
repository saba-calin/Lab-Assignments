'''
2. Consider a positive number `n`. Determine all its decompositions as sums of prime numbers.
'''

def InputNumber():
    print("Enter your number")
    x = input()
    x = int(x)
    return x

def EratosthenesSieve(n):
    arr = [True for i in range(n + 1)]
    idx = 2
    while (idx * idx <= n):
        if arr[idx] == True:
            for i in range(idx * idx, n + 1, idx):
                arr[i] = False
        idx += 1

    primeArr = []
    for i in range(2, n + 1):
        if arr[i] == True:
            primeArr.append(i)
    return primeArr

def Backtrack(primeArr, ans, n, sum = 0):
    for num in primeArr:
        sum += num
        ans.append(num)

        if sum == n:
            print(ans)
        elif sum < n:
            Backtrack(primeArr, ans, n, sum)

        ans.pop()
        sum -= num

def main():
    n = InputNumber()
    if n <= 1:
        print(n, "cannot be written as a sum of prime numbers")
    else:
        primeArr = EratosthenesSieve(n)
        ans = []

        Backtrack(primeArr, ans, n)

main()