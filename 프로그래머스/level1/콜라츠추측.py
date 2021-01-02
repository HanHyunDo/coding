def num(n):
    if n % 2 == 0:
        return n // 2
    elif n % 2 != 0:
        return n * 3 + 1

def solution(n):
    cnt = 0
    while (n != 1):
        if cnt < 500:
            n = num(n)
            cnt += 1
        else:
            cnt = -1
            break
    return cnt

print(solution(626331))
