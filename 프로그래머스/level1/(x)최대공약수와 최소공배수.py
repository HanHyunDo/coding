def pre(n):
    return n*2
def solution(n, m):
    while m % n == 0:
        if m % n == 0:
            return [n, m]
        elif n > m:
            m = pre(m)
        else:
            n = pre(n)

print(solution(2,5))
            
