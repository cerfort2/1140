import networkx as nx

G = nx.Graph()

class test():
    a = False
    setted = False

a = test()
b = test()
c = test()
d = test()
G.add_nodes_from([a,b,c,d])
G.add_edge(a,b)
G.add_edge(b,c)
G.add_edge(b,d)

for main in list(G.nodes):
    for neighbors in G.adj[main]:
        if(main.a == neighbors.a) and (not neighbors.setted):
            neighbors.a = not main.a
            neighbors.setted = True

print(a.a)
print(b.a)
print(c.a)
print(d.a)

print(G.nodes)
print(G.edges)
