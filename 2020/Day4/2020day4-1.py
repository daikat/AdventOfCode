def validate(passport):
    isValid = False

    # count keys
    length = len(passport.keys())

    # if 8 records present or if 7 records but cid is missing, call it good
    if (length == 8 or (length == 7 and not passport.get('cid', False))):
        isValid = True

    return isValid    


def main():
    good = 0
    passports = []

    with open( "2020day4.txt" ) as fd:
        lines = fd.readlines()

        record = {}
        for data in lines:
            if data in ['\n', '\r\n']:
                # if line is blank, append record
                passports.append(record)
                # process record
                if(validate(record)):
                    good += 1
                record = {}

            else:
                # if line is not blank, process line
                pairs = data.split()
                # add the key value pairs
                for pair in pairs:
                    (key, value) = pair.split(':')
                    record[key] = value
        passports.append(record)
        if(validate(record)):
            good += 1
    print("good = ", good)

main()