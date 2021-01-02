n = 121
def solution(n):
    for i in range(1, n+1):
        if n / i*i == 1:
            return (i+1)  * (i+1)
        elif i * i > n:
            return -1

    
print(solution(121))

#### 못풀었음
