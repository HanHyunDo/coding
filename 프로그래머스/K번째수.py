def solution(array, commands):
    answers = []
    for i in commands:
        first_array = array[i[0]-1:i[1]]
        sort_first = sorted(first_array)
        sort_first = sort_first[i[2]-1]
        answers.append(sort_first)
    return answers