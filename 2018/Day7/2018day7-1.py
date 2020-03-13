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

print(dot.source)
dot.render(filename='dagtest.gv', view=True)
