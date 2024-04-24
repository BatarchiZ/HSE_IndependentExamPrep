n = int(input())

RUB = [0. for i in range(n+1)]
USD = [0. for i in range(n+1)]
EU = [0. for i in range(n+1)]

RUB[0] = 100. * 100 * 100 * 100 * 100
U = [0. for i in range(n + 1)]
E = [0. for i in range(n + 1)]
for i in range(1, n + 1):
    U[i], E[i] = map(float, input().split())
U = [i * 100000 for i in U]
E = [i * 100000 for i in E]

for i in range(1, n + 1):
    RUB[i] = max(RUB[i - 1], USD[i - 1] * U[i], EU[i - 1] * E[i])
    USD[i] = max(USD[i - 1], RUB[i - 1] / U[i])
    EU[i] = max(EU[i - 1], RUB[i - 1] / E[i])

print(f'{RUB[n]/100/100/100/100:.2f}')
