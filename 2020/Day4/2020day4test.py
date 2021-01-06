passports = []
good = 0
bad = 0

with open( "2020day4.txt" ) as fd:
    lines = fd.readlines()

    record = {}
    for data in lines:
        if data in ['\n', '\r\n']:
            # if line is blank, append record
            passports.append(record)
            # process record
            # count keys
            length = 0
            for item in record.items():
                length += 1
            # if 8 records present, mark it good    
            if length == 8:
                good += 1
            # if 7 records, but cid is missing, call it good
            elif (length == 7 and not record.get('cid', False)):
                good += 1
            # else mark it bad
            else:
                bad += 1
            record = {}
        else:
            # if line is not blank, process line
            pairs = data.split()
            # add the key value pairs
            for pair in pairs:
                (key, value) = pair.split(':')
                record[key] = value
    print(record)
    passports.append(record)

    print("good = ", good, "bad = ", bad)           

#     data = lines[0].split()
#    record = {}
#    for pair in data:
#        (key, value) = pair.split(':')
#        record[key] = value
#    passports.append(record)
#    length = 0
#    for item in record.items():
#        length += 1
#    print("items = ", length)
#    print("dict = ", passports)
#        print("key = ", key, "value = ", value)
#        record['']
#    print("data = ", data)
#    for line in lines:
#        data = line.split()
