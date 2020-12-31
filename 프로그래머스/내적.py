def solution(a, b):
    cnt = 0
    for i, z in zip(a, b):
        cnt += i * z
    return cnt

print(solution([1,2,3,4],[-3,-1,0,2]))
