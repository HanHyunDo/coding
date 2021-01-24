# 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합

def fibo(x):
    answers = [1, 2]
    while answers[-2] + answers[-1] < x:
        c = answers[-2] + answers[-1]
        answers.append(c)
    d = 0
    i = 0
    while i <= len(answers):
        if answers[-1] == answers[i]:
            if answers[i] % 2 == 0:
                d += answers[i]
                break
        if answers[i] % 2 == 0:
            d += answers[i]
            i += 1
        else:
            i += 1
    return d
print(fibo(4000000))
