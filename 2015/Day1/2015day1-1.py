import numpy as np
floor = 0
index = 1

with open( "2015day1.data" ) as file:
	instructions = np.array(list(file.read()))

print(instructions)

for instruction in instructions:
    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1

    if floor < 0:
        break

    index += 1

print (floor)
print (index)

