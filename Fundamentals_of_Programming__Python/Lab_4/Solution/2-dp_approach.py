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

def PrintResult(arr, mat, n, m):
    if mat[n][m] == False:
        print("There does not exist any subset for the given sum")
    else:
        ans = []

        while m != 0:
            while mat[n - 1][m] != False:
                n -= 1
            m -= arr[n - 1]
            ans.append(arr[n - 1])

        ans.reverse()
        print(ans)

def DP_Approach(arr, targetSum):
    # Initializing a matrix of (len(arr) + 1) rows and (targetSum + 1) columns
    dp = [[False for i in range(targetSum + 1)] for j in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        dp[i][0] = True

    for i in range(1, len(arr) + 1):
        for j in range(1, targetSum + 1):
            if arr[i - 1] - j > 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])

    PrintResult(arr, dp, len(arr), targetSum)

def main():
    arr = InputSet()
    targetSum = InputTargetSum()

    DP_Approach(arr, targetSum)

main()