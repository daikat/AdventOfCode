with open( "2020day2.txt" ) as fd:
    legit = 0

    for entry in fd:
        entry = entry.replace(": ", " ").replace("-", " ")
        entry = entry.split(" ")
        pos1 = int(entry[0]) - 1
        pos2 = int(entry[1]) - 1
        target = entry[2]
        password = entry[3]

        if((password[pos1] == target) ^ (password[pos2] == target)):
            legit += 1
    print(legit)        
