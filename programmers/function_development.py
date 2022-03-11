def solution(progresses, speeds):
    answer = []
    i = 0
    while i < len(progresses):
        for j in range(len(progresses)):
            progresses[j] += speeds[j]
        c = 0
        for k in range(i,len(progresses)):
            if progresses[k] >= 100:
                i += 1
                c += 1
            else:
                break
        if c != 0:
            answer.append(c)
    return answer