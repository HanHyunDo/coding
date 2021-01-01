def solution(n):
    answer = ''
    a = list(reversed(sorted([i for i in str(n)])))
    for i in a:
        answer += i
    return int(answer)

print(solution(118372))
