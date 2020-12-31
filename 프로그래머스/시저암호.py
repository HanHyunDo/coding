# # def solution(s, n):
# a = 'abcdefghijklmnopqrstuvwxyz'
# b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# c = [i for i in a]
# d = [y for y in b]
# print(c[25])
########## 아직 못풀었음

def solution(s, n):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c = [i for i in a]
    d = [y for y in b]

    answer = ''

    try:
        for i in s:
            if ord(i) == 32:
                answer += i
            elif c.index(i) + n >= 25:
                answer += c[(c.index(i)+n) - 25]
            elif d.index(i) + n >= 25:
                answer += d[(d.index(i)+n) - 25]
            else:
                answer += chr(ord(i) + n)
        return answer
    except:
        pass

print(solution('AB', 1))
