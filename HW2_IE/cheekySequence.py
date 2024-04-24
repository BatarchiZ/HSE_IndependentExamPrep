n = int(input())

dp = [0 for i in range(1001)]
dp[0] = 1
dp[1] = 1
for i in range(2, 1001, 2):
    dp[i] = dp[i // 2] + 1
    if i != 2:
        dp[i - 1] = dp[i] + dp[i // 2 - 1]
print(dp[n])
