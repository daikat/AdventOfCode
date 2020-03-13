dataset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
twosets = 0
threesets = 0

with open( "2018day2.data" ) as file:
    boxes = file.readlines()

    for box in boxes:
        found2 = 0
        found3 = 0
        
        for letter in dataset:
            if not found2 and box.count(letter) == 2:
                twosets += 1
                found2 = 1
            elif not found3 and box.count(letter) == 3:
                threesets += 1
                found3 = 1

print (twosets)
print (threesets)
print (twosets * threesets)

