def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b, a+1):
            answer += i
        return answer
    elif b > a:
        for y in range(a, b+1):
            answer += y
        return answer
    else:
        return a
