def solution(arr, divisor):
    b = [-1]
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            b.append(arr[i])
    if len(b) == 1:
        return b
    else:
        b.pop(0)
        return sorted(b)
