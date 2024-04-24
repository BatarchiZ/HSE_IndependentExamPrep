n = int(input())
dp = [0 for i in range(1002)]
dp[0] = 1
dp[1] = 1
for i in range(2, 1001):
    if i % 2 == 0:
        dp[i] = dp[i // 2] + dp[i // 2 - 1]
    else:
        dp[i] = dp[i // 2] - dp[i // 2 - 1]
    # print(*dp, sep= " ")

print(dp[n])
