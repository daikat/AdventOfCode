with open( "2019day3.data" ) as file:
    wires = list(file.read().splitlines())

x = 0
y = 0
nodes = []
wire = wires[0].split(",")
for i in range(len(wire)):
    direction = wire[i][:1]
    length = int(wire[i][1:])
    for j in range(length):
        if(direction == 'R'):
            x += 1
        elif(direction == 'L'):
            x -= 1
        elif(direction == 'U'):
            y += 1
        elif(direction == 'D'):
            y -= 1
        nodes.append([x, y])

x = 0
y = 0
nodes2 = []
manDist = 65536
wire = wires[1].split(",")
print(len(wire))
for i in range(len(wire)):
    print(i)
    direction = wire[i][:1]
    length = int(wire[i][1:])
    for j in range(length):
        if(direction == 'R'):
            x += 1
        elif(direction == 'L'):
            x -= 1
        elif(direction == 'U'):
            y += 1
        elif(direction == 'D'):
            y -= 1
        try:
            index = nodes.index([x, y])
            print('x =', x, 'y =', y, 'index =', index)
        except ValueError:
            continue
        else:
            newManDist = abs(x) + abs(y)
            if(newManDist < manDist):
                manDist = newManDist
print(manDist)
