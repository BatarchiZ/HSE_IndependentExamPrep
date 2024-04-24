





n = int(input())
dp = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0:
            print(dp[i][j], end=' ')
    print()
# print(*dp, sep="\n")

