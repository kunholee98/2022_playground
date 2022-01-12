from collections import deque
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end, d = list(map(int, input().split()))
    tree[start].append((end, d))
    tree[end].append((start,d))

distFromRoot = [0 for _ in range(N+1)]

def BFS(start):
    q = deque([(start,0)])
    visited = [False for _ in range(N+1)]
    visited[start] = True
    while q:
        now, totalDist = q.popleft()
        distFromRoot[now] = totalDist
        lst = tree[now]
        for end, dist in lst:
            if not visited[end]:
                visited[end] = True
                q.append((end, totalDist+dist))
        
BFS(1)
BFS(distFromRoot.index(max(distFromRoot)))
print(max(distFromRoot))
