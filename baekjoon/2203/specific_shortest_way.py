# 정점과 간선의 정보가 주어졌을 때, v1, v2를 반드시 거쳐서 1번 노드에서 N번 노드까지의 최단 거리를 구해라.
INF = int(1e9)
N,E = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))
v1,v2 = map(int, input().split())

def get_nearest_node(visited, dist):
    min_ = INF
    index = 0
    for i in range(1, N+1):
        if not visited[i] and dist[i] < min_:
            min_ = dist[i]
            index = i
    return index

def dijkstra(start, end):
    dist = [INF for _ in range(N+1)]
    visited = [False] * (N+1)
    visited[start] = True
    dist[start] = 0
    for m, d in edges[start]:
        dist[m] = d
    for _ in range(N-1):
        now = get_nearest_node(visited, dist)
        visited[now] = True
        for m, d in edges[now]:
            dist[m] = min(dist[m], dist[now]+d)
    if dist[end] == INF:
        return -1
    return dist[end]

d1 = dijkstra(1, v1)
d2 = dijkstra(v1, v2)
d3 = dijkstra(v2, N)
d4 = dijkstra(1, v2)
d5 = dijkstra(v2, v1)
d6 = dijkstra(v1, N)
s1, s2 = d1+d2+d3, d4+d5+d6

answer = 0
if d1 != -1 and d2 != -1 and d3 != -1:
    if d4 != -1 and d5 != -1 and d6 != -1:
        # print('both', s1, s2)
        answer = min(s1, s2)
    else:
        # print('s1')
        answer = s1
elif d4 != -1 and d5 != -1 and d6 != -1:
    # print('s2')
    answer = s2
else:
    answer = -1
print(answer)