







x, y = map(int, input().split())
# x-=1
y-=1
dp = [[-1 for j in range(10)] for i in range(8)]

dp[y][x] = 1
# print(*dp, sep="\n")
for i in range(y + 1, 8):
    for j in range(1, 9):
        if dp[i - 1][j - 1] != -1 and dp[i - 1][j + 1] != -1:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        elif dp[i - 1][j + 1] != -1:
            dp[i][j] = dp[i - 1][j + 1]
        elif  dp[i - 1][j - 1] != -1:
            dp[i][j] = dp[i - 1][j - 1]

sum = 0
for i in dp[7]:
    if i != -1:
        sum += i
print(sum)



