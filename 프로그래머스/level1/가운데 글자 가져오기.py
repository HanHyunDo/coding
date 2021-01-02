def solution(x):
    a = len(x)
    if a % 2 == 0:
        return x[(a//2)-1:(a//2)+1]
    else:
        return x[a//2]
