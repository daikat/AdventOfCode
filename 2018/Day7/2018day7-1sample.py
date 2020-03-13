from graphviz import Digraph
nodes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dot = Digraph()
for node in nodes:
    dot.node(node, node)

with open( "2018day7.data" ) as file:
    steps = file.readlines()

    for step in steps:
        step = step.split(' ')
        dot.edge(step[1], step[7])

#dot.node('A', 'A')
#dot.node('B', 'B')
#dot.node('C', 'C')
#dot.node('D', 'D')
#dot.node('E', 'E')
#dot.node('F', 'F')
#dot.edge('C', 'A')
#dot.edge('C', 'F')
#dot.edge('A', 'B')
#dot.edge('A', 'D')
#dot.edge('B', 'E')
#dot.edge('D', 'E')
#dot.edge('F', 'E')

print(dot.source)
dot.render(filename='dagtest.gv', view=True)
