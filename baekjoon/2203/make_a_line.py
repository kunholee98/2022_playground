from collections import deque

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
result = []
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1
print(graph, degree)
for i,d in enumerate(degree):
    if i != 0 and d == 0:
        result.append(i)
q = deque(result)
while q:
    now = q.popleft()
    for n in graph[now]:
        degree[n] -= 1
        if degree[n] == 0:
            result.append(n)
            q.append(n)

print(' '.join(list(map(str, result))))