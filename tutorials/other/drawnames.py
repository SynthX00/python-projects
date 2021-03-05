import random

names = ['daniel','david','diogo','ucrania','joao']

i = (len(names))
print(i)
while i >= 1:
    
    n = random.randrange((len(names)))
    print(names[n])
    names.pop(n)
    i = i-1
    print(i)