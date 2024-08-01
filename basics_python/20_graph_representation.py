import networkx as nx
import matplotlib.pyplot as plt


graph = {
    'A': [ 'C'],
    'B': ['G', 'D', 'E'],
    'C': ['A', 'F', 'E'],
    'D': ['B','G'],
    'E': ['B', 'C', 'H'],
    'F': ['C'],
    'G': ['B'],
    'H': ['E']
}



G = nx.Graph()


# G.add_edge(1,{2,3})

for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node,neighbor)

# print(list(G.nodes))
pos = nx.spring_layout(G)
edges = G.edges(data=True)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold')


plt.title("Graph Representation")
plt.show()