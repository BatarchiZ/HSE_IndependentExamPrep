





m, n = map(int, input().split())

cost = [[int(x) for x in input().split()] for y in range(m)]

dp = [[0 for x in range(n)] for y in range(m)]

dp[0][0] = cost[0][0]
for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = cost[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + cost[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + cost[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]

# print(*dp, sep= '\n')
print(dp[-1][-1])
