# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?

# a = [i for i in range(1, 1001) if i % 3 == 0 or i % 5 == 0]
# b = sum(set(a))
# print(b)

a = [i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]
print(sum(a))
print(sum(set(a)))