n = int(input())

dp = [0 for i in range(10001)]
dp[0] = 1
dp[1] = 1
# dp[2] = 2
# print(0, dp[0])
# print(1, dp[1])

for i in range(2,10001):
    dp[i] = sum(dp[i-2:i])
    # print(i, dp[i])
number = str(dp[n])
print(number[-1])

# print(*dp, sep='\n')

