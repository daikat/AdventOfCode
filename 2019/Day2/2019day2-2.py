import numpy as np
import Intcode as ic

# Modify computer data
for noun in range(100):
    for verb in range(100):
        opcodes = np.genfromtxt("2019day2.csv", delimiter=",", dtype=int)
        print(noun, verb)
        opcodes[1] = noun
        opcodes[2] = verb

        x = ic.Intcode(opcodes)

        if(x.data[0] == 19690720):
            print(noun, verb, 100 * noun + verb)
            quit()
