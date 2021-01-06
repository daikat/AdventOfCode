x = 0
trees = 0

with open( "2020day3.txt" ) as fd:
    rows = fd.readlines()

    for row in rows:
        row = row.strip()
        if('#' == row[x]):
            trees += 1
        x += 3
        x = x % len(row)
    print("trees: ", trees)
