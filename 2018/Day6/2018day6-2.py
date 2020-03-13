import numpy as np

nearest = 0 # nearest coordinate 
deltaSum = 1 # Manhattan distance sum
# xmax, ymax = 353, 358
xmax = 353
ymax = 358
space = np.zeros((xmax, ymax), dtype=np.uint32)

with open( "2018day6.data" ) as file:
#with open( "2018day6sample.data" ) as file:
    points = list(file.read().splitlines())
 
maxSum = 10000
inRegion = 0
for x1 in range(xmax):
    for y1 in range(ymax):
        for point in points:
            x2,y2 = point.split(', ')
            x2 = int(x2)
            y2 = int(y2)
            manDist = abs(x1 - x2) + abs(y1 - y2)
            space[x1, y1] += manDist
        if space[x1, y1] < maxSum:
            inRegion += 1

print(space)
print(inRegion)
