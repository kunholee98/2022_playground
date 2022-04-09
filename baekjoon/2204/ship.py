N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
indice= [0] * N
visited = [0] * M

def find_next(i, crane):
    while i < M:
        if not visited[i] and boxes[i] <= crane:
            visited[i] = 1
            return i
        i += 1
    return -1

def Solution():
    cnt = 0
    if cranes[0] < boxes[0]:
        return -1
    while sum(visited) < M:
        for i, crane in enumerate(cranes):
            next_idx = find_next(indice[i],crane)
            if next_idx == -1:
                cranes.pop(i)
                indice.pop(i)
            else:
                indice[i] = next_idx
        cnt += 1
    return cnt
print(Solution())