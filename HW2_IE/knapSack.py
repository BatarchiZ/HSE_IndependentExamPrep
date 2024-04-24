#
#
#
#






S,n = map(int, input().split())
w = [int(i) for i in input().split()]

dp = [0 for i in range(S)]
for i in range(S):
    for j in w:
        if i - j >= 0:
            dp[i] = max(dp[i], dp[i - j] + j)
# print(*dp)
print(max(dp[:]))


# 10 2
# 4 8
