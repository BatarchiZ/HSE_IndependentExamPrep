import sys
sys.setrecursionlimit(100001)

f = open('input.txt')
n, m = [int(x) for x in f.readline().split()]


gr = [[] for i in range(n)]

for line in f.readlines():
   u, v = [int(x) for x in line.split()]
   u -= 1
   v -= 1
   gr[u].append(v)

used = [0 for i in range(n)]

path = []
ans = []

def dfs(v: int) -> None:
   global path, ans
   used[v] = 1
   path.append(v)
   for to in gr[v]:
       if used[to] == 1:
           ans = path[:] + [to]
       elif used[to] == 0:
           dfs(to)
   used[v] = 2
   path.pop()

for i in range(n):
   if used[i] == 0:
       dfs(i)

if len(ans) > 0:
   print("YES")
   i = ans.index(ans[-1])
   ans = ans[i:-1]
   print(*[x + 1 for x in ans])
else:
   print("NO")