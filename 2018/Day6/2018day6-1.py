import numpy as np

nearest = 0 # nearest coordinate 
delta = 1 # Manhattan distance sum
# xmax, ymax = 353, 358
#xmax = 353
#ymax = 358
xmax = 10
ymax = 10
space = np.zeros((xmax, ymax, 2), dtype=np.uint32)

# set max Manhattan distance for comparison
for x in range(xmax):
    for y in range(ymax):
        space[x, y, nearest] = 1000
        space[x, y, delta] = 1000

#with open( "2018day6.data" ) as file:
with open( "2018day6sample.data" ) as file:
    points = list(file.read().splitlines())
    pointIdx = list(np.arange(len(points)))

for x1 in range(xmax):
    for y1 in range(ymax):
        idx = 0
        for point in points:
            x2,y2 = point.split(', ')
            x2 = int(x2)
            y2 = int(y2)
            manDist = abs(x1 - x2) + abs(y1 - y2)
            if manDist < space[x1, y1, delta]:
                space[x1, y1, nearest] = idx
                space[x1, y1, delta] = manDist
            elif manDist == space[x1, y1, delta]:
                space[x1, y1, nearest] = 1000
            idx += 1

# Remove row infinite entries
print(pointIdx)
for x in range(xmax):
    if space[x, 0, nearest] in pointIdx:
        pointIdx.remove(space[x, 0, nearest])
    if space[x, ymax-1, nearest] in pointIdx:
        pointIdx.remove(space[x, ymax-1, nearest])

# Remove column infinite entries
for y in range(ymax):
    if space[0, y, nearest] in pointIdx:
        pointIdx.remove(space[0, y, nearest])
    if space[xmax-1, y, nearest] in pointIdx:
        pointIdx.remove(space[xmax-1, y, nearest])
print(pointIdx)

pointAccum = np.zeros(len(points), dtype=np.uint32)
for x in range(xmax):
    for y in range(ymax):
        temp = space[x, y, nearest]
        if(temp == 1000):
            continue
        else:
            pointAccum[temp] += 1

print(pointAccum)
maxTotal = 0
for i in pointIdx:
    print(i)
    if pointAccum[i] > maxTotal:
        maxTotal = pointAccum[1]
print(maxTotal)
