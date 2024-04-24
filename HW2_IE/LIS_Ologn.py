

n,a1,k,b,m = map(int, input().split())

arr = [a1]
for i in range(1, n):
    arr.append((arr[i - 1]*k + b)%m)


inf = 2**64
dp = [inf for i in range(n + 1)]
dp[0] = -inf
dp[1] = a1
for i in range(2, n + 1):
    key = arr[i - 1]
    l = 0
    r = n + 1
    while l + 1 < r:
        mid = (l + r)//2
        if(dp[mid] < key):
            l = mid
        else:
            r = mid
    dp[r] = key

# print(dp)
counter = 0
for i in dp:
    if abs(i) != inf:
        counter += 1
print(counter)

