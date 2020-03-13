import numpy as np
xymax = 300
fuelCells = np.zeros((xymax,xymax), dtype=int)
sums = np.zeros((xymax-2, xymax-2), dtype=int)

for x in range(xymax):
    for y in range(xymax):
        fuelCells[x, y] = ((((((x+11) * (y+1)) + 5153) * (x+11)) / 100) % 10) - 5

for x in range(0, xymax-2):
    for y in range(0, xymax-2):
        cellgroup = fuelCells[x:x+3, y:y+3]
        sums[x,y] = np.sum(cellgroup)

cellx, celly = np.where(sums == np.amax(sums))
print(cellx+1, ",", celly+1)
