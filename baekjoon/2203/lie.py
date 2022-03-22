from collections import deque
N,M = map(int, input().split())
known = list(map(int, input().split()))
known.pop(0)
parties = []
in_party = [[] for _ in range(N+1)]
for i in range(M):
    party = list(map(int, input().split()))
    party.pop(0)
    parties.append(party)
    for person in party:
        in_party[person].append(i)

checked = [False] * (M+1)
cant_lie = []
q = deque()
for p in known:
    q.extend(in_party[p])
q = deque(set(q))
while q:
    known_party_num = q.popleft()
    if not checked[known_party_num]:
        cant_lie.append(known_party_num)
        checked[known_party_num] = True
        for person in parties[known_party_num]:
            if not person in known:
                known.append(person)
            q.extend(in_party[person])

print(M-len(cant_lie))