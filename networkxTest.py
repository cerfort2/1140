import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

class test():
    a = False
    setted = False

a = test()
b = test()
c = test()
d = test()
G.add_nodes_from([1,2,3,4])
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(2,4)

for main in list(G.nodes):
    for neighbors in G.adj[main]:
        pass
        # if(main.a == neighbors.a) and (not neighbors.setted):
        #     neighbors.a = not main.a
        #     neighbors.setted = True

for edge in list(G.edges):
    pass



# print(a.a)
# print(b.a)
# print(c.a)
# print(d.a)

# print(G.nodes)
# print(G.edges)
