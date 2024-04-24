





n = int(input())
notes = [int(i) for i in input().split()]
w = int(input())

dp = [2**32 for i in range(w + 1)]
dp[0] = 0
p = [0 for i in range(w+1)]
for i in range(1, w + 1):
    for note in notes:
        if i - note >= 0:
            val = dp[i]
            dp[i] = min(dp[i - note] + 1, dp[i])
            if dp[i] != val:
                p[i] = i - note

if(dp[w] != 2**32):
    print(dp[w])
    # print(p)
    i = w
    ans = []
    while i != 0:
        ans.append(i - p[i])
        i = p[i]

    print(*ans)
else:
    print(-1)

