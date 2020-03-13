import numpy as np
xymax = 300
fuelCells = np.zeros((xymax,xymax), dtype=int)

for x in range(xymax):
    for y in range(xymax):
        fuelCells[x, y] = ((((((x+11) * (y+1)) + 5153) * (x+11)) / 100) % 10) - 5

summax = 0
nmax = 0
xmax = 0
ymax = 0
for n in range(xymax):
    for x in range(0, xymax-n):
        for y in range(0, xymax-n):
            cellgroup = fuelCells[x:x+n, y:y+n]
            cellsum = np.sum(cellgroup)
            if cellsum > summax:
                summax = cellsum
                xmax = x
                ymax = y
                nmax = n
    if n%10 == 0:
        print(n)


print("xmax =", xmax, "ymax = ", ymax, "nmax =", nmax)
