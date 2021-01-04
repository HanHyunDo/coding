def solution(n, lost, reserve):
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
            # print(lost)
        elif i in lost:
            lost.remove(i)
            # print(lost)
        elif i+1 in lost:
            lost.remove(i+1)
            # print(lost)

    return n - len(lost)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3, [3], [1]))

print(solution(5,[2,3,4],[3,4,5]))