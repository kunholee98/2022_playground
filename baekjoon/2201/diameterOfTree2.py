from collections import deque
V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    lst = list(map(int,input().split()))
    now = lst[0]
    for i, n in enumerate(lst):
        if i == 0:
            continue
        if i % 2 == 1 and n != -1:
            end = n
            dist = lst[i+1]
            tree[now].append((end,dist))
# print(tree)

distFromRoot = [0 for _ in range(V+1)]

def BFS(start):
    q = deque([(start,0)])
    visited = [False for _ in range(V+1)]
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