fuel = 0

with open( "2019day1.data" ) as file:
    masses = file.readlines()

    for line in masses:
        line = line.rstrip('\n')
        mass = int(line)
        tempFuel = (int(mass/3) - 2)
        while tempFuel > 0:
            fuel += tempFuel
            tempFuel = (int(tempFuel/3) - 2)            
        print (fuel)

