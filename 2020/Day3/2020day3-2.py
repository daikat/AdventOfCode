def day3p1(right=3, down=1):
    x = 0
    trees = 0

    with open( "2020day3.txt" ) as fd:
        rows = fd.readlines()

        for i in range(0, len(rows), down):
            row = rows[i].strip()
            if('#' == row[x]):
                trees += 1
            x += right
            x = x % len(row)
    return trees

print(day3p1())

def day3p2():
    total = 1
    total *= day3p1(1)
    total *= day3p1(3)
    total *= day3p1(5)
    total *= day3p1(7)
    total *= day3p1(1,2)
    return total

print(day3p2())