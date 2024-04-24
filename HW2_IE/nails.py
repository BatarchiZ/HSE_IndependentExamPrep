n = int(input())
N = [int(x) for x in input().split()]
N.append(0)
N.sort()
dp = [0 for i in range(1000)]
# print(N)
dp[2] = N[2] - N[1]
if(n != 2):
    dp[3] = N[3] - N[1]
# print(dp)
for i in range(4, len(N)):
    dp[i] = min(dp[i - 2], dp[i - 1]) + N[i] - N[i - 1]
    # print(dp)
print(dp[n])


# 6
# 3 4 6 12 13 14
# 6
# 3 4 6 9 13 14