







n = int(input())
arr = [int(x) for x in input().split()]


dp = [1 for i in range(n)]
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if arr[i] % arr[j] == 0:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
# print(n - max(dp))
