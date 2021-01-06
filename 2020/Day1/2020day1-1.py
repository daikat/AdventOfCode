with open( "2020day1.txt" ) as file:
    entries = file.readlines()

    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            entry1 = int(entries[i])
            entry2 = int(entries[j])
            if ( ( entry1 + entry2 ) == 2020):
                print(entry1 * entry2)