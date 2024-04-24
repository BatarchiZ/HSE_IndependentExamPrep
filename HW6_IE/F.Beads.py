def dfs(v):
    global used, ans, path
    used[v] = 1
    path.append(v)
    for to in gr[v]:
        if used[to] == 0:
            dfs(to)
    if len(ans) < len(path):
        ans = path[:]
    path.pop()


f = open('input.txt')
n = int(f.readline())
gr = [[] for i in range(n + 1)]

if n != 1:
    for line in f.readlines():
        v, u = [int(x) for x in line.split()]
        gr[u].append(v)
        gr[v].append(u)
    used = [0 for i in range(n + 1)]
    path = []
    ans = []
    dfs(1)
    used = [0 for i in range(n + 1)]
    dfs(ans[-1])
    print(len(ans))
else:
    print(1)
