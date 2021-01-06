import re

def validate(passport):
    isValid = False

    # count keys
    length = len(passport.keys())

    # if 8 records present or if 7 records but cid is missing, call it good
    if (length == 8 or (length == 7 and not passport.get('cid', False))):
        if ((1920 <= int(passport['byr']) <= 2002) and (2010 <= int(passport['iyr']) <= 2020) and (2020 <= int(passport['eyr']) <= 2030)):
            if ((re.search("^#[0-9a-f]{6}", passport['hcl']) is not None) and (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and (len(passport['pid']) == 9)):
                if (re.search("cm", passport['hgt']) is not None):
                    temp = re.split("cm", passport['hgt'])
                    if (150 <= int(temp[0]) <= 193):
                        isValid = True
                if (re.search("in", passport['hgt']) is not None):
                    temp = re.split("in", passport['hgt'])
                    if (59 <= int(temp[0]) <= 76):
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