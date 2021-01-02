def solution(x):
    my_list = []
    while x != []:
        for i in range(len(x)-1):
            my_list.append(x[0] + x[i+1])
        x.pop(0)
    return sorted(list(set(my_list)))