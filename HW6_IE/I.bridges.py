import sys
sys.setrecursionlimit(10 ** 6)
f = open('input.txt')
n, m = map(int, f.readline().split())
gr = [[] for i in range(n + 1)]

dic = dict()
cnt = 0
for line in f.readlines():
    cnt += 1
    v, u = map(int, line.split())
    gr[u].append(v)
    gr[v].append(u)
    dic[(u,v)] = cnt
    dic[(v,u)] = cnt
used = [0 for i in range(n + 1)]
tin = [0 for i in range(n + 1)]
up = [0 for i in range(n + 1)]
timer = 0
ans = set()
# points = set()
# print(gr)
def dfs(v: int, p:int = -1) -> None:
    global used, ans, timer, tin, up
    timer += 1
    tin[v] = timer
    up[v] = timer
    used[v] = 1
    # cnt = 0
    for to in gr[v]:
        if to == p:
            continue
        if used[to] == 0:
            dfs(to, v)
            # cnt += 1
            up[v] = min(up[v], up[to])
            if tin[v] < up[to]:
                # print()
                ans.add(dic.get((v,to)))
            # if tin[v] <= up[to] and p != -1:
            #     points.add(v)
        else:
            up[v] = min(up[v], tin[to])
    # if p == -1 and cnt > 1:
    #     points.add(v)
for i in range(1, len(gr)):
    dfs(i)
print(len(ans))
print(*sorted(ans), sep = ' ')
# print(points)
#
# 11 13
# 0 1
# 1 2
# 2 0
# 0 3
# 2 5
# 1 4
# 4 7
# 8 7
# 8 4
# 6 9
# 9 10
# 10 6
# 3 6