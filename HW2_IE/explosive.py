n = int(input())

dpA = [0 for i in range(21)]
dpB = [0 for i in range(21)]

dpA[1] = dpB[1] = 1
for i in range(2, 21):
    dpA[i] = dpB[i - 1]
    dpB[i] = dpB[i - 1] + dpA[i - 1]
print(dpA[n] + dpB[n])
