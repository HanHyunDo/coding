a = sum(i**2 for i in range(101))
b = sum(i for i in range(101)) ** 2
print(b - a)