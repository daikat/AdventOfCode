import numpy as np
import re

units = ['[Aa]', '[Bb]', '[Cc]', '[Dd]', '[Ee]', '[Ff]', '[Gg]', '[Hh]', '[Ii]', '[Jj]', '[Kk]', '[Ll]', '[Mm]', '[Nn]', '[Oo]', '[Pp]', '[Qq]', '[Rr]', '[Ss]', '[Tt]', '[Uu]', '[Vv]', '[Ww]', '[Xx]', '[Yy]', '[Zz]']
unitScores = np.zeros(26, dtype=np.uint32)

unitIndex = 0
for idx, unit in enumerate(units):
    print("===================================== ", unitIndex)
    print("unit = ", unit)
    with open( "2018day5.data" ) as file:
        polymer = file.read()
        polymer = re.sub(unit, '', polymer)
        print(len(polymer))
        polymerList = np.array(list(polymer))
        i = int(0)
        while i < (len(polymerList)-1):
            #print(len(polymerList))
            if polymerList[i].isupper() and polymerList[i+1].islower():
                if polymerList[i].lower() == polymerList[i+1]:
                    reaction = [i, i+1]
                    polymerList = np.delete(polymerList, reaction)
                    if i > 0:
                        i -= 1
                else:
                    i += 1
            elif polymerList[i].islower() and polymerList[i+1].isupper():
                if polymerList[i].upper() == polymerList[i+1]:
                    reaction = [i, i+1]
                    polymerList = np.delete(polymerList, reaction)
                    if i > 0:
                        i -= 1
                else:
                    i += 1
            else:
                i += 1
    unitScores[unitIndex] = len(polymerList)
    unitIndex += 1
    print(unitScores)

np.savetxt('test.out', unitScores)
print("polymerList = ", polymerList)
print("len(polymerList) = ", len(polymerList))
