import networkx as nx

g = nx.DiGraph()
g.add_node({"name":"sample video","isRoot":True,index=1,cid = 20021})
g.add_node({"name":"another video","isRoot":True,index=2,cid = 20022})
# how to do this?
# for x in g.nodes
# g.add_edge((x,y))