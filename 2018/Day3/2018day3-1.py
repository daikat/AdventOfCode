import numpy as np
fabric = np.zeros((1000,1000), dtype=np.uint16)

with open( "2018day3.data" ) as file:
    patterns = file.readlines()

    for pattern in patterns:
        a = pattern.split(' ')
        x,y = a[2].split(',')
        y = y.rstrip(':')
        x = int(x)
        y = int(y)
        m,n = a[3].split('x')
        n = n.rstrip()
        m = int(m)
        n = int(n)

        for index in range(n):
            fabric[x:x+m,y+index] += 1

accumulator = 0
for fullx in range(1000):
    for fully in range(1000):
        diffCount = 0
        if fabric[fullx,fully] > 1:
            accumulator += 1

print(accumulator)