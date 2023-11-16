import networkx as nx

G = nx.Graph()

class test():
    a = False

a = test()
b = test()
c = test()
d = test()
G.add_nodes_from([a,b,c,d])
G.add_edge(a,b)
G.add_edge(b,c)
G.add_edge(c,d)
G.add_edge(d,a)

for obj in G.nodes:
    for node in G.adj:
        pass
        
        
    print("Done")
print(G.nodes)
print(G.edges)
