N = int(input())
M = int(input())
INF = int(1e9)
Map = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    Map[i][i] = 0

for _ in range(M): 
    start, end, d = list(map(int, input().split()))
    Map[start][end] = min(Map[start][end], d)

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            Map[i][j] = min(Map[i][j], Map[i][k]+Map[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if Map[i][j] == INF:
            Map[i][j] = 0
    print(*Map[i][1:], sep=" ")