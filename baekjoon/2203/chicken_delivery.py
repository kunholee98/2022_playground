from copy import deepcopy
INF = 101
N,M = map(int, input().split())
map_ = []
chickens = []
houses = []
cnt = 0
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 1:
            houses.append((i,j))
            cnt += 1
        elif lst[j] == 2:
            chickens.append((i,j))
dists = [INF]*cnt
cnt = 0
def dist(a1,b1,a2,b2):
    return abs(a1-a2)+abs(b1-b2)

def calc(ds,a2,b2):
    ds_copy = deepcopy(ds)
    for i, house in enumerate(houses):
        a1,b1 = house
        ds_copy[i] = min(ds[i], dist(a1,b1,a2,b2))
    return ds_copy

def recursion(ds, m, cs):
    result = sum(ds)
    if m == 0:
        return result
    for i in range(len(cs)):
        a2, b2 = cs[i]
        result = min(result, recursion(calc(ds,a2,b2), m-1, cs[i+1:]))
    return result

print(recursion(dists, M, chickens))
