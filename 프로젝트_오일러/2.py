# 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합

def fibo(x):
    answers = [1, 2]
    while answers[-2] + answers[-1] < x:
        c = answers[-2] + answers[-1]
        answers.append(c)

    return sum(list(filter(lambda x : x % 2 == 0, answers)))
print(fibo(4000000))
