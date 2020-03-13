class newOrbit(object): 
    def __init__(self, key): 
        self.val = key
        self.left = None
        self.right = None
        self.orbits = 0

def findOrbit(node, key):
    if (node == None):
        return None
    if (node.val == key):
        return node

    res1 = findOrbit(node.left, key)
    if res1 != None:
        return res1
    
    res2 = findOrbit(node.right, key)
    return res2

def sumOrbits(node):
    if (node == None):
        return 0
    
    res1 = sumOrbits(node.left)
    res2 = sumOrbits(node.right)

    return (node.orbits + res1 + res2)

with open( "2019day6sample1.data" ) as file:
    orbits = file.read().splitlines()

orbitMap = newOrbit('COM')
for orbit in orbits:
    parent, orbiter = orbit.split(")")
    tempParent = findOrbit(orbitMap, parent)
    if (tempParent == None):
        print("Whoops, parent not found")
        exit()
    elif (tempParent.left == None):
        tempParent.left = newOrbit(orbiter)
        tempParent.left.orbits = tempParent.orbits + 1
    elif (tempParent.right == None):
        tempParent.right = newOrbit(orbiter)
        tempParent.right.orbits = tempParent.orbits + 1
    else:
        print("Doh! Both children full!")
        exit()
orbitSum = sumOrbits(orbitMap)
print(orbitSum)
