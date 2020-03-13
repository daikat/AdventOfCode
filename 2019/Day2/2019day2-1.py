import numpy as np
import Intcode as ic

opcodes = np.genfromtxt("2019day2.csv", delimiter=",", dtype=int)

# Restore computer data
opcodes[1] = 12
opcodes[2] = 2

x = ic.Intcode(opcodes)

print(x.data[0])