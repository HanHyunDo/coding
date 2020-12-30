def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False

print(solution('1234'))

# a = 'a123'
# print(a.isdigit())