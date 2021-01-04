def solution(strings, n):
    a = sorted([(i,(i[n])) for i in strings], key = lambda x : (x[1], x[0]))
    return [i[0] for i in a]



print(solution(['abce', 'abcd', 'cdx'], 1))
