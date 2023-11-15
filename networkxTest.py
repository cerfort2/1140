import networkx as nx

G = nx.Graph()

G.add_nodes_from([1,2,3,4])
G.add_edge(3,1)
G.add_edge(1,2)
G.add_edge(3,4)

print(G.adj[1])
print(G.nodes)
print(G.edges)
