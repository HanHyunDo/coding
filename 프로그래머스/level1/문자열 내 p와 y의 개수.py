def solution(s):
    answer = ''
    for i in reversed(sorted(s)):
        answer += i
    return answer
