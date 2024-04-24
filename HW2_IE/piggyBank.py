



wMin, wMax = map(int, input().split())
w = wMax - wMin
n = int(input())

pA = [0] + [0 for i in range(n)]
wA = [0] + [0 for i in range(n)]

for i in range(1, n + 1):
    pA[i], wA[i] = map(int, input().split())


dp = [[-1 for i in range(w + 1)] for j in range(n + 1)]
dpMin = [[2**64 for i in range(w + 1)] for j in range(n + 1)]
dp[0][0] = 0
dpMin[0][0] = 0
maxW = -2**32
minW = 2**32
for i in range(1, n + 1):
    wi = wA[i]
    for j in range(w + 1):
        dp[i][j] = dp[i - 1][j]
        dpMin[i][j] = dpMin[i - 1][j]
        if j - wi >= 0 and dp[i][j - wi] >= 0:
            # print(j - wi)
            dp[i][j] = max(dp[i][j - wi] + pA[i], dp[i][j])
            dpMin[i][j] = min(dpMin[i][j - wi] + pA[i], dpMin[i][j])
        if(j == w and dp[i][j] != -1):
            maxW = max(maxW, dp[i][j])
            minW = min(minW, dpMin[i][j])

# print(*dp, sep='\n')
# # print()
# print(*dpMin, sep='\n')
if maxW != -2**32:
    print(minW, maxW)
else:
    print("This is impossible.")
# 1 1
# 1
# 1 1