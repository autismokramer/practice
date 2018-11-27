import random

def veryRandom(num):
    if num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return 'wow number 4'

r = random.randint(1,4)

 # veryRandom(r)
print(veryRandom(r))
