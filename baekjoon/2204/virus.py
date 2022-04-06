from collections import deque
from copy import deepcopy

N,M = map(int, input().split())
virus = []
graph = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 2:
            virus.append((i,j))
    graph.append(lst)

def Wall(graph, cnt):
    g = deepcopy(graph)
    result = 0
    if cnt == 0:
        return BFS(g)
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                g[i][j] = 1
                result = max(result, Wall(g, cnt-1))
                g[i][j] = 0
    return result

def BFS(g):
    q = deque(virus)
    dij = [(0,1), (1,0), (0,-1), (-1,0)]
    cnt = 0
    while q:
        i,j = q.popleft()
        for di, dj in dij:
            if 0<=i+di<N and 0<=j+dj<M and g[i+di][j+dj] == 0:
                g[i+di][j+dj] = 2
                q.append((i+di, j+dj))
    for lst in g:
        for c in lst:
            if c == 0:
                cnt += 1
    return cnt

print(Wall(graph,3))