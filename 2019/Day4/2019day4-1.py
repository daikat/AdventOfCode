passwords = {}
for password in range(125730, 579382):
#for password in range(125730, 125900):
    passwordString = str(password)
    isAdjacent = False
    isIncreasing = True
    for iter in range(len(passwordString) - 1):
#        print("iter is", iter)
        if(passwordString[iter+1] >= passwordString[iter]):
            if(passwordString[iter+1] == passwordString[iter]):
                isAdjacent = True
        else:
            isIncreasing = False
            break
    if(isIncreasing and isAdjacent):
        print("Password is", password)
        passwords[password] = 1
print("Number of passwords is", len(passwords))

            


