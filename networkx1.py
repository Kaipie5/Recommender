import networkx as nx
import matplotlib-pyplot as plt

g=nx.Graph()

g.add_node(2)
g.add_node(3)

g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,6)
g.add_edge(4,1)

# print detrails of graph
print(nx.info(g)

# visualize Graph
nx.draw(g)
plt.show()
