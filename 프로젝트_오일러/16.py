a = 2**1000
c = []
for i in str(a):
    c.append(int(i))
b = sum(filter(lambda x : x, c))
print(b)