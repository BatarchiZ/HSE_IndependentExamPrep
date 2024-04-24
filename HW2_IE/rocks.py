







n = int(input())
w = [int(i) for i in input().split()]

ans = 2 ** 50
for mask in range(0, 2 ** n):
    s = str(bin(mask)[2:]).rjust(n, '0')
    w0 = 0
    w1 = 0
    for i in range(len(s)):
        if s[i] == '0':
            w0 += w[i]
        else:
            w1 += w[i]
    ans = min(ans, abs(w0 - w1))
print(ans)
