import numpy as np
guardEntry = {}   # Ensure it acts as a dictionary

with open( "2018day4.data" ) as file:
    logs = file.readlines()

    guardNumber = 0
    asleep = 0
    awake = 0
    for log in logs:
        idx = log.find("Guard")
        if idx is not -1: # Then it is a Guard line
            temp = log.split('#')
            temp = temp[1].split(' ')
            guardNumber = temp[0]
        idx = log.find("asleep")
        if idx is not -1: # Guard is falling asleep
            temp = log.split(':')
            temp = temp[1].split(']')
            asleep = int(temp[0])
        idx = log.find("wakes")
        if idx is not -1: # Guard wakes up
            temp = log.split(':')
            temp = temp[1].split(']')
            awake = int(temp[0])
            naps = np.zeros(60, dtype=np.uint16)
            if guardNumber in guardEntry:
                naps = guardEntry[guardNumber]
            for index in range(asleep, awake):
                naps[index] += 1
            guardEntry[guardNumber] = naps

#print(guardEntry['3109'])
for key in guardEntry.keys():
    naps = guardEntry[key]
    total = np.sum(naps)    
    index = np.argmax(naps)
    frequency = naps[index]
    print("key =", key, ", total =", total, ", index =", index, ", frequency =", frequency)
#print(guardEntry)
#print(len(guardEntry))
