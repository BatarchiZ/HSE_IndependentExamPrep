r, c = map(int, input().split())

dp = [[0 for i in range(c + 4)] for j in range(r + 4)]

dp[2][2] = 1
# print(*dp, sep='\n')
# print()
# try:
for i in range(2, r + 2):
        for j in range(2, c + 2):
            if dp[i - 2][j - 1] != 0 and dp[i - 1][j - 2] != 0:
                dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]
            elif dp[i - 2][j - 1] != 0:
                dp[i][j] = dp[i - 2][j - 1]
            elif dp[i - 1][j - 2] != 0:
                dp[i][j] = dp[i - 1][j - 2]
# except IndexError:
#     pass
    #
# print(*dp, sep='\n')
print(dp[r + 1][c  + 1])