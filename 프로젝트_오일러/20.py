x = 1
for i in range(1, 101):
    x *= int(i)
b = []
for y in str(x):
    b.append(int(y))

c = sum(list(filter(lambda x : x, b)))
print(c)