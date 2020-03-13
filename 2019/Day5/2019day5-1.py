import numpy as np
import Intcode as ic

opcodes = np.genfromtxt("2019day5.csv", delimiter=",", dtype=int)

x = ic.Intcode(opcodes)
