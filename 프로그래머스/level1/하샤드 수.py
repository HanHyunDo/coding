def solution(arr):
    return True if arr % sum([int(i) for i in str(arr)]) == 0 else False

print(solution(11))
