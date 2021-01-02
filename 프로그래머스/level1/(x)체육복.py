def solution(n, lost, reserve):
    person = [i for i in range(1, n+1)]
    cnt = 0
    for i in reserve:
        if i in lost:
            cnt += 1
        elif i - 1 or i + 1 in lost:
            lost.pop(cnt)
            reserve.pop(reserve.index(i))
        else:
            person.pop(cnt)
            cnt += 1
            
    return len(person) if lost == [] else len(person) - len(lost)

print(solution(5,[2,4],[3]))
        
            