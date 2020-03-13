with open( "2018day2.data" ) as file:
    boxes = file.readlines()

    for box1 in boxes:
        for box2 in boxes:
            diffCount = 0
            if box1 is box2:
                # Do not compare box against itself
                continue
            else:
                for x, y in zip(box1, box2):
                    if x is not y:
                        diffCount += 1
                if diffCount == 1:
                    print(box1)
                    print(box2)
