n = int(input())

dpA = [0 for i in range(21)]
dpB = [0 for i in range(21)]
dpC = [0 for i in range(21)]

dpA[1] = dpB[1] = dpC[1] = 1
for i in range(2, 21):
    dpA[i] = dpB[i - 1] + dpC[i - 1]
    dpB[i] = dpC[i] = dpA[i - 1] + dpB[i - 1] + dpC[i - 1]

print( dpA[n] + dpB[n] + dpC[n])