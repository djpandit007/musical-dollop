import webbrowser


import networkx as nx
import matplotlib.pyplot as plt


def plotInit(labels,Edges):
    G = nx.DiGraph()
    G.add_edges_from(Edges)
    
    
    black_edges = [edge for edge in G.edges()]
    
    
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos, node_color='c')
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges,edge_color='b', arrows=False)
    plt.savefig("init_graph")
    
    
    f = open('graph_init.html','w')
      
    img_tag_1 = '<img src="{0}">'.format("init_graph.png")
     
    f.write(img_tag_1)
    f.close()
     
    filename = 'graph.html'
    webbrowser.open_new(filename)

