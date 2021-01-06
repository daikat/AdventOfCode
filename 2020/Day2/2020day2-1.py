with open( "2020day2.txt" ) as fd:
    legit = 0

    for entry in fd:
        entry = entry.replace(": ", " ").replace("-", " ")
        entry = entry.split(" ")
        minChars = int(entry[0])
        maxChars = int(entry[1])
        target = entry[2]
        password = entry[3]
        count = password.count(target)

        if(minChars <= count <= maxChars):
            legit += 1
    print(legit)        
