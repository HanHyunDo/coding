def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i == ' ':
            answer += ' '
            cnt = 0
        elif cnt % 2 == 0:
            cnt += 1
            answer += i.upper()

        else:
            cnt += 1
            answer += i.lower()

    return answer

print(solution('ab cde a'))
