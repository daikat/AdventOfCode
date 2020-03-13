with open( "2019day3.data" ) as file:
    wires = list(file.read().splitlines())

x = 0
y = 0
steps = 0
nodes = {}
wire = wires[0].split(",")
for i in range(len(wire)):
    direction = wire[i][0]
    length = int(wire[i][1:])
    for j in range(length):
        steps += 1
        if(direction == 'R'):
            x += 1
        elif(direction == 'L'):
            x -= 1
        elif(direction == 'U'):
            y += 1
        elif(direction == 'D'):
            y -= 1
        nodes[x,y] = steps
#print(nodes)

x = 0
y = 0
steps = 0
minSteps = 999999999999
wire = wires[1].split(",")
#print(len(wire))
for i in range(len(wire)):
    direction = wire[i][0]
    length = int(wire[i][1:])
    for j in range(length):
        steps += 1
        if(direction == 'R'):
            x += 1
        elif(direction == 'L'):
            x -= 1
        elif(direction == 'U'):
            y += 1
        elif(direction == 'D'):
            y -= 1
        if(x,y) in nodes:
            print("Wire1 steps", nodes[x,y], "Steps", steps)
            newSteps = nodes[x,y] + steps
            if(newSteps < minSteps):
                minSteps = newSteps
print("minSteps =", minSteps)
