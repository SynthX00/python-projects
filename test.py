

a = []
print(len(a))

for i in range(0, 10, 3):
    a.append(i)
    print(a)

del(a[2])
print(a)
del(a[2])
print(a)