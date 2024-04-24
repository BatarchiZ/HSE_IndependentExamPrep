n = int(input())

a = [0 for i in range(5001)]
b = [0 for i in range(5001)]
c = [0 for i in range(5001)]

for i in range(1, n + 1):
    a[i], b[i], c[i] = map(int, input().split())

dp = [0 for i in range(5001)]
dp[1] = a[1]
dp[2] = min(a[2] + a[1], b[1])

for i in range(3, 5001):
    dp[i] = min(a[i] + dp[i-1], b[i - 1] + dp[i-2], c[i-2] + dp[i-3])
print(dp[n])
