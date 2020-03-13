passwords = {}
#for password in range(125730, 125900):
for password in range(125730, 579382):
    passwordString = str(password)
    isIncreasing = True
    isAdjacent = False
    adjacents = {}
    for iter in range(len(passwordString) - 1):
        if(passwordString[iter+1] >= passwordString[iter]):
            if(passwordString[iter+1] == passwordString[iter]):
                if passwordString[iter] in adjacents:
                    adjacents[passwordString[iter]] += 1
                else:
                    adjacents[passwordString[iter]] = 2
        else:
            isIncreasing = False
            break
    if(isIncreasing):
        for digit in adjacents:
            if adjacents[digit] == 2:
                isAdjacent = True
        if(isAdjacent):
            passwords[password] = 1
print("Number of passwords is", len(passwords))

            


