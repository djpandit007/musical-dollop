import webbrowser


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py


def plotGraoph(labels,Edges):
    G = nx.DiGraph()
    G.add_edges_from(Edges)
    
    
    black_edges = [edge for edge in G.edges() if edge not in red_edges]
    
    
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos, node_color='c')
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edge_labels(G, pos,red_edges_lbl)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges,edge_color='b', arrows=False)
    plt.savefig("graph")
    
    
    f = open('graph.html','w')
      
    img_tag_1 = '<img src="{0}">'.format("init_graph.png")
     
    f.write(img_tag_1)
    f.close()
     
    filename = 'graph.html'
    webbrowser.open_new(filename)

