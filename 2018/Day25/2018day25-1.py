import sys
import re
from collections import deque

P = []
for line in open("2018day25.data").read().strip().split('\n'):
    w,x,y,z = map(int, re.findall('-?\d+', line))
    P.append((w,x,y,z))
E = [set() for _ in range(len(P))]
for i,(w1,x1,y1,z1) in enumerate(P):
    for j,(w2,x2,y2,z2) in enumerate(P):
        d = abs(w1-w2)+abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
        if d <= 3:
            E[i].add(j)

S = set()
ans = 0
for i in range(len(P)):
    if i in S:
        continue
    ans += 1
    Q = deque()
    Q.append(i)
    while Q:
        x = Q.popleft()
        if x in S:
            continue
        S.add(x)
        for y in E[x]:
            Q.append(y)
print(ans)