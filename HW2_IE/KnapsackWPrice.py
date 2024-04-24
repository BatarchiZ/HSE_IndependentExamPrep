
n, m = map(int, input().split())
w = [0] + [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]
dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    wi = w[i]
    for j in range(0, m + 1):
        dp[i][j] = dp[i - 1][j]
        if j - wi >= 0 and dp[i - 1][j - wi] + c[i] > dp[i][j] and dp[i - 1][j - wi] != -1:
            dp[i][j] = dp[i - 1][j - wi] + c[i]
# print(*dp, sep='\n')

max_ = 0
for i in dp:
    for j in i:
        max_ = max(max_, j)
print(max_)
