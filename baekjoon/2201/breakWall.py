from collections import deque
N,M = list(map(int, input().split()))
Map = []
list1 = []
for i in range(N):
    lst =list( map(int, list(input())))
    for j, num in enumerate(lst):
        if num == 1:
            list1.append((i,j))
    Map.append(lst)

q = deque([(0,0)])
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True
fromStart = [[0 for _ in range(M)] for _ in range(N)]
fromEnd = [[0 for _ in range(M)] for _ in range(N)]

drc = [(1,0), (-1,0), (0,1), (0,-1)]
while q:
    r,c = q.popleft()
    if Map[r][c] == 0:
        for dr, dc in drc:
            cr, cc = r+dr, c+dc
            if 0<=cr<N and 0<=cc<M and not visited[cr][cc]:
                q.append((cr,cc))
                visited[cr][cc] = True
                fromStart[cr][cc] = fromStart[r][c] + 1
print(fromStart)

q = deque([(N-1, M-1)])
visited = [[False for _ in range(M)] for _ in range(N)]
visited[N-1][M-1] = True
while q:
    r,c = q.popleft()
    if Map[r][c] == 0:
        for dr, dc in drc:
            cr, cc = r+dr, c+dc
            if 0<=cr<N and 0<=cc<M and not visited[cr][cc]:
                q.append((cr,cc))
                visited[cr][cc] = True
                fromEnd[cr][cc] = fromEnd[r][c] + 1
print(fromEnd)

distList = []

for r,c in list1:
    if fromStart[r][c] and fromEnd[r][c]:
        distList.append(fromStart[r][c]+fromEnd[r][c]+1)
if fromStart[N-1][M-1]:
    distList.append(fromStart[N-1][M-1]+1)
print(distList)

if distList:
    print(min(distList))
elif N==M and N == 1:
    print(1)
else:
    print(-1)
