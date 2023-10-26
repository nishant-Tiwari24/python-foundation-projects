import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(100)
graph = nx.gnp_random_graph(20,0.5)


print(G.nodes(),G.edges())
nx.draw(G)
plt.show()

