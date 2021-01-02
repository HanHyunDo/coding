def solution(arr1, arr2):
    my_list = []
    for a, b in zip(arr1, arr2):
        my_list_1 = []
        for i in range(len(a)):
            my_list_1.append(a[i] + b[i])
            if i == len(a)-1:
                my_list.append(my_list_1)
    return my_list


print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
