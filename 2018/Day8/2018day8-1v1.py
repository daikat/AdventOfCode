import numpy as np

metaAccum = 0
with open( "2018day8.data" ) as file:
#with open( "2018day8sample.data" ) as file:
    nodes = np.array(file.read().split(' '))

while len(nodes):
    print("numNodes =", len(nodes))
    numChildren = int(nodes[0])
    numMeta = int(nodes[1])
    print("numChildren =", numChildren, "numMeta =", numMeta)
    nodes = nodes[2:len(nodes)]
    if numChildren == 0:
        metas = nodes[0:numMeta]
        print("metas =", metas)
        for meta in metas:
           metaAccum += int(meta)
        nodes = nodes[numMeta:len(nodes)]
        print("zero nodes =", nodes)
    else:
        print("in nums.......")
        metas = nodes[-numMeta:len(nodes)]
        print("metas =", metas)
        for meta in metas:
            metaAccum += int(meta)
        nodes = nodes[0:-numMeta]
    print(nodes)
    print(metaAccum)
    
print(metaAccum)
