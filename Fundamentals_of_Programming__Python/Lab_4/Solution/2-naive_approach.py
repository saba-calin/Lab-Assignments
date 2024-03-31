'''
2. Given the set of positive integers `S` and the natural number `k`,
display one of the subsets of `S` which sum to `k`. For example,
if `S = { 2, 3, 5, 7, 8 }` and `k = 14`, subset `{ 2, 5, 7 }` sums to `14`.
'''

def InputSize():
    print("Enter the size of the set")
    x = input()
    x = int(x)
    return x

def InputTargetSum():
    print("Enter the target sum")
    x = input()
    x = int(x)
    return x

def InputSet():
    size = InputSize()
    print("Enter", size, "numbers")

    arr = []
    for i in range(size):
        arr.append(int(input()))
    return arr

def CheckResult(arr, targetSum):
    sum = 0
    for num in arr:
        sum += num
        
    if sum == targetSum:
        print(arr)
        exit()

def GenerateSubsets(idx, arr, ans, targetSum):
    for i in range(idx, len(arr)):
        ans.append(arr[i])
        CheckResult(ans, targetSum)

        GenerateSubsets(i + 1, arr, ans, targetSum)

        ans.pop()

def main():
    arr = InputSet()
    targetSum = InputTargetSum()
    ans = []

    GenerateSubsets(0, arr, ans, targetSum)

main()