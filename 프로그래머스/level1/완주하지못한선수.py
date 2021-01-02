def solution(participant, completion):
    participant_dict = {}
    answer = ''
    for i in participant:
        if i in participant_dict:
            participant_dict[i] += 1
        else:
            participant_dict[i] = 1

    for y in completion:
        if y in participant_dict:
            participant_dict[y] -= 1
        else:
            participant_dict[y] = 1
            
    for z in participant_dict.items():
        if z[1] > 0:
            answer += z[0]
    return answer