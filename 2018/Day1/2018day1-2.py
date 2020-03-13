frequency = 0
frequencies = [ 0 ]
found = 0
iteration = 0

while found < 1:
    with open( "2018day1.data" ) as file:
        print(iteration)
        iteration += 1
        deltas = file.readlines()

        for line in deltas:
            line = line.rstrip('\n')
            delta = int(line)
            frequency += delta
            if frequency in frequencies:
                found = 1
                print (frequency)
                break
            else:
                frequencies.append(frequency)


#print (frequencies)

