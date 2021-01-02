def solution(arr1, arr2):
    cnt = 0
    for i in arr1:  # i = arr[]
        for y in len(i):
            arr2[cnt][y] = arr1[cnt][y] + arr2[cnt][y]
        cnt += 1
    return arr2

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))

# a = [[1,2],[2,3]]
# print(a[0][0])