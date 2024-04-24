n = int(input())
cost = [int(x) for x in input().split()]
dp = [0 for i in range(200)]
if n == 1:
    print(cost[0])
else:
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i-2:i]) + cost[i]
    print(dp[n - 1])