# 가장 큰 소인수 구하기
n = 600851475143
for i in range(2, n+1):
    while(n % i == 0):
        n /= i
        print(i)
        i += 1