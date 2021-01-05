def solution(numbers):
    a = sorted([str(i) for i in numbers], key=lambda x: x[0])
    return a

print(solution([6, 10, 2]))