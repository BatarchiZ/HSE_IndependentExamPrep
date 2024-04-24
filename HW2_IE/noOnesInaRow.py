n = int(input())
d0 = [0 for i in range(101)]
d1 = [0 for i in range(101)]
d0[1] = d1[1] = 1
for i in range(2, n + 1):
    d0[i] = d0[i - 1] + d1[i - 1]
    d1[i] = d0[i - 1]
print(d0[n] + d1[n])