from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _i in range(N+1)] # 편의를 위해 1개 더 추가
for i in range(M):
    x, y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(len(graph)):
    graph[i].sort()
dfs_check = [0] *(N+1)
dfs_route = []
bfs_check = [0] *(N+1)
bfs_route = []

def dfs(start):
    dfs_check[start] = 1
    dfs_route.append(start)
    for i in graph[start]:
        if dfs_check[i] == 0:
            dfs(i)
    return dfs_route

s = ''
for i in dfs(V):
    s += (str(i)+ ' ')
print(s)
# for i in dfs(V):
#     print(i, end= ' ')
  
    
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        if bfs_check[a] == 0:
            bfs_check[a] =1
            bfs_route.append(a)
            q.extend(graph[a])
    return bfs_route
s = ''
for i in bfs(V):
    s += (str(i)+ ' ')
print(s)