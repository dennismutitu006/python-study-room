# Python program for the above approach

# Recursive function to count the numeber of distinct ways
# to make the sum by using n coins


def count(coins, sum, n, dp):
  # Base Case
    if (sum == 0):
        dp[n][sum] = 1
        return dp[n][sum]

     # If number of coins is 0 or sum is less than 0 then there is no way to make the sum.
    if (n == 0 or sum < 0):
        return 0

     # If the subproblem is previously calculated then simply return the result
    if (dp[n][sum] != -1):
        return dp[n][sum]

      # Two options for the current coin

    dp[n][sum] = count(coins, sum - coins[n - 1], n, dp) + \
        count(coins, sum, n - 1, dp)

    return dp[n][sum]


# Driver code
if __name__ == '__main__':
    tc = 1
    while (tc != 0):
        n = 3
        sum = 5
        coins = [1, 2, 3]
        dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
        res = count(coins, sum, n, dp)
        print(res)
        tc -= 1

